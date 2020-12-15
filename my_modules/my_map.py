
n = 42
# find square root of all integers up to n
# we can map a lambda function
roots = map(lambda x: x**0.5, range(1, n+1))
for root in roots:
    print(root)

def my_comp(): # here we have a list comprehension
    roots = [x**0.5 for x in range(1, n+1)]
    # print(type(roots))
    for root in roots:
        print(root)

def my_gen(): # here is a generator comprehension
    roots = (x**0.5 for x in range(1, n+1)) # a tuple results in a generator object
    # print(type(roots))
    for root in roots:
        print(root)

if __name__ == '__main__':
    my_comp()
    my_gen()