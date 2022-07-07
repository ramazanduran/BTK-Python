'''
   1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile
   buldurmaya çalışın. (hak = 5)
   ** "random modülü" için "python random" şeklinde arama yapın.
   ** 100 üzerinden puanlama yapın. Her soru 20 puan.
   ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı 
      üzerinden hesaplansın.
'''

import random

num = random.randint(1,100)
print(num)
can = int(input('Tahminleme oyununa hoşgeldiniz. Kaç canla başlamak istersiniz: '))
hak = can


    

while hak > 0 :
   deneme = int(input('Sayı giriniz: '))
     
   if num == deneme :
      print(f'Tebrikler Kazandınız. {100- (100/can) * (can - hak)} puan alınız')
      break

   if hak-1 == 0: 
      break 

   elif deneme < num:
      
      print(f'{hak-1} hakkınız kaldı. Tahmininiz küçük bu nedenle sayıyı büyütün.')

   elif  deneme > num:
      
      print(f'{hak-1} hakkınız kaldı. Tahmininiz büyük bu nedenle sayıyı küçültün.')
   
   

   hak -= 1

print('Kaybettiniz.')
