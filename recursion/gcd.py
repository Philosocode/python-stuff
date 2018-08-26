def gcd(a, b):
    r = a % b
    if r == 0:  # Divisor found
        return b
    elif r == 1:
        return 1
    return gcd(b, r)


print(gcd(55, 72))


def iter_gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


print(iter_gcd(5, 10))
