import time
from dataclasses import dataclass

@dataclass
class Translation:
    id: str
    language: str
    text: str
    create_date = time.strftime('%Y-%m-%d %H:%m:%S')
    
def __translation_key_sql(tl_ids: list[str], file_name: str, language: str):
    insert_string = 'INSERT INTO translation_keys(id) VALUES '
    for tl_id in tl_ids:
        insert_string += ("".join([
            f"('{tl_id}'),\n\t"]))
    sql_file = open(f"sql/{language}/{file_name}_key.sql", encoding="utf-8", mode="w")
    sql_file.write(f'{insert_string[:insert_string.__len__()-3]} ON CONFLICT DO NOTHING')
    sql_file.close()
    
def tl_sql(tls: list[Translation], file_name: str, language: str):
    insert_string = 'INSERT INTO translations(id,lang_code,translated_text, create_date) VALUES '
    tl_ids = []
    for tl in tls:
        if tl.id not in tl_ids:
            tl_ids.append(tl.id)
        insert_string += ("".join([
            f"('{tl.id}',\n\t",
            f"'{tl.language}',\n\t",
            f"$${tl.text}$$,\n\t",
            f"'{tl.create_date}'),\n\t"]))
    __translation_key_sql(tl_ids, file_name, language)
    sql_file = open(f"sql/{language}/{file_name}.sql", encoding="utf-8", mode="w")
    sql_file.write(f'{insert_string[:insert_string.__len__()-3]} ON CONFLICT DO NOTHING')
    sql_file.close()
