# serializers.py
from rest_framework import serializers
from .models import Region, ModelDataTest
from django.db.models import  Count, Q
import datetime


class RegionQOLSerializer(serializers.ModelSerializer):
    qol = serializers.SerializerMethodField()
    qol_change = serializers.SerializerMethodField()
    longitude = serializers.SerializerMethodField()
    latitude = serializers.SerializerMethodField()

    class Meta:
        model = Region
        fields = ['id', 'name', 'qol', 'qol_change', 'longitude', 'latitude']

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
    def get_longitude(self, obj):
        return obj.longitude

    def get_latitude(self, obj):
        return obj.latitude
    
CATEGORY_MAPPING = {
    '0': 'Здравоохранение',
    '1': 'ЖКХ',
    '2': 'Образование',
    '3': 'Инфраструктура',
    '4': 'Культура',
    '5': 'Экологические условия',
    '6': 'Социальная защита',
    '7': 'Политика',
    '8': 'Безопасность',
    '9': 'Доступность товаров и услуг',
    '10': 'Официальные заявления',
    '11': 'Туризм',
    '12': 'Факты'
}

class RegionDetailSerializer(serializers.ModelSerializer):
    count_data = serializers.SerializerMethodField()
    qol = serializers.SerializerMethodField()
    qol_category = serializers.SerializerMethodField()

    class Meta:
        model = Region
        fields = ['name', 'qol', 'count_data', 'qol_category']

    def get_count_data(self, obj):
        return ModelDataTest.objects.filter(region=obj).count()

    def get_qol(self, obj):
        data = ModelDataTest.objects.filter(region=obj).values('category').annotate(
            positive_count=Count('id', filter=Q(tonality='1')),
            neutral_count=Count('id', filter=Q(tonality='0')),
            negative_count=Count('id', filter=Q(tonality='2')),
        )

        category_qols = []
        for category in data:
            total_count = category['positive_count'] + category['neutral_count'] + category['negative_count']
            if total_count == 0:
                continue
            positive_neutral_ratio = (category['positive_count'] + category['neutral_count']) / total_count
            qol = positive_neutral_ratio * 10
            category_qols.append(qol)

        if not category_qols:
            return 0
        return round(sum(category_qols) / len(category_qols), 1)

    def get_qol_category(self, obj):
        data = ModelDataTest.objects.filter(region=obj).values('category').annotate(
            positive_count=Count('id', filter=Q(tonality='1')),
            neutral_count=Count('id', filter=Q(tonality='0')),
            negative_count=Count('id', filter=Q(tonality='2')),
        )

        category_qol = {}
        for category in data:
            category_name = CATEGORY_MAPPING[str(category['category'])]
            total_count = category['positive_count'] + category['neutral_count'] + category['negative_count']
            if total_count == 0:
                category_qol[category_name] = 0
                continue
            positive_neutral_ratio = (category['positive_count'] + category['neutral_count']) / total_count
            qol = positive_neutral_ratio * 10
            category_qol[category_name] = round(qol, 1)

        return category_qol


class BestCategoryQOLSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='region.name')
    category_name = serializers.SerializerMethodField()
    qol = serializers.FloatField()
    qol_change = serializers.SerializerMethodField()
    
    class Meta:
        model = ModelDataTest
        fields = ['id', 'name', 'category_name', 'qol', 'qol_change']

    def get_category_name(self, obj):
        return CATEGORY_MAPPING[str(obj['category'])]

    def get_qol_change(self, obj):
        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)

        today_qol = self.calculate_daily_qol(obj, today)
        yesterday_qol = self.calculate_daily_qol(obj, yesterday)

        return round(today_qol - yesterday_qol, 1)

    def calculate_daily_qol(self, obj, date):
        data = ModelDataTest.objects.filter(region=obj['region'], category=obj['category'], data=date)
        total_count = data.count()
        if total_count == 0:
            return 0

        positive_count = data.filter(tonality='1').count()
        neutral_count = data.filter(tonality='0').count()
        negative_count = data.filter(tonality='2').count()

        positive_neutral_ratio = (positive_count + neutral_count) / total_count
        return positive_neutral_ratio * 10
    
class WorstCategoryQOLSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='region.name')
    category_name = serializers.SerializerMethodField()
    qol = serializers.FloatField()
    qol_change = serializers.SerializerMethodField()

    class Meta:
        model = ModelDataTest
        fields = ['id', 'name', 'category_name', 'qol', 'qol_change']

    def get_category_name(self, obj):
        return CATEGORY_MAPPING[str(obj['category'])]

    def get_qol_change(self, obj):
        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)

        today_qol = self.calculate_daily_qol(obj, today)
        yesterday_qol = self.calculate_daily_qol(obj, yesterday)

        return round(today_qol - yesterday_qol, 1)

    def calculate_daily_qol(self, obj, date):
        data = ModelDataTest.objects.filter(region=obj['region'], category=obj['category'], data=date)
        total_count = data.count()
        if total_count == 0:
            return 0

        positive_count = data.filter(tonality='1').count()
        neutral_count = data.filter(tonality='0').count()
        negative_count = data.filter(tonality='2').count()

        positive_neutral_ratio = (positive_count + neutral_count) / total_count
        return round(positive_neutral_ratio * 10, 1)

def get_avg_qol(date):
    '''
    Функция, которая возвращает среднее значения качества жизни всех регионов в определённую дату
    '''
    data = ModelDataTest.objects.filter(data=date)
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
    return round(sum(category_qols) / len(category_qols), 1)


class AvgRegionQOLSerializer(serializers.ModelSerializer):
    labels = serializers.ListField(child=serializers.DateField())
    data = serializers.ListField(child=serializers.FloatField())

    def to_representation(self, instance):
        labels = []
        data = []

        # Получаем все даты, когда были посты
        dates = ModelDataTest.objects.values_list('data', flat=True).distinct().order_by('data')

        for date in dates:
            qol = get_avg_qol(date)
            labels.append(date.strftime('%B %d'))  # измененный формат даты
            data.append(qol)

        return {'labels': labels, 'data': data}

class RegionDataSerializer(serializers.ModelSerializer):
    count_data = serializers.SerializerMethodField()
    bestcategory = serializers.SerializerMethodField()
    worstcategory = serializers.SerializerMethodField()
    qol = serializers.SerializerMethodField()
    name = serializers.CharField()

    class Meta:
        model = Region
        fields = ['id', 'name', 'count_data', 'bestcategory', 'worstcategory', 'qol']

    def get_count_data(self, obj):
        return ModelDataTest.objects.filter(region=obj).count()

    def get_bestcategory(self, obj):
        data = ModelDataTest.objects.filter(region=obj).values('category').annotate(
            positive_count=Count('id', filter=Q(tonality='1')),
            neutral_count=Count('id', filter=Q(tonality='0')),
            negative_count=Count('id', filter=Q(tonality='2')),
        )

        best_qol = 0
        for category in data:
            total_count = category['positive_count'] + category['neutral_count'] + category['negative_count']
            if total_count == 0:
                continue
            positive_neutral_ratio = (category['positive_count'] + category['neutral_count']) / total_count
            qol = positive_neutral_ratio * 10
            if qol > best_qol:
                best_qol = qol

        return round(best_qol, 1)

    def get_worstcategory(self, obj):
        data = ModelDataTest.objects.filter(region=obj).values('category').annotate(
            positive_count=Count('id', filter=Q(tonality='1')),
            neutral_count=Count('id', filter=Q(tonality='0')),
            negative_count=Count('id', filter=Q(tonality='2')),
        )

        worst_qol = 10
        for category in data:
            total_count = category['positive_count'] + category['neutral_count'] + category['negative_count']
            if total_count == 0:
                continue
            positive_neutral_ratio = (category['positive_count'] + category['neutral_count']) / total_count
            qol = positive_neutral_ratio * 10
            if qol < worst_qol:
                worst_qol = qol

        return round(worst_qol, 1)

    def get_qol(self, obj):
        data = ModelDataTest.objects.filter(region=obj).values('category').annotate(
            positive_count=Count('id', filter=Q(tonality='1')),
            neutral_count=Count('id', filter=Q(tonality='0')),
            negative_count=Count('id', filter=Q(tonality='2')),
        )

        category_qols = []
        for category in data:
            total_count = category['positive_count'] + category['neutral_count'] + category['negative_count']
            if total_count == 0:
                continue
            positive_neutral_ratio = (category['positive_count'] + category['neutral_count']) / total_count
            qol = positive_neutral_ratio * 10
            category_qols.append(qol)

        if not category_qols:
            return 0
        return round(sum(category_qols) / len(category_qols), 1)