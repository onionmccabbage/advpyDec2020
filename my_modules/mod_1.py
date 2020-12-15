# modules can expose reuseable code

def askForInt():
    my_int = ''
    while not my_int.isdigit():
        my_int = input('Enter a number ')
    my_int = int(my_int)
    return my_int

# local code exercising
if __name__ == '__main__':
    age = askForInt()
    print( type(age), age)
    