import time
from dataclasses import dataclass

@dataclass
class Memoria_Growth:
    ext_id: str
    level: int
    value: int
    create_date = time.strftime('%Y-%m-%d %H:%m:%S')

def memoria_growth_sql(growths: list[Memoria_Growth]):
    insert_string = 'INSERT INTO `MEMORIA_GROWTH`(`EXT_ID`,`LEVEL`,`STAT_VALUE`,`CREATE_DATE`) VALUES '
    for growth in growths:
        insert_string += ("".join([
            f"({growth.ext_id},\n\t",
            f"{growth.level},\n\t",
            f"{growth.value},\n\t",
            f"'{growth.create_date}'),\n\t"]))
    sql_file = open("sql/memoria_growth.sql", encoding="utf-8", mode="w")
    sql_file.write(f'{insert_string[:insert_string.__len__()-3]} ON DUPLICATE KEY UPDATE EXT_ID = EXT_ID')
    sql_file.close()
