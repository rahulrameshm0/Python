class Library_Managemnet:

    def __init__(self):
        self.users = {}
        self.books = ["The Power Of Now", "Ikigai", "The Secret","Surrounded by idiots"]
        self.current_user = None

    def is_book_found(self, book_name):
        if book_name in self.books:
            return True
        print(f"{book_name} is not available!")
    def is_privilege(self):
        if self.current_user.privilege == "admin":
            return True
        print("You don't have privilege!")
        return False

    def list_books(self):
        if self.is_privilege():
            for index, books in enumerate(self.books,start=1):
                print(f"{index}.{books}")

    def list_users(self):
        if self.is_privilege():
            for index, (name,details) in enumerate(self.users.items(),start=1):
                print(f"{index}.Name: {name}, Privilege: {details.privilege}")

    def create_user(self):
        if self.is_privilege():
            user_name = input("Enter the name of the user: ")
            create_password = input("Create password: ")
            self.users[user_name] = User(user_name,create_password,"user")
            print("user has been successfully created")
    def add_books(self):
        if self.is_privilege():
            book_name = input("Enter the name of the book: ")
            self.books.append(book_name)
            print(f"{book_name} has added to the library")

    def purchase(self):
        book_name = input("Enter the name of the book: ")
        if self.is_book_found(book_name):
            self.books.remove(book_name)
            print(f"{book_name} has successfully purchased!")

    def check(self):
        if self.is_privilege():
            check_book_name = input("Enter the name of the book weather it is available or not: ")
            if self.is_book_found(check_book_name):
                print(f"{check_book_name} is available.")

    def delete_books(self):
        if self.is_privilege():
            delete_books = input("Enter the name of the book: ")
            if self.is_book_found(delete_books):
                self.books.remove(delete_books)
                print("Book successfully deleted!")

    def login(self):
        while True:
            try:
                print("Welcome to our library")
                print("1.Login\n2.Exit")
                option = int(input("Enter your option: "))
                if option == 1:
                    username = input("username: ")
                    password = input("password: ")
                    if username not in self.users or library.users[username].password != password:
                        print("username or password incorrect!")
                        continue
                    self.current_user = self.users[username]
                    self.menu()
                elif option == 2:
                    print("Thank you for using our Library!")
                    exit()
            except ValueError:
                print("Enter a valid input!")

    def menu(self):
        while True:
            try:
                print("1.LIST BOOK\n2.LIST USER\n3.CREATE USER\n4.ADD BOOKS\n5.PURCHASE BOOK\n6.CHECK BOOK\n7.RETURN BOOK\n8.LOGOUT")
                choice = int(input("Enter your choose: "))
                if choice == 1:
                    library.list_books()
                elif choice == 2:
                    library.list_users()
                elif choice == 3:
                    library.create_user()
                elif choice == 4:
                    library.add_books()
                elif choice == 5:
                    library.purchase()
                elif choice == 6:
                    library.check()
                elif choice == 7:
                   if self.current_user:
                       library.current_user.return_book()
                elif choice == 8:
                    library.login()
                    break
                else:
                    print("Enter a valid input")
            except ValueError:
                print("Enter a valid number!")
class User:

    def __init__(self,username,password,privilege):
        self.username = username
        self.privilege = privilege
        self.password = password


    def return_book(self):
        returning = input("returning book name: ")
        library.books.append(returning)
        print("Book Written Successfully!")


library = Library_Managemnet()
library.users["Rahul"] = User("Rahul", "7248", "admin")
library.users["Jonny"] = User("Jonny", "6512", "user")
library.users["Malavika"] = User("Malavika", "6312", "user")
library.login()