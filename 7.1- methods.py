# method
"""
Nesne tabanlı programlamada sınıftan türetilmiş her bir nesneye 
hizmet eden ve belli bir görevi yerine getiren fonksiyona method diyoruz.
Örneğin string bir ifadenin type yazdırıldığı zaman class  'str' ifade eder
buradaki class bir metoddur. Yani method bir sınıf bünyesinde değerlendirilir.
"""

list = [1,2,3]

list.append(4)
list.pop()

print(type(list))
print(list)

myString = 'Hello'
 
print(myString.upper())


print(type(myString))

# fonksiyon
"""Fonksiyonların görevi, karmaşık işlemleri bir araya toplayarak, bu 
işlemleri tek adımda yapmamızı sağlamaktır. Fonksiyonlar çoğu zaman, yapmak
istediğimiz işlemler için bir şablon vazifesi görür. Fonksiyonları kullanarak,
bir veya birkaç adımdan oluşan işlemleri tek bir isim altında toplayabiliriz.
Python’daki ‘fonksiyon’ kavramı başka programlama dillerinde ‘rutin’ veya
‘prosedür’ olarak adlandırılır. Gerçekten de fonksiyonlar rutin olarak tekrar
edilen görevleri veya prosedürleri tek bir ad/çatı altında toplayan araçlardır.
"""