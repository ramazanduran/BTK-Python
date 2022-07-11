#error handling => hata yönetimi
"""
Okumakta fayda var.
https://python-istihza.yazbel.com/hata_yakalama.html
"""


try:
    x = int(input("x: "))
    y = int(input("y: "))
    print(x/y)
except ZeroDivisionError:
    print('y 0 dan başka değer olmalı')
except ValueError:  
    print('x ve y ye rakamdan başka veri girmeyiniz')

"""
"""

try:
    x = int(input("x: "))
    y = int(input("y: "))
    print(x/y)
except (ZeroDivisionError) as e:
    print("Yanlış bilgi girdiniz.")
    print(e)

"""
"""

try:
    x = int(input("x: "))
    y = int(input("y: "))
    print(x/y)
except (ZeroDivisionError) as e:
    print("Yanlış bilgi girdiniz.")
else:
    print("Herşey yolunda")

    """
    """

while True:
    try:
        x = int(input('x: '))
        y = int(input('y: '))
        print(x/y)
    except Exception as ex:
        print('yanlış bilgi girdiniz', ex)  #ex ile hata kodları yazdırılır.
    else:
        break
    finally:
        print('try except sonlandı.')
