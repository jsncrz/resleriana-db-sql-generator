import time
from dataclasses import dataclass

@dataclass
class Ability_Effect:
    ability_id: str
    effect_id: str
    value: int
    create_date = time.strftime('%Y-%m-%d %H:%m:%S')

def ability_effect_sql(ability_effects: list[Ability_Effect]):
    insert_string = 'INSERT INTO `ABILITY_EFFECT`(`ABILITY_ID`,`EFFECT_ID`,`VALUE`,`CREATE_DATE`) VALUES '
    for ability_effect in ability_effects:
        insert_string += ("".join([
            f"({ability_effect.ability_id},\n\t",
            f"'{ability_effect.effect_id}',\n\t",
            f"'{ability_effect.value}',\n\t",
            f"'{ability_effect.create_date}'),\n\t"]))
    sql_file = open("sql/ability_effects.sql", encoding="utf-8", mode="w")
    sql_file.write(f'{insert_string[:insert_string.__len__()-3]} ON DUPLICATE KEY UPDATE ABILITY_ID = ABILITY_ID')
    sql_file.close()
