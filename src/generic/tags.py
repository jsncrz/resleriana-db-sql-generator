import time
from dataclasses import dataclass

@dataclass
class Tag:
    ext_id: str
    name: str
    priority: int
    create_date = time.strftime('%Y-%m-%d %H:%m:%S')

def tag_sql(tags: list[Tag]):
    insert_string = 'INSERT INTO `TAG`(`EXT_ID`,`NAME`,`PRIORITY`,`CREATE_DATE`) VALUES '
    for tag in tags:
        insert_string += ("".join([
            f"({tag.ext_id},\n\t",
            f"'{tag.name}',\n\t",
            f"{tag.priority},\n\t",
            f"'{tag.create_date}'),\n\t"]))
    sql_file = open("sql/tag.sql", encoding="utf-8", mode="w")
    sql_file.write(f'{insert_string[:insert_string.__len__()-3]} ON DUPLICATE KEY UPDATE EXT_ID = EXT_ID')
    sql_file.close()
