import time
from dataclasses import dataclass

@dataclass
class Character_Resist:
    ext_id: str
    fire: int
    ice: int
    wind: int
    lightning: int
    impact: int
    piercing: int
    slashing: int
    create_date = time.strftime('%Y-%m-%d %H:%m:%S')

def res_sql(stats: list[Character_Resist]):
    insert_string = 'INSERT INTO `CHARACTER_RESIST`(`EXT_ID`,`FIRE`,`ICE`,`AIR`, `BOLT`,`STRIKE`,`STAB`,`SLASH`,`CREATE_DATE`) VALUES '
    for stat in stats:
        insert_string += ("".join([
            f"({stat.ext_id},\n\t",
            f"{stat.fire},\n\t",
            f"{stat.ice},\n\t",
            f"{stat.wind},\n\t",
            f"{stat.lightning},\n\t",
            f"{stat.impact},\n\t",
            f"{stat.piercing},\n\t",
            f"{stat.slashing},\n\t",
            f"'{stat.create_date}'),\n\t"]))
    sql_file = open("sql/character_resist.sql", encoding="utf-8", mode="w")
    sql_file.write(f'{insert_string[:insert_string.__len__()-3]} ON DUPLICATE KEY UPDATE EXT_ID = EXT_ID')
    sql_file.close()
