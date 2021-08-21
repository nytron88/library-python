from book import Book
from BooksInLibrary import Books


class Catalog:
    def __init__(self):
        self.books = [Books.book, Books.book2, Books.book3]

    def addbook(self, Book):
        self.books.append(Book)

    def removebook(self, Book):
        self.books.remove(Book)

