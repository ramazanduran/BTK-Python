"""
    Daire Alanı : πr²
    Dairenin Çevresi : 2πr

    *Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız. (π: 3.14)

"""

r = float(input('Yarı Çapı : '))
pi = 3.14

daireninAlanı = pi * r**2
daireninCevresi = 2 * pi * r

print('Dairenin Alanı: ', daireninAlanı, 've Dairenin Çevresi: ', daireninCevresi)
print('Dairenin Alanı: '+ str(daireninAlanı)+ 've Dairenin Çevresi: '+ str(daireninCevresi))