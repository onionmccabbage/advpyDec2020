# exploring timings

def fib(n):
    if n <=1:
        return n
    else:
        return( fib(n-1) + fib(n-2) )

if __name__ == '__main__':
    # platform dependant timing
    import time # this can accurately measure moments for the whole system
    start = time.time() # take a snapshot of the moment we begin
    print(fib(35))
    end = time.time() # we're done
    delta = end-start
    print(f'Time to complete: {delta} seconds')

    # platform independent timing
    from timeit import default_timer # this is Python-aware, measures those moments used by Python
    start = default_timer()
    print(fib(35))
    end = default_timer()
    delta = end-start
    print(f'Time to complete: {delta} seconds')

