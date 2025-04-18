def append_sql_files(scripts:list[str], appended_filename: str):
    sql_script = ''
    sql_scripts = scripts
    for script in sql_scripts:
        with open(f'sql/{script}.sql', encoding="utf8") as f:
            data = f.read()
        f.close()
        sql_script += '\n'
        sql_script += data + ';'
    with open (f'sql/{appended_filename}.sql', mode='w', encoding="utf8") as f:
        f.write(sql_script)
    f.close()
    
def str_format(obj_col):
    if obj_col is None:
        return ''
    elif isinstance(obj_col, str):
        return obj_col.replace("'", "\\'")
    return obj_col

def get_attribute_string(attack_attribute):
    if attack_attribute == 1:
        return 'SLASH'
    elif attack_attribute == 2:
        return 'STRIKE'
    elif attack_attribute == 3:
        return 'STAB'
    elif attack_attribute == 5:
        return 'FIRE'
    elif attack_attribute == 6:
        return 'ICE'
    elif attack_attribute == 7:
        return 'BOLT'
    elif attack_attribute == 8:
        return 'AIR'
    
def get_role_string(role):
    if role == 1:
        return 'ATTACKER'
    elif role == 2:
        return 'BREAKER'
    elif role == 3:
        return 'DEFENDER'
    elif role == 4:
        return 'SUPPORTER'