import sqlite3
# import pickle
# import datetime
# import json
import doctest

# open a conection to a db
conn = sqlite3.connect('zoo.db') # create if not exist
cur = conn.cursor() # cursor lets use use the db
def createDatabaseTable():
    # here I chose to make hte animal type the unique primary key
    statement = '''CREATE TABLE zoo 
    (creatures VARCHAR(64) PRIMARY KEY,
    count INT, 
    damages FLOAT)'''
    cur.execute(statement)

def InitialPopulateTable():
# populate the table (CREATE)
    try:
        st = '''INSERT INTO zoo VALUES("goose", 3, 0.0)'''
        cur.execute(st)
        st = '''INSERT INTO zoo (creatures, count, damages) VALUES(?, ?, ?)'''
        cur.execute(st, ('egret', 5, 2000.00))
        cur.execute(st, ('panda', 19, 1000000.00))
    except Exception as err:
        print(err)
    finally:
        # we must tell the db we actually wish to commit the changes!
        conn.commit()

def loadFromJson():
# load up the animals from json
    cmd_str = '''
    INSERT INTO zoo (creatures, count, damages) VALUES(?, ?, ?) 
    '''
    with open('animals.json', 'r') as animals_j: 
        animals_l = json.load(animals_j) # it's a list
        for animal in animals_l: # iterate over the list to get the dictionaries
            animal_props_list = []
            for key, value in animal.items(): # not actually using key in this case
                animal_props_list.append(value)
            cur.execute(cmd_str, animal_props_list)
    conn.commit()

# read the data back
def doShowAll():
    '''
    Read all data from the database snd print it all out nicely
    >>> doShowAll()
    [('panda', 19, 1000000.0), ('goose', 3, 0.0)]
    '''
    st = '''SELECT * FROM zoo ORDER BY count DESC'''
    cur.execute(st)
    # use the cursor we have
    rows = cur.fetchall()
    print(rows)

def doInsert():
    animal = ''
    quantity = -1
    damages = -1
    while animal =='':
        animal = input('Animal type? ')
    while quantity<0:
        quantity = int(input('how many? '))
    while damages <0:
        damages = float(input('maintenance cost? '))
    cmd_str = '''
    INSERT INTO zoo (creatures, count, damages) VALUES(?, ?, ?) 
    '''
    cur.execute(cmd_str, [animal, quantity, damages])
    conn.commit()

def doUpdate():
    whichAnimal = ''
    while whichAnimal == '':
        whichAnimal = input('Which animal to update? ')
    quantity = -1
    cost = -1
    while quantity<0:
        quantity = int(input('how many now? '))
    while cost <0:
        cost = float(input('new maintenance cost? '))
    cmd_str = f'''
    UPDATE zoo
    SET count={quantity}, damages={cost}
    WHERE creatures = '{whichAnimal}'
    '''
    cur.execute(cmd_str)
    conn.commit()

def doDelete():
    deleteWhich = ''
    while deleteWhich=='':
        deleteWhich = input('Delete which animal? ')
    cmd = f'''
    DELETE from zoo where creatures = '{deleteWhich}'
    '''
    cur.execute(cmd) # we really should check 'are you sure?'
    conn.commit()


if __name__ == '__main__':
    # run any doctests
    doctest.testmod(verbose=True)

    # ask user for a choice
    choice = 4
    while  1 <= choice <= 4:
        choice = int(input('Choose: 1 insert, 2 update, 3 delete 4 retrieve all 5 quit'))
        if choice==  1:
            doInsert()
        elif choice == 2:
            doUpdate()
        elif choice == 3:
            doDelete()
        elif choice == 4:
            doShowAll()
        else:
            print('bye')
            break

# remember to clean up by closing connections and dropping cursors
cur.close() 
conn.close()