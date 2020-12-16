import sqlite3

# we need a connection to the db
conn = sqlite3.connect('books_db') # creates if not exist

# now we can try to insert into the db
cur = conn.cursor()

cmd = '''
INSERT INTO book VALUES(1, 'Lovelace', 'Ada', 'ada@babbage.ie', 'without whom we would not have computers')
'''

try:
    cur.execute(cmd)
except:
    pass # we really should handle eceptions!
else:
    conn.commit()
finally:
    conn.close()