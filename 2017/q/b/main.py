# make sure all digits in the number is
# staying the same value or incrising
# when checking digits left to right
def tidy(n):
    for i in range(len(n) - 1):
        if n[i] > n[i + 1]:
            return False
    return True

# since a, and b (b = n[i]) int tidy
# we need to lower a one and bump b to 9
def lower(n, i):
    a = n[i - 1]
    n[i - 1] = a - 1
    n[i] = 9

def last_tidy(n):
    n = list(map(int, list(str(n))))
    i = len(n) - 1

    while not tidy(n):
        lower(n, i)
        i -= 1
    n = list(map(str, n))
    return int(''.join(n))


with open('B-large.in') as f:
    f.readline()
    for i, line in enumerate(f):
        n = int(line.strip())
        print('case #{}: {}'.format(i+1, last_tidy(n)))
