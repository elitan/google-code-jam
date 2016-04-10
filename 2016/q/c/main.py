#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from baseconv import BaseConverter
from math import sqrt
from time import sleep

def find_next_prime(a, n, top):
    n += 1
    try:		
        while a[n] != 2:
            n += 1
    except:
        return top
    return n


def prime_list(top):
    primes = []
    a = [2] * top
    a[0] = 0
    a[1] = 0
    a[2] = 1
    p = 2

    while p < top:
        a[p] = 1
        for n in range(p*2, top, p):
            a[n] = 0
        p = find_next_prime(a, p, top)

    for p in range(0, top):
        if a[p] == 1:
            primes.append(p)

    return primes

def find_prime_fact(f, primes):
    f = int(f)
    for p in primes:
        if p >= f:
            return False
        if f / p == int(f / p):
            return p
    return False

def is_jam_coin(f, base, primes, res):
    conv = BaseConverter(('').join(map(str, [ tmp for tmp in range(0, base) ])))
    f = int(conv.decode(f))
    if base == 10:
        factor = find_prime_fact(f, primes)
        if factor:
            res.append(factor)
            return True
        else:
            return False

    factor = find_prime_fact(f, primes)
    if factor:
        res.append(factor)
        return is_jam_coin(conv.encode(f), base+1, primes, res)
    else:
        return False

def main():
    for t in range(int(input())):

        print('Case #%d:' % (t + 1))
        n, j = map(int, input().split(' '))
        #print(('').join(map(str, [ tmp for tmp in range(0, x) ])))
        #conv = BaseConverter(('').join(map(str, [ tmp for tmp in range(0, x) ])))
        #s = ('%s1' % (('').join(map(str, [0 for tmp in range(0, n-2)]))))
        b2 = BaseConverter('01')
        f = b2.encode(pow(2, n-1) + 1)
        f = pow(2, n-1) + 1
        
        found = 0
        primes = prime_list(1000)
        
        while found < j:
            res = []
            if is_jam_coin(b2.encode(f), 2, primes, res):
                print('%s %d %d %d %d %d %d %d %d %d' % (b2.encode(f), res[0], res[1], res[2], res[3], res[4], res[5], res[6], res[7], res[8]))
                found += 1
            f += 2


if __name__ == "__main__":
    main()
