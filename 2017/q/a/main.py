def calc_flips(pancakes, k):
    i = 0
    flips = 0
    while i < len(pancakes):
        pancake = pancakes[i]
        if pancake == 1:
            i += 1
            continue

        # impossible
        if len(pancakes) < i + k:
            return -1

        # flip from i and k pancakes in front
        for j in range(k):
            pancakes[i + j] = (pancakes[i + j] + 1) % 2

        # next pancake
        flips += 1
        i += 1
    return flips

with open('intext.txt') as f:

    # skip first int
    f.readline()

    # loop all lines
    for i, line in enumerate(f):

        # split s and k
        s, k = line.strip().split(' ')

        # convert to 0,1 instead of '-','+'
        pancakes = [0 if i == '-' else 1 for i in s]
        k = int(k)

        # lets do the flippiliflippp
        flips = calc_flips(pancakes, k)

        answer = flips
        if answer == -1:
            answer = 'IMPOSSIBLE'

        print('case #{}: {}'.format(i+1, answer))
