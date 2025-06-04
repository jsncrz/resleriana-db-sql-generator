import time
from dataclasses import dataclass

@dataclass
class Skill_Effect:
    skill_id: str
    effect_id: str
    value: int
    index: int
    create_date = time.strftime('%Y-%m-%d %H:%m:%S')

def skill_effect_sql(skill_effects: list[Skill_Effect], language: str):
    insert_string = 'INSERT INTO skill_effect(skill_id,effect_id,number_value,skill_effect_index,create_date) VALUES '
    for skill_effect in skill_effects:
        insert_string += ("".join([
            f"({skill_effect.skill_id},\n\t",
            f"'{skill_effect.effect_id}',\n\t",
            f"{skill_effect.value},\n\t" ,
            f"{skill_effect.index},\n\t" if skill_effect.index else "NULL,\n\t",
            f"'{skill_effect.create_date}'),\n\t"]))
    sql_file = open(f"sql/{language}/skill_effects.sql", encoding="utf-8", mode="w")
    sql_file.write(f'{insert_string[:insert_string.__len__()-3]} ON CONFLICT DO NOTHING')
    sql_file.close()
