#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    for i, x in enumerate(range(int(input())), 1):
        sleep_set = set() # must contain all 0-9 before falling asleep
        n_prev = -1
        start_n = n = int(input())
        if start_n == 0:
            print('Case #%d: INSOMNIA' % (i))

        while len(sleep_set) < 10:
            for x in str(n):
                sleep_set.add(int(x))
            n += start_n
        
        print('Case #%d: %s' % (i, n - start_n))


if __name__ == "__main__":
    main()
