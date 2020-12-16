import sqlite3
conn = sqlite3.connect('books_db')
cur = conn.cursor()

# retrieve data
cmd = '''
SELECT * FROM book
'''
cur.execute(cmd) # no need to commit since db is unaltered

for row in cur.fetchall(): # members are retrieved into an (indexed) tuple
    print(  f'Row {row[0]} {row}'  )

conn.close()