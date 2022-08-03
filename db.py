import sqlite3 as sq

def sql_start():
    global base, cur
    base = sq.connect('personal_data.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK')
    base.execute('CREATE TABLE IF NOT EXISTS  personal_data(id TEXT PRIMARY KEY, '
                 'nickname TEXT, first_name TEXT, last_name TEXT)')
    base.commit()

async def sql_add_command(data):
    cur.execute('INSERT INTO personal_data VALUES(?,?,?,?)', tuple(data.values()))
    base.commit()
