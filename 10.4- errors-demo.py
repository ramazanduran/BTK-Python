liste = ["1","2","3","5a","10b","asd", "10", "50"]

# 1: Liste elemanları içindeki sayısal değerleri bulunuz. 

for x in liste: 
    try:
        result = int(x)
        print(result)
    except ValueError:
        continue

# 2:  Kullanıcı 'q' değerini girmedikçe aldığınız her inputun sayı 
# olduğundan emin olunuz aksi halde hata mesajı yazın.

while True:
    sayi = input("Sayı: ")
    if sayi == "q":
        break

    try : 
        result = float(sayi)
        print("Girdiğiniz sayı: ", result)
        break

    except ValueError:
        print("Geçersiz sayı")
        continue

"""
"""

# 3: Girilen parola içinde türkçe karakter hatası veriniz.  

def checkPassword(parola):
    turkce_karakterler = "şçğüöıİ"

    for i in parola:
        if i in turkce_karakterler:
            raise TypeError("Parola Türkçe karakter içeremez.")
        else : 
            pass
    print("Geçerli parola")

parola = input("Parlola Giriniz: ")

try:
    checkPassword(parola)
except TypeError as error:
    print(error)

"""
"""

# 4: Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için
# hata mesajları verin.

def farktoriyel (x):
    x = int(x)

    if x < 0:
        raise ValueError ("Negatif değer")

    result = 1

    for i in range (1, x + 1):
        result *= i

    return result

for x in [5,10,20,-3, '10a']:
    try:
        y = farktoriyel(x)
    except ValueError :
        print(ValueError)
        continue
    print(y)