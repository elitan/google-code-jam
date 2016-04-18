#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import copy

def main():
    for t in range(int(input())):
        print(t)
        n = int(input())
        colrow = []
        for x in range(2 * n - 1):
            colrow.append(list(map(int, input().split(' '))))
        colrow_copy = copy.deepcopy(colrow)


        # initiate main grid
        main_grid = [[0 for x in range(n)] for x in range(n)]

        # find top row
        lowest = colrow[0][0]
        lowest_index = 0
        for i, row in enumerate(colrow):
            if row[0] < lowest:
                lowest = row[0]
                lowest_index = i

        # initiate first column
        for i, num in enumerate(colrow[lowest_index]):
            main_grid[i][0] = num
        del colrow[lowest_index]

        print('start colrow')
        for row in colrow:
            print(row)
        print('end colrow')
        print('start main grid')
        for row in main_grid:
            print(row)
        print('end main grid')


        # for each number in the column, find a row
        for r in range(n):
            # the number we are looking for in the col
            looking_for = main_grid[r][0]

            # find the corresponding column
            for i, row in enumerate(colrow):
                if row[0] == looking_for:
                    print('found')
                    print(row)
                    main_grid[r] = copy.deepcopy(row)
                    del colrow[i]
                    break
         


        # rotate 90 degrees counter clockwise
        cc = [[0 for x in range(n)] for x in range(n)]
        for r, row in enumerate(main_grid):
            for i, n in enumerate(row[::-1]):
                cc[i][r] = n

        print('start main grid')
        for row in main_grid:
            print(row)
        print('end main grid')

        # now, find what row does not exists in the original.
        for row in cc:
            if row not in colrow_copy:
                print('Case #%d: %s' % (t+1, ' '.join(list(map(str, row)))))
                break



if __name__ == '__main__':
    main()
