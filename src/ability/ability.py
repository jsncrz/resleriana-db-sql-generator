import time
from dataclasses import dataclass

@dataclass
class Ability:
    ext_id: str
    name: str
    description: str
    create_date = time.strftime('%Y-%m-%d %H:%m:%S')

def ability_sql(abilities: list[Ability]):
    insert_string = 'INSERT INTO `ABILITY`(`EXT_ID`,`NAME`,`DESCRIPTION`,`CREATE_DATE`) VALUES '
    for ability in abilities:
        insert_string += ("".join([
            f"({ability.ext_id},\n\t",
            f"'{ability.name}',\n\t",
            f"'{ability.description}',\n\t",
            f"'{ability.create_date}'),\n\t"]))
    sql_file = open("sql/ability.sql", encoding="utf-8", mode="w")
    sql_file.write(f'{insert_string[:insert_string.__len__()-3]} ON DUPLICATE KEY UPDATE EXT_ID = EXT_ID')
    sql_file.close()
