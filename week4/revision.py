countries = ['Finland','Sweden','Denmark','Norway','Iceland']
print(len(countries))
print(countries[0])
print(countries[1])
print(countries[-1])
print(countries[-2])
# append, extend, pop, remove, del, insert etc

nums = [1, 2, 3, 4, 5] # [1, 4, 9, 16, 25]

new_nums = []
for i in nums:
    new_nums.append(i * i)

print(new_nums)

print(list(range(1, 11, 2)))

# find the sum of all numbers from 0 to 100

all_nums = 0
for i in range(0, 101):
    all_nums = all_nums + i
print(all_nums)


# find the sum of all evens from 0 to 100

evens = 0
for i in range(0, 101, 2):
    evens = evens + i
print(evens)


# find the sum of all odds from 0 to 100

odds = 0
for i in range(1, 101, 2):
    odds = odds + i
print(odds)

new_countries = []
for country in countries:
    new_countries.append([country, country.upper(), country.upper()[:3], len(country)])

print(new_countries)


hashes = ''
for i in range(7):
    hashes = hashes + '#'
    print(hashes)



for i in range(1, 8):
    print('#'*i, i)

countries_with_land = []
for country in countries:
    if 'land' in country:
        countries_with_land.append(country)
print(countries_with_land)


