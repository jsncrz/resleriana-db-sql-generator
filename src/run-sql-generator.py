import argparse
from ability.ability_fields import create_ability_sql
from character.character_filter_fields import create_character_sqls
from effect.effect_fields import create_effect_sql
from memoria.memoria_fields import create_memoria_sqls
from skill.skill_fields import create_skill_sql
from util.util import append_sql_files

parser = argparse.ArgumentParser(
                    prog='Resleriana DB Scripts',
                    description='Resleriana MySql scripts generator using JSON data from Resleriana-DB')
parser.add_argument("locale", type=str, default=['en', 'jp'], help="Locale of the JSON data")

parser.add_argument('-c', '--char', action='store_true', help="Flag for character script creation")
parser.add_argument('-e', '--effect', action='store_true', help="Flag for effect script creation")
parser.add_argument('-a', '--ability', action='store_true', help="Flag for ability script creation")
parser.add_argument('-m', '--memory', action='store_true', help="Flag for memoria script creation")
parser.add_argument('-s', '--skill', action='store_true', help="Flag for skill script creation")
parser.add_argument('-p', '--appended', action='store_true', help="Flag for appending scripts")
args = parser.parse_args()

if __name__ == "__main__":
    locale = args.locale
    print(args)
    # The order of these calls are important
    if args.char:
        create_character_sqls(locale)
    if args.ability:
        create_ability_sql(locale)
    if args.memory:
        create_skill_sql(locale)
    if args.effect:
        create_effect_sql(locale)
    if args.memory:
        create_memoria_sqls(locale)
    if args.appended:
        append_sql_files(['appended_effect', 'appended_skill', 'appended_ability', 'appended_chara', 'appended_memoria'], 
                         'appended', locale, True)