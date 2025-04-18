import time
from dataclasses import dataclass

@dataclass
class Effect:
    ext_id: str
    description: str
    create_date = time.strftime('%Y-%m-%d %H:%m:%S')

def effect_sql(effects: list[Effect]):
    insert_string = 'INSERT INTO `EFFECT`(`EXT_ID`,`DESCRIPTION`,`CREATE_DATE`) VALUES '
    for effect in effects:
        insert_string += ("".join([
            f"({effect.ext_id},\n\t",
            f"'{effect.description}',\n\t",
            f"'{effect.create_date}'),\n\t"]))
    sql_file = open("sql/effect.sql", encoding="utf-8", mode="w")
    sql_file.write(f'{insert_string[:insert_string.__len__()-3]} ON DUPLICATE KEY UPDATE EXT_ID = EXT_ID')
    sql_file.close()
