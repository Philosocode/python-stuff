# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# REGULAR
# my_list = []
# for n in nums:
#     my_list.append(n)
# print(my_list)

# COMPREHENSION
# my_list = [n for n in nums]
# print(my_list)

# my_list = [n * n for n in nums]

# REGULAR:
# for n in nums:
#     if n % 2 == 0:
#         my_list.append(n)

# COMPREHENSION
# my_list = [n for n in nums if n % 2 == 0]

# my_list = [(letter, num) for letter in 'abcd' for num in range(4)]

# print(my_list)

# names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
# heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

# my_dict = {name: hero for name, hero in zip(names, heroes)}

# print(my_dict)

nums = [1, 1, 1, 1, 2, 1, 3, 4, 5, 5, 6, 7, 8, 9, 9]
# my_set = set()
# for n in nums:
#     my_set.add(n)

my_set = {n for n in nums}

print(my_set)
