# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın. 

def word(word,num):
    print(word*num)

word('RD',3)


# 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazınız.

sinirsiz = []

def sinirrsiz (*sinirsizzz):
    sinirsiz.append(sinirsizzz)

result = sinirrsiz(3,5,5,9,'RD','Sınırsız')
print(sinirsiz)
print(type(sinirsiz))

# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.

num1 = int(input('İlk sayıyı giriniz: '))
num2 = int(input('İkinci sayıyı giriniz: '))
asallar = []
def asal (num1, num2):
    
    for sayi in range(num1, num2+1):
         if sayi > 1:
            for i in range(2, sayi):
                if (sayi % i == 0):
                     break
            else:
                asallar.append(sayi)       
                

asal (num1, num2)
print(asallar)

# 4- Kendisine gönderilen bir say   ının tam bölenlerini bir liste şeklinde döndürünüz.

num4 = int(input('Sayı Giriniz: '))

bolen = []
def soru4 (num4):
    for i in range (1, num4+1):
        if num4 % i == 0:
            bolen.append (i)
soru4(num4)
print(bolen)


