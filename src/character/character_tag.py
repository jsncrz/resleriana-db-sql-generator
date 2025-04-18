import time
from dataclasses import dataclass

@dataclass
class Character_Tag:
    character_id: str
    tag_id: str
    create_date = time.strftime('%Y-%m-%d %H:%m:%S')

def char_tag_sql(character_tags: list[Character_Tag]):
    insert_string = 'INSERT INTO `CHARACTER_TAG`(`CHARACTER_ID`,`TAG_ID`,`CREATE_DATE`) VALUES '
    for tag in character_tags:
        insert_string += ("".join([
            f"({tag.character_id},\n\t",
            f"'{tag.tag_id}',\n\t",
            f"'{tag.create_date}'),\n\t"]))
    sql_file = open("sql/character_tag.sql", encoding="utf-8", mode="w")
    sql_file.write(f'{insert_string[:insert_string.__len__()-3]} ON DUPLICATE KEY UPDATE CHARACTER_ID = CHARACTER_ID')
    sql_file.close()
