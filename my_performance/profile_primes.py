# explore two ways to find prime numbers
# then run profiling code against them to see which is more performant
# we use cProfile for this

def find_primes_1(number_of_primes):
    primes = [1, 2]
    number = 3
    while len(primes) < number_of_primes:
        for divisor in range(2, number//2+1):
            if number % divisor == 0:
                break
        else: # for ...else!!!
            primes.append(number)
        number +=1
    return primes

def find_primes_2(number_of_primes):
    primes = [1, 2]
    number = 3
    while len(primes) < number_of_primes:
        for divisor in range(2, int(number**0.5)+1 ):
            if number % divisor == 0:
                break
        else:
            primes.append(number)
        number +=1
    return primes


if __name__ == '__main__':
    # to profile any code:
    # python -m cProfile -o profile_output profile_primes.py
    find_primes_1(10000) # takes about 16 seconds
    find_primes_2(10000) # takes under half a second