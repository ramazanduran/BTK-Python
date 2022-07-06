sayilar = [1,3,5,7,9,12,19,21]

# 1- Sayilar listesindeki hangi sayılar 3'ün katıdır ?

ucunkatı = []
for i in sayilar :
    if i % 3 == 0:
        ucunkatı.append(i)
print(ucunkatı)

# 2- Sayilar listesinde sayıların toplamı kaçtır ?

toplam = 0
for a in sayilar:

    toplam += a
   
print(toplam)

# 3- Sayilar listesindeki tek sayıların karesini alınız.

tek_kare = []

for s in sayilar : 
    if s % 2 == 1:
        tek_kare.append(s**2)
print(tek_kare)


sehirler = ['kocaeli','istanbul','ankara','izmir','rize']

# 4- Şehirlerden hangileri en fazla 5 karakterlidir ?
sehir_5 = []

for sehir in sehirler:
    if len(sehir) <=5:
        sehir_5.append(sehir)
print(sehir_5)



urunler = [
    {'name':'samsung S6', 'price': '3000' },
    {'name':'samsung S7', 'price': '4000' },
    {'name':'samsung S8', 'price': '5000' },
    {'name':'samsung S9', 'price': '6000' },
    {'name':'samsung S10', 'price': '7000' }
]

# 5- Ürünlerin fiyatları toplamı nedir ?
toplam_5 = 0

for urun in urunler:
    
    fiyat = int(urun['price'])
    
    toplam_5 += fiyat

print(toplam_5)

# 6- Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz ?

urun_5k = []
for urun1 in urunler :
    urun_price = int(urun1['price'])
    if urun_price <= 5000:
        urun_5k.append(urun1)
print(urun_5k)
