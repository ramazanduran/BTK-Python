"""
1- Bir müşterinin aşağıdaki bilgileri içi değişken oluşturunuz.
    Müşteri adı
    Müşteri Soyadı
    Müşteri adı + soyadı
    Müşteri cinsiyeti
    Müşteri tc kimlik numarası
    Müşteri doğum yılı
    Müşteri adres bilgisi
    Müşteri yaşı
"""

customerName = 'Ali'
customerSurname= 'Yılmaz'
customerNameSurname = 'Ali Yılmaz'
customerNameSurname1 = customerName + ' ' + customerSurname
customerGender = True #Erkekse 
customerNationalNumber  = '123456789'
customerBirthYear = 1990
customerAddress = 'Malikgazi Kayseri'
customerAge = 2022 - customerBirthYear

print(customerNameSurname1 + ' ve '+ customerNameSurname )
print(customerAddress + ' ve ' + customerNationalNumber)
print (customerAge)


"""
2- Aşağıdaki siparişlerin toplam bilgisini hesaplayınız.
    Sipariş 1 = 110 ₺
    Sipariş 2 = 1100.5 ₺
    Siipariş 3 = 356.95 ₺
"""

order1 = 110
order2 = 1100.5
order3 = 356.95

Total_Order = (order1 + order2 + order3)
  
print('Total', Total_Order, '₺')