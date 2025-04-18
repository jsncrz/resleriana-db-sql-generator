from dataclasses import dataclass
import time

@dataclass
class Memoria:
    description: str
    ext_id: str
    name: str
    rarity: str
    release_date: str
    create_date = time.strftime('%Y-%m-%d %H:%m:%S')
    
def memoria_sql(memorias: list[Memoria]):
    insert_string = 'INSERT INTO `MEMORIA`(`NAME`,`DESCRIPTION`,`EXT_ID`,`RARITY`,`RELEASE_DATE`, `CREATE_DATE`) VALUES '
    for memoria in memorias:
        insert_string += (''.join([
            f"('{memoria.name}',\n\t",
            f"'{memoria.description}',\n\t",
            f"{memoria.ext_id},\n\t",
            f"{memoria.rarity},\n\t",
            f"'{memoria.release_date}',\n\t",
            f"'{memoria.create_date}'),\n\t"]))
    sql_file = open('sql/memoria.sql', encoding='utf-8', mode='w')
    sql_file.write(f'{insert_string[:insert_string.__len__()-3]} ON DUPLICATE KEY UPDATE EXT_ID = EXT_ID')
    sql_file.close()
