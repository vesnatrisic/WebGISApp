from django.contrib import admin
from django.contrib.gis.admin import  OSMGeoAdmin

from .models import  SolarPanel, WindPowerPlant

@admin.register(SolarPanel)
class SolarPanel(OSMGeoAdmin):
    list_display = ('owner_name', 'geometry')

@admin.register(WindPowerPlant)
class WindPlant(OSMGeoAdmin):
    list_display = ('owner_name', 'geometry')