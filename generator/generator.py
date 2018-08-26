def square_numbers(nums):
    for i in nums:
        yield(i * i)


square_list = square_numbers([1, 2, 3, 4, 5])

for num in square_list:
    print(num)

