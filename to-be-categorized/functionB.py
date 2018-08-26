def function_b(b_list, high_num):
    c_list = [0, 0, 0, 0, 0, 0, 0]
    i = 0
    for num in b_list:  # [1, 3, 6, 4, 1, 2, 8]
        if num > high_num:
            # If b_list num > 4:
            # change c_list[i] to that num
            c_list[i] = num
        i = i + 1
    b_list = c_list


def main():
    b_list = [1, 3, 6, 4, 1, 2, 8]
    high_num = 4
    function_b(b_list, high_num)
    print(b_list)
    """
    Okay, so the reason b_list doesn't change is
    because we never modify the list at ID:1234.

    Let's forget b_list.
    We have a list @ 12345.
    In the function, we re-direct it, to list @ 123456
    There are really 2 different lists: 12345 and
    123456

    In function_a, we modify list 12345 directly.
    In function_b, we don't do this.
    That's why it stays the same.
    Rather than modifying the list values directly,
    we just say, "hey, here's the reference number
    for this new list", and so the inital list's
    values stay the same.
    """


main()
