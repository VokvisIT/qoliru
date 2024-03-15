from rest_framework import viewsets
from .models import ModelData
from .serializers import DataSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import get_resource_stats

class DataViewSet(viewsets.ModelViewSet):
    queryset = ModelData.objects.all()[10:]
    serializer_class = DataSerializer


class ResourceStatsAPIView(APIView):
    def get(self, request):
        start_date = '2023-08-01'
        end_date = '2023-12-31'
        stats = get_resource_stats(start_date, end_date)
        return Response(stats)