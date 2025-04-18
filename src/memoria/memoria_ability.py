import time
from dataclasses import dataclass

@dataclass
class Memoria_Ability:
    memoria_id: str
    ability_id: str
    create_date = time.strftime('%Y-%m-%d %H:%m:%S')

def memoria_ability_sql(memoria_abilities: list[Memoria_Ability]):
    insert_string = 'INSERT INTO `MEMORIA_ABILITY`(`MEMORIA_ID`,`ABILITY_ID`,`CREATE_DATE`) VALUES '
    for memoria_ability in memoria_abilities:
        insert_string += ("".join([
            f"({memoria_ability.memoria_id},\n\t",
            f"'{memoria_ability.ability_id}',\n\t",
            f"'{memoria_ability.create_date}'),\n\t"]))
    sql_file = open("sql/memoria_ability.sql", encoding="utf-8", mode="w")
    sql_file.write(f'{insert_string[:insert_string.__len__()-3]} ON DUPLICATE KEY UPDATE MEMORIA_ID = MEMORIA_ID')
    sql_file.close()
