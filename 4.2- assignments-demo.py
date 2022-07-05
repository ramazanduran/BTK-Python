x, y, z = 2, 5, 10

numbers = 1, 5, 7, 10, 6 

# 1- Kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir?

number1 = int(input('Sayı 1: '))
number2 = int(input('Sayı 2: '))

result1 = (number1*number2)-(x+y+z)
print(result1)

# 2- y'nin x'e kalansız bölümünü hesaplayınız.

result2 = y//2
print(result2)

# 3- (x,y,z) toplamının mod 3'ü nedir?

result3 = (x+y+z)%3
print(result3)

# 4- y'nin x. kuvvenini hesaplayınız.

result4 = y**x
print(result4)

# 5- x, *y, z = numbers işlemine göre z'nin küpü kaçtır?

x, *y, z = numbers
print(z)

# 6- x, *y, z = numbers işlemine göre y'nin değerleri toplamı kaçtır?

x, *y, z = numbers
result6 = y[0]+y[1]+y[2]
print(result6)
