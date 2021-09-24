# countries = ['Finland','Sweden','Denmark','Norway','Iceland']

nums = [1, 2, 3, 4, 5] # [1, 4, 9, 16, 25]

def map_a_list(lst):
    new_nums = []
    for item in lst:
        new_nums.append(item * item)
    return new_nums

print(map_a_list(nums))
print(map_a_list([10, 20, 30]))

countries = ['Finland','Sweden','Denmark','Norway','Iceland','Netherlands','Germany','Belgium','France']
# ['FIN', 'SWE', 'DEN', 'NOR','ICE']

def get_country_codes(lst):
    country_codes = []
    for item in lst:
        country_codes.append(item.upper()[:3])
    return country_codes

print(get_country_codes(countries))

# How to make use of list comprehension to achieve the same result