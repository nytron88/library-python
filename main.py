from library import Library
from book import Book
from student import Student

lib = Library()
stud = ""
done = False
logged = False

print("Welcome to my Library System \n")
sign = input("Sign 'up' or Sign 'in': ")

while not done:
    if sign == "up":
        up_name = input("What's your name: ")
        up_roll = int(input("Choose a roll number: "))
        stud = Student(up_name, up_roll)
        checker = False
        for i in lib.students:
            if stud.__eq__(i):
                print("Change roll number please")
                checker = True
                done = True
                break
            else:
                checker = False
        if not checker:
            print("Success")
            lib.students.append(stud)
            done = True
            logged = True
    elif sign == "in":
        in_name = input("What's your name: ")
        in_roll = int(input("What's your roll number: "))
        stud = Student(in_name, in_roll)
        for i in lib.students:
            if stud.__eq__(i):
                print("Successfully signed in!")
                done = True
                logged = True
                break
            else:
                print("Invalid login")
                done = True
                break

if logged:
    print()
    print("'lib' to check what books are available in the library. 'details' to check what books are checked out "
          "to you. 'checkout' to checkout a book. 'checkin' to return a book to the library. 'done' to end the program \n")

while logged:
    command = input("Type in the command you want to use: ")

    if command.lower() == "lib":
        print(lib.checkitems())

    elif command.lower() == "checkout":
        print(lib.checkitems())
        count = int(input("How many books: "))
        i = 0
        while i < count:
            name = input("Book name: ")
            author = input("Author: ")
            book = Book(name, author)
            lib.checkout(stud, book)
            print(lib.itemsoutStu(stud))
            print("Successfully checkedout")
            i += 1

    elif command.lower() == "checkin":
        f"\n These items are checkedout to you: {lib.itemsoutStu(stud)} \n"
        count = int(input("How many books: "))
        print("Which ones: ")
        i = 0
        while i < count:
            name = input("Book name: ")
            author = input("Author: ")
            book = Book(name, author)
            lib.checkin(stud, book)
            print(lib.itemsoutStu(stud))
            print("Successfully checkedin")
            i += 1

    elif command.lower() == "done":
        print("Thanks for using my library system!")
        logged = False
        break

    elif command.lower() == "details":
        print(lib.itemsoutStu(stud))

    else:
        print("Error command please try again")
