class Library_Management:

    def __init__(self):
        self.users_details = {}
        self.current_user = None

    def check_privilege(self):
        if self.current_user.privilege == "admin":
            return True
        else:
            print("You don't have privilege to access this account")
            return False

    def is_book_found(self,books_name):
        if books_name in self.book_details:
            return True
        else:
            print(f"{books_name} is not available")

    def maximum_book(self):
        pass

    def is_users_found(self,username):
        if username in self.users_details:
            return True
        else:
            print("User is not found in the list")

    def check_borrowig_book_true(self, borrowed_book):
        if borrowed_book in library_user.borrowed_books:
            return True
        else:
            print("This is not the book you have borrowed from this library: ")
            return False

    def check_borrowed_book(self):
        if self.check_privilege():
            for index, book in enumerate(library_user.borrowed_books, start=1):
                print(f"{index}.{book}")

    def view_user_profile(self):
        if self.check_privilege():
            viewer_name = input("Enter the name of the user: ")
            if self.is_users_found(viewer_name):
                print(f"Privilege: {self.current_user.privilege}\nAge: {self.current_user.age}\nContact: {self.current_user.contact}\n")

    def add_user(self):
        if self.check_privilege():
            add_name = input("Enter the name of the user: ")
            create_password = input("Create a password: ")
            add_age = input("Enter age")
            add_contact = input("Enter contact no: ")
            add_book = input("Enter the name of the book that has been collected from the library: ")
            self.users_details[add_name] = User(add_name, create_password, add_contact, add_age, "user", add_book)
            print("User has been added successfully into the library: ")

    def delete_user(self):
        if self.check_privilege():
            remove_user = input("Enter the name of the user: ")
            if self.is_users_found(remove_user):
                self.users_details.pop(remove_user)
                print(f"{remove_user} has been successfully removed!")

    def view_all_user(self):
        if self.check_privilege():
            for index, (user, details) in enumerate(self.users_details.items(), start=1):
                print(f"{index}. Name: {user}, Contact: {details.contact}, {details.age}, Privilege: {details.privilege}")

    def add_book(self):
        if self.check_privilege():
            book_name = input("Enter the name of the book: ")
            author_name = input("Enter the name of the author: ")
            library_books.book_details[book_name] = Book(book_name, author_name)
            print("Book added successfully to the library!")

    def delete_book(self):
        if self.check_privilege():
            remove_book = input("Enter the name of the book: ")
            if self.is_book_found(remove_book):
                library_books.book_details.pop(remove_book)
                print(f"{remove_book} has been removed successfully from the library!")

    def borrowed_book(self, name_of_book):
        if name_of_book in library_user.borrowed_books:
            return True
        return False


    def view_all_book(self):
        # if self.check_privilege():
        for index, (book,detail) in enumerate(library_books.book_details.items(), start=1):
            print(f"{index}. Book Name: {book}, Author name: {detail.author_name}")

    def search_and_filter(self):
        book_or_name = input("Enter the name of the book or name of the author: ")
        for index, i in enumerate(self.users_details.values(), start=1):
            if self.is_book_found(book_or_name):
                if self.is_book_found(book_or_name):
                    print(f"{index}. Book Name: {i.book_name}, Author Name: {i.author_name}")

    def view_borrowed_book(self):
        if self.check_privilege():
            if library_user.borrowed_books:
                for index, (username, book) in enumerate(library_user.borrowed_books):
                    print(f"Name: {username}. Book Borrowed: {book}")
            else:
                print("No one borrowed any book!")
    def borrow_book(self):
        borrowing_name_of_book = input("Enter the name of the book you need to borrow: ")
        if self.is_book_found(borrowing_name_of_book):
            # if self.current_user is not None:
            library_books.book_details.pop(borrowing_name_of_book)
            library_user.borrowed_books[borrowing_name_of_book] = library_user.books_collected
            print(f"You have borrowed {borrowing_name_of_book} form the library.")

    def return_books(self):
        return_book_name = input("Enter the name of the book you are returning: ")
        if self.check_borrowig_book_true(return_book_name):
            library_user.borrowed_books.pop(return_book_name)
            library_books.book_details[return_book_name] = Book(library_books.book_name, library_books.author_name)
            print("Book return successfully.")

    def search_book(self):
        searching_books = input("Enter the name of the book: ")
        if self.is_book_found(searching_books):
            print(f"{searching_books} is available")
            question = input("Do you need to borrow the book? (yes/no): ")

            if question == "yes":
                library_books.book_details.pop(searching_books)
                library_user.borrowed_books.pop(searching_books)
                print("You have successfully borrowed the book")

            elif question == "no":
                return

            else:
                print("Enter a valid input")

    # def accept_book_return(self):
    #     if self.check_privilege():
    #         taken_book_name = input("Enter the name of the book taken: ")
    #         if self.check_borrowig_book_true(taken_book_name):
    #             library_books.book_details.pop(taken_book_name)
    #             library_user.borrowed_books.pop(taken_book_name)
    #             print("Book accepted!")

    def menu(self):
        print("Welcome to our library")
        while True:
            print("1.VIEW ALL USER\n2.ADD USER\n3.DELETE USER\n"
                  "4.VIEW USER PROFILE\n"
                  "5.ADD BOOK\n6.DELETE BOOK\n7.VIEW ALL BOOK\n"
                  "8.SEARCH BOOK\n9.BORROW BOOK\n10.RETURN BOOK\n"
                  "11.ACCEPT BOOK RETURN\n12.LIST BORROWED BOOK\n13.UPDATE USER DETAILS\n"
                  "14.UPDATE BOOK\n15.SEARCH BY NAME AUTHOR OF THE BOOK\n16.LOG OUT")
            try:
                user_choice = int(input("Enter your choice: "))
                if user_choice == 1:
                    library.view_all_user()
                elif user_choice == 2:
                    library.add_user()
                elif user_choice == 3:
                    library.delete_user()
                elif user_choice == 4:
                    library.view_user_profile()
                elif user_choice == 5:
                    library.add_book()
                elif user_choice == 6:
                    library.delete_book()
                elif user_choice == 7:
                    library.view_all_book()
                elif user_choice == 8:
                    library.search_book()
                elif user_choice == 9:
                    library.borrow_book()
                elif user_choice == 10:
                    library.return_books()
                elif user_choice == 11:
                    library.accept_book_return()
                elif user_choice == 12:
                    library.view_borrowed_book()
                elif user_choice == 13:
                    library_user.update_user_details()
                elif user_choice == 14:
                    library_books.update_book()
                elif user_choice == 15:
                    library.search_and_filter()
                elif user_choice == 16:
                    library.login()
                else:
                    print("Enter the number that has give above!")

            except ValueError:
                print("Enter a valid number!")

    def login(self):
        while True:
            print("1.Login\n2.Exit")
            try:
                option = int(input("Enter your choice: "))
                if option == 1:
                    user_name = input("Enter your username: ")
                    password = input("Enter your password: ")
                    if user_name not in self.users_details or library.users_details[user_name].password != password:
                        print("Username or password incorrect!")
                        continue
                    self.current_user = self.users_details[user_name]
                    self.menu()
            except ValueError:
                print("Please enter a valid input!")

