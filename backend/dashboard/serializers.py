from rest_framework import serializers
from .models import ModelData

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelData
        fields = ('Data', 'Time', 'Resource_Name',)

class ModelDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelData
        fields = '__all__'



class ResourceStatsSerializer(serializers.Serializer):
    resource_name = serializers.CharField()
    categories = serializers.DictField()
    data_count = serializers.IntegerField()  # Добавляем поле data_count

def calculate_category_ratio(data):
    total_count = data.count()
    if total_count == 0:
        return {}
    
    categories = {}

    category_fields = ModelData._meta.fields[15:27]  # Assuming the boolean fields start from index 13 and end at 26

    for category_field in category_fields:
        category_name = category_field.name
        category_count = data.filter(**{category_name: True}).count()
        
        if category_count > 0:
            positive_count = data.filter(**{category_name: True, 'Positive': True}).count()
            ratio = positive_count / category_count * 10.0  # Calculate ratio
            categories[category_name] = round(ratio, 1)

    return categories

def get_resource_stats(start_data, end_data):
    resources = ModelData.objects.values_list('Resource_Name', flat=True).distinct()

    stats = []
    for resource in resources:
        data = ModelData.objects.filter(Resource_Name=resource, Data__range=[start_data, end_data])
        data_count = data.count()
        print(data_count) # Подсчет количества записей
        categories = calculate_category_ratio(data)
        if categories:
            avg_rating = sum(categories.values()) / len(categories)  # Calculate average rating
            stats.append({
                'resource_name': resource,
                'data_count': data_count,  # Добавление количества записей в результат
                'categories': categories
            })

    serializer = ResourceStatsSerializer(data=stats, many=True)
    serializer.is_valid(raise_exception=True)
    serialized_data = serializer.validated_data

    # Add 'avg' field manually to each serialized dictionary
    for stat in serialized_data:
        avg_rating = sum(stat['categories'].values()) / len(stat['categories'])  # Calculate average rating
        stat['avg'] = round(avg_rating, 1)

    return serialized_data
