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

def memoria_status_sql(status: list[Memoria_Status], language: str):
    insert_string = 'INSERT INTO memoria_status(memoria_id,attack,defense,hp,magic,mental,speed,create_date) VALUES '
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
    sql_file = open(f"sql/{language}/memoria_status.sql", encoding="utf-8", mode="w")
    sql_file.write(f'{insert_string[:insert_string.__len__()-3]} ON CONFLICT DO NOTHING')
    sql_file.close()
