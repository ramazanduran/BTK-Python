numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a', 'g', 's', 'b', 'y', 'a', 's']

val = min(numbers)
val = max(numbers)
val = max(letters)
val = min(letters)

val = numbers[3:6]
val = numbers[:3]
val = numbers[4:]

numbers[4] = 40

numbers.append(49)
numbers.append(59)
numbers.insert(3, 78)   #3. indeksten sonra ekler     
numbers.insert(-1,52)   #-1 denilirse en sondaki indeksten bir önce eklenir

#numbers.pop()         en sondaki elemanı siler
# numbers.pop(0)       ilk elemanı siler    
# numbers.pop(-1)      en sondaki elemanı siler boş olanla aynıdır.
# numbers.remove(59)   burada aradığı elemanı siler 


numbers.sort()      #küçükten büyüğe doğru sıralar
numbers.reverse()   #tersine çevirmeye yarar

letters.sort()      #alfabetik sıraya göre sıralar 
letters.reverse()   #tersine çevirir


print(numbers)
print(letters)

print(len(numbers))
print(len(letters))

print(numbers.count(10))
print(letters.count('a'))

numbers.clear()
print(numbers)