# using filter

def between(n): # this can be used as a filter function
    # we only want those values between 10 and 20
    return 10<= n <= 20 # True or False

if __name__ == '__main__':
    between(3) # False
    between(13) # True
    values = [-3, 4, 8, 11, 13, 17, 17, 17, 18, 13, 21, 31, 99999]
    f = filter(between, values)
    for n in f:
        print(n)