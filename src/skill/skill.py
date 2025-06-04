import time
from dataclasses import dataclass

@dataclass
class Skill:
    ext_id: str
    name: str
    description: str
    power: int
    break_power: int
    wait: int
    attribute: str
    skill_type: str
    target_type: str
    linked_skill: str
    create_date = time.strftime('%Y-%m-%d %H:%m:%S')

def skill_sql(skills: list[Skill], language: str):
    insert_string = 'INSERT INTO skill(id,linked_skill,skill_name,skill_description,skill_power,skill_break_power,skill_wait,skill_attribute,skill_effect_type,skill_target_type,create_date) VALUES '
    for skill in skills:
        insert_string += ("".join([
            f"({skill.ext_id},\n\t",
            f"{skill.linked_skill},\n\t" if skill.linked_skill else "NULL,\n\t",
            f"'{skill.name}',\n\t",
            f"'{skill.description}',\n\t",
            f"{skill.power},\n\t",
            f"{skill.break_power},\n\t",
            f"{skill.wait},\n\t",
            f"'{skill.attribute}',\n\t" if skill.attribute else "NULL,\n\t",
            f"'{skill.skill_type}',\n\t",
            f"'{skill.target_type}',\n\t" if skill.target_type else "NULL,\n\t",
            f"'{skill.create_date}'),\n\t"]))
    sql_file = open(f"sql/{language}/skill.sql", encoding="utf-8", mode="w")
    sql_file.write(f'{insert_string[:insert_string.__len__()-3]} ON CONFLICT DO NOTHING')
    sql_file.close()
