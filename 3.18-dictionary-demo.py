'''
    ogrenciler = {
        '120': {
            'ad': 'Ali',
            'soyad': 'Yılmaz',
            'doğum yılı' : 1999
            'ev adresi' : 'İstanbul'
            'telefon': '532 000 00 01'
        },
        '125': {
            'ad': 'Can',
            'soyad': 'Korkmaz',
            'doğum yılı' : 1999
            'ev adresi' : 'Kocaeli'
            'telefon': '532 000 00 02'
        },
        '128': {
            'ad': 'Volkan',
            'soyad': 'Yükselen',
            'doğum yılı' : 1998
            'ev adresi' : 'İzmir'
            'telefon': '532 000 00 03'
        },
    }

    1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle
       dictionary içinde saklayınız.

    2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.
'''


ogrenciler = {}

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyad: ")
birthday = input('doğum yılı: ')
address = input("Ev Adresi: ")
phone = input("öğrenci telefon: ")

# Birinci Yöntem
# ogrenciler[number] = {
#     'ad': name,
#     'soyad': surname,
#     'doğum yılı' : birthday,
#     'ev adresi' : address, 
#     'telefon': phone
# }

ogrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'doğum yılı' : birthday,
        'ev adresi' : address, 
        'telefon':phone 
    }
})

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyad: ")
birthday = input('doğum yılı: ')
address = input("Ev Adresi: ")
phone = input("öğrenci telefon: ")

ogrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'doğum yılı' : birthday,
        'ev adresi' : address, 
        'telefon':phone 
    }
})

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyad: ")
birthday = input('doğum yılı: ')
address = input("Ev Adresi: ")
phone = input("öğrenci telefon: ")

ogrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'doğum yılı' : birthday,
        'ev adresi' : address, 
        'telefon':phone 
    }
})



print('*'*50)

ogrNo = input('öğrenci no: ')
ogrenci = ogrenciler[ogrNo]
print(ogrenci)

print(f"Aradığınız {ogrNo} nolu öğrencinin adı: {ogrenci['ad']} soyadı: {ogrenci['soyad']} ve telefonu ise {ogrenci['telefon']}")
