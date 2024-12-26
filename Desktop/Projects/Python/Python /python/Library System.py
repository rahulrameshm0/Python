class Library_Management:
    def __init__(self):
        self.user_details = {}
        self.current_user = None

    def check_privilege(self):
        if self.current_user.privilege == "admin":
            return True
        else:
            print("You have no privilege to access this one!")
            return False

    def user_found(self, name):
        if name in self.user_details:
            return True
        else:
            print("user is not found!")
            return False

    def list_all_user(self):
        if self.check_privilege():
            for index, (user, details) in enumerate(self.user_details.items(), start=1):
                print(f"{index}.Name: {user}, privilege: {details.privilege}, Contact No: {details.contact} Books Taken: {details.books_collected}")

    def add_user(self):
        if self.check_privilege():
            add_name = input("Enter the name: ")
            add_password = input("Enter the password")
            add_age = input("Enter your age: ")
            contact = int(input("Enter contact no: "))
            taken_books = input("Enter the books Taken: ")
            self.user_details[add_name] = User(add_name, add_password, add_age, contact, "user", taken_books)
            print("New user has been successfully created in library!")

    def remove_user(self):
        if self.check_privilege():
            remover_name = input("Enter the name of the remover: ")
            if self.user_found(remover_name):
                self.user_details.pop(remover_name)
                print("User has been removed form the library!")

    def search_user_details(self):
        if self.check_privilege():
            search_name = input("Enter the name of the user: ")
            if self.user_found(search_name):
                print(f"{self.user_details}")

    def update_user_information(self):
        if self.check_privilege():
            current_name = input("Enter your current name: ")
            if self.user_found(current_name):
                update_name = input("Enter new name: ")
                update_contact = int(input("Update the number: "))
                self.user_details.update({update_name: update_contact})
                print("User and contact")

    def view_profile(self):
        if self.check_privilege():
            view_user = input("Enter the name of the user: ")
            if self.user_found(view_user):
                print(f"Privilege: {self.current_user.privilege}")
                print(f"Age: {self.current_user.age}")
                print(f"Borrowed Books: {self.current_user.books_collected}")

    def user_login(self):
        while True:
            print("1.Login\n2.Exit")
            try:
                option = int(input("Enter your option: "))
                if option == 1:
                    username = input("username: ")
                    password = input("password: ")
                    if username not in self.user_details or library.user_details[username].password != password:
                        print("username or password is incorrect!")
                        continue
                    print(f"Welcome {username}")
                    self.current_user = self.user_details[username]
                    self.menu()
            except ValueError:
                print("Enter a valid input!")

    def menu(self):
        while True:
            print("1[ADD USER]\t2[REMOVE USER]\t3[USER DETAILS]\t4[SEARCH NAME OR AUTHOR OF THE BOOK]\t5[VIEW BOOK]\t"
                  "6[ADD BOOK]\n7[REMOVE BOOK]\t8[BORROW BOOK]\t9[RETURN BOOK]\t10[VIEW PROFILE]\t11[SEARCH BOOK]\t12[LIST BORROWED BOOKS]\t13[LOGOUT]")
            try:
                choice = int(input("Enter your choice: "))

                if choice == 1:
                    library.add_user()

                elif choice == 2:
                    library.remove_user()

                elif choice == 3:
                    library.view_profile()

                elif choice == 4:
                    users.search_and_filter()

                elif choice == 5:
                    library_book.view_books()

                elif choice == 6:
                    library_book.add_book()

                elif choice == 7:
                    library_book.remove_book()

                elif choice == 8:
                    users.borrow()

                elif choice == 9:
                    users.return_books()

                elif choice == 10:
                    library.view_profile()

                elif choice == 11:
                    users.search_book()

                elif choice == 12:
                    library_book.list_borrowed_book()

                elif choice == 13:
                    library.user_login()
                    break

            except ValueError:
                print("Enter a valid input: ")
