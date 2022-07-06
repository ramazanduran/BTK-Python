sayilar = [1,3,5,7,9,12,19,21]

# 1: sayilar listesini while ile ekrana yazdırın.
index = 0
while (index < len(sayilar)):
    print(sayilar[index])
    index += 1


# 2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm
#    tek sayıları bir listeye ekleyin ve ekrana yazdırın.

baslangic = int(input('Başlangıç değeri giriniz: '))
bitis = int(input('Bitiş değerini giriniz: '))

tek = []
while baslangic < bitis :
    baslangic += 1
    if baslangic % 2 == 1:
        tek.append(baslangic)

print(tek)


# 3: 1-100 arasındaki sayıları azalan şekilde yazdırın.

a = 100
while a > 1 : 
    print (a)
    a -= 1


# 4: Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde
#    yazdırın.

sayi = int(input('Girmek istediğiniz sayı adetini giriniz: '))
sayilar = []
i = 0
while i < sayi :
    num = int(input('Sayı Giriniz: '))
    sayilar.append(num)
    i += 1
sayilar.sort()
print (sayilar)


# 5: Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız.
#    ** ürün sayısını kullanıcıya sorun.
#    ** dictionary listesi yapısı (name, price) şeklinde olsun.
#    ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.

urunler = []
sayi = int(input('Girmek istediğiniz sayı adetini giriniz: '))

i = 0
while i < sayi :
    name = input('Ürün Adını Giriniz: ')
    price = input('Ürün Ücretini Giriniz: ')
    urunler.append (
         {
        'name:' : name, 
        'price:' : price 
         }
    )
    i += 1

print(urunler)


  

