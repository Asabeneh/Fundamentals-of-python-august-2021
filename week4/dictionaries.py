# 
from pprint import pprint
dct = {
'kissa':'Cat', 
'Kirja':'Book',
'talo':'House'
}

empty_dct = {} 
empty_dct = dict()

user = {
    'firstname':'Asabeneh',
    'lastname':'Yetayeh',
    'age':250,
    'country':'Finland',
    'city':'Helsink',
    'skills':['Python','NumPy','Pandas'],
    'is_married':True,
    'address':{
        'street_name':'Space Street',
        'zipcode':'02770',
        'city':'Espoo'
    }
}

print(user['firstname'])
print(user['lastname'])
print(user.get('nationality'))
print(user.get('address')['zipcode'])
user['skills'].append('Machine Learning')
print(user['skills'])
user['point']  = 25
pprint(user)
print(len(user))
user['age'] = 105
pprint(user)

print('nationality' in user)

""" for key in user:
    print(key, user[key])

user.pop('point')
user.popitem()
del user['age'] """

pprint(user)
pprint(user.items())
for key, value in user.items():
    print(key, value)

user_2 = user.copy()
# list, set, dictionary => mutable, modified
# tuples => immuatable, unmodifiable

keys = user.keys()
print(keys)
values = user.values()
print(values)