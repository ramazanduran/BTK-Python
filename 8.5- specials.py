myList = [1,2,3]
myString = 'my string'

print(len(myList))
print(len(myString))
print(type(myList))
print(type(myString))

"""
*********************************
"""

class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print('movie objesi oluşturuldu.')

    def __str__(self):
        return "{} by {}".format(self.title, self.director)

    def __len__(self):
        return self.duration

    def __del__(self):
        print('film ögesi silindi.')

m = Movie('film adı', 'yönetmen abı', 'film süresi')
m1 = Movie('Titanic', 'James Cameron', 194)

print(str(myList))
print(str(m))
print(str(m1))

print(len(myList))
print(len(m1))


"""
Bakmakta faydalı olacak yerler
https://python-istihza.yazbel.com/nesne_tabanli_programlama2.html
https://docs.python.org/3/reference/datamodel.html
https://www.informit.com/articles/article.aspx?p=453682&seqNum=6
"""
