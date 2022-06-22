import zipfile
import os

current_dir = os.getcwd()
files = os.listdir(current_dir)
for file in files:
    file_name, file_extension = os.path.splitext(file)
    if file_extension == '.zip':
        dir_name = os.path.join(current_dir, './extracted archive/', file_name)
        with zipfile.ZipFile(file, 'r') as zip_file:
            zip_file.extractall(dir_name)
