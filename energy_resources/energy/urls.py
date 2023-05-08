from django.urls import path
from . import views


urlpatterns = [
    path('solar_panel_update/<int:id>/', views.SolarPanelUpdateDelete.as_view(), name="solar_panel_update_delete"),
    path('wind_power_plant_update/<int:id>/', views.WindPowerPlantUpdateDelete.as_view(), name="wind_plant_update_delete"),
    path('solar_panels/', views.SolarPanelListAPIView.as_view(), name="solar_panel_list"),
    path('wind_power_plants/', views.WindPowerPlantListAPIView.as_view(), name="wind_power_plant_list"),
    path('entity_choice/', views.EntityListAPIView.as_view(), name="entity_choice"),
    path('canton_choice/', views.CantonListAPIView.as_view(), name="canton_choice"),
    path('zone_choice/', views.ZoneListAPIView.as_view(), name="zone_choice"),
    path('import_shp_solar_panel/', views.ImportShapeFileSolarPanelAPIView.as_view(), name="import_shp_solar_panel"),
    path('import_shp_wind_power_plant/', views.ImportShapeFileWindPowerPlantAPIView.as_view(), name="import_shp_wind_power_plant")
    ]
