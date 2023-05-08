import os.path
from zipfile import ZipFile

from django.conf import settings


class InvalidShapefileError(Exception):
    """Raised when a shapefile is invalid or missing required components."""
    pass


def validate_required_shp_components(file_names):
    required_extensions = ['.shp', '.dbf', '.shx']
    imported_extensions = [os.path.splitext(file_name)[1] for file_name in file_names]
    if set(required_extensions).issubset(set(imported_extensions)):
        return True
    return False


def unzip_archive(shapefile, wind_power_plant_folder):
    with ZipFile(shapefile, 'r') as zipPowerPlant:

        if not validate_required_shp_components(zipPowerPlant.namelist()):
            raise InvalidShapefileError("No required components.")

        folder_name = os.path.splitext(os.path.basename(shapefile.name))[0]
        zipPowerPlant.extractall(f'{settings.MEDIA_ROOT}/{wind_power_plant_folder}/{folder_name}/')
        return folder_name


def find_shapefile(folder_name, wind_power_plant_folder):
    try:
        for file_name in os.listdir(f'{settings.MEDIA_ROOT}/{wind_power_plant_folder}/{folder_name}/'):
            if os.path.splitext(file_name)[1] == '.shp':
                shapefile_path = f'{settings.MEDIA_ROOT}/{wind_power_plant_folder}/{folder_name}/{file_name}'
                return shapefile_path
    except FileNotFoundError:
        print("The specified directory or file does not exist.")

