import time
from dataclasses import dataclass

@dataclass
class Memoria_Growth:
    ext_id: str
    level: int
    value: int
    create_date = time.strftime('%Y-%m-%d %H:%m:%S')
    
def __memoria_growth_key_sql(growth_ids: list[str], language: str):
    insert_string = 'INSERT INTO memoria_growth_key(id) VALUES '
    for growth_id in growth_ids:
        insert_string += ("".join([
            f"({growth_id}),\n\t"]))
    sql_file = open(f"sql/{language}/memoria_growth_key.sql", encoding="utf-8", mode="w")
    sql_file.write(f'{insert_string[:insert_string.__len__()-3]} ON CONFLICT DO NOTHING')
    sql_file.close()
    

def memoria_growth_sql(growths: list[Memoria_Growth], language: str):
    insert_string = 'INSERT INTO memoria_growth(id,memoria_level,stat_value,create_date) VALUES '
    ids = []
    for growth in growths:
        if growth.ext_id not in ids:
            ids.append(growth.ext_id)
        insert_string += ("".join([
            f"({growth.ext_id},\n\t",
            f"{growth.level},\n\t",
            f"{growth.value},\n\t",
            f"'{growth.create_date}'),\n\t"]))
    __memoria_growth_key_sql(ids, language)
    sql_file = open(f"sql/{language}/memoria_growth.sql", encoding="utf-8", mode="w")
    sql_file.write(f'{insert_string[:insert_string.__len__()-3]} ON CONFLICT DO NOTHING')
    sql_file.close()
