import pickle
import datetime
import json

# create a complex data structure
now = datetime.datetime.utcnow()
print(type(now))
pickled = pickle.dumps(now) # dump would write to a given file, dumps just converts it to a pickled object
print(type(pickled))
# we could persist this pickled data, store it in a file, send over http etc.
# later we can retireve
retrieved = pickle.loads(pickled)
print(pickled, type(retrieved), retrieved)

class Tiny:
    def __init__(self):
        pass
    def __str__(self):
        return 'this is the Tiny class'

t = Tiny()
pickled_t = pickle.dumps(t)

r = pickle.loads(pickled_t)
print(r) # uses the __str__ method

# we can open a fiile for access
# 'r' to read, 'w' to (over)write 'a' append
# 't' for text (default) (e.g. 'rt') and 'b' for bytes (e.g. 'wb')
f = open('users.json', 'r') # if we just open, we MUST close
print(type(f))
f.close() # tidy up

# now lets load some json
with open('users.json', 'r') as users_j: # using with will ALWAYS close when done
    users_d = json.load(users_j) # make it into a dict by loading teh file
    print(type(users_d), type(users_j))

    for key, value in users_d.items():
        print( f'{key}:{value}' )

    # convert back to json
    j = json.dumps(users_d)
    print(j)
# no need to close, since 'with' will auto close the file when done