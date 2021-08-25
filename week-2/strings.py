# string is a text data type
# A string could be a single character or a paragraph

char = 'A'
print(char)
first_name = 'Asabeneh'
last_name = 'Yetayeh'

print(first_name)
print(len(first_name), len(last_name))
print(len(first_name) > len(last_name))

txt = 'fundamentals of Python'
print(len(txt))
words = txt.split()
print(words)
print(txt.upper())
print(txt.lower())
print(txt.islower())
print(txt.isupper())
print(txt.title())
print(txt.swapcase())

# startswith, index, find, rfind, endswith
print(txt.startswith('Python'))
print(txt.startswith('Fun'))
print(txt.startswith('fun'))
print(txt.endswith('Python'))
print(txt.endswith('thon'))

print(txt.find('of'))
print(txt.find('f'))
print(txt.rfind('f'))
print(txt.find('F'))

lang = 'Python'
print(lang[0])
print(lang[1])
print(lang[2:5])
print(lang[1:])
print(lang[-1])
print(lang[4:])
print(lang[::-1])
print(lang[0:6:1])

city = 'Mississipi'
print(city.count('s'))
print(city.count('i'))

pandemic = 'COVID19'
print(type(pandemic))
print(pandemic.isalpha())
print(pandemic.isalnum())

challenge = '\u00B2'
print(challenge.isdigit())   # True

num = '10.5'
print(num.isnumeric()) # False

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']

print(', '.join(web_tech))

text = '   some thimes we may have space in the left and right    '
print(text, 'just to see the space')
print(text.strip(), 'just to see the space')

txt = 'I like Pyhton becuase it is asesome. If you do not like Python whatelse can you like.'
print(txt.replace('like', 'love'))

words = txt.split()
print(words)