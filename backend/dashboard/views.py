# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Region
from .serializers import RegionQOLSerializer

class BestRegionQOLView(APIView):
    def get(self, request):
        regions = Region.objects.all()
        serializer = RegionQOLSerializer(regions, many=True)
        sorted_regions = sorted(serializer.data, key=lambda x: x['qol'], reverse=True)
        
        if sorted_regions:
            return Response(sorted_regions[0], status=status.HTTP_200_OK)
        return Response({"detail": "No data available"}, status=status.HTTP_404_NOT_FOUND)
