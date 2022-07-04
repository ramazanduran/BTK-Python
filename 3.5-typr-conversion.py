"""
x = input ( '1. Sayı: ')
y = input ( '2. Sayı: ')

total = x + y

print('Total: ', total) #Eğer girdilerin string olduğunu bilmezsek hatalı işlermler yapmış oluruz. 
                        #Bu nedenle bunları sayıya çevirmemiz lazım.




x = int(input ( '1. Sayı: '))
y = int(input ( '2. Sayı: '))

total = x + y

print('Total: ', total)



x = input ( '1. Sayı: ')
y = input ( '2. Sayı: ')

print('Type x:', type(x))
print('Type y:', type(y))

total = int(x) + int(y)

print('Total: ', total)

"""


x = 5               #int
y = 2.5             #float
name = 'Ramazan'    #string
isOnline = True     #bool

#print('Type x: ', type(x))
#print('Type y: ', type(y))
#print('Type name: ', type(name))
#print('Type isOnline: ', type(isOnline))


#Type Conversion - Veri Dönüştürme

"""
#int to float
x = float(x)
print(x)
print(type(x))
"""

"""
#float to int 
y = int(y)
print(y)
print(type(y))
"""
"""
result = x + y
print(result)
print(type(result))

result = str(x) + str(y)
print(result)
print(type(result))
"""
"""
#bool to str

isOnline = str(isOnline)
print(isOnline)
print(type(isOnline))
"""

#bool to int

isOnline = int(isOnline)
print(isOnline)
print(type(isOnline))