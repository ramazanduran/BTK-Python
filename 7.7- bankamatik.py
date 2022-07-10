#Bankamatik Uygulaması

RamazanHesap = {
    'Adı' : 'Ramazan',
    'HesapNo' : '123456789',
    'Bakiye' : 3000 ,
    'EkHesap' : 2000
}

DuranHesap = {
    'Adı' : 'Duran',
    'HesapNo' : '147258369',
    'Bakiye' : 2000,
    'EkHesap' : 1000
}


def paraCek (hesap, miktar):
    print(f"Merhaba {hesap['Adı']}")

    if (hesap['Bakiye'] >= miktar):
        hesap['Bakiye'] -= miktar
        print('Paranızı alabilirsiniz.')
        bakiyeSorgula(hesap)
    else:
        toplam = hesap['Bakiye'] + hesap['EkHesap']

        if (toplam >= miktar):
            ekHesapKullanımı = input ( 'Ek hesap kullanılsın mı? (e/h)')

            if ekHesapKullanımı == 'e': 
                ekHesapKullanilacakMiktar = miktar - hesap['Bakiye']
                hesap['Bakiye'] = 0
                hesap['EkHesap'] -= ekHesapKullanilacakMiktar
                print('Paranızı alabilirsiniz.')
                bakiyeSorgula(hesap)

            else:
                print(f"{hesap['HesapNo']} nolu hesabınızda {hesap['Bakiye']} bulunmaktadır.")

        else : 
            print('Üzgünüz bakiye yetersiz.')
            bakiyeSorgulama(hesap)
def bakiyeSorgula (hesap):
    print(f"{hesap['HesapNo']} nolu hesabınızda {hesap['Bakiye']} ₺ bulunmaktadır. Ek hesap ise {hesap['EkHesap']} ₺ bulunmaktadır.")



paraCek(RamazanHesap, 3000)

print("*************************")

paraCek(RamazanHesap, 2000)

