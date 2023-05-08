from .layermapping import CustomLayerMapping
from .models import SolarPanel

mapping = {'owner_name': 'owner_name',
           'manufacturer': 'manuf',
           'note': 'note',
           'entity': 'entity',
           'canton': 'canton',
           'city': 'city',
           'zone': 'zone',
           'altitude': 'altitude',
           'panel_angle': 'panel_angl',
           'field_strength': 'field_stre'}


def import_shapefile_sp(filepath, request_user_id):
    lm = CustomLayerMapping(model=SolarPanel, data=filepath, mapping=mapping, last_user_id=request_user_id)
    lm.save(verbose=True)