import sys

def primes_upto(limit):
    is_prime = [False] * 2 + [True] * (limit - 1)
    for n in range(int(limit**0.5 + 1.5)): # stop at ``sqrt(limit)``
        if is_prime[n]:
            for i in range(n*n, limit+1, n):
                is_prime[i] = False
    return [i for i, prime in enumerate(is_prime) if prime]

primes = primes_upto(10**8)
# print(primes)
def get_factor(n, primes):
    for prime in primes:
        if n % prime == 0:
            return prime
    return False

for x in range(int(input())):

    _ = input() # skip this line
    l = list(map(int, input().split(' ')))

    factor = get_factor(l[0], primes)
    print(l)
    print(factor)

print(len(l))
print(l)
