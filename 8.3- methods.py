#class
class Person:
    #class attributes
    adress = 'no information'
    #constructor (yapıcı metod)
    def __init__(self, name, year) :
        #object attributes
        self.name = name
        self.year = year

    #instance methods
    def intro(self):
        print('Hello There. I am '+ self.name)
        print(f'I was born in {self.year}')
    
    #instance methods
    def calculateAge (self):
        import datetime
        dir(datetime.datetime)
        year = datetime.datetime.now()
        year = year.year

        return year - self.year

#object (instance)
p1 = Person (name='Zehra', year= 1998)
p2 = Person (name= 'Ramazan', year= 1996)
p3 = Person ( name = 'Bahri', year = 1997)

p3.adress = 'Portekiz'

p1.intro()
p2.intro()

print(f'adım: {p1.name} ve yaşım: {p1.calculateAge()}')
print(f'adım: {p2.name} ve yaşım: {p2.calculateAge()}')
print(f"adım: {p3.name}, yaşım: {p3.calculateAge()} ve {p3.adress}'de yaşıyorum ")

"""
***************************************
"""

class Circle:
    #Class object attribute
    import math

    def __init__(self, yaricap = 1) :
        self.yaricap = yaricap

    #Methods
    def cevre_hesaplama (self):
        return (2 * self.math.pi * self.yaricap)

    def alan_hesaplama (self):
        return (self.math.pi * (self.yaricap ** 2))


c1 = Circle()    #yaricap belirtmezsek 1 alır yukraıda belirttiğimiz için
c2 = Circle(5)
num = int(input('Yarıçapı giriniz: '))
c3 = Circle(num)

print(f'c1 : alan = {c1.alan_hesaplama()} çevre = {c1.cevre_hesaplama()}')
print(f'c2 : alan = {c2.alan_hesaplama()} çevre = {c2.cevre_hesaplama()}')
print(f'Girilen değerin : alan = {c3.alan_hesaplama()} çevre = {c3.cevre_hesaplama()}')
