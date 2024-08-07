import sqlite3

conn = sqlite3.connect('userData.db')

tabelCreationQuerry = """
create table email(messege varchar(300),result varchar(10))
"""
cur = conn.cursor()
cur.execute(tabelCreationQuerry)
print('table created successfully')
cur.close()
conn.close()