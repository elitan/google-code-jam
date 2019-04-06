# if 4. Make it a '3' and the corresponding digit a '1' at number B
lines = int(input())

for x in range(lines):
    n_str = input()

    a = ''
    b = ''
    for i, l in enumerate(n_str):
        if l == '4':
            b += '3'
            a += '1'
        else:
            b += l
            a += '0'

    a = int(a)
    b = int(b)
    case = x + 1
    print('Case #{}: {} {}'.format(case, a, b))
