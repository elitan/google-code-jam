#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def main():
    i = 1
    for x in range(int(input())):
        s_win = ''
        s = input()

        s_win = s[0]
        high = low = ord(s_win)
        s = s[1:]
        for l in s:
            if ord(l) < high:
                s_win += l
                low = ord(l)
            else:
                s_win = "%s%s" % (l, s_win)
                high = ord(l)
            
        print("Case #%d: %s" % (i, s_win))
        i += 1



if __name__ == '__main__':
    main()
