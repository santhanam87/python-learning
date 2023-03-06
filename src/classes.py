class Book:
    title = ''
    authors = []
    def __init__(self, title='', authors=[]):
        self.title = title
        self.authors = authors
    def getTitle(self):
        return self.title
    def addAuthor(self, author):
        self.authors.append(author)
    def getAuthors(self):
        return self.authors
    
class TextBook(Book):
    grade = None
    def __init__(self, title='', authors=[]):
        super().__init__(title, authors)
    def getGarde(self):
        return self.grade

    
englishBook = TextBook('A new text book', ['shakunth'])
#englishBook.title = 'New litrature book'
englishBook.addAuthor('santhanam')
englishBook.addAuthor('shravan')
englishBook.grade = 'collage'

print(englishBook.title)
print(englishBook.authors)
print(englishBook.grade)