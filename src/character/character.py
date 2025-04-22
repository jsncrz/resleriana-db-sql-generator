import time
from datetime import datetime

from util.util import get_attribute_string, get_role_string

class Character:
    type = 'CHARA'
    
    def __init__(self, acquisition_text, another_name, description, fullname, ext_id, is_alchemist, name, initial_rarity, max_rarity, release_date, attack_attribute, role):
        self.acquisition_text = acquisition_text
        self.another_name = another_name
        self.description = description
        self.fullname = fullname
        self.ext_id = ext_id
        self.is_alchemist = is_alchemist
        self.name = name
        self.initial_rarity = initial_rarity
        self.max_rarity = max_rarity
        self.attack_attribute = get_attribute_string(attack_attribute)
        self.role = get_role_string(role)
        self.release_date = datetime.fromisoformat(release_date).strftime('%Y-%m-%d %H:%m:%S')
        self.create_date = time.strftime('%Y-%m-%d %H:%m:%S')
        pass

def char_sql(charas: list[Character], language: str):
    insert_string = 'INSERT INTO character(acquisition_text,another_name,character_description,full_name, id,is_alchemist,character_name, initial_rarity, max_rarity, attack_attribute, character_role, release_date, create_date) VALUES '
    for chara in charas:
        insert_string += ("".join([
            f"('{chara.acquisition_text}',\n\t",
            f"'{chara.another_name}',\n\t",
            f"'{chara.description}',\n\t",
            f"'{chara.fullname}',\n\t",
            f"{chara.ext_id},\n\t",
            f"{chara.is_alchemist},\n\t",
            f"'{chara.name}',\n\t",
            f"{chara.initial_rarity},\n\t",
            f"{chara.max_rarity},\n\t",
            f"'{chara.attack_attribute}',\n\t",
            f"'{chara.role}',\n\t",
            f"'{chara.release_date}',\n\t",
            f"'{chara.create_date}'),\n\t"]))
    sql_file = open(f"sql/{language}/character.sql", encoding="utf-8", mode="w")
    sql_file.write(f'{insert_string[:insert_string.__len__()-3]} ON CONFLICT DO NOTHING')
    sql_file.close()
