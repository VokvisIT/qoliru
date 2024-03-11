from django.urls import path
from .views import DataViewSet, ResourceStatsAPIView

urlpatterns = [
    path('dashboard/', DataViewSet.as_view({'get': 'list'}), name='dashboard-list'),
    path('dashboard/resource_stats/', ResourceStatsAPIView.as_view(), name='resource-stats'),
]