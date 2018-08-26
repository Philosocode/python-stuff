# def square_numbers(nums):
#     for i in nums:
#         yield (i * i)


# my_nums = square_numbers([1, 2, 3, 4, 5])

my_nums = (x * x for x in [1, 2, 3, 4, 5])
list_nums = list(my_nums)

print(list_nums)
