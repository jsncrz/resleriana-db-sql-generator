import time
from dataclasses import dataclass

@dataclass
class Ability_Effect:
    ability_id: str
    effect_id: str
    value: int
    create_date = time.strftime('%Y-%m-%d %H:%m:%S')

def ability_effect_sql(ability_effects: list[Ability_Effect], language: str):
    insert_string = 'INSERT INTO ability_effect(ability_id,effect_id,number_value,create_date) VALUES '
    for ability_effect in ability_effects:
        insert_string += ("".join([
            f"({ability_effect.ability_id},\n\t",
            f"'{ability_effect.effect_id}',\n\t",
            f"'{ability_effect.value}',\n\t",
            f"'{ability_effect.create_date}'),\n\t"]))
    sql_file = open(f"sql/{language}/ability_effects.sql", encoding="utf-8", mode="w")
    sql_file.write(f'{insert_string[:insert_string.__len__()-3]} ON CONFLICT DO NOTHING')
    sql_file.close()
