import json
import os
from pathlib import Path
from dotenv import load_dotenv
from pathlib import Path
import shutil

from image_mapping import create_generic_image_mapping
load_dotenv()


def copy_image_from_path_hash(DB_FILEPATH, map_to_images, folder_name, file_prepend):
    DB_FILEPATH = Path(
        f'{os.getenv("DB_FILEPATH")}/resources/Japan/path_hash_to_name.json')
    with open(DB_FILEPATH.absolute(), encoding="utf8") as f:
        d = json.load(f)
        for item in map_to_images:
            for key, value in vars(item.image_path).items():
                file_source = f'{os.getenv("DB_FILEPATH")}/assets/images/{d[value]}.png'
                file_destination = f'assets/{folder_name}/'
                Path(file_destination).mkdir(parents=True, exist_ok=True)
                if d[value].endswith("_S") or d[value].endswith("_square"):
                    file_destination += f'{file_prepend}_{item.item_id}_small.png'
                else:
                    file_destination += f'{file_prepend}_{item.item_id}.png'
                if os.path.isfile(file_source):
                    print(
                        f'{os.getenv("DB_FILEPATH")}/assets/images/{d[value]}.png exists')
                    shutil.copy(file_source, file_destination)
    f.close()

def copy_generic_item_to_asset_folder(json_file_name, folder_name, file_prepend):
    language = os.getenv('LANGUAGE')
    DB_FILEPATH = Path(
        f'{os.getenv("DB_FILEPATH")}/data/master/{language}/{json_file_name}')
    copy_image_from_path_hash(DB_FILEPATH, create_generic_image_mapping(
        DB_FILEPATH), folder_name, file_prepend)

copy_generic_item_to_asset_folder('equipment_tool.json', 'equipments', 'equipment')
copy_generic_item_to_asset_folder('memoria.json', 'memorias', 'memoria')