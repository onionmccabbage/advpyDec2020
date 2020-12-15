import sys
# sys.path.append() # we could add extra places for python to look

entry = input('Enter name and age ') # assume a comma
fn, age = entry.split(', ')
if not fn.isalpha():
    print(f'{fn} needs to be alphabetic')
    sys.exit(-1)
if not age.isdigit():
    print(f'{age} needs to be numeric')
    sys.exit(-1)
print(fn, age)