# there are several data constructs in Python

# scalars
n = 3
m = 3.0
p = 7

print(n/m, p//n)
# also None, True, False

# collections
# most collections are indexed, starting from zero
stri = '''hello and "welcome" to 
this     course''' # single double or tripple quotes
print(stri[1:4])
l = []
t = (1,) # comma needed if only one member

# other collections are UNORDERED, such as set, frozenset and dict
s = set(['Athlone', 'Athenry', 'Dublin'])

f = frozenset(['Athlone', 'Athenry', 'Dublin'])
print(type(f))

