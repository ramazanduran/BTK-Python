for item in range (10):
    print(item)

for item1 in range(3,10):
    print(item1)

for item2 in range (3,10,2):
    print(item2)

print(list(range(5,50,7)))

# enumarate
indexx = 0
greeting = 'Hello There'

for letter in greeting:
    print(f'indexx: {indexx} letter: {greeting[indexx]}')
    indexx +=1

for index, letter in enumerate(greeting):
    print(f'index: {index} letter: {letter}')

for item in enumerate(greeting):
    print(item)

# zip

list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
list3 = [100,200,300,400,500]

print(list(zip(list1, list2, list3)))

for item in zip(list1, list2, list3):
    print(item)

for a,b,c in zip(list1, list2, list3):
    print(a,b,c)