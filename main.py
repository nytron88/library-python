from book import Book
from student import Student
from library import Library
from catalog import Catalog

catalog = Catalog()
lib = Library(catalog)

id = input("id: ")
passw = (input("Passcode: "))
done = False

if id == "AdiJai8334" and int(passw) == 1111:

    stud = Student("Sid", 1)
    stud2 = Student("Adi", 2)

    who_name = input("Your Name: ")
    who_rollnumber = int(input("Your roll number: "))

    print("You Logged in as a student")
    print("'lib' to check what books are available in the library. 'details' to check what books are checked out "
          "to you. 'checkout' to checkout a book. 'checkin' to return a book to the library")

    stud_1 = False

    if who_name == stud.name and who_rollnumber == stud.roll_number:
        stud_1 = True
    elif who_name == stud2.name and who_rollnumber == stud2.roll_number:
        stud_1 = False
    else:
        done = True
        print("Wrong student, restart")
    while not done:
        command = input("\n Type in the command you want to use: ")

        if command == 'checkout':
            book_name = input("Book name: ")
            book_author = input("Author name: ")
            book = Book(book_name, book_author)
            lib.checkout(stud, book)


elif id == "SidJai6944" and int(passw) == 0000:
    print("You Logged in as a teacher")

else:
    print("Login failed, please try again")
    done = True
