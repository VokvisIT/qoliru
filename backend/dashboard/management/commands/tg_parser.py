from django.core.management.base import BaseCommand
import pandas as pd
from dashboard.models import ModelDataTest, Region, Source, Resource
from asgiref.sync import async_to_sync
import os
from datetime import datetime
from .parser_tg import main
from .parser_vk import get_prediction_tonality, get_prediction, preprocess_text
def save_data(data, time, resource, text, comment_text, type_text, category, tonality):
    ModelDataTest.objects.create(
        data=data,
        time=time,
        region=Region.objects.get(name=resource.source.region.name),
        source=resource.source,
        resource=resource,
        text=text,
        comment_text=comment_text,
        type_text=type_text,
        category=category,
        tonality=tonality
    )

class Command(BaseCommand):
    help = 'Parse TG data for the last day'

    def handle(self, *args, **options):
        print("handle сработал")
        resources = Resource.objects.filter(source__name='Telegram')
        api_id = '22762367'
        api_hash = '9af9f0416416e4b8d3cde1a358c4129f'
        for resource in resources:
            last_post = ModelDataTest.objects.filter(resource=resource, source__name='Telegram').order_by('-data', '-time').first()
            last_post_date = last_post.data if last_post else datetime.date.today()
            last_post_time = last_post.time if last_post else datetime.time.min
            async_to_sync(main)(resource.link, api_id, api_hash, resource, last_post_date, last_post_time)
            # Сохраняем данные в модель
            output_folder = "dashboard/csvdata"
            csv_file = f"{output_folder}/{resource.link}.csv"
            df = pd.read_csv(csv_file)

            for index, row in df.iterrows():
                process_text = preprocess_text(row["Text"])
                tonality = get_prediction_tonality(process_text)
                category = get_prediction(process_text)
                save_data(
                    data=row["Date"],
                    time=row["Time"],
                    resource=resource,
                    text=row["Text"],
                    comment_text='',
                    type_text=row["Text Type"],
                    category=category,
                    tonality=tonality,
                )

            # Удаляем CSV-файлы
            os.remove(csv_file)

        self.stdout.write(self.style.SUCCESS('Successfully parsed and saved TG data'))
