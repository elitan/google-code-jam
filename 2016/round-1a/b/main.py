#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def main():
    for t in range(int(input())):
        n = int(input())
        for rowcol in range(2 * n - 1):
            print(input())

if __name__ == '__main__':
    main()
