numbers = []
for x in range(10):
    numbers.append(x)
print(numbers)

number = [x for x in range (10)]
print(number)

"""
"""

for a in range(10):
    print(a**2)

num = [s**2 for s in range (10)]
print(num)

num1 = [c*c for c in range(10) if c % 3 == 0]
print(num1)

"""
"""

myString = 'Hello'
myList = []

for letter in myString:
    myList.append(letter)

print(myList)

myList1 = [letter1 for letter1 in myString]
print(myList)

"""
"""
years = [1983, 1999, 2008, 1956, 1986]

ages = [2022 - year for year in years]
print(ages)

"""
"""

results = [a if a % 2 == 0 else 'TEK' for a in range(1,10)]
print(results)

"""
"""

result = []

for b in range(3):
    for y in range (3):
        result.append((b,y))

print(result)

numm = [(r,d) for r in range(3) for d in range(3)]

print(numm)

"""
"""
numm = [(r,d,m) for r in range(3) for d in range(3) for m in range(3)]

print(numm)


