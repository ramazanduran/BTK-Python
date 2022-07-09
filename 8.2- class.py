class Person:
    pass

p1 = Person()
p2 = Person()

print(p1)
print(p2)
print(p1 == p2)

"""
Genel Bilgi için okunması tavsiye edilir.
https://medium.com/@alper_guven/pythonda-class-s%C4%B1n%C4%B1f-ve-object-nesne-yap%C4%B1s%C4%B1-c1deb10c4edc
https://python.sitesi.web.tr/python-class.html#:~:text=Python%2C%20nesne%20tabanl%C4%B1%20bir%20programlama,s%C4%B1n%C4%B1flara%20%C3%B6zellik%20ve%20y%C3%B6ntemler%20atanabilir.
"""

#class
class Person1:
    #class attributes 
    address = 'no information'
    #consstructor (yapıcı metod)
    def __init__(self, name, year):
        #object attributes
        self.name = name
        self.birthday = year
        print('init metodu çalıştı.')
        
        #methods

#object (instance)

p1_1 = Person1 (name= 'Ramazan', year= 1996)
p1_2 = Person1 (name='Zehra', year= 1998)
p1_3 = Person1 (name='Ali', year= 1993)

#updating
p1_3.name = 'Duran'
p1_1.address = 'Kayseri'

#accessing object attributes 
print(f'p1_1 : name : {p1_1.name}, year :{p1_1.birthday}, and addres: {p1_1.address}')
print(f'p1_2 : name : {p1_2.name}, year :{p1_2.birthday}, and addres: {p1_2.address}')
print(f'p1_3 : name : {p1_3.name}, year :{p1_3.birthday}, and addres: {p1_3.address}')

#birthday ve year ikisi de year yapılarak dönüş alınırdı. Burada farklı 
#olduğunu görmek için yaptım.

print(p1_1)
print(p1_2)
print(type(p1_1))
print(type(p1_2))
print(p1_1 == p1_2)