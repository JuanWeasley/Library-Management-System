# Library Management System
# Demonstrates OOP: Encapsulation, Inheritance, Polymorphism

# Book class to represent a book in the library
class Book:
    def __init__(self, book_id, title, author, copies):
        # Initialize book attributes
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies = copies

    def display_info(self):
        # Display book details
        print(f"[Book] ID: {self.book_id}, Title: '{self.title}', Author: {self.author}, Copies Available: {self.copies}")


# Member class to represent a library member
class Member:
    def __init__(self, member_id, name):
        # Initialize member attributes
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []                                                                                                        # List to track borrowed books

    def display_info(self):
        # Display member details
        print(f"[Member] ID: {self.member_id}, Name: {self.name}, Borrowed Books: {self.borrowed_books}")

    def borrow_book(self, book):
        # Borrow a book if copies are available
        if book.copies > 0:
            self.borrowed_books.append(book.book_id)                                                                                    # Add book ID to borrowed list
            book.copies -= 1                                                                                                            # Decrease available copies
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print(f"No copies available for '{book.title}'.")

    def return_book(self, book):
        # Return a borrowed book
        if book.book_id in self.borrowed_books:
            self.borrowed_books.remove(book.book_id)  # Remove book ID from borrowed list
            book.copies += 1  # Increase available copies
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} has not borrowed '{book.title}'.")


# Library class to manage books and members
class Library:
    def __init__(self):
        # Initialize dictionaries to store books and members
        self.books = {}
        self.members = {}

    # Book Management
    def add_book(self, book):
        # Add a book to the library
        self.books[book.book_id] = book
        print(f"Book '{book.title}' added.")

    def remove_book(self, book_id):
        # Remove a book from the library
        if book_id in self.books:
            removed_book = self.books.pop(book_id)                                                                                      # Remove book by ID
            print(f"Book '{removed_book.title}' removed.")
        else:
            print(f"Book ID {book_id} not found.")

    def update_book(self, book_id, title=None, author=None, copies=None):
        # Update book details
        if book_id in self.books:
            book = self.books[book_id]
            if title: book.title = title                                                                                                # Update title if provided
            if author: book.author = author                                                                                             # Update author if provided
            if copies is not None: book.copies = copies                                                                                 # Update copies if provided
            print(f"Book ID {book_id} updated.")
        else:
            print(f"Book ID {book_id} not found.")

    def display_books(self):
        # Display all books in the library
        print("\n--- All Books ---")
        for book in self.books.values():
            book.display_info()

    # Member Management
    def add_member(self, member):
        # Add a member to the library
        self.members[member.member_id] = member
        print(f"Member '{member.name}' added.")

    def remove_member(self, member_id):
        # Remove a member from the library
        if member_id in self.members:
            removed_member = self.members.pop(member_id)                                                                                # Remove member by ID
            print(f"Member '{removed_member.name}' removed.")
        else:
            print(f"Member ID {member_id} not found.")

    def update_member(self, member_id, name=None):
        # Update member details
        if member_id in self.members:
            if name:
                self.members[member_id].name = name                                                                                     # Update name if provided
                print(f"Member ID {member_id} updated.")
        else:
            print(f"Member ID {member_id} not found.")

    def display_members(self):
        # Display all members in the library
        print("\n--- All Members ---")
        for member in self.members.values():
            member.display_info()

    # Book Issuing & Returning
    def issue_book(self, member_id, book_id):
        # Issue a book to a member
        member = self.members.get(member_id)                                                                                            # Get member by ID
        book = self.books.get(book_id)                                                                                                  # Get book by ID

        if member and book:
            member.borrow_book(book)                                                                                                    # Member borrows the book
        else:
            print("Invalid member or book ID.")

    def return_book(self, member_id, book_id):
        # Return a book from a member
        member = self.members.get(member_id)                                                                                            # Get member by ID
        book = self.books.get(book_id)                                                                                                  # Get book by ID

        if member and book:
            member.return_book(book)                                                                                                    # Member returns the book
        else:
            print("Invalid member or book ID.")


# Optional Command-Line Interface
def main():
    library = Library()                                                                                                                 # Create a library instance

    # Sample books and members
    b1 = Book(1, "Engle og Dæmoner", "Dan Brown", 3)
    b2 = Book(2, "Den Afrikanske Farm", "Karen Blixen", 2)
    m1 = Member(101, "Carl Børge")
    m2 = Member(102, "Knud Jensen")

    # Add books and members to the library
    library.add_book(b1)
    library.add_book(b2)
    library.add_member(m1)
    library.add_member(m2)

    # Example usage
    library.display_books()                                                                                                             # Display all books
    library.display_members()                                                                                                           # Display all members

    library.issue_book(101, 1)                                                                                                          # Issue a book to a member
    library.issue_book(101, 2)                                                                                                          # Issue another book
    library.return_book(101, 2)                                                                                                         # Return a book

    library.update_book(1, copies=10)                                                                                                   # Update book details
    library.update_member(102, name="Knud Jensen")                                                                                      # Update member details

    library.display_books()                                                                                                             # Display updated books
    library.display_members()                                                                                                           # Display updated members

    library.remove_book(2)                                                                                                              # Remove a book
    library.remove_member(101)                                                                                                          # Remove a member

    library.display_books()                                                                                                             # Display final list of books
    library.display_members()                                                                                                           # Display final list of members


if __name__ == "__main__":
    main()                                                                                                                              # Run the program