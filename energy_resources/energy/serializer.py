from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import SolarPanel, WindPowerPlant, LastUser


class SolarPanelSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = SolarPanel
        geo_field = 'geometry'
        fields = '__all__'
        read_only_fields = ('id', 'creation_date', 'modification_date')


class WindPowerPlantSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = WindPowerPlant
        geo_field = 'geometry'
        fields = '__all__'
        read_only_fields = ('id', 'creation_date', 'modification_date')


class ChoiceSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=4)
    name = serializers.CharField(max_length=24)

    class Meta:
        fields = ('code', 'name')


class LastUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LastUser
        fields = ('creation_date', 'modification_date')


class ShapeFileWindPowerPlantSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = WindPowerPlant
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        user_id = request.user.id if request and request.user else None

        wind_power_plant = WindPowerPlant.objects.create(
            user_id=user_id,
            owner_name=validated_data.get('owner_name'),
            manufacturer=validated_data.get('manuf'),
            note=validated_data.get('note'),
            entity=validated_data.get('entity'),
            canton=validated_data.get('canton'),
            city=validated_data.get('city'),
            zone=validated_data.get('zone'),
            altitude=validated_data.get('altitude'),
            geometry=validated_data.get('geometry'),
            wind_direction=validated_data.get('wind_direc'),
            power_supplied=validated_data.get('power_supp'),
            document=validated_data.get('document'),
        )

        return wind_power_plant


class ShapeFileSolarPanelSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = SolarPanel
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        user_id = request.user.id if request and request.user else None

        solar_panel = SolarPanel.objects.create(
            user_id=user_id,
            owner_name=validated_data.get('owner_name'),
            manufacturer=validated_data.get('manuf'),
            note=validated_data.get('note'),
            entity=validated_data.get('entity'),
            canton=validated_data.get('canton'),
            city=validated_data.get('city'),
            zone=validated_data.get('zone'),
            altitude=validated_data.get('altitude'),
            geometry=validated_data.get('geometry'),
            panel_angle=validated_data.get('panel_angl'),
            field_strength=validated_data.get('field_stre'),
            document=validated_data.get('document'),
        )

        return solar_panel






