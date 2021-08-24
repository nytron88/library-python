from book import Book
from student import Student
from catalog import Catalog


# catalog1 = Catalog()

class Library:

    def __init__(self, Catalog):
        self.Catalog = Catalog
        self.itemsOut = {}
        self.books = []

    def addBook(self, Book):
        Catalog.addbook(self.Catalog, Book)

    def removeBook(self, Book):
        Catalog.removebook(self.Catalog, Book)

    def checkout(self, Student, Book):
        checker = False
        for i in self.Catalog.books:
            if Book.__eq__(i):
                self.books.append(Book)
                self.itemsOut[Student] = self.books
                self.Catalog.removebook(Book)
                print(f"Book checkout - {Student.__str__()} : {Book.__str__()}")
                checker = False
                break
            else:
                checker = True
        if checker:
            print("Book not available in the library")

    def checkIn(self, Student, Book):
        idk = False
        checker = False
        for i in self.itemsOut.keys():
            if Student.__eq__(i):
                idk = True
                break
            elif not Student.__eq__(i):
                idk = False
                print("That Book was never issued to you")
                break
        for i in self.books:
            if Book.__eq__(i) and idk:
                self.books.remove(Book)
                self.Catalog.addbook(Book)
                print(f"Book CheckIn- {Student.__str__()}, {Book.__str__()}")
                checker = False
                break
            else:
                checker = True
        if checker:
            print("Book was never issued to you")

    def checkItems(self, Student):
        return self.itemsOut.get(Student)
