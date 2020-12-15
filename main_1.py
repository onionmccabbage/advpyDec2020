# the main module can import from other modules
from my_modules.mod_1 import askForInt

if __name__ == '__main__':
    a = askForInt()
    print (f'{a} years old')