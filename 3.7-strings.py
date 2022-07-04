name = 'Ramazan'
surname = 'Duran'
age = 27
deneme = 'My name is '

#print (deneme + name + ' ' + surname+ 'and I am '+ str(age) + ' years old'   )
#print (deneme + name + ' ' + surname+ '\nI am '+ str(age) + ' years old'   )

greeting = deneme + name + ' ' + surname+ '\nI am '+ str(age) + ' years old'
length = len(greeting)

#print(greeting)
#print(greeting[0])
#print(greeting[3])
#print(len(greeting))
#print(greeting[-1])
#print(greeting[length-1])

#print( greeting[3:7])

#print(greeting[3:])
#print(greeting[:15])
print(greeting[2:40:3])