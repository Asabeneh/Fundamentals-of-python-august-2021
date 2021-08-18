# What is a string data type

char = 'B'
sentence = 'I love Python. It is most popular programming language'

country = 'Finland'
statement = 'i love Finalnd'
print(char)
print(len(char))
print(len(sentence))
print(len(country))
print('land' in country)
print(country.upper())
print(statement.upper())
print(statement.lower())
print(statement.title())
print(statement.swapcase())
print(statement.islower())

first_name = 'Asabeneh'
last_name = 'Yetayeh'
age = 250
is_married = True
is_raining = True
city = 'Helsiki'
skills = ['HTML','CSS','JavaScript','Python']

full_name = first_name + ' '+ last_name

print(full_name)
# I am a Asabeneh. I am 250 years old. I live in Helsinki, Finland. 

print('I am ' + full_name + '. I am ' + str(age) + ' years old. ' + 'I live in ' + city + ', ' + country + '.')

print('I am %s. I am %d years old. I live in %s, %s.' %(full_name, age, city, country))

print('I am {}. I am {} years old. I live in {}, {}.'.format(full_name, age, city, country))

print(f'I am {full_name}. I am {age} years old. I live in {city}, {country}.')