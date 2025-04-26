import json, os
from pathlib import Path
from dotenv import load_dotenv
from character.character_skill import Character_Skill, char_skill_sql
from generic.tags import Tag, tag_sql
from generic.translation import Translation, tl_sql
from util.util import append_sql_files, get_skill_type, str_format
from character.character import Character, char_sql
from character.character_tag import Character_Tag, char_tag_sql
from character.character_stats import Character_Stat, stat_sql
from character.character_resist import Character_Resist, res_sql

load_dotenv()
language = None
db_filepath = None

def __add_chara_tls(tl_id_preval, translations, obj, id):
    translations.append(Translation(id=f'{tl_id_preval}_{id}_AT', language=language, text=str_format(obj['acquisition_text'])))
    translations.append(Translation(id=f'{tl_id_preval}_{id}_AN', language=language, text=str_format(obj['another_name'])))
    translations.append(Translation(id=f'{tl_id_preval}_{id}_D', language=language, text=str_format(obj['description'])))
    translations.append(Translation(id=f'{tl_id_preval}_{id}_FN', language=language, text=str_format(obj['fullname'])))
    translations.append(Translation(id=f'{tl_id_preval}_{id}_N', language=language, text=str_format(obj['name'])))
    
def __add_tags_and_tls(translations, tags):
    with open(Path(db_filepath + 'character_tag.json').absolute(), encoding="utf8") as f:
        d = json.load(f)
        for obj in d:
            id = obj['id']
            translations.append(Translation(id=f'TAG_{id}_N', language=language, text=str_format(obj['name'])))
            tags.append(Tag(
                            ext_id=str_format(id),
                            priority=obj['priority'],
                            name=f'TAG_{id}_N'))
            
def __add_character_tags(character_id, character_tags, tag_ids):
    for tag in tag_ids:
        character_tags.append(Character_Tag(character_id=character_id, tag_id=tag))
            
def __add_character_skills(character_id: str, character_skills: list, skill_ids: list[list:int]):
    for index, skills in enumerate(skill_ids):
        for skill in skills:
            character_skills.append(Character_Skill(character_id=character_id, skill_id=skill, skill_type=get_skill_type(index)))

def create_character_sqls(locale: str):
    tl_id_preval = 'CHARA'
    global language
    global db_filepath
    language = locale
    db_filepath = f'{os.getenv("DB_FILEPATH")}/data/master/{language}/'
    translations:list[Translation] = []
    charas:list[Character] = []
    stats:list[Character_Stat] = []
    resists:list[Character_Resist] = []
    tags:list[Tag] = []
    character_tags:list[Character_Tag] = []
    character_skills:list[Character_Tag] = []
    __add_tags_and_tls(translations, tags)
    with open(Path(db_filepath + 'character.json').absolute(), encoding="utf8") as f:
        d = json.load(f)
        for obj in d:
            id = obj['id']
            if id == 43599:
                continue
            __add_chara_tls(tl_id_preval, translations, obj, id)
            charas.append(Character(acquisition_text= f'{tl_id_preval}_{id}_AT',
                            another_name= f'{tl_id_preval}_{id}_AN',
                            description=f'{tl_id_preval}_{id}_D',
                            fullname=f'{tl_id_preval}_{id}_FN',
                            ext_id=str_format(id),
                            is_alchemist=str_format(obj['is_alchemist']),
                            initial_rarity=obj['initial_rarity'],
                            max_rarity=obj.get('max_rarity', 0) ,
                            role=obj['role'],
                            attack_attribute=obj['attack_attributes'][0],
                            release_date=obj['start_at'],
                            name=f'{tl_id_preval}_{id}_N'))
            # Add tags objects
            __add_character_tags(id, character_tags, obj['tag_ids'])
            # Add Character skills
            __add_character_skills(id, character_skills, [obj['normal1_skill_ids'], obj['normal2_skill_ids'],obj['burst_skill_ids']])
            # Add stats objects
            init_stat = obj['initial_status'];
            stats.append(Character_Stat(ext_id=id,
                attack=init_stat['attack'],
                defense=init_stat['defense'],
                hp=init_stat['hp'],
                magic=init_stat['magic'],
                mental=init_stat['mental'],
                speed=init_stat['speed'],
            ))
            # Add resistance objects
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
    char_sql(charas, language)
    tl_sql(translations, 'chara_translation', language)
    stat_sql(stats, language)
    res_sql(resists, language)
    tag_sql(tags, language)
    char_tag_sql(character_tags, language)
    char_skill_sql(character_skills, language)
    append_sql_files(scripts=['chara_translation_key','chara_translation', 'tag', 'character', 'character_tag', 'character_skill', 'character_stat', 'character_resist'], appended_filename='appended_chara', language=language)
