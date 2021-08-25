# List : is a collection of an ordered indexed items

countries = ['Finland', 'Sweden','Denmark','Norway','Iceland']

print(countries[0])
print(countries[1])
print(countries[-1])
print(countries[4])

last_index = len(countries) - 1
print(countries[last_index])
print(len(countries))

# countries[0]  = 'Estonia'
# print(countries)
# countries[2] = 'Germany'
# print(countries)
# countries.append('France')
# print(countries)
# countries.extend(['Belgium','The Netherlands','Poland'])
# print(countries)
# countries.insert(3, 'Greenland')
# countries.pop(3)
# print(countries)
# countries.remove('Finland')
print(countries)
fin, _, den, *rest = countries
print(fin,den, rest)
print(countries)

print(countries[:])
print(countries[::])
print(countries[::-1])
print(countries[::2])
print(countries[1:4])

print('py' in 'python')
print('land' in 'Finland')

print('Greenland' in countries)
print('Finland' in countries)

# print(countries)
# del countries[-1]
# print(countries)
# del countries[1:3]
# print(countries)
# countries.clear()
countries_2 = countries.copy()
countries_2.sort()
print(countries)
print(countries_2)

fruits = ['banana', 'orange', 'mango', 'lemon', 'orange']

print(fruits.count('orange'))

ages = [22, 19, 24, 25, 26, 24, 25, 24]

sorted_ages = sorted(ages)
print(ages)
print(sorted_ages)