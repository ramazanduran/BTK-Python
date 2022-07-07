def sayHello1():
    print ('Hello')

sayHello1()

def sayHello2(name):
    print(f'Hello {name}')

sayHello2('ramazan')
#sayHello2()   #böyle boş bırakırsak hata aırız parametresi olmadığı için

def sayHello3(name = 'user'):
    return 'Hello '+ name

msg1 = sayHello3('Çınar')
msg2 = sayHello3('Ada')
msg3 = sayHello3()  # name = 'user' denildiği için hata almaz user yazar.

print(msg1)
print(msg2)
print(msg3)

"""
"""

def total(num1, num2):
    return num1 + num2

result1 = total(10,20)
result2 = total(15,20)
print(result1)
print(result2)

"""
"""

def yasHesapla(dogumYili):
    return 2022 - dogumYili

ageCinar = yasHesapla(2017)
ageAda = yasHesapla(2010)
ageSena = yasHesapla(1999)

print(ageCinar, ageAda, ageSena)

"""
"""

def EmekliligeKacYilKaldi(dogumYili, isim):
    '''
    DOCSTRING: Dogum yiliniza gore emekliliginize kac yil kaldı
    INPUT: Dogum yili
    OUTPUT: Hesaplanan yil bilgisi
    '''
    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas

    if emeklilik > 0:
        print(f'emekliliğinize {emeklilik} yıl kaldı')
    else:
        print('Zaten emekli oldunuz')


EmekliligeKacYilKaldi(1983, 'Ali')
EmekliligeKacYilKaldi(1950, 'Ahmet')
EmekliligeKacYilKaldi(1974, 'Yağmur')

print(help(EmekliligeKacYilKaldi))

list = [1,2,3]

print(help(list.append))

#help methodu nelerin önüne yazıldıysa onların nasıl kullaıldığını belirtir.