# serializers.py
from rest_framework import serializers
from .models import Region, ModelDataTest
from django.db.models import Avg, Count, Q
import datetime
class RegionQOLSerializer(serializers.ModelSerializer):
    qol = serializers.SerializerMethodField()
    qol_change = serializers.SerializerMethodField()

    class Meta:
        model = Region
        fields = ['id', 'name', 'qol', 'qol_change']

    def get_qol(self, obj):
        return round(self.calculate_qol(obj), 1)

    def get_qol_change(self, obj):
        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)
        
        today_qol = self.calculate_daily_qol(obj, today)
        yesterday_qol = self.calculate_daily_qol(obj, yesterday)

        return round(today_qol - yesterday_qol, 1)

    def calculate_qol(self, obj):
        data = ModelDataTest.objects.filter(region=obj)
        categories = data.values('category').annotate(
            positive_count=Count('id', filter=Q(tonality='1')),
            neutral_count=Count('id', filter=Q(tonality='0')),
            negative_count=Count('id', filter=Q(tonality='2')),
        )

        category_qols = []
        for category in categories:
            total_count = category['positive_count'] + category['neutral_count'] + category['negative_count']
            if total_count == 0:
                continue
            positive_neutral_ratio = (category['positive_count'] + category['neutral_count']) / total_count
            qol = positive_neutral_ratio * 10
            category_qols.append(qol)

        if not category_qols:
            return 0
        return sum(category_qols) / len(category_qols)

    def calculate_daily_qol(self, obj, date):
        data = ModelDataTest.objects.filter(region=obj, data=date)
        categories = data.values('category').annotate(
            positive_count=Count('id', filter=Q(tonality='1')),
            neutral_count=Count('id', filter=Q(tonality='0')),
            negative_count=Count('id', filter=Q(tonality='2')),
        )

        category_qols = []
        for category in categories:
            total_count = category['positive_count'] + category['neutral_count'] + category['negative_count']
            if total_count == 0:
                continue
            positive_neutral_ratio = (category['positive_count'] + category['neutral_count']) / total_count
            qol = positive_neutral_ratio * 10
            category_qols.append(qol)

        if not category_qols:
            return 0
        return sum(category_qols) / len(category_qols)