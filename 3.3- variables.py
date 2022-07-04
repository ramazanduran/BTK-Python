
#Değişken Tanımlama Kuralları

#rakam ile başlayamayız

number1 = 12
print(number1)

number1= 21
print(number1)

number1 +=12
print(number1)

#Büyük küçük harf duyarlılığı vardır

age= 23
AGE= 32
print(age)
print(AGE)

#Türkçe karakterler kullanmayalım

yas = 14
_age = 13

x = 1               #int     

y = 1.4             #float

name = "Ramazan"    #string 

isStudent = False   #bool

a= '12'
b='34'

print(a+b)          # ikisini yan yana birleştirir numara olmadığı için cevap 1234 olur

firstName = 'Ramazan'
lastName = 'Duran'

print(firstName + ' ' + lastName)

x, y, name, isStudent = (1,b, 'Ramazan', False)     #Çok fazla bilgiyi bir satıra atamış olabiliriz
