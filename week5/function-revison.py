# 
def make_square(n):
    return n ** 2

print(make_square(3))
print(make_square(30))
print(make_square(2))

def add_two_nums(a, b):
    return a + b

print(add_two_nums(1, 1))
print(add_two_nums(1, 4))
print(add_two_nums(99, 1))
print(add_two_nums(452, 958))

def add_numbers(*args):
    total = 0
    for item in args:
        total = total + item
    return total
    

print(add_numbers(1, 2, 3, 4, 5, 10, 9, 2))

# Lambda function

younameless = lambda x : x ** 2 + 2 *x  + 1
print(younameless(2))

