import time
from dataclasses import dataclass

@dataclass
class Memoria_Status:
    memoria_id: str
    attack: str
    defense: str
    hp: str
    magic: str
    mental: str
    speed: str
    create_date = time.strftime('%Y-%m-%d %H:%m:%S')

def memoria_status_sql(status: list[Memoria_Status]):
    insert_string = 'INSERT INTO `MEMORIA_STATUS`(`MEMORIA_ID`,`ATTACK`,`DEFENSE`,`HP`,`MAGIC`,`MENTAL`,`SPEED`,`CREATE_DATE`) VALUES '
    for status_value in status:
        insert_string += ("".join([
            f"({status_value.memoria_id},\n\t",
            f"{status_value.attack},\n\t",
            f"{status_value.defense},\n\t",
            f"{status_value.hp},\n\t",
            f"{status_value.magic},\n\t",
            f"{status_value.mental},\n\t",
            f"{status_value.speed},\n\t",
            f"'{status_value.create_date}'),\n\t"]))
    sql_file = open("sql/memoria_status.sql", encoding="utf-8", mode="w")
    sql_file.write(f'{insert_string[:insert_string.__len__()-3]} ON DUPLICATE KEY UPDATE MEMORIA_ID = MEMORIA_ID')
    sql_file.close()