class Book:

    def __init__(self, book_name, author_name):
        self.book_name = book_name
        self.author_name = author_name
        self.book_details = {}
    def update_book(self):
        if library.check_privilege():
            update_books = input("update the name of the book: ")
            author_name = input("update the name of the author: ")
            self.book_details.update({update_books: author_name})
            print("Book name and author name updated successfully")

class User:

    def __init__(self, name, password, contact, age, privilege, books_collected):
        self.name = name
        self.password = password
        self.contact = contact
        self.age = age
        self.privilege = privilege
        self.books_collected = books_collected
        self.borrowed_books = {}

    def update_user_details(self):
        current_username = input("Enter your current name: ")
        if library.is_users_found(current_username):
            new_name = input("Enter new name: ")
            update_number = int(input("Change number: "))
            update_age = input("Enter new age: ")
            library.users_details[new_name] = {
                "name": new_name,
                "contact": update_number,
                "age": update_age,
                "privilege": "user"
           }
            print("User detail has been updated successfully!")

library = Library_Management()

library_books = Book("", "")
library_user = User("default","default","default","default","default","default")

#USER DATA

library.users_details["Rahul"] = User("Rahul", "7248", 99496320858, "26", "admin", [])
library.users_details["James"] = User("James", "9648", 99423520829, "21", "user", [])
library.users_details["Jonny"] = User("Jonny", "3698", 9934579459, "18", "user",[])
library.users_details["Manu"] = User("Manu", "1478", 3645128974, "27", "user", [])
library.users_details["Charlie"] = User("Charlie", "3648", 9036254875, "15", "user", [])

#BOOK DATA

library_books.book_details["Think Like A Monk"] = Book("Think Like A Monk", "Jay Shetty")
library_books.book_details["Harry Potter 1"] = Book("Harry Potter 1", "JK Rowling")
library_books.book_details["Harry Potter 2"] = Book("Harry Potter 2", "JK Rowling")
library_books.book_details["Harry Potter 3"] = Book("Harry Potter 3", "JK Rowling")

library.login()