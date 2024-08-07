import sqlite3

conn = sqlite3.connect('userData.db')

fetchQuerry = """
select * from email
"""
cur = conn.cursor()
cur.execute(fetchQuerry)
output = cur.fetchall()
i = 0
for row in output:
    print(i," ",row)
    i += 1
cur.close()
conn.close()