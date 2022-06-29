from catalog import Catalog
from book import Book
from student import Student
from students import students

catalog = Catalog()


class Library:

    def __init__(self):
        self.itemsout = {}
        self.books = []
        self.students = [students.student1, students.student2, students.student3, students.student4]

    def addbook(self, Book):
        catalog.addbook(Book)

    def removebook(self, Book):
        catalog.removebook(Book)

    def checkout(self, Student, Book):
        checked = True
        checker = True
        for j in self.students:
            if Student.__eq__(j):
                checker = True
                for i in catalog.books:
                    if Book.__eq__(i):
                        catalog.removebook(Book)
                        self.books.append(Book)
                        self.itemsout[Student] = self.books
                        print("Book successfully checkedout")
                        checked = True
                    else:
                        checked = False
                break
            else:
                checker = False
        if (checked == False):
            print("Book not available in the library")

        if (checker == False):
           print("Student isn't even signed up")

    def checkin(self, Student, Book):
        checked = True
        for i in self.books:
            if Book.__eq__(i):
                self.books.remove(Book)
                catalog.addbook(Book)
                checked = True
                print("Book successfully checkedin")
            else:
                checked = False
        if (checked == False):
            print("Book was never checkedout to you")

    def itemsoutStu(self, Student):
        return self.itemsout.get(Student)

    def checkitems(self):
        return catalog.books
