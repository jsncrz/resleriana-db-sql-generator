import time
from dataclasses import dataclass

@dataclass
class Ability:
    ext_id: str
    name: str
    description: str
    create_date = time.strftime('%Y-%m-%d %H:%m:%S')

def ability_sql(abilities: list[Ability], language: str):
    insert_string = 'INSERT INTO ability(id,ability_name,ability_description,create_date) VALUES '
    for ability in abilities:
        insert_string += ("".join([
            f"({ability.ext_id},\n\t",
            f"'{ability.name}',\n\t",
            f"'{ability.description}',\n\t",
            f"'{ability.create_date}'),\n\t"]))
    sql_file = open(f"sql/{language}/ability.sql", encoding="utf-8", mode="w")
    sql_file.write(f'{insert_string[:insert_string.__len__()-3]} ON CONFLICT DO NOTHING')
    sql_file.close()
