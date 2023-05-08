from django.db import models
from django.contrib.gis.db import models as gis_models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Entity(models.TextChoices):
    RS = 'RS', _('Republic of Srpska'),
    FBiH = 'FBiH', _('Federation of Bosnia and Herzegovina'),
    BD = 'BD', _('District Brcko')


class Canton(models.TextChoices):
    USK = 'USK', _('Una-Sana Canton'),
    POS = 'POS', _('Posavina Canton'),
    TUZ = 'TUZ', _('Tuzla Canton'),
    ZDK = 'ZDK', _('Zenica-Doboj Canton'),
    BPO = 'BPO', _('Bosnian-Podrinje Canton Goražde'),
    SBK = 'SBK', _('Central Bosnia Canton'),
    HN = 'HN', _('Herzegovina-Neretva Canton'),
    HB = 'HB', _('Herzeg-Bosnian Canton'),
    SA = 'SA', _('Sarajevo Canton'),
    ZHK = 'ZHK', _('Western Herzegovina Canton')


class Zone(models.TextChoices):
    U = 'U', _('Urban'),
    R = 'R', _('Rural')


class Resource(models.Model):
    class Meta:
        abstract = True

    owner_name = models.CharField(max_length=100, blank=True, null=True)
    manufacturer = models.CharField(max_length=100, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    entity = models.CharField(choices=Entity.choices, max_length=50)
    canton = models.CharField(choices=Canton.choices, max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100)
    zone = models.CharField(choices=Zone.choices, max_length=50, blank=True, null=True)
    altitude = models.IntegerField(blank=True, null=True)
    geometry = gis_models.PointField(srid=4326, dim=2)


class LastUser(models.Model):

    class Meta:
        abstract = True

    creation_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modification_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    last_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, blank=True, null=True)


class WindPowerPlant(Resource, LastUser):
    wind_direction = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    power_supplied = models.DecimalField(max_digits=10, decimal_places=2)
    document = models.FileField(upload_to='windpowerplantdocuments/', blank=True, null=True)


class SolarPanel(Resource, LastUser):
    panel_angle = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    field_strength = models.DecimalField(max_digits=5, decimal_places=2)
    document = models.FileField(upload_to='solarpaneldocuments/', blank=True, null=True)

