from functools import reduce


numbers = [1, 2, 3, 4, 5]

odd_numbers = reduce(lambda x, y: x + y, numbers)

print(odd_numbers)