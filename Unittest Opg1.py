import unittest
from ObligatoriskOpg1 import Book, Member, Library

class TestLibrarySystem(unittest.TestCase):
    def setUp(self):
        # Setup test data
        self.library = Library()
        self.book1 = Book(1, "Engle og Dæmoner", "Dan Brown", 3)
        self.book2 = Book(2, "Den Afrikanske Farm", "Karen Blixen", 2)
        self.member1 = Member(101, "Carl Børge")
        self.member2 = Member(102, "Knud Jensen")

        # Add books and members to the library
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.library.add_member(self.member1)
        self.library.add_member(self.member2)

    def test_add_book(self):
        # Test adding a book
        book3 = Book(3, "Harry Potter og den vise sten", "J.K. Rowling", 5)
        self.library.add_book(book3)
        self.assertIn(3, self.library.books)
        self.assertEqual(self.library.books[3].title, "Harry Potter og den vise sten")

    def test_remove_book(self):
        # Test removing a book
        self.library.remove_book(1)
        self.assertNotIn(1, self.library.books)

    def test_issue_book(self):
        # Test issuing a book
        self.library.issue_book(101, 1)
        self.assertIn(1, self.member1.borrowed_books)
        self.assertEqual(self.book1.copies, 2)

    def test_return_book(self):
        # Test returning a book
        self.library.issue_book(101, 1)
        self.library.return_book(101, 1)
        self.assertNotIn(1, self.member1.borrowed_books)
        self.assertEqual(self.book1.copies, 3)

    def test_update_book(self):
        # Test updating book details
        self.library.update_book(1, title="Engle og Dæmoner", copies=10)
        self.assertEqual(self.library.books[1].title, "Engle og Dæmoner")
        self.assertEqual(self.library.books[1].copies, 10)

    def test_add_member(self):
        # Test adding a member
        member3 = Member(103, "Melissa Storsk")
        self.library.add_member(member3)
        self.assertIn(103, self.library.members)
        self.assertEqual(self.library.members[103].name, "Melissa Storsk")

    def test_remove_member(self):
        # Test removing a member
        self.library.remove_member(101)
        self.assertNotIn(101, self.library.members)

if __name__ == "__main__":
    unittest.main()