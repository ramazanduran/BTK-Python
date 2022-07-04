names = ['Ali','Yağmur','Hakan','Deniz']
names1 = ['Ali','Yağmur','Hakan','Deniz']
years = [1998, 2000, 1998, 1987]

# 1-  "Cenk" ismini listenin sonuna ekleyiniz.
names.append('Cenk')
print(names)

# 2-  "Sena" değerini listenin başına ekleyiniz.
names.insert(0,'Sena')
print(names)
# names.insert(-1, 'Mehmet')
# names.insert(len(names), 'Mehmet')


# 3-  "Deniz" ismini listeden siliniz.
names.remove('Deniz')
print(names)
# names.pop()       #bu farklı silme tarzıdır. indeks vermeden silinir.
# names.pop(1)


# 4-  "Deniz" isminin indeksi nedir ?
index = names1.index('Deniz')
print(index)
names1.pop(index)
print(names1)

# 5-  "Ali" listenin bir elemanı mıdır ?
result5 = 'Ali' in names
print(result5)
result5_1 = names.index('Ali')
print(result5_1)

# 6-  Liste elemanlarını ters çevirin.
names.reverse()
print(names)

# 7-  Liste elemanlarını alfabetik olarak sıralayınız.
names.sort()
print(names)

# 8-  years listesini rakamsal büyüklüğe göre sıralayınız.
years.sort()
print(years)

# 9-  str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.
str = "Chevrolet,Dacia"
result9_1 = str.split(',')
print(result9_1)

# 10- years dizisinin en büyük ve en küçük elemanı nedir ?
enBuyuk = max(years)
enKucuk = min(years)

print('En Büyük: ', enBuyuk, '\nEn Küçük: ', enKucuk)

# 11- years dizisinde kaç tane 1998 değeri vardır ?

result10 = years.count(1998)
print(result10)

# 12- years dizisinin tüm elemanlarını siliniz.
years.clear
print(years)

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.

markalar = []

marka = input('marka: ')
markalar.append(marka)
marka = input('marka: ')
markalar.append(marka)
marka = input('marka: ')
markalar.append(marka)

print (markalar)
