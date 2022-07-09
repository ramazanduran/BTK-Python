# Inheritance (Kalıtım): Miras alma

# Person => name, lastname , age, eat(), run(), drink()
# Student(Person), Teacher(Person)

# Animal => Dog(Animal), Cat(Animal)


class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print('Person Created')

    def who_am_i(self):
        print('I am a person')

    def eat (self):
        print('I am eating')

class Student(Person):
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname)
        self.studenNumber = number
        print('Student Created')

     # override
    def who_am_i(self):             #bunu yazmasak perdondan alırdı. 
        print('I am a student')     #bunu yazınca üstteki bilgiyi es 
                                    #geçip burayı kabul eder.

    def sayHello(self):
        print('Hello I am a student')
        print(f'Hello {self.who_am_i()}') #bir atama olmadığı için print
                                          #içini yazdırmaz none der
    
class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname)  #Person(). yazımının alternatifi
        self.branch = branch            #super(). şeklinde olabilir

    def who_am_i(self):
        print(f'I am a {self.branch} teacher')

p1 = Person ('Ali', 'Yılmaz')
s1 = Student('Bahri', 'Yaylamaz', 123456)
t1 = Teacher('Mustafa', 'Özcan', 'Math')

t1.who_am_i()

print(p1.firstName + ' ' + p1.lastName)
print(s1.firstName + ' ' + s1.lastName+ ' '+ str(s1.studenNumber))

p1.who_am_i()
s1.who_am_i()
p1.eat()
s1.eat()
s1.sayHello()