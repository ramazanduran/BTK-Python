from traceback import print_tb


name = 'Ramazan'
surname = 'Duran'
'''
print('My Name İs {} {}'.format(name, surname))
print('My Name İs {0} {1}'.format(name, surname))
print('My Name İs {1} {0}'.format(name, surname))
print('My Name İs {n} {s}'.format(n=name, s=surname))
print('My Name İs {s} {n}'.format(n=name, s=surname))
'''
age = 27

print('My Name İs {} {} and I am {} years old'.format(name, surname, age))

#result = 200/700
#print('The result is {}' .format(result))
#print('The result is {r:1.3}' .format(r=result))

#print('The result is {r:10.3}' .format(r=result))


print(f'My Name İs {name} {surname} and I am {age} years old')