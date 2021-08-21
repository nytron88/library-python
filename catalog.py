dfrom book import Book

book = Book("No", "No")
book2 = Book("Hi", "hi")


class Catalog:
    def __init__(self):
        self.books = [book, book2]

    def addbook(self, Book):
        self.books.append(Book)

    def removebook(self, Book):
        self.books.remove(Book)

    def __str__(self):
        return f"{self.books}"
