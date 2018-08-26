#  my_sum = 0

#  for i in range(101):
    #  my_sum += i

#  print(my_sum)


def get_total(num, my_sum):
    if num == 0:
        return my_sum
    return get_total(num - 1, num + my_sum)


print(get_total(5, 0))
