import time
from dataclasses import dataclass

@dataclass
class Tag:
    ext_id: str
    name: str
    priority: int
    create_date = time.strftime('%Y-%m-%d %H:%m:%S')

def tag_sql(tags: list[Tag], language: str):
    insert_string = 'INSERT INTO tag(id,tag_name,priority,create_date) VALUES '
    for tag in tags:
        insert_string += ("".join([
            f"({tag.ext_id},\n\t",
            f"'{tag.name}',\n\t",
            f"{tag.priority},\n\t",
            f"'{tag.create_date}'),\n\t"]))
    sql_file = open(f"sql/{language}/tag.sql", encoding="utf-8", mode="w")
    sql_file.write(f'{insert_string[:insert_string.__len__()-3]} ON CONFLICT DO NOTHING')
    sql_file.close()
