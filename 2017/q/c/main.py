import sys


def update_bathroom(bathrooms, min_list, max_list, i):

    # skip if occupied, no need to know l nor r
    if bathrooms[i][0] == 1:
        return
    # check left
    i_left = i - 1
    l = 0
    while bathrooms[i_left][0] != 1:
        i_left -= 1
        l += 1

    # check right
    i_right = i + 1
    r = 0
    while bathrooms[i_right][0] != 1:
        i_right += 1
        r += 1

    # update
    bathrooms[i] = [0, l, r]
    min_list[i] = min(l, r)
    max_list[i] = max(l, r)

def update_bathrooms(bathrooms, min_list, max_list, from_index):
    # first update min and max list of current index
    min_list[from_index] = -1
    max_list[from_index] = -1
    # update left
    i_left = from_index - 1
    while bathrooms[i_left][0] != 1:
        update_bathroom(bathrooms, min_list, max_list, i_left)
        i_left -= 1

    i_right = from_index + 1
    while bathrooms[i_right][0] != 1:
        update_bathroom(bathrooms, min_list, max_list, i_right)
        i_right += 1


def update_min_max_list(bathrooms, min_list, max_list):
    for i, bathroom in enumerate(bathrooms):

        # skip if occupied
        if bathroom[0] == 1:
            min_list[i] = -1
            max_list[i] = -1
            continue

        # calc current min value
        update_specific_min_max_list_item(bathrooms, min_list, max_list, i)

def update_specific_min_max_list_item(bathrooms, min_list, max_list, i):
        bathroom = bathrooms[i]
        l, r = bathroom[1], bathroom[2]
        min_list[i] = min(l, r)
        max_list[i] = max(l, r)

def get_occupy_index(bathrooms, min_list, max_list):
    max_min = max(min_list)
    n_max_min = min_list.count(max_min)

    if n_max_min == 1:
        return min_list.index(max_min)

    # else, move on to find the max of those mins
    max_min_indexes = []
    for i, min_value in enumerate(min_list):
        if min_value == max_min:
            max_min_indexes.append(i)

    max_max = max([max_list[i] for i in max_min_indexes])
    n_max_max = max_list.count(max_max)

    if n_max_max == 1:
        return max_list.index(max_max)

    # else, move on to find the left most index of those maxs
    for i, max_v in enumerate(max_list):
        if max_max == max_v:
            return i


# a bathrooms is represented by [o, l, r]
# o = 0 if not occupied, 1 if occupied
# l = number of empty stalls left of the bathroom
# r = number of empty stalls right of the bathroom
with open('C-small-1-attempt3.in') as f:
    f.readline()
    for case_index, line in enumerate(f):
        n, k = list(map(int, line.strip().split(' ')))
        bathrooms = []
        min_list = [-1 for x in range(n + 2)]
        max_list = [-1 for x in range(n + 2)]

        for i in range(n):
            bathrooms.append([0, 0, 0])

        # insert first and last occupied bathrooms
        bathrooms.insert(0, [1, 0, 0])
        bathrooms.append([1, 0, 0])

        # calculate l and r of all bahtrooms
        for i in range(len(bathrooms)):
            update_bathroom(bathrooms, min_list, max_list, i)

        # init min and max list

        update_min_max_list(bathrooms, min_list, max_list)

        for i in range(k):
            index = get_occupy_index(bathrooms, min_list, max_list)
            l, r = bathrooms[index][1], bathrooms[index][2]
            bathrooms[index] = [1, l, r]

            # update calculate l and r of all bahtrooms
            update_bathrooms(bathrooms, min_list, max_list, index)
            #update_min_max_list(bathrooms, min_list, max_list)

        print('case #{}: {} {}'.format(case_index + 1, max(l, r), min(l, r)))
