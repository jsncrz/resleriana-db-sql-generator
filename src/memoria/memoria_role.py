import time
from dataclasses import dataclass

@dataclass
class Memoria_Role:
    memoria_id: str
    role: str
    create_date = time.strftime('%Y-%m-%d %H:%m:%S')

def memoria_role_sql(memoria_roles: list[Memoria_Role], language: str):
    insert_string = 'INSERT INTO memoria_role(memoria_id,memoria_role,create_date) VALUES '
    for memoria_role in memoria_roles:
        insert_string += ("".join([
            f"({memoria_role.memoria_id},\n\t",
            f"'{memoria_role.role}',\n\t",
            f"'{memoria_role.create_date}'),\n\t"]))
    sql_file = open(f"sql/{language}/memoria_role.sql", encoding="utf-8", mode="w")
    sql_file.write(f'{insert_string[:insert_string.__len__()-3]} ON CONFLICT DO NOTHING')
    sql_file.close()
