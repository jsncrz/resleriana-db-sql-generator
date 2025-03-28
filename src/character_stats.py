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

def create_sql_script(stats: list[Character_Stat]):
    insert_string = 'INSERT INTO `CHARACTER_STATS`(`EXT_ID`,`ATTACK`,`DEFENSE`,`HP`, `MAGIC`,`MENTAL`,`SPEED`,`CREATE_DATE`) VALUES '
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
    sql_file = open("sql/character_stat.sql", encoding="utf-8", mode="w")
    sql_file.write(insert_string[:insert_string.__len__()-3])
    sql_file.close()
