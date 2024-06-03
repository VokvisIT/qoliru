from django.contrib import admin
from .models import Region, Source, Resource, ModelDataTest

# Register your models here.

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','subject_code', 'description', 'longitude', 'latitude')
    list_filter = ('name',)
    search_fields = ('name',)

@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'region')
    list_filter = ('region',)
    search_fields = ('name',)

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link', 'description', 'source')
    list_filter = ('source',)
    search_fields = ('name',)

@admin.register(ModelDataTest)
class ModelDataTestAdmin(admin.ModelAdmin):
    list_display = ('id', 'data', 'time', 'region', 'source', 'resource', 'type_text', 'category', 'tonality')
    list_filter = ('region', 'source', 'resource', 'type_text', 'category', 'tonality')
    search_fields = ('type_text', 'category', 'tonality')