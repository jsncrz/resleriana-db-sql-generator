import time
from dataclasses import dataclass

@dataclass
class Memoria_Attribute:
    memoria_id: str
    attribute: str
    create_date = time.strftime('%Y-%m-%d %H:%m:%S')

def memoria_attribute_sql(memoria_attributes: list[Memoria_Attribute]):
    insert_string = 'INSERT INTO `MEMORIA_ATTRIBUTE`(`MEMORIA_ID`,`ATTRIBUTE`,`CREATE_DATE`) VALUES '
    for memoria_attribute in memoria_attributes:
        insert_string += ("".join([
            f"({memoria_attribute.memoria_id},\n\t",
            f"'{memoria_attribute.attribute}',\n\t",
            f"'{memoria_attribute.create_date}'),\n\t"]))
    sql_file = open("sql/memoria_attribute.sql", encoding="utf-8", mode="w")
    sql_file.write(f'{insert_string[:insert_string.__len__()-3]} ON DUPLICATE KEY UPDATE MEMORIA_ID = MEMORIA_ID')
    sql_file.close()
