import numpy as np


def primes_sieve(n):
    limit = n + 1
    not_prime = {1}
    primes = []

    for i in range(2, limit):
        if i in not_prime:
            continue

        for f in range(i * 2, limit, i):
            not_prime.add(f)

        primes.append(i)

    return primes


def nth_prime(n):
    i = 2
    count = 0
    not_prime = {1}
    maxsize = 1000000

    while True:

        if i in not_prime:
            continue

        for f in range(i * 2, maxsize, i):
            not_prime.add(f)

        if count == n:
            break
        else:
            print("{} {}".format(i, count))
            count += 1
        i += 1

    return i

def prime_factors(n):
    factor = [1]
    primes = primes_sieve(int(np.sqrt(n)))
    for prime in primes:
        if prime % n == 0:
            factor.append(prime)

    return factor[-1]


#print(nth_prime(10001))
#print(sum(primes_sieve(2000000)))
#primes = primes_sieve(1000000)
#print(primes[10000])
print(prime_factors(600851475143))
