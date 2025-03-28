import time
from datetime import datetime


class Character:
    type = 'CHARA'
    
    def __init__(self, acquisition_text, another_name, description, fullname, ext_id, is_alchemist, name, initial_rarity, release_date):
        self.acquisition_text = acquisition_text
        self.another_name = another_name
        self.description = description
        self.fullname = fullname
        self.ext_id = ext_id
        self.is_alchemist = is_alchemist
        self.name = name
        self.initial_rarity = initial_rarity
        self.release_date = datetime.fromisoformat(release_date).strftime('%Y-%m-%d %H:%m:%S')
        self.create_date = time.strftime('%Y-%m-%d %H:%m:%S')
        pass

def create_sql_script(charas: list[Character]):
    insert_chara_string = 'INSERT INTO `CHARACTER`(`ACQUISITION_TEXT`,`ANOTHER_NAME`,`DESCRIPTION`,`FULL_NAME`, `EXT_ID`,`IS_ALCHEMIST`,`NAME`, `INITIAL_RARITY`, `RELEASE_DATE`, `CREATE_DATE`) VALUES '
    for chara in charas:
        insert_chara_string += ("".join([
            f"('{chara.acquisition_text}',\n\t",
            f"'{chara.another_name}',\n\t",
            f"'{chara.description}',\n\t",
            f"'{chara.fullname}',\n\t",
            f"{chara.ext_id},\n\t",
            f"{chara.is_alchemist},\n\t",
            f"'{chara.name}',\n\t",
            f"{chara.initial_rarity},\n\t",
            f"'{chara.release_date}',\n\t",
            f"'{chara.create_date}'),\n\t"]))
    sql_file = open("sql/character.sql", encoding="utf-8", mode="w")
    sql_file.write(insert_chara_string[:insert_chara_string.__len__()-3])
    sql_file.close()
