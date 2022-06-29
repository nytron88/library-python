from booksinlibrary import Books
from book import Book

class Catalog:
    def __init__(self):
        self.books = [Books.book1, Books.book2, Books.book3]

    def addbook(self, Book):
        self.books.append(Book)

    def removebook(self, Book):
        self.books.remove(Book)
