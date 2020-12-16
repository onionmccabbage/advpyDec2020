import sqlite3

# we need a connection to the db
conn = sqlite3.connect('books_db') # creates if not exist

# now we can try to insert into the db
cur = conn.cursor()
# declare some data members
b1 = [2, 'Climate', 'Greta', 'warm@chilly.se', 'bit of a hero']
b2 = [3, 'GGG', 'Timnit', 'ex@google.com', 'general good bod' ]
b3 = [4, 'Miller', 'Gina', 'problem@gov.uk', '.....']
# id, surname, fname, email, notes
cmd_str = '''
INSERT INTO book VALUES(?, ?, ?, ?, ?) 
'''

# consider injecting ' where 0=0 drop table - that is dangerous!!!

try:
    for user in [b1, b2, b3]:
        cur.execute(cmd_str, user)
except:
    pass # we really should handle eceptions!
else:
    conn.commit()
finally:
    conn.close()