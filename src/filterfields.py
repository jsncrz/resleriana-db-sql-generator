import json, os
from pathlib import Path
from dotenv import load_dotenv
from character import Character, create_sql_script as char_sql
from translation import Translation, create_sql_script as tl_sql
from character_stats import Character_Stat, create_sql_script as stat_sql
from character_resist import Character_Resist, create_sql_script as res_sql

load_dotenv()
tl_id_preval = 'CHARA'
language = os.getenv('LANGUAGE')
DB_FILEPATH= Path(f'{os.getenv("DB_FILEPATH")}/data/master/{language}/character.json')
def str_format(obj_col):
    if obj_col is None:
        return ''
    elif isinstance(obj_col, str):
        return obj_col.replace("'", "\\'")
    return obj_col
    
def add_chara_tls(tl_id_preval, str_format, translations, obj, id):
    translations.append(Translation(id=f'{tl_id_preval}_{id}_AT', language=language, text=str_format(obj['acquisition_text'])))
    translations.append(Translation(id=f'{tl_id_preval}_{id}_AN', language=language, text=str_format(obj['another_name'])))
    translations.append(Translation(id=f'{tl_id_preval}_{id}_D', language=language, text=str_format(obj['description'])))
    translations.append(Translation(id=f'{tl_id_preval}_{id}_FN', language=language, text=str_format(obj['fullname'])))
    translations.append(Translation(id=f'{tl_id_preval}_{id}_N', language=language, text=str_format(obj['name'])))

translations:list[Translation] = []
charas:list[Character] = []
stats:list[Character_Stat] = []
resists:list[Character_Resist] = []
with open(DB_FILEPATH.absolute(), encoding="utf8") as f:
    d = json.load(f)
    for obj in d:
        id = obj['id']
        add_chara_tls(tl_id_preval, str_format, translations, obj, id)
        charas.append(Character(acquisition_text= f'{tl_id_preval}_{id}_AT',
                            another_name= f'{tl_id_preval}_{id}_AN',
                            description=f'{tl_id_preval}_{id}_D',
                            fullname=f'{tl_id_preval}_{id}_FN',
                            ext_id=str_format(id),
                            is_alchemist=str_format(obj['is_alchemist']),
                            initial_rarity=obj['initial_rarity'],
                            attack_attribute=obj['attack_attributes'][0],
                            release_date=obj['start_at'],
                            name=f'{tl_id_preval}_{id}_N'))
        init_stat = obj['initial_status'];
        stats.append(Character_Stat(ext_id=id,
            attack=init_stat['attack'],
            defense=init_stat['defense'],
            hp=init_stat['hp'],
            magic=init_stat['magic'],
            mental=init_stat['mental'],
            speed=init_stat['speed'],
        ))
        resistance = obj['resistance'];
        resists.append(Character_Resist(ext_id=id,
            fire=resistance['fire'],
            ice=resistance['ice'],
            impact=resistance['impact'],
            lightning=resistance['lightning'],
            piercing=resistance['piercing'],
            slashing=resistance['slashing'],
            wind=resistance['wind'],
        ))
f.close()
char_sql(charas)
tl_sql(translations)
stat_sql(stats)
res_sql(resists)