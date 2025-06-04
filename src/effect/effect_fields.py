import json, os
from pathlib import Path
from dotenv import load_dotenv
from effect.effect import Effect, effect_sql
from generic.translation import Translation, tl_sql
from util.util import append_sql_files, load_array_from_file, str_format

load_dotenv()
language = None
db_filepath= None

def create_effect_sql(locale: str):
    tl_id_preval = 'EFFECT'
    global language
    global db_filepath
    language = locale
    db_filepath = f'{os.getenv("DB_FILEPATH")}/data/master/{language}/'
    translations:list[Translation] = []
    effects:list[Effect] = []
    included_effects = load_array_from_file(['skill_effects', 'ability_effects'])
    with open(Path(db_filepath + 'effect.json').absolute(), encoding="utf8") as f:
        d = json.load(f)
        for obj in d:
            id = obj['id']
            if str(id) not in included_effects:
                continue
            translations.append(Translation(id=f'{tl_id_preval}_{id}_D', language=language, text=str_format(obj['description'])))
            effects.append(Effect(ext_id=obj['id'], description=f'{tl_id_preval}_{id}_D'))
    f.close()
    tl_sql(translations, 'effect_translation', language);
    effect_sql(effects, language);
    append_sql_files(scripts=['effect_translation_key', 'effect_translation', 'effect'], appended_filename='appended_effect', language=language)
