# exploring closure

def knights(saying):
    def inner(): # a closure
        return f'we are the knights who say {saying}'
    return inner # note - no brackets so we are not invoking the method

if __name__ == '__main__':
    ni = knights('Ni')
    eh = knights('eh')
    # take a look at the objects
    print(ni, eh)
    # invoke the closure
    print(ni(), eh())
