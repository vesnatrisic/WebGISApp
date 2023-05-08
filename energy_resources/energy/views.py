import zipfile

from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView, CreateAPIView
from rest_framework.response import Response

from .file_methods import unzip_archive, find_shapefile, InvalidShapefileError
from .models import SolarPanel, WindPowerPlant, Entity, Canton, Zone
from .serializer import SolarPanelSerializer, WindPowerPlantSerializer, ChoiceSerializer, ShapeFileSolarPanelSerializer, \
    ShapeFileWindPowerPlantSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework_gis.filters import InBBoxFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.utils.translation import gettext_lazy as _

from .solar_panel_shp_import import import_shapefile_sp
from .wind_power_plant_shp_import import import_shapefile_wpp

WIND_POWER_PLANT_FOLDER = 'wind_power_plant_folder'
SOLAR_PANEL_FOLDER = 'solar_panel_folder'


class SolarPanelListAPIView(ListCreateAPIView):
    queryset = SolarPanel.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = SolarPanelSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend, InBBoxFilter]
    bbox_filter_field = 'geometry'
    filterset_fields = ['entity', 'canton', 'zone']
    search_fields = ['city']

    def perform_create(self, serializer):
        serializer.save(last_user = self.request.user)


class WindPowerPlantListAPIView(ListCreateAPIView):
    queryset = WindPowerPlant.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = WindPowerPlantSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend, InBBoxFilter]
    bbox_filter_field = 'geometry'
    filterset_fields = ['entity', 'canton', 'zone']
    search_fields = ['city']

    def perform_create(self, serializer):
        serializer.save(last_user = self.request.user)


class SolarPanelUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = SolarPanel.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = SolarPanelSerializer
    lookup_url_kwarg = 'id'

    def perform_update(self, serializer):
        serializer.save(last_user=self.request.user)


class WindPowerPlantUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = WindPowerPlant.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = WindPowerPlantSerializer
    lookup_url_kwarg = 'id'

    def perform_update(self, serializer):
        serializer.save(last_user=self.request.user)


class EntityListAPIView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ChoiceSerializer
    queryset = [{"code": code, "name": name} for code, name in Entity.choices]


class CantonListAPIView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ChoiceSerializer
    queryset = [{"code": code, "name": name} for code, name in Canton.choices]


class ZoneListAPIView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ChoiceSerializer
    queryset = [{"code": code, "name": name} for code, name in Zone.choices]


class ImportShapeFileSolarPanelAPIView(CreateAPIView):
    queryset = SolarPanel.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ShapeFileSolarPanelSerializer

    def post(self, request):
        try:
            shapefile = request.FILES['shapefile']

            if not shapefile:
                return Response(data={'detail': _('Zip file is required')})

            if not zipfile.is_zipfile(shapefile):
                raise InvalidShapefileError("Uploaded file is not zip.")

            folder_name = unzip_archive(shapefile, SOLAR_PANEL_FOLDER)
            shapefile_path = find_shapefile(folder_name, SOLAR_PANEL_FOLDER)
            import_shapefile_sp(shapefile_path, self.request.user.id)
            return Response(status=status.HTTP_201_CREATED)

        except InvalidShapefileError as error:
            return Response({"detail": error.args[0]}, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as error:
            return Response({"detail": error.args[0]}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response({"detail": error.args[0]}, status=status.HTTP_400_BAD_REQUEST)


class ImportShapeFileWindPowerPlantAPIView(CreateAPIView):
    queryset = SolarPanel.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ShapeFileWindPowerPlantSerializer

    def post(self, request):
        try:
            shapefile = request.FILES['shapefile']

            if not shapefile:
                return Response(data={'detail': _('Zip file is required')})

            if not zipfile.is_zipfile(shapefile):
                raise InvalidShapefileError("Uploaded file is not zip.")

            folder_name = unzip_archive(shapefile, WIND_POWER_PLANT_FOLDER)
            shapefile_path = find_shapefile(folder_name, WIND_POWER_PLANT_FOLDER)
            import_shapefile_wpp(shapefile_path, self.request.user.id)
            return Response(status=status.HTTP_201_CREATED)

        except InvalidShapefileError as error:
            return Response({"detail": error.args[0]}, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as error:
            return Response({"detail": error.args[0]}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response({"detail": error.args[0]}, status=status.HTTP_400_BAD_REQUEST)

