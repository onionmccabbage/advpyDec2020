import doctest

def square_list(a,b):
    '''
    return the squares of all numbers in range a to b
    >>> square_list(1, 10) # doctest:+ELLIPSIS +NORMALIZE_WHITESPACE
    [1,4, ..., 100]
    '''
    answer = []
    for i in range(a, b+1):
        answer.append(i*i)
    return answer

if __name__ == '__main__':
    doctest.testmod(verbose=True)