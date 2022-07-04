#dictionary için {} kullanmamız gerekmektedir.
# key - value

# 41 => kocaeli 34 => istanbul

# sehirler = ['kocaeli','istanbul']
# plakalar = [41, 34]

# print(plakalar[sehirler.index('istanbul')])

# print(plakalar['kocaeli']) => 41
# print(plakalar['istanbul']) => 34

plakalar = { 'kocaeli' : 41, 'istanbul': 34 }

print(plakalar['kocaeli'])
print(plakalar['istanbul'])

plakalar['ankara'] = 6
plakalar['kocaeli'] = 'new value'

print(plakalar)


users = {
    'ramazanduran':{
        'age' : 27,
        'roles' : ['user'],
        'email': 'ramazan@gmail.com',
        'address': 'kayseri',
        'phone': '123654789'
    },

    'sadikturan': {
        'age': 36,        
        'roles': ['user'],
        'email': 'sadik@gmail.com',
        'address': 'kocaeli',
        'phone': '1231321'
    },
    'cinarturan': {
        'age': 2,
        'roles': ['admin','user'],
        'email': 'cinar@gmail.com',
        'address': 'kocaeli',
        'phone': '1231321'
    }
}

print(users['cinarturan']['roles'][0])
rd = (users['ramazanduran']['address'][5]).upper()

print(rd)


