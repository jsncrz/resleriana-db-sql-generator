import time
from dataclasses import dataclass

@dataclass
class Character_Stat:
    ext_id: str
    attack: int
    defense: int
    hp: int
    magic: int
    mental: int
    speed: int
    create_date = time.strftime('%Y-%m-%d %H:%m:%S')

def stat_sql(stats: list[Character_Stat], language: str):
    insert_string = 'INSERT INTO character_status(id,attack,defense,hp,magic,mental,speed,create_date) VALUES '
    for stat in stats:
        insert_string += ("".join([
            f"({stat.ext_id},\n\t",
            f"{stat.attack},\n\t",
            f"{stat.defense},\n\t",
            f"{stat.hp},\n\t",
            f"{stat.magic},\n\t",
            f"{stat.mental},\n\t",
            f"{stat.speed},\n\t",
            f"'{stat.create_date}'),\n\t"]))
    sql_file = open(f"sql/{language}/character_stat.sql", encoding="utf-8", mode="w")
    sql_file.write(f'{insert_string[:insert_string.__len__()-3]} ON CONFLICT DO NOTHING')
    sql_file.close()
