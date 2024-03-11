from django.core.management.base import BaseCommand
from dashboard.models import ModelData

class Command(BaseCommand):
    help = 'Вывод уникальных Resource_Name!'

    def handle(self, *args, **kwargs):
        # Получаем уникальные значения поля Resource_Name
        unique_resource_names = ModelData.objects.values_list('Resource_Name', flat=True).distinct()

        # Выводим уникальные значения в консоль
        for resource_name in unique_resource_names:
            self.stdout.write(resource_name)