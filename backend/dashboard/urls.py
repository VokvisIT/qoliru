from django.urls import path
from .views import BestRegionQOLView

urlpatterns = [
    path('dashboard/best-region-qol/', BestRegionQOLView.as_view(), name='best-region-qol'),
]