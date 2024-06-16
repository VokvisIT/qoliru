from django.urls import path
from .views import AVGRegionQOLView, BestRegionQOLView, BestCategoryQOLView, DataCountYesterdayView, WorstCategoryQOLView

urlpatterns = [
    path('dashboard/best-region-qol/', BestRegionQOLView.as_view(), name='best-region-qol'),
    path('dashboard/best-category-qol/', BestCategoryQOLView.as_view(), name='best-category-qol'),
    path('dashboard/worst-category-qol/', WorstCategoryQOLView.as_view(), name='worst-category-qol'),
    path('dashboard/data-count-yesterday/', DataCountYesterdayView.as_view(), name='data-count-yesterday'),
    path('dashboard/avg-qoliru/', AVGRegionQOLView.as_view(), name='avg-qoliru'),
]