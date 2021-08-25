
# for i in [1, 2, 3, 4, 5]:
#     print(f'{i} * {i} = {i * i}')

# for i in range(5):
#     print(f'{i} * {i} = {i * i}')

# for i in range(10, -1, -1):
#     print(i)

# for i in [2, 3, 4, -5, 0, 8, 9]:
#     if i == -5:
#         break
#     print(i)

# for i in [2, 3, 4, -5, 0, 8, 9]:
#     if i == -5:
#         continue
#     print(i)

countries = ['Finland', 'Sweden','Denmark','Norway','Iceland']

for country in countries:
    print(country, country.upper(),  country.upper()[:3], len(country))



countries_with_land = []
for country in countries:
    if 'land' in country:
        countries_with_land.append(country)
print(countries_with_land)

countries_without_land = []
for country in countries:
    if 'land' not in country:
        countries_without_land.append(country)
print(countries_without_land)

countries_without_way = []
for country in countries:
    if 'way' not in country:
        countries_without_way.append(country)
print(countries_without_way)

for i in range(11):
    print(f'{i} x {i} = {i * i}')

lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in lst:
    print(item)

for i in range(101):
    if i % 2 == 0:
        print(i)
