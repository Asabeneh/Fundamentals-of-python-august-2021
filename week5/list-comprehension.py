countries = ['Finland','Sweden','Denmark','Norway','Iceland']
nums = [1, 2, 3, 4, 5] # [1, 4, 9, 16, 25]
new_nums = [n ** 2 for n in nums]
print(new_nums)
country_codes = [c.upper()[:3] for c in countries]
print(country_codes)

countries_with_land = [c for c in countries if 'land' in c]
print(countries_with_land)
countries_without_land = [c for c in countries if 'land' not in c]
print(countries_without_land)

countries_without_way = [c for c in countries if 'way' not in c]
print(countries_without_way)

