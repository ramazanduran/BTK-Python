'''
1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.

'''
num1 = int(input('Sayı Giriniz: '))
if (num1 > 0) and (num1 < 100):
    print('Girdiğiniz sayı 0 ile 100 arasındadır.')
else:
    print('Girdiğiniz sayı 0 ile 100 arasında değildir.')


'''
2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.

sayi = int(input('sayı: '))

'''
num2 = int(input('Sayı Giriniz: '))

if (num2 % 2 == 0):
    print('Girdiğiniz sayısı çifttir.')
else:
    print('Girdiğiniz sayı tektir')


'''
3- Email ve parola bilgileri ile giriş kontrolü yapınız. 

'''
email = 'email@rd.com.tr'
password = '123456'

e_mail = input('Mailinizi giriniz: ')
pass_word = input('Şifrenizi giriniz: ')

if (email == e_mail):
    if (password == pass_word):
        print('Hoşgeldiniz.')
    else:
        print('Yanlış şifre girdiniz.')
else:
    print('Yanlış email girdiniz.')        


'''
4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

'''

num4_1 = int(input('İlk sayıyı giriniz: '))
num4_2 = int(input('İkinci sayıyı giriniz: '))
num4_3 = int(input('Üçüncü sayıyı giriniz: '))

if (num4_1 > num4_2) and (num4_1 > num4_3):
    print(f'İlk girdiğin sayı ({num4_1}) en büyüktür.')
elif (num4_2 > num4_3):
    print(f'İkinci girdiğin sayı ({num4_2}) en büyüktür.')
else:
    print(f'Üçüncü girdiğin sayı ({num4_3}) en büyüktür.')
    

'''
5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
   Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
   a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
   b-) Finalden 70 alındığında ortalamanın önemi olmasın.

'''

vize1 = int(input('İlk vizenizi girin: '))
vize2 = int(input('İkinci vizenizi girin: '))
final = int(input('Final notunuzu girin: '))

ortalama = (vize1 + vize2) / 2 * 0.6 + final * 0.4

if (ortalama >= 50) :
    if(final >= 50) : 
        print(f'öğrencinin ortalaması: {ortalama}, final notu :{final} ve geçme durumu: başarılı')
    else :
        print(f'öğrencinin ortalaması: {ortalama}, final notu :{final} ve geçme durumu: başarısız')
elif (ortalama <= 50) and (final >= 70):
    print(f'öğrencinin ortalaması: {ortalama}, final notu :{final} ve geçme durumu: Final notu nedeni ile başarılı')
else:
    print(f'öğrencinin ortalaması: {ortalama}, final notu :{final} ve geçme durumu: başarısız')


'''
6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
   Formül: (Kilo / boy uzunluğunun karesi)
   Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
   0-18.4    => Zayıf 
   18.5-24.9 => Normal  
   25.0-29.9 => Fazla Kilolu
   30.0-34.9 => Şişman (Obez)

'''
name = input('Adınızı Girin: ')
weight = float(input('Kilonuzu Girin: '))
length = float(input('Boyunuzu Girin: '))

result = weight / ((length/100)**2)

if (result >= 0) and (result <= 18.4):
    print(f'{name} kilo indeksin: {result} ve kilo değerlendirmen zayıf.')
elif (result > 18.4) and (result <= 24.9):
    print(f'{name} kilo indeksin: {result} ve kilo değerlendirmen normal.')
elif (result > 24.9) and (result <= 29.9):
    print(f'{name} kilo indeksin: {result} ve kilo değerlendirmen kilolu.')
elif (result >= 29.9) and (result<=45.9):
    print(f'{name} kilo indeksin: {result} ve kilo değerlendirmen obez.')
else:
    print('bilgileriniz yanlış.')