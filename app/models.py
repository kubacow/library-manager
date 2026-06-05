from utils import LibraryDatabaseError, validate_isbn, logger
import os
import json

class Book:
    def __init__(self, isbn, title, author, is_borrowed, borrower_name):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
        self.borrower_name = borrower_name
    
    def to_dict(self):
        return {
            "isbn": self.isbn,
            "title": self.title,
            "author": self.author,
            "is_borrowed": self.is_borrowed,
            "borrower_name": self.borrower_name
        }
    
class Library: 
    def __init__(self, filename="library.json") :
        self.filename = filename
        self.books = {}
        self.load_data()

# ===== OPERATION FUNCTIONS =====

    @logger
    def get_sorted_books(self):
        return sorted(self.books.values(), key=lambda book: book.title)
    
    @logger
    def get_available_books(self):
        return [book for book in self.books.values() if not book.is_borrowed]
    
    @logger
    def add_book(self, book):
        if not validate_isbn(book.isbn):
            raise LibraryDatabaseError("Wrong ISBN format!")
        
        if book.isbn in self.books:
            raise LibraryDatabaseError("Book already exists in database!")
        
        self.books[book.isbn] = book
        print(f'Book {book.title} added!')
        self.save_data()
    
    @logger
    def remove_book(self, isbn):
        if isbn not in self.books:
            raise LibraryDatabaseError("Book does not exist in database!")
        
        deleted_title = self.books[isbn].title
        
        del self.books[isbn]
        print(f'Book {deleted_title} deleted!')
        self.save_data()

    @logger
    def borrow_book(self, isbn, borrower_name) :
        if isbn not in self.books:
            raise LibraryDatabaseError("Book does not exist in database!")
        if self.books[isbn].is_borrowed:
            raise LibraryDatabaseError("Book already borrowed!")
        
        self.books[isbn].is_borrowed = True
        self.books[isbn].borrower_name = borrower_name
        print(f'Book {self.books[isbn].title} borrowed by {borrower_name}.')
        self.save_data()

    @logger
    def return_book(self, isbn) :
        if isbn not in self.books:
            raise LibraryDatabaseError("Book does not exist in database!")
        if not self.books[isbn].is_borrowed:
            raise LibraryDatabaseError("Book is not borrowed!") 
        
        self.books[isbn].is_borrowed = False
        self.books[isbn].borrower_name = None
        print(f'Book {self.books[isbn].title} returned!')
        self.save_data()

    @logger
    def borrowed_books(self):
        for book in self.books.values():
            if book.is_borrowed:
                yield book

# ===== DATABASE FUNCTIONS =====

    def load_data(self):
        if not os.path.exists(self.filename):
            self.books = {}
            return
        
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                raw_data = json.load(file)

                self.books = {}
                for item in raw_data:
                    book_obj = Book(
                        isbn=item["isbn"],
                        title=item["title"],
                        author=item["author"],
                        is_borrowed=item["is_borrowed"],
                        borrower_name=item.get("borrower_name")
                    )
                    self.books[book_obj.isbn] = book_obj
        except (json.JSONDecodeError, KeyError) as e:
            raise LibraryDatabaseError(f'Failed to parse databse file: {e}')
    
    def save_data(self):
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                data_to_save = [book.to_dict() for book in self.books.values()]
                json.dump(data_to_save, file, indent=2, ensure_ascii=False)
        except Exception as e:
            raise LibraryDatabaseError(f'Failed to save data: {e}')
