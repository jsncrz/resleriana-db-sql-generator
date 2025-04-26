import time
from dataclasses import dataclass

@dataclass
class Character_Skill:
    character_id: str
    skill_id: str
    skill_type: str
    create_date = time.strftime('%Y-%m-%d %H:%m:%S')

def char_skill_sql(character_skills: list[Character_Skill], language: str):
    insert_string = 'INSERT INTO character_skill(character_id,skill_id,skill_type,create_date) VALUES '
    for skill in character_skills:
        insert_string += ("".join([
            f"({skill.character_id},\n\t",
            f"'{skill.skill_id}',\n\t",
            f"'{skill.skill_type}',\n\t",
            f"'{skill.create_date}'),\n\t"]))
    sql_file = open(f"sql/{language}/character_skill.sql", encoding="utf-8", mode="w")
    sql_file.write(f'{insert_string[:insert_string.__len__()-3]} ON CONFLICT DO NOTHING')
    sql_file.close()
