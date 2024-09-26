class Book:
    def __init__(self, title, pb_year, author, b_type, status='available'):
        self.title = title
        self.pb_year = pb_year
        self.author = author
        self.b_type = b_type
        self.status = status

    def borrow(self):
        if self.status == 'available':
            self.status = 'borrowed'

    def return_book(self):
        if self.status == 'borrowed':
            self.status = 'available'

    def description(self):
        print(f'The book "{self.title}" was published in {self.pb_year} by {self.author}. It is a {self.b_type} book and is currently {self.status}.')


class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def book_list(self):
        return [book.title for book in self.books]


class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.status == 'available':
            book.borrow()  # Call the borrow method of the Book class
            self.borrowed_books.append(book)
            print(f'The book "{book.title}" has been borrowed by {self.name}')
        else:
            print(f'{self.name} cannot borrow the book "{book.title}" because it is not available.')

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()  # Call the return method of the Book class
            self.borrowed_books.remove(book)
            print(f'The book "{book.title}" has been returned by {self.name}')
        else:
            print(f'{self.name} does not have the book "{book.title}" borrowed.')

    def list_borrowed_books(self):
        return [book.title for book in self.borrowed_books]


class Library:
    def __init__(self):
        self.books = []
        self.authors = []
        self.users = []

    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)
            print(f'{book.title} has been added to the library.')
        else:
            print(f'{book.title} already exists in the library.')

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f'{book.title} has been removed from the library.')
        else:
            print(f'{book.title} does not exist in the library.')

    def add_author(self, author):
        self.authors.append(author)

    def remove_author(self, author):
        if author in self.authors:
            # Remove all books associated with this author
            self.books = [book for book in self.books if book.author != author.name]
            self.authors.remove(author)
            print(f'Author "{author.name}" and their books have been removed from the library.')
        else:
            print(f'Author "{author.name}" not found in the library.')

    def add_user(self, user):
        self.users.append(user)
        print(f'User "{user.name}" has been added to the library.')

    def remove_user(self, user):
        if user in self.users:
            # Check if the user has borrowed books
            if user.borrowed_books:
                print(f'User "{user.name}" has borrowed books and must return them before removal.')
            else:
                self.users.remove(user)
                print(f'User "{user.name}" has been removed from the library.')
        else:
            print(f'User "{user.name}" not found in the library.')

    def show_available_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Available books:")
            for book in self.books:
                if book.status == 'available':
                    print(f'- {book.title} by {book.author}')

    def list_authors(self):
        if not self.authors:
            print("No authors in the library.")
        else:
            print("Authors in the library:")
            for author in self.authors:
                print(f'- {author.name}')

    def list_borrowed_books(self):
        borrowed_books = [book for user in self.users for book in user.borrowed_books]
        if not borrowed_books:
            print("No books have been borrowed.")
        else:
            print("Borrowed books:")
            for book in borrowed_books:
                print(f'- {book.title} by {book.author}')

    def show_users(self):
        if not self.users:
            print("There are no users in the library.")
        else:
            print("Current users in the library:")
            for user in self.users:
                print(user.name)

# Displaying how the project works :

# Creating instances of the Library, Author, and Book classes
library = Library()

# Adding authors
author1 = Author("George Orwell")
author2 = Author("J.K. Rowling")

library.add_author(author1)
library.add_author(author2)

# Creating books
book1 = Book("1984", 1949, author1.name, "Dystopian")
book2 = Book("Harry Potter and the Philosopher's Stone", 1997, author2.name, "Fantasy")

# Adding books to the library
library.add_book(book1)
library.add_book(book2)

# Creating a user
user1 = User("Alice")

# Adding user to the library
library.add_user(user1)

# Showing available books before borrowing
library.show_available_books()

# User borrowing a book
user1.borrow_book(book1)

# Showing available books after borrowing
library.show_available_books()

# Listing borrowed books by the user
print(f'Books borrowed by {user1.name}: {user1.list_borrowed_books()}')

# User returning the book
user1.return_book(book1)

# Showing available books after returning
library.show_available_books()

# Listing borrowed books again
print(f'Books borrowed by {user1.name}: {user1.list_borrowed_books()}')

# Listing all authors
library.list_authors()

# Listing current users
library.show_users()
