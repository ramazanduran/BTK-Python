
website = "http://www.sadikturan.com"
course  = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"


# 1-  ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
result1_1 = ' Hello World '.strip()
result1_2 = ' Hello World '.lstrip()
result1_3 = ' Hello World '.rstrip()
result1_4 = website.lstrip('/:pth')     #Parantez içindeki karakterlerin hepsi silinir.
 

# 2- 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.

result2 = 'www.sadikturan.com'.strip('w.moc')

# 3-  'course' karakter dizisinin tüm karakterlerini küçük harf yapın.

result3_1 = 'course'.upper()
result3_2 = result3_1.lower()
result3_3 = result3_1.title()

# 4- 'website' içinde kaç tane a karakteri vardır ? (count('a'))

result4_1 = 'website'.count('a')
result4_2 = 'website'.count('www')
result4_3 = 'website'.count('www',0,10)  #www ifadesi 0 ile 10. karakter arasındaysa sayıyor.
 
# 5- 'website' "www" ile başlayıp com ile bitiyor mu?

result5_1 = website.startswith('www')
result5_2 = website.startswith('http')
result5_3 = website.endswith('com')

# 6-  'website' içinde '.com' ifadesi var mı?

result6_1 = website.find('com')
result6_2 = website.find('com',0,10)
result6_3 = course.find('Python')
result6_3 = course.rfind('Python')

result6_4 = website.index('com')
result6_5 = website.rindex('com')

# result = website.rindex('comm') # exception burada find da -1 
                                  # dönerken yok diye index de hata verir.

# 7- 'course' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)

result7_1 = course.isalpha()
result7_2 = 'Hello'.isalpha()
result7_3 = course.isdigit()
result7_4 = '123'.isdigit()

# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.

result8_1 = 'Contents'.center(50, '*')
result8_2 = 'Contents'.ljust(50, '*')
result8_3 = 'Contents'.rjust(50, '*')

# 9-  'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.

result9_1 = course.replace(' ', '-')
result9_2 = course.replace(' ', '-',5) 
result9_3 = course.replace(' ', '')

# 10- 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin

result10 = 'Hello World'.replace('World','There')

# 11-  'course' karakter dizisini boşluk karakterlerinden ayırın.

result11_1 = course.split(' ')
result11_2 = result11_1[2]
result11_3 = result11_1[5]


print(result11_3)
