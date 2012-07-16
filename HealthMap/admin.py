from django.contrib import admin
from HealthMap.models import *
        
class RangeAdmin(admin.ModelAdmin):
    list_display = ('low', 'high', 'name', 'dataset')
    search_fields = ['name']
    ordering = ('low',)

class DatarowAdmin(admin.ModelAdmin):
    list_display = ('dataset', 'region', 'value')
    search_fields = ['dataset']
    ordering = ('dataset', 'region',)
    
admin.site.register(Region)
admin.site.register(Polyline)
admin.site.register(Category)
admin.site.register(Dataset)
admin.site.register(Range, RangeAdmin)
admin.site.register(Datarow, DatarowAdmin)
admin.site.register(History)

