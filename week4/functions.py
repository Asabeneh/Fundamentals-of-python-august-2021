# What is a function? It is a block of codes that allow us to do some operations
# What is a the purpose of functions? it is easy to reuse, it is easy to test

def add_two_numbers(a, b):
    return a + b

print(add_two_numbers(3, 1))
print(add_two_numbers(3, 7))
print(add_two_numbers(3, 97))
print(add_two_numbers(3, 22))


def print_fullname(firstname, lastname):
    return firstname + ' ' + lastname


print(print_fullname('Donald','Trump'))
print(print_fullname('Barack','Obama'))
print(print_fullname('Bills','Gates'))
print(print_fullname('Steve','Jobs'))


def sum_all_nums(n):
    total = 0
    for i in range(n+1):
        total +=  i
    return total

print(sum_all_nums(5)) # 0, 1, 2, 3, 4, 5
print(sum_all_nums(10)) # 0, 1, 2, 3, 4, 5,6, 7, 8,9, 10
print(sum_all_nums(1000))

# calculate the area of a circle

def calculate_circle_area(r):
    area = 3.14 * r * r
    return area

print(calculate_circle_area(10))
print(calculate_circle_area(50))

# calculate the weight of an object in any planet w  = mass * gravity

def calculate_weight(mass, gravity = 9.81):
    weight = mass * gravity
    return weight

print(calculate_weight(75))
print(calculate_weight(75, 1.6))
print(calculate_weight(75, 3.7))

def sum_numbers(value, *args):
    print('We can pass' + value)
    total = 0
    for n in args:
        total += n
    return total

print(sum_numbers('Some Argument', 1, 2, 2, 4, 9, 10))


countries = ['Finland','Sweden','Denmark','Norway','Iceland']



def revese_list_func(lst):
    reveresed_lst = []
    for i in range(len(lst) - 1, -1, -1):
        reveresed_lst.append(lst[i])
    return reveresed_lst

print(revese_list_func(countries))
print(revese_list_func([3, 5, 6, 9]))
