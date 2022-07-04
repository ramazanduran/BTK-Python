list = [1, 2, 3]
tuple = (1, 'iki', 3)

"""
tuple liste ile aynı özellikte fakrlılık olarak 
tuple listesi oluşturulduktan sonra işlemlerle 
ekleme çıkarma gibi iznimiz bulunmamaktadı. 
"""

# print(type(list))
# print(type(tuple))

# print(list[2])
# print(tuple[2])

# print(len(tuple))
# print(len(list))

list = ['ali','veli']
tuple = ('damla','ayşe','ayşe')
names = ('demet','emel','ayşe') + tuple

print(type(names))
print(names)

list[0] = 'ahmet'
# tuple[0] = 'deniz'

print(tuple.count('ayşe'))
print(tuple.index('ayşe'))

print(list)
print(tuple)