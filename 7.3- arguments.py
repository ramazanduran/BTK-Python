def changeName(n):
    n = 'ada'

name = 'Ramazan'

changeName(name)

print(name)

"""
"""

def change(n):
    n[0] = 'İstanbul'

sehirler = ['Ankara', 'İzmir']

change (sehirler[:])

print(sehirler)

sehirler[0] = 'Kayseri'

print(sehirler)

"""
"""
def add(a, b):
    return sum ((a,b))

print(add(10,20))
#print(add(10,20,25))  # bunda hata alacağız. eğer istediğimiz zaman eklemek
                      # istersek aşağıdaki gibi olur.

"""
"""

def add1(a, b, c=0, d=0, e=0):
    return sum ((a,b,c,d,e))

print(add1(10,20,25))

"""
"""

def add2(*params):                        #bu komutta ne kadar veri 
    print(f'ilk index: {params[0]}')      #girilirse onları ekler
    print(f'üçüncü index: {params[3]}')   #yapılacak işleme sokar.
    return sum ((params))                 
   

print(add2(10,20,25,65,42,13))

"""
*args
Sınırsız sayıda parametreli fonksiyon oluşturmak için parametremizin 
önüne tek yıldız (*) koyabiliriz.  Burada, fonksiyon parametresinden
önce tek yıldız(*) kullandığımız için sonucumuz tuple olarak döner.
Peki ya *args nedir? Aslında *rakamlar ile arasında hiçbir fark yoktur. 
Asıl önemli önemli nokta, parametreden önce kullandığımız yıldız (*) 
yapısıdır. Python kullanıcıları için *args geleneksel bir parametredir. 
Bu geleneksel parametre Python kodumuzun kullanıcılar tarafından hem daha 
rahat anlaşılabilmesi için hem de okunabilirliğini arttırabilmek için 
önemlidir.
Bu tür fonksiyonların alabileceği parametre sayısı,pratikte sınırsızdır, 
ama teknik olarak bu sayı 256 adedi geçemez.
"""

def add3(*params): 
    print(type(params))                       
    sum = 0
    for n in params:
        sum += n
    return sum
   
print(add3(10,20,25,65,42,13))

"""
"""

def displayUser(**args):
    print(type(args))
    for key, value in args.items():
        print('{} is {}'.format(key,value))

displayUser(name= 'Çınar', age = 2, city = 'istanbul')
displayUser(name= 'Ada', age = 12, city = 'kocaeli', phone = '123132')
displayUser(name= 'Yiğit', age = 14, city = 'ankara', phone = '123132', email= 'yigit@gmail.com')

def myFunc(a, b, c, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunc(10, 20, 30, 40, 50, 60, 70, key1 = 'value 1', key2 = 'value 2')

"""
**kwargs
Çift yıldızlı (**) parametrelerin tek yıldızlı (*) parametrelerden en 
önemli farkı, fonksiyonu çağırırken anahtar değer ilişkisiyle 
çağırabilmemizdir. Burada, fonksiyon parametresinden önce çift yıldız(**) 
kullandığımız için sonucumuz sözlük (dictionary) olarak döner.
Buradada önemli olan parametreden önce kullandığımız olan çift yıldızdır. 
Parametre ismi kişiye göre değişebilir. Ama **kwargs gelenekselleşmiştir. 
Python kodumuzun kullanıcılar tarafından hem daha rahat anlaşılabilmesi 
için hem de okunabilirliğini arttırabilmek için kişisel parametre ismi 
yerine **kwargs kullanımı önemlidir.

Bu iki bilgi de aşağıda yazdığım yerden alınmıştır:
https://medium.com/@buraksekili0/python-args-ve-kwargs-nedir-ve-nas%C4%B1l-kullan%C4%B1l%C4%B1r-burak-sekili-d7692cb916f4
"""

