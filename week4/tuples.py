import math
from pprint import pprint

print(math.sqrt(2))

empty_tuple = ()
empty_tuple = tuple()
print(empty_tuple, type(empty_tuple))


fruits = ('banana', 'orange', 'mango', 'lemon','banana','guava')
print(fruits)
print(fruits[0])
print(fruits[-1])
print(fruits[2:])
print(fruits[1:5])
print(fruits.count('banana'))
print(fruits.index('lemon'))
print('apple' in fruits)
print('lemon' in fruits)

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_vegs = fruits + vegetables
# print(fruits_vegs)
# del fruits_vegs
# print(fruits_vegs)

# we create it but we cannot modify it, we call immutable. 
# it is indexed and an order almost like list
# we can use tuple() to create a tuple from list or other data types
# we can use count() method to count items
# we can completely delete the tuple using del
# we can use zero or negative indexing to access each element
# we can use the in membership operator to check if an item exist
# you use tuples if you have fixed set of items

"""

lst_tuples = []
for item in fruits_vegs:
    lst_tuples.append((item, item.upper(), len(item)))
pprint(lst_tuples)


"""


lst_tuples = []
for item in fruits_vegs:
    lst_tuples.append((item, item.upper(), len(item)))
pprint(lst_tuples)


