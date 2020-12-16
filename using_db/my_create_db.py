import sqlite3

# we need a connection to the db
conn = sqlite3.connect('books_db') # creates if not exist

# now we can create a table within the db
cur = conn.cursor()
cmd = '''
CREATE TABLE book (
id int primary key,
surname varchar(60),
firstname varchar(60),
email varchar(60),
notes text
)
'''
cur.execute(cmd)
conn.commit() # this is the moment when the command is commited to the db

# clean up when done
conn.close()