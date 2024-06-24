# views.py
from datetime import time
from django.db.models import  Count, Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from .models import ModelDataTest, Region
from .serializers import AvgRegionQOLSerializer, BestCategoryQOLSerializer, RegionDataSerializer, RegionDetailSerializer, RegionQOLSerializer, WorstCategoryQOLSerializer

class RegionDetailView(APIView):
    def get(self, request, region_id):
        try:
            region = Region.objects.get(id=region_id)
        except Region.DoesNotExist:
            return Response({"detail": "Region not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = RegionDetailSerializer(region)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RegionQOLDataView(APIView):
    def get(self, request):
        regions = Region.objects.all()
        serializer = RegionDataSerializer(regions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BestRegionQOLView(APIView):
    def get(self, request):
        regions = Region.objects.all()
        serializer = RegionQOLSerializer(regions, many=True)
        sorted_regions = sorted(serializer.data, key=lambda x: x['qol'], reverse=True)
        
        if sorted_regions:
            return Response(sorted_regions[0], status=status.HTTP_200_OK)
        return Response({"detail": "No data available"}, status=status.HTTP_404_NOT_FOUND)

class MapRegionQOLView(APIView):
    def get(self, request):
        regions = Region.objects.all()
        serializer = RegionQOLSerializer(regions, many=True)
        sorted_regions = sorted(serializer.data, key=lambda x: x['qol'], reverse=True)
        
        if sorted_regions:
            return Response(sorted_regions, status=status.HTTP_200_OK)
        return Response({"detail": "No data available"}, status=status.HTTP_404_NOT_FOUND)

class BestCategoryQOLView(APIView):
    def get(self, request):
        data = ModelDataTest.objects.values('region', 'category').annotate(
            positive_count=Count('id', filter=Q(tonality='1')),
            neutral_count=Count('id', filter=Q(tonality='0')),
            negative_count=Count('id', filter=Q(tonality='2'))
        ).filter(positive_count__gt=0)

        best_category = None
        best_qol = 0

        for record in data:
            total_count = record['positive_count'] + record['neutral_count'] + record['negative_count']
            if total_count == 0:
                continue
            positive_neutral_ratio = (record['positive_count'] + record['neutral_count']) / total_count
            qol = round(positive_neutral_ratio * 10, 1)

            if qol > best_qol:
                best_qol = qol
                best_category = record
                best_category['qol'] = qol

        if best_category:
            region = Region.objects.get(id=best_category['region'])
            best_category['region'] = region
            serializer = BestCategoryQOLSerializer(best_category)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"detail": "No data available"}, status=status.HTTP_404_NOT_FOUND)
    
class WorstCategoryQOLView(APIView):
    def get(self, request):
        data = ModelDataTest.objects.values('region', 'category').annotate(
            positive_count=Count('id', filter=Q(tonality='1')),
            neutral_count=Count('id', filter=Q(tonality='0')),
            negative_count=Count('id', filter=Q(tonality='2'))
        ).filter(positive_count__gt=0)

        worst_category = None
        worst_qol = float('inf')

        for record in data:
            total_count = record['positive_count'] + record['neutral_count'] + record['negative_count']
            if total_count == 0:
                continue
            positive_neutral_ratio = (record['positive_count'] + record['neutral_count']) / total_count
            qol = round(positive_neutral_ratio * 10, 1)

            if qol < worst_qol:
                worst_qol = qol
                worst_category = record
                worst_category['qol'] = qol

        if worst_category:
            region = Region.objects.get(id=worst_category['region'])
            worst_category['region'] = region
            serializer = WorstCategoryQOLSerializer(worst_category)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"detail": "No data available"}, status=status.HTTP_404_NOT_FOUND)
    
class DataCountYesterdayView(APIView):
    def get(self, request):
        yesterday = timezone.now().date() - timezone.timedelta(days=1)
        day_before_yesterday = yesterday - timezone.timedelta(days=1)
        
        count_yesterday = ModelDataTest.objects.filter(data=yesterday).count()
        count_day_before_yesterday = ModelDataTest.objects.filter(data=day_before_yesterday).count()
        
        count_difference = count_yesterday - count_day_before_yesterday
        
        response_data = {
            "count_yesterday": count_yesterday,
            "count_day_before_yesterday": count_day_before_yesterday,
            "count_difference": count_difference
        }
        
        return Response(response_data, status=status.HTTP_200_OK)
    
class AVGRegionQOLView(APIView):
    def get(self, request):
        serializer = AvgRegionQOLSerializer(ModelDataTest.objects.all())
        return Response(serializer.data)