def countDown(n):
    if n == 0:
        return

    print("Count: {}".format(n))

    return countDown(n - 1)


def iter_countDown(n):
    while n > 0:
        print(n)
        n -= 1


#  countDown(5)
iter_countDown(5)
''' countDown(5)
Count: 5
coundDown(4)
Count: 4
countDown(3)
Count: 3
countDown(2)
Count: 2
countDown(1)
Count: 1
countDown(0)
if n == 0: stop
'''
