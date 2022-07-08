
def square (num): return num*2
result = square(2)
print(result)

"""
"""
def square1 (num1): return num1**2

numbers1 = [1,3,5,9]
num1=[]
for i in numbers1:
    num1.append(square1(i))
print(num1)

"""
"""

def square2 (num2): return num2**2

numbers2 = [1,3,5,9]
result = list( map (square2, numbers2) )
print(result)

# ikinci yazdırma şekli for ile

for item in map(square2, numbers2):
    print(item)

"""
"""

numbers3 = [1,3,5,9]
result3 = list( map (lambda num3:num3**2, numbers2) )
print(result3)
#def olmadan kullanım şeklinde lambda kullanım yöntemi

"""
"""

square4 = lambda num4 : num4**2 
numbers4 = [1,3,5,9]
list4 = []
for a in numbers4:
    result4 = square4(a)
    list4.append(result4)
print(f'list4: {list4}')

"""
"""

numbers5 = [1,3,5,9,10,4]
def check_even (num5):
    return num5 % 2 == 0

result5= list(filter(check_even, numbers5))

print(result5)

#def dışında lambda yöntemi ile çözüm

numbers6 = [1,3,5,9,10,4]
 
result6= list(filter(lambda  num6 : num6 % 2 == 0, numbers6))

print(result6)

"""
"""

numbers7 = [1,3,5,9,10,4]

check_even1 = lambda num7 : num7 % 2 == 0 

result7= list(filter(check_even1, numbers7))

print(result7)