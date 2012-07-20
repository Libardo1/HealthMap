from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'HealthMap.views.HomePage'),
    (r'^lookup/$', 'HealthMap.views.LookupRequest'),
    url(r'^dataset_lookup/$','HealthMap.views.dataset_lookup', name='dataset_lookup'),
    url(r'^dataset_gis/$','HealthMap.views.dataset_gis', name='dataset_gis'),
    url(r'^admin/', include(admin.site.urls)),
)
