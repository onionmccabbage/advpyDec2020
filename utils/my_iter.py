# we can iterate using custom generators which override next and iter

my_list = [1, 7, 11, 42]

list_iter = iter(my_list)

my_string = 'European unity is worth striving for'
str_iter = iter(my_string)

# we can create an iterable class
class Evens: # this implicitly inherits from object
    # we can override __ members of the class
    def __init__(self, limit):
        self.limit = limit
        self.val = 0
    def __iter__(self): # this factory method makes this class iterable
        return self
    def __next__(self):
        if self.val > self.limit:
            raise StopIteration
        else:
            rval = self.val
            self.val += 2
        return rval

# we can write a custom generator which will yield values
def make_evens(limit=0): # nb default value
    value = 0
    while value <= limit:
        yield value # the yield word indicates this is a generator
        value +=2

if __name__ == '__main__':
    print( str_iter.__next__() )
    print( str_iter.__next__() )
    print( str_iter.__next__() )
    for i in Evens(6):
        print(i)
    # make use of our custom generator
    for num in make_evens(10*100):
        print(num)

