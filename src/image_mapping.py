from dataclasses import dataclass
import json

@dataclass
class Image_Path:
    large_image: str
    small_image: str

@dataclass
class Map_To_Image:
    image_path: Image_Path
    item_id: int

def create_generic_image_mapping(DB_FILEPATH):
    map_to_images: list[Map_To_Image] = []
    with open(DB_FILEPATH.absolute(), encoding="utf8") as f:
        d = json.load(f)
        for obj in d:
            item_id = obj['id']
            map_to_images.append(Map_To_Image(item_id=item_id,
                                               image_path=Image_Path(
                                                   large_image=obj['large_still_path_hash'],
                                                   small_image=obj['small_still_path_hash']
                                               ),
                                               ))
    f.close()
    return map_to_images

