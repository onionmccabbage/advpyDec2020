# make a filter with params for low and high facets

def lo_hi_filter(low, high):
    return lambda n: low <= n <= high

if __name__ == '__main__':
    lo = -4
    hi = 9
    nums = [-8, -2, 0, 5, 8, 3]
    filt = filter( lo_hi_filter(lo, hi), nums )
    for n in filt:
        print(n)