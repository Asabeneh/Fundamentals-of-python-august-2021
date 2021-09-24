# Higher order functions take another function as a parameter
# Higher order function return another function as a parameter

def make_square(n):
    return n ** 2


def make_cube(func, n):
    return func(n) * n

print(make_cube(make_square, 10))
print(make_cube(make_square, 2))
print(make_cube(make_square, 3))

def hof(n):
    def add_ten():
        return n  + 10
    return add_ten()

print(hof(100))

# Functional Programming : map, filter, reduce
# 
nums = [1, 2, 3, 4, 5] #[1, 4, 9, 16, 25]

new_nums = map(lambda x : x ** 2, nums)
print(list(new_nums))

countries = ['Finland','Sweden','Denmark','Norway','Iceland']

countries_code = map(lambda c: (c, c.upper(), c.upper()[:3]), countries)
print(list(countries_code))
print([(c, c.upper(), c.upper()[:3]) for c in countries])

# Filter

print(list(filter(lambda n : n % 2 == 0, nums)))
print(list(filter(lambda c: 'land' in c, countries)))
print(list(filter(lambda c: 'land' not in c, countries)))
print([c for c in countries if 'land' in c])

# reduce => 

from functools import reduce
total = reduce(lambda x, y: x * y, nums)
print(total)
