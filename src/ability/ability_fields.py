import json, os
from pathlib import Path
from dotenv import load_dotenv
from ability.ability import Ability, ability_sql
from ability.ability_effect import Ability_Effect, ability_effect_sql
from effect.effect import Effect, effect_sql
from generic.translation import Translation, tl_sql
from util.util import append_sql_files, str_format

load_dotenv()
language = None
db_filepath = None

            
def __add_ability_effect(ability_id, ability_effects, effect_ids):
    for effect in effect_ids:
        ability_effects.append(Ability_Effect(ability_id=ability_id, effect_id=effect['id'], value=effect['value']))
        
def create_ability_sql(locale: str):
    tl_id_preval = 'ABILITY'
    global language
    global db_filepath
    language = locale
    db_filepath = f'{os.getenv("DB_FILEPATH")}/data/master/{language}/'
    translations:list[Translation] = []
    abilities:list[Ability] = []
    ability_effects:list[Ability_Effect] = []
    with open(Path(db_filepath + 'ability.json').absolute(), encoding="utf8") as f:
        d = json.load(f)
        for obj in d:
            id = obj['id']
            translations.append(Translation(id=f'{tl_id_preval}_{id}_N', language=language, text=str_format(obj['name'])))
            translations.append(Translation(id=f'{tl_id_preval}_{id}_D', language=language, text=str_format(obj['description'])))
            abilities.append(Ability(description= f'{tl_id_preval}_{id}_D',
                            ext_id=str_format(id),
                            name=f'{tl_id_preval}_{id}_N'))
            __add_ability_effect(ability_id=id, ability_effects=ability_effects, effect_ids=obj['effects'])
    f.close()
    tl_sql(translations, 'ability_translation');
    ability_sql(abilities);
    ability_effect_sql(ability_effects=ability_effects)
    append_sql_files(scripts=['ability_translation', 'ability', 'ability_effects'], appended_filename='appended_ability')
