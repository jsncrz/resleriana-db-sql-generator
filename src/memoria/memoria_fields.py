from datetime import datetime
import json, os
from pathlib import Path
from dotenv import load_dotenv
from generic.translation import Translation, tl_sql
from memoria.memoria import Memoria, memoria_sql
from memoria.memoria_ability import Memoria_Ability, memoria_ability_sql
from memoria.memoria_attribute import Memoria_Attribute, memoria_attribute_sql
from memoria.memoria_growth import Memoria_Growth, memoria_growth_sql
from memoria.memoria_status import Memoria_Status, memoria_status_sql
from memoria.memoria_role import Memoria_Role, memoria_role_sql
from util.util import append_sql_files, get_attribute_string, get_role_string, str_format, write_array_to_file

load_dotenv()
language = None
db_filepath = None

def __add_memoria_growths(growths:list):
    with open(Path(db_filepath + 'memoria_buff_growth.json').absolute(), encoding="utf8") as f:
        d = json.load(f)
        for obj in d:
            id = obj['id']
            counter = 1
            for value in obj['values']:
                growths.append(Memoria_Growth(ext_id=id, level=counter, value=value))
                counter += 1
            
def __add_memoria_tls(tl_id_preval, translations:list, obj, id):
    translations.append(Translation(id=f'{tl_id_preval}_{id}_D', language=language, text=str_format(obj['description'])))
    translations.append(Translation(id=f'{tl_id_preval}_{id}_N', language=language, text=str_format(obj['name'])))
    
def __add_memoria_abilities(memoria_id, memoria_abilities:list, ability_ids):
    for ability in ability_ids:
        memoria_abilities.append(Memoria_Ability(memoria_id=memoria_id, ability_id=ability))
        
def __add_memoria_attributes(memoria_id, memoria_attributes:list, attributes):
    for attribute in attributes:
        memoria_attributes.append(Memoria_Attribute(memoria_id=memoria_id, attribute=get_attribute_string(attribute)))
        
def __add_memoria_roles(memoria_id, memoria_roles:list, roles):
    for role in roles:
        memoria_roles.append(Memoria_Role(memoria_id=memoria_id, role=get_role_string(role)))
        
def __add_memoria_status(memoria_id, memoria_status:list, status):
    for status_value in status:
        if status_value['type'] == 1:
            hp = status_value['growth_id']
        elif status_value['type'] == 2:
            spd = status_value['growth_id']
        elif status_value['type'] == 3:
            attack = status_value['growth_id']
        elif status_value['type'] == 4:
            magic = status_value['growth_id']
        elif status_value['type'] == 5:
            defense = status_value['growth_id']
        elif status_value['type'] == 6:
            mental = status_value['growth_id']
    memoria_status.append(Memoria_Status(memoria_id=memoria_id, hp=hp, speed=spd, magic=magic, defense=defense, mental=mental, attack=attack))

def add_memoria_to_array(tl_id_preval, memorias, obj, id, release_date):
    memorias.append(Memoria(
                            description=f'{tl_id_preval}_{id}_D',
                            ext_id=str_format(id),
                            rarity=obj['rarity'],
                            release_date=release_date,
                            name=f'{tl_id_preval}_{id}_N'))

def __create_sql_files(translations, memorias, memoria_abilities, memoria_attributes, memoria_roles, memoria_status, memoria_growth):
    tl_sql(translations, 'memoria_translation', language)
    memoria_growth_sql(memoria_growth, language)
    memoria_sql(memorias, language)
    memoria_ability_sql(memoria_abilities, language)
    memoria_attribute_sql(memoria_attributes, language)
    memoria_role_sql(memoria_roles, language)
    memoria_status_sql(memoria_status, language)
    append_sql_files(scripts=['memoria_translation_key','memoria_translation', 'memoria_growth_key','memoria_growth', 'memoria', 'memoria_ability', 'memoria_attribute', 'memoria_status', 'memoria_role'], appended_filename='appended_memoria', language=language)

def create_memoria_sqls(locale: str):
    tl_id_preval = 'MEMORIA'
    global language
    global db_filepath
    language = locale
    db_filepath = f'{os.getenv("DB_FILEPATH")}/data/master/{language}/'
    translations:list[Translation] = []
    memorias:list[Memoria] = []
    memoria_abilities:list[Memoria_Ability] = []
    memoria_attributes:list[Memoria_Attribute] = []
    memoria_roles:list[Memoria_Role] = []
    memoria_status:list[Memoria_Status] = []
    memoria_growth:list[Memoria_Growth] = []
    ability_list: list[int] = []
    __add_memoria_growths(memoria_growth)
    with open(Path(db_filepath + 'memoria.json').absolute(), encoding="utf8") as f:
        d = json.load(f)
        for obj in d:
            id = obj['id']
            __add_memoria_tls(tl_id_preval, translations, obj, id)
            release_date = datetime.fromisoformat(obj['start_at']) if obj['start_at'] is not None else '2023-09-23 00:00:01'
            add_memoria_to_array(tl_id_preval, memorias, obj, id, release_date)
            __add_memoria_abilities(id, memoria_abilities, obj['ability_ids'])
            __add_memoria_attributes(id, memoria_attributes, obj['attack_attributes'])
            __add_memoria_roles(id, memoria_roles, obj['roles'])
            __add_memoria_status(id, memoria_status, obj['status_buffs'])
            ability_list = ability_list + obj['ability_ids']
    f.close()
    write_array_to_file(ability_list, 'memoria_ability')
    __create_sql_files(translations, memorias, memoria_abilities, memoria_attributes, memoria_roles, memoria_status, memoria_growth)
