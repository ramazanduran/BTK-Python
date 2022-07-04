fruits = { 'orange', 'apple', 'banana'}

# print(fruits[0]) indekslenemez

for x in fruits:
    print(x)

fruits.add('cherry')
fruits.update(['mango','grape','apple'])   #karışık olarak ekliyor, 
                                           #aynısı olan şeyleri de eklemiyor.

fruits.remove('mango')          #silmek için kullanılıyor
fruits.discard('apple')         #silmek için kullanılıyor
fruits.pop()                    #indeksi olanlarda en sondakini siler burada belli değil.

fruits.clear()

print(fruits)

# myList = [1,2,5,4,4,2,1]
# print(myList)
# print(set(myList))