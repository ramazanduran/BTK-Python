
# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
numb1 = float(input('Sayı Giriniz: '))
result1 = (numb1 > 0) and (numb1 < 100) 
print(f'Girilen sayı 0 ile 100 arasındadır : {result1} ')

# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
numb2 = float(input('Soru 2 için sayı giriniz: '))
result2 = (numb2 % 2 == 0) and (numb2 > 0)
print(f'Kullanıcının girdiği {numb2} sayısı pozitif ve çifttir {result2}')

# 3- Email ve parola bilgileri ile giriş kontrolü yapınız. 

email = 'email@rd.com.tr'
password = '123456'
e_mail = input('Mailinizi giriniz: ')
pass_word = input('Şifrenizi giriniz: ')

result3 = (email == e_mail) and (password == pass_word)
print(f'Girilen email ve şifre doğrudur: {result3}')

# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

num1 = int(input('4. soru için ilk sayıyı giriniz: '))
num2 = int(input('4. soru için ikinci sayıyı giriniz: '))
num3 = int(input('4. soru için üçüncü sayıyı giriniz: '))

result4_1 = (num1 > num2) and (num1 > num3)
print(f'İlk Girilen sayı en büyüktür: {result4_1}')
result4_2 = (num2 > num1) and (num2 > num3)
print(f'İkinci Girilen sayı en büyüktür: {result4_2}')
result4_3 = (num3 > num1) and (num3 > num2)
print(f'Üçüncü Girilen sayı en büyüktür: {result4_3}')


# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#    a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
#    b-) Finalden 70 alındığında ortalamanın önemi olmasın.

vize1 = int(input('İlk vize notunu giriniz: '))
vize2 = int(input('İkinci vize notunu giriniz: '))
final = int(input('Final notunu giriniz: '))

ortalama = (vize1+vize2)/2*0.6 + final*0.4
result5 = (final >= 70) or (ortalama >= 50) or((ortalama >= 50) and (final >= 50))
print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu: {result5}')

# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#    Formül: (Kilo / boy uzunluğunun karesi)
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#    0-18.4    => Zayıf 
#    18.5-24.9 => Normal  
#    25.0-29.9 => Fazla Kilolu
#    30.0-34.9 => Şişman (Obez)

ad = input('Adınızı girin: ')

kilo = int(input('Kilonuzu girin: '))
boy = int(input('Boyunuzu girin: '))
Formul = (kilo / boy**2)

zayif = (Formul >= 0) and (Formul <=18.4)
normal = (Formul >18.4) and (Formul <=24.9)
kilolu = (Formul >24.9) and (Formul <=29.9)
obez = (Formul >=29.9) and (Formul <=34.9)


print(f'{ad} kilo indeksin: {Formul} ve kilo değerlendirmen zayıf: {zayif}')
print(f'{ad} kilo indeksin: {Formul} ve kilo değerlendirmen normal: {normal}')
print(f'{ad} kilo indeksin: {Formul} ve kilo değerlendirmen kilolu: {kilolu}')
print(f'{ad} kilo indeksin: {Formul} ve kilo değerlendirmen obez: {obez}')

