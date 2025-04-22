import time
from dataclasses import dataclass

@dataclass
class Effect:
    ext_id: str
    description: str
    create_date = time.strftime('%Y-%m-%d %H:%m:%S')

def effect_sql(effects: list[Effect], language: str):
    insert_string = 'INSERT INTO effect(id,effect_description,create_date) VALUES '
    for effect in effects:
        insert_string += ("".join([
            f"({effect.ext_id},\n\t",
            f"'{effect.description}',\n\t",
            f"'{effect.create_date}'),\n\t"]))
    sql_file = open(f"sql/{language}/effect.sql", encoding="utf-8", mode="w")
    sql_file.write(f'{insert_string[:insert_string.__len__()-3]} ON CONFLICT DO NOTHING')
    sql_file.close()
