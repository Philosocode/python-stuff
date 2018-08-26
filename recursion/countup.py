# add(3): 3 + add(2) = 6
# add(2): 2 + add(1) = 3
# add(1): 1 + add(0) = 1
# add(0): 0


def add(num):
    if num == 0:
        return 0

    return num + add(num - 1)


def add_up(n):
    if n == 100:
        return 100
    return n + add_up(n + 1)


def iter_add(num):
    total = 0

    for i in range(1, num + 1):
        total += i
        print(total)


# Add all numbers up to num
#  print(add(3))
#  iter_countup(3)
add_up(0)
