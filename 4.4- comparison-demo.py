# 1- Girilen 2 sayıdan hangisi büyüktür ? 
# if bloğu görmediğimiz için basit yapacağız

num1 = int(input('1. Sayıyı Giriniz: '))
num2 = int(input('2. Sayıyı Giriniz: '))
result1 = (num1>num2)
print(f'1. ssyı: {num1} 2. sayı: {num2} den büyüktür: {result1}')

# 2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.

vize1 = int(input('1. Vize notunu giriniz: '))
vize2 = int(input('2. Vize notunu giriniz: '))
final = int(input('Final notunu giriniz: '))

result2 = (vize1+vize2)/2*0.6+ final*0.4

print(f'not ortalamanız : {result2} ve dersten geçme durumunuz: {result2>=50}')


# 3- Girilen bir sayının tek mi çift mi olduğunu yazdırın.

sayi = int(input('Sayı giriniz: '))

tekcift = sayi % 2 == 0 

print(f'girilen sayının çift olma durumu: {tekcift}')

# 4- Girilen bir sayının negatif pozitif durumunu yazdırın.

sayi1 = int(input('Sayı giriniz: '))

tekcift1 = sayi1 % 2 > 0 

print(f'girilen sayının pozitif olma durumu: {tekcift1}')


# 5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
#    (email: email@rd.com parola:abc123)

email = 'email@rd.com'
password = 'abc123'

girilenEmail = input('email: ')
girilenPassword = input('parola: ')

isEmail = (email == girilenEmail.lower().strip())
isPassword = (password == girilenPassword.lower())

print(f'Email bilgisi doğrumu: {isEmail} ve Parola doğru mu: {isPassword}')