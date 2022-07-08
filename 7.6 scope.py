#global scope
x = 'global x'

def function ():
    #local scope
    x= 'local x'
    print(x)

function()
print(x)


"""
okumakta fayda var
https://medium.com/kodelim/global-ve-yerel-de%C4%9Fi%C5%9Fkenler-9f4480db8402
"""

#global
name = 'Ramazan'

def changeName (new_name):
#local
    name = new_name
    print (name)

changeName('Duran')
print(name)

"""
"""

name1 = 'global string'

def greeting():
    name1 = 'Ramazan'

    def hello():
        print('Hello ' + name1)

    hello()

greeting()

"""
"""

name1 = 'global string'

def greeting():
    name1 = 'Ramazan'

    def hello():
        name1 = 'Duran'
        print('Hello ' + name1)

    hello()

greeting()

"""
"""

name1 = 'global string'

def greeting():
    #name1 = 'Ramazan'

    def hello():
        print('Hello ' + name1)

    hello()

greeting()


"""
"""

x = 50
def test(): 
    global x
    print(f'x : {x}')

    x = 100
    print(f'changed x to {x}')

test()
print(x)



