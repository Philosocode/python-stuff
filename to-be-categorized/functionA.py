def function_a(a_list, high_num):
    for i in range(len(a_list)):  # range 7
        # if EL in a_list is greater than high_num,
        # increment the EL by 1
        # otherwise, make it 0
        if a_list[i] > high_num:
            a_list[i] = a_list[i] + 1
        else:
            a_list[i] = 0
        # [0, 0, 7, 0, 0, 0, 9]
    high_num = 0


def main():
    list_1 = [1, 3, 6, 4, 1, 2, 8]
    my_num = 4
    function_a(list_1, my_num)
    print(list_1)
    print(my_num)


main()
