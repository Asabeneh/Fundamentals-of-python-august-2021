# set is a collection of un order items items

'''
A = {3, 5, 7, 9}
B = {2, 3, 5, 9}
C = {3, 5}
# Union
AUB = {2,3,5,7,9}
AnB = {3, 5, 9}
A\B = {7}
B\A = {2}
(A\B) U (B\A) = {2, 7}

C C A => True
C C B => True
empty C A
A C A

'''

A = {3, 5, 7, 9}
B = {2, 3, 5, 9}
C = {3, 5}
empty_set = set()

print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(B.difference(A))
print(A.symmetric_difference(B))
print(A.issubset(A))
print(A.issubset(B))
print(C.issubset(A))
print(C.issubset(B))
print(A.isdisjoint(B))

for element in A:
    print(element)

print(9 in A)

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')
print(fruits)
fruits.update(['apple','avocado','guava'])
print(fruits)

fruits.remove('banana')
print(fruits)
# fruits.clear()
# print(fruits)

# What are the 10 spoken languages in the world
# English 95 Spanish

languages = ['English', 'Swedish','Finish', 'Swedish', 'French','French', 'English']
languages_set = set(languages)
print(languages_set)

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruit_and_vegs = fruits.union(vegetables)
print(fruit_and_vegs)