from collections import defaultdict

p_table = defaultdict(int)
p_table['Hydrogen'] = 1
p_table['Helium'] = 2
p_table['Lithium'] = 3
p_table['Berilium'] = 4

# try adding a member with no number
p_table['Unobtanium'] # this will have defalt value of 0

print(p_table)

# another example
def no_idea():
    return 'Huh?'

things = defaultdict(no_idea)
things['A'] = 'Abominable Snowman'
things['B'] = 'Basilisk'
print(things['A']) # 'Abominable Snowman'
print(things['B']) # 'Basilisk'
print(things['C']) # 'Huh?'
