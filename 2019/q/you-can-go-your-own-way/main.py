# just mirror the grid horizontally
lines = int(input())

for line_n in range(lines):
    steps_n = int(input())
    steps = input()

    x,y = 0,0

    my_steps = ''
    last_cut = 0

    for steps_i, step in enumerate(steps):
        if step == 'E':
            y += 1
        else:
            x += 1

        if x == y:
            my_steps += steps[last_cut:steps_i + 1][::-1]
            last_cut = steps_i + 1

    case = line_n + 1
    print('Case #{}: {}'.format(case, my_steps))
