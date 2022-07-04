# 1-  "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.

from itertools import count


cars = ['Bmw', 'Mercedes', 'Opel', 'Mazda']
print(cars)

# 2-  Liste Kaç elemanlıdır ?

cars_length = len(cars)
print(cars_length)

# 3-  Listenin ilk ve son elemanı nedir ?

cars_first = cars[0]
cars_finally = cars[-1]
cars_finally1 = cars[cars_length-1]

print(cars_first)
print(cars_finally)
print(cars_finally1)

# 4-  Mazda değerini Toyota ile değiştirin.

cars[-1] = 'Toyota'
cars_new = cars
print(cars_new)

# 5-  Mercedes listenin bir elemanı mıdır ?

result = 'Mercedes' in cars
print (result)
result1 = 'Mercedess' in cars
print(result1)

# 6-  Listenin -2 indeksindeki değer nedir ?

cars_final_2 = cars[-2]
print(cars_final_2)

# 7-  Listenin ilk 3 elemanını alın.

cars_first_3 = cars[:3]
print(cars_first_3)


# 8-  Listenin son 2 elemanı yerine "Totoya" ve "Renault" değerlerini ekleyin.

cars[-2:] = ['Toyota','Renault']
print(cars)

# 9-  Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.

cars= cars + ['Audi', 'Nissan']
print(cars)

# 10- Listenin son elemanını silin.

del cars [-1]
print(cars)

# 11- Liste elemanlarını tersten yazdırınız.

cars = cars[::-1],
print(cars)

# 12- Aşağıdaki verileri bir liste içinde saklayınız. 

      # studentA: Yiğit Bilgi 2010, (70,60,70)
      # studentB: Sena Turan  1999, (80,80,70)
      # studentC: Ahmet Turan 1998, (80,70,90) 

studentA = ['Yiğit', 'Bilgi', 2010, [70,60,70]]
studentB = ['Sena', 'Turan', 1999, [80,80,70]]
studentC = ['Ahmet', 'Turan', 1998, [80,70,90]]

total_list = [[studentA],[studentB], [studentC]]

print(total_list)

# 13- Liste elemanlarını ekrana yazdırınız.

result = studentA[0]
result = studentB[1]
result = studentC[3][1]

result = f"{studentA[0]} {studentA[1]} {2019-studentA[2]} yaşında ve not ortalaması {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}"

#result1 = f"{total_list[0][0]} {total_list[0][1]} {2019-total_list[0][2]} yaşında ve not ortalaması {(total_list[0][3][0] + total_list[0][3][1] + total_list[0][3][2])/3}"
#result1 i kontrol et hata alıyorsun


print(result)
print(result1)