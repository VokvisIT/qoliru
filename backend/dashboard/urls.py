from django.urls import path
from .views import AVGRegionQOLView, BestRegionQOLView, BestCategoryQOLView, DataCountYesterdayView, RegionDetailView, RegionQOLDataView, WorstCategoryQOLView, MapRegionQOLView

urlpatterns = [
    path('dashboard/best-region-qol/', BestRegionQOLView.as_view(), name='best-region-qol'),
    path('dashboard/best-category-qol/', BestCategoryQOLView.as_view(), name='best-category-qol'),
    path('dashboard/worst-category-qol/', WorstCategoryQOLView.as_view(), name='worst-category-qol'),
    path('dashboard/data-count-yesterday/', DataCountYesterdayView.as_view(), name='data-count-yesterday'),
    path('dashboard/avg-qoliru/', AVGRegionQOLView.as_view(), name='avg-qoliru'),
    path('dashboard/region-qol/', MapRegionQOLView.as_view(), name='region-qol'),
    path('dashboard/region-qol-data/', RegionQOLDataView.as_view(), name='region-qol-data'),
    path('dashboard/region-detail/<int:region_id>/', RegionDetailView.as_view(), name='region-detail'),
]