""" Factorial of 5:
5 * factorial(4) = 120
4 * factorial(3) = 24
3 * factorial(2) = 6
2 * factorial(1) = 2 """


def factorial(num):
    if num == 0:
        return 1

    return num * factorial(num - 1)


def iter_factorial(num):
    product = 1

    for num in range(num, 1, -1):
        product *= num
        print(product)


num = 5
print(factorial(num))
iter_factorial(num)
