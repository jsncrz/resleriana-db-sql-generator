import time
from dataclasses import dataclass

@dataclass
class Translation:
    id: str
    language: str
    text: str
    create_date = time.strftime('%Y-%m-%d %H:%m:%S')
    
def create_sql_script(tls: list[Translation]):
    
    insert_tl_string = 'INSERT INTO `TRANSLATION`(`ID`,`LANGUAGE`,`TEXT`, `CREATE_DATE`) VALUES '
    for tl in tls:
        insert_tl_string += ("".join([
            f"('{tl.id}',\n\t",
            f"'{tl.language}',\n\t",
            f"'{tl.text}',\n\t",
            f"'{tl.create_date}'),\n\t"]))
    sql_file = open("sql/translation_chara.sql", encoding="utf-8", mode="w")
    sql_file.write(insert_tl_string[:insert_tl_string.__len__()-3])
    sql_file.close()
