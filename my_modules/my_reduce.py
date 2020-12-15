from functools import reduce # reduce is part of the functional programmnig tools

# using reducers
def add_r(x, y):
    return x+y

if __name__ == '__main__':
    print(reduce(add_r, range(1, 99, 3))) # start at 1, stop at 98, every third member
    print( reduce( lambda x, y: x * y, range(1,6) ) )