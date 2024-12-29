class Library:
    def __init__(self):
        self.user_details = {}
        self.book_details = {}
        self.current_user = None

    def privilege(self):
        if self.current_user.privilege == "admin":
            return True
        else:
            print("You have no privilege to access this section!")
            return False

    def is_book_found(self, book_name):
        if book_name in self.book_details:
            return True
        else:
            print(f"{book_name} is not available")
            return False

    def is_users_found(self, user_name):
        if user_name in self.user_details:
            return True
        print("User is not found!")
        return False
    def add_book(self):
        if self.privilege():
            book_name = input("Enter the name of the book: ")
            author_name = input("Enter the name of the author: ")
            book_count = int(input("Enter how many copy's of this book is available: "))
            self.book_details[book_name] = Book(book_name, author_name, book_count)
            print("book added successfully!")
    def remove_book(self):
        if self.privilege():
            remove_book = input("Enter the name of the book to remove: ")
            if self.is_book_found(remove_book):
                self.book_details.pop(remove_book)
                print("Book removed successfully")

    def borrow_book(self):
        book_name = input("Enter the name of the book: ")
        if self.is_book_found(book_name):
            book = self.book_details[book_name]
            if book_name in self.current_user.borrow_copy:
                print("You can only borrow 1 copy at time!")
                return
            if book.book_count > 0:
                self.current_user.borrow_copy.append(book_name)
                book.book_count -= 1
                print("book taken successfully")
        else:
            print("This book is not available now, please come back later.")

    def returns_book(self):
        return_book_name = input("Enter the name of the book: ")
        self.book_details[return_book_name].book_count += 1
        self.current_user.borrow_copy.remove(return_book_name)
        print(f"Book returned successfully")

    def add_user(self):
        if self.privilege():
            username = input("Enter the name of the user: ")
            password = input("Create a password: ")
            contact = int(input("Enter the contact information: "))
            age = input("Enter the age: ")
            id_no = input("Enter the ID number: ")
            total_book = int(input("Enter total book taken: "))
            self.user_details[username] = User(username, password, contact, id_no, age, "user", 1)
            print("user added successfully!")

    def delete_user(self):
        if self.privilege():
            remove_user = input("Enter the name of the user you need to remove: ")
            if self.is_users_found(remove_user):
                self.user_details.pop(remove_user)
                print("user has been deleted successfully: ")
    def list_users(self):
        if self.privilege():
            for user, details in self.user_details.items():
                print(f"- Name: {user}, Age: {details.age}, Contact: {details.contact}, Privilege: {details.privilege}")


    def menu(self):
        while True:
            print("1.ADD BOOK\n2.DELETE BOOK\n3.BORROW BOOK\n4.RETURN BOOK\n5.SEARCH BOOK\n6.LIST BORROWED BOOK\n7.LIST AVAILABLE BOOK\n8.ADD USER\n9.DELETE USER\n10.LIST USER\n12.LOGOUT")
            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    library_management.add_book()
                elif choice == 2:
                    library_management.remove_book()
                elif choice == 3:
                    library_management.borrow_book()
                elif choice == 4:
                    library_management.returns_book()
                elif choice == 5:
                    pass
                elif choice == 6:
                    pass
                elif choice == 7:
                    pass
                elif choice == 8:
                    self.add_user()
                elif choice == 9:
                    self.delete_user()
                elif choice == 10:
                    self.list_users()
                elif choice == 11:
                    pass
                elif choice == 12:
                    self.log_in()
                else:
                    print("Enter a valid option!")
                    break

            except ValueError:
                print("Enter a valid input: ")

    def log_in(self):
        while True:
            print("1.Login\n2.Exit")
            try:
                option = int(input("Enter your option: "))
                if option == 1:
                    username = input("username: ")
                    password = input("password: ")

                    if username not in self.user_details or self.user_details[username].password != password:
                        print("username or password is correct!")
                        continue
                    self.current_user = self.user_details[username]
                    self.menu()

                elif option == 2:
                    print("Thank You!")
                    break

                else:
                    print('provide a valid number!')

            except ValueError:
                print("Please enter a valid input!")
class Book:
    def __init__(self, book_name, author_name, book_count):
        self.book_name = book_name
        self.author_name = author_name
        self.book_count = book_count

class User:
    def __init__(self, name, password, contact, id_no, age, privilege, user_count):
        self.name = name
        self.password = password
        self.contact = contact
        self.id_no = id_no
        self.age = age
        self.privilege = privilege
        self.user_count = user_count
        self.borrow_limit = 1
        self.borrow_copy = []

    def update_user(self):
        pass


library_management = Library()
library_user = User("default","","","","","", "")
library_books = Book("Harry 2", "Jk",3)
library_management.book_details["Harry 1"] = Book("Harry 1", "JK", 5)
library_management.user_details["Rahul"] = User("Rahul", "7248", 9496320858, 1, 26, "admin",1)
library_management.log_in()


