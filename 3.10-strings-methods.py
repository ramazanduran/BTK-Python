from __future__ import nested_scopes
from textwrap import indent


message = '  Hello There. My name is Ramazan Duran  '

mUpper = message.upper()
mLower = message.lower()
mTitle = message.title()
mCap = message.capitalize()

mStript = message.strip()   #Karakterlerin baş ve son boşluları siler
mSplit = message.split()    #Her bir kelime boşluktan ayrılır, parçalar.
mSplit1 = message.split('.')    #Noktalardan itibaren ayırır.

mJoin = ' '.join(mSplit)    #Kelimeleri birleştirmeye yarar.
mJoin1 = '*'.join(mSplit)   #Kelimeleri birleştirir ortaya * koyar.


print(mUpper)
print(mLower)
print(mTitle)
print(mCap)
print(mStript)
print(mSplit)
print(mSplit1)

print(mSplit[2])
print(mSplit1[1])

print(mJoin)
print(mJoin1)

index = message.find('Ramazan')
print(index)
isFound  = message.startswith('H')
print(isFound)
isFound1 = message.startswith('R')
print(isFound1)
isFound2 = message.endswith('n')
print(isFound2)

message1 = message.replace('Ramazan', 'Gülseren')
message2 = message.replace(' ', '*')
message3 = message.replace(' ', '*').replace('Duran', 'DR').replace('Ramazan', 'RD')
message4 = message.center(100)  #100 karakter oluşturup yazıyı ortaya alır.

print(message1)
print(message2)
print(message3)
print(message4)