from django.core.management.base import BaseCommand
from dashboard.models import ModelDataTest, Region, Source, Resource



class Command(BaseCommand):
    help = 'Parse TG data for the last day'

    def handle(self, *args, **options):
        api_id = '22762367'
        api_hash = '9af9f0416416e4b8d3cde1a358c4129f'

        resources = Resource.objects.filter(source__name='Telegram')
        for resource in resources:
            