class Book:
    def __init__(self, author_name, book_name):
        self.author_name = author_name
        self.book_name = book_name
        self.is_borrowed = False
        self.book_details = {}
        self.borrowed_book = []


    def is_book_found(self, books_name):
        if books_name in self.book_details:
            return True
        print(f"{books_name} is not available!")
        return False

    def borrowed_books(self, name_of_book):
        if name_of_book in self.borrowed_book:
            return True
        else:
            print("No borrowed book from library!")
            return False

    def list_borrowed_book(self):
        if self.borrowed_book:
            for index, i in enumerate(self.borrowed_book, start=1):
                print(f"{index}) {i}")
        else:
            print("No borrowed books from the library!")

    def view_books(self):
        for index, (book, details) in enumerate(self.book_details.items(), start=1):
            print(f"{index} Book Name: {book}, Author name: {details.author_name}")

    def add_book(self):
        if library.check_privilege():
            add_book_name = input("Enter the name of the book: ")
            add_author_name = input("Enter the name of the author: ")
            self.book_details[add_book_name] = Book(add_author_name, add_book_name)
            print("Book & Author name has been saved!")

    def remove_book(self):
        if library.check_privilege():
            removing_book = input("Enter the name of the book: ")
            if library_book.is_book_found(removing_book):
                self.book_details.pop(removing_book)
                print("Book has been removed successfully!")

    def accept_book_return(self):
        if library.check_privilege():
            borrowed_book_name = input("Enter the name of the book you borrowed: ")
            if borrowed_book_name in self.is_book_found(borrowed_book_name):
                self.borrowed_book.remove(borrowed_book_name)
                print("Book Accepted!")

class User:
    def __init__(self, username, password, age, contact, privilege, books_collected):
        self.username = username
        self.password = password
        self.age = age
        self.contact = contact
        self.privilege = privilege
        self.books_collected = books_collected

    def max_book_allowed(self, maximum_book):
        if len(self.books_collected) >= maximum_book:
            print("Your are only allowed three books at a time!")
            return True
        return False

    def search_book(self):
        search_books = input("Enter the name of the book")
        if library_book.is_book_found(search_books):
            print(f"{search_books} is available right now!")
    def search_and_filter(self):
        search = input("Enter the Title of the book or Name of the auther: ")
        for index, book, details in enumerate(library_book.book_details.items(), start=1):
            if search in book or search in details['author']:
                print(f"{index}.{book}, {details["author"]}")

    def borrow(self):
        borrow_book = input("Enter the name of the book: ")
        if library_book.is_book_found(borrow_book):
            if self.max_book_allowed(3):
                print("You are only allowed 3 books at a time!")
                return
            library_book.borrowed_book.append(borrow_book)
            print("Book has been borrowed successfully!")

    def return_books(self):
        return_book_name = input("Enter your name: ")
        if return_book_name not in library_book.borrowed_book:
            print("This is not the book you have taken from the library!")
            return False
        library_book.borrowed_book.remove(return_book_name)
        print("Book has return successfully!")
        return True

library = Library_Management()

library_book = Book("Default Author", "Default Book")

library_book.book_details["Think like A Monk"] = Book("Jay Shetty", "Think like A Monk")
library_book.book_details["Ikigai"] = Book("Japanese", "Ikigai")
library_book.book_details["The Secret"] = Book("Secret", "John")

library.user_details["Rahul"] = User("Rahul", "7248", 25, 9037579459, "admin", "The power of now, Ikigai")
library.user_details["Fazil"] = User("Fazil", "7968", 21, 9400771367, "user", "Atomic Habits")
library.user_details["Afam"] = User("Afam", "6548", 25, 9496320858, "user", "The Secret")
library.user_details["Sonny"] = User("Sonny", "2341", 25, 2315698475, "user", "The Monster")

users = User("DefaultUser", "defaultpass", 0, 0, "user", [])

library.user_login()