import zipfile

zip_file_path = "C:/Users/Vesna/Downloads/solar_panel.zip"  # Replace with the path to your ZIP file

with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall('C:/Users/Vesna/PycharmProjects/er-backend-g2/energy_resources/media/import_shapefile/solar_panel')  # Replace with the path of the desired directory for extraction
