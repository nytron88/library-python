dfrom book import Book
from student import Student
from catalog import Catalog


# catalog1 = Catalog()

class Library:

    def __init__(self, Catalog):
        self.Catalog = Catalog
        self.itemsOut = {}
        self.books = []
        self.test = list(self.itemsOut)

    def addBook(self, Book):
        Catalog.addbook(self.Catalog, Book)

    def removeBook(self, Book):
        Catalog.removebook(self.Catalog, Book)

    def checkout(self, Student, Book):

        for i in self.Catalog.books:
            if not Book.__eq__(i):
                print("No")
                break
            else:
                self.books.append(Book)
                self.itemsOut[Student] = self.books
                self.Catalog.removebook(Book)
                print(f"Book checkout - {Student.__str__()} : {Book.__str__()}")
                break

    def checkIn(self, Student, Book):
        idk = False
        idk2 = False
        for i in self.itemsOut.keys():
            if Student.__eq__(i):
                idk = True
                break
            else:
                idk = False
                break
        for i in self.books:
            if Book.__eq__(i) and idk:
                idk2 = True
                self.books.remove(Book)
                self.Catalog.addbook(Book)
                print("Hello")
                break
            else:
                idk2 = False
                break

    def checkItems(self, Student):
        return self.itemsOut.get(Student)