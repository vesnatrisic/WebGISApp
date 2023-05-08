from .layermapping import CustomLayerMapping
from .models import WindPowerPlant

mapping = {'owner_name': 'owner_name',
           'manufacturer': 'manuf',
           'note': 'note',
           'entity': 'entity',
           'canton': 'canton',
           'city': 'city',
           'zone': 'zone',
           'altitude': 'altitude',
           'wind_direction': 'wind_direc',
           'power_supplied': 'power_supp'}


def import_shapefile_wpp(filepath, request_user_id):
    lm = CustomLayerMapping(model=WindPowerPlant, data=filepath, mapping=mapping, last_user_id=request_user_id)
    lm.save(verbose=True)
