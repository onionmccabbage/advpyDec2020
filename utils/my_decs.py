# we can use decorator functions on other functions
def my_decorator(fn):
    print('decorator called')
    print(id(fn))
    return fn

def trace(fn): # args are positional (0, 1, ...) kwargs are keyword dictionary of arguments
    def enhance(*args, **kwargs): # * unpacks the ordinals into a tuple, ** unpacks the keywords into a dict
        print(f'calling fn with {args}, {kwargs}')
        if len(args)==0:
            return fn(kwargs['x'])
        else:
            return fn(args[0])
    return enhance

@my_decorator # decorators are called IN ORDER
@trace
def square_it(x):
    return x*x

@trace
@my_decorator
def cube_it(x):
    return x*x*x


if __name__ == '__main__':
    print(square_it(x=7))
    print(cube_it(3))