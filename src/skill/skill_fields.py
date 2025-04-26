import json, os
from pathlib import Path
import re
from dotenv import load_dotenv
from skill.skill import Skill, skill_sql
from skill.skill_effect import Skill_Effect, skill_effect_sql
from generic.translation import Translation, tl_sql
from util.util import append_sql_files, get_attribute_string, get_skill_effect_type, get_skill_target_type, str_format

load_dotenv()
language = None
db_filepath = None
            
def __add_skill_effect(skill_id, skill_effects, effect_ids, description):
    
    indexes = re.findall(r"\{(\d+)\}", description)
    for index, effect in enumerate(effect_ids):
        skill_index = None
        if index < len(indexes):
            skill_index = indexes[index]
        skill_effects.append(Skill_Effect(skill_id=skill_id, effect_id=effect['id'], value=effect['value'], index=skill_index))
        
def __get_linked_skill(hyperlinks, linked_id):
    skill_id = None
    try:
        linked_id = int(linked_id)
    except (ValueError, TypeError):
        pass
    
    for obj in hyperlinks:
        if obj['id'] == linked_id:
            skill_id = obj['skill_id']
    return skill_id

def __get_hyper_link_json():
    with open(Path(db_filepath + 'hyperlink.json').absolute(), encoding="utf8") as f:
        d = json.load(f)
        return d
        
def create_skill_sql(locale: str):
    tl_id_preval = 'SKILL'
    global language
    global db_filepath
    language = locale
    db_filepath = f'{os.getenv("DB_FILEPATH")}/data/master/{language}/'
    hyperlinks = __get_hyper_link_json()
    translations:list[Translation] = []
    skills:list[Skill] = []
    skill_effects:list[Skill_Effect] = []
    with open(Path(db_filepath + 'skill.json').absolute(), encoding="utf8") as f:
        d = json.load(f)
        for obj in d:
            id = obj['id']
            description = obj['description'];
            linked_id = re.search(r"\{hyperlink_id (\d+)\}", description)
            linked_skill = None
            if linked_id:
                linked_skill = __get_linked_skill(hyperlinks, linked_id.group(1))
            filtered_desc = re.sub(r'\{hyperlink_id (\d+)\}', '{linked_skill}', description)
            translations.append(Translation(id=f'{tl_id_preval}_{id}_N', language=language, text=str_format(obj['name'])))
            translations.append(Translation(id=f'{tl_id_preval}_{id}_D', language=language, text=str_format(filtered_desc)))
            attribute = obj['attack_attributes']
            skills.append(Skill(description= f'{tl_id_preval}_{id}_D',
                            ext_id=str_format(id),
                            wait=obj['wait'],
                            power=obj['power'],
                            break_power=obj['break_power'],
                            linked_skill=linked_skill,
                            attribute=get_attribute_string(attribute[0]) if attribute else None,
                            skill_type=get_skill_effect_type(obj['skill_effect_type']),
                            target_type=get_skill_target_type(obj['skill_target_type']),
                            name=f'{tl_id_preval}_{id}_N'))
            __add_skill_effect(skill_id=id, skill_effects=skill_effects, effect_ids=obj['effects'], description=filtered_desc)
    f.close()
    tl_sql(translations, 'skill_translation', language);
    skill_sql(skills, language);
    skill_effect_sql(skill_effects, language)
    append_sql_files(scripts=['skill_translation_key','skill_translation', 'skill', 'skill_effects'], appended_filename='appended_skill', language=language)
