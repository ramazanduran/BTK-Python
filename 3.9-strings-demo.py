website = "http://www.sadikturan.com"
course  = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır ?

result1=(len(course))
length = len(website)

# 2- 'website' içinden www karakterlerini alın.

result2 = website[7:10]

# 3- 'website' içinden com karakterlerini alın.

result3_1 = website[22:25]
result3_2 = website[length-3:length]

# 4- 'course' içinden ilk 15 ve son 15 karakterlerini alın.

result4_1 = course[0:15]
result4_2 = course[:15]
result4_3 = course[-15:]

# 5- 'course' ifadesindeki karakterleri tersten yazdırın.

result5 = course[::-1]

name, surname, age, job = 'Bora','Yılmaz', 32, 'mühendis' 

# 6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
#    'Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis.' 

result6_1 = "Benim adım "+ name+ " " + surname+ ", Yaşım "+ str(age) + " ve mesleğim "+ job
result6_2 = "Benim adım {0} {1}, Yaşım {2} ve mesleğim {3}.".format(name,surname,age,job) 
result6_3 = f'Benim adım {name} {surname}, Yaşım {age} ve "mesleğim" {job}.'


# 7- 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.

s = 'Hello world'

result7 = s[0:6] + 'W'+ s[-4:]

# 8- 'abc' ifadesini yan yana 3 defa yazdırın.

result8 = 'abc ' * 3


print(result1)
print(result2)
print(result3_1)
print(result3_2)
print(result4_1)
print(result4_2)
print(result4_3)
print(result5)
print(result6_1)
print(result6_2)
print(result6_3)
print(result7)
print(result8)