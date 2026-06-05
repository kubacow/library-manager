import sys
from models import Library, Book
from utils import LibraryDatabaseError
import time

def display_menu():
    time.sleep(2)
    print("\n" + "="*40)
    print("---- MINI LIBRARY MANAGEMENT SYSTEM ----")
    print("="*40)
    print("1. Display All Books")
    print("2. Display Available Books")
    print("3. Add a New Book")
    print("4. Remove a Book from Database")
    print("5. Borrow a Book")
    print("6. Return a Book")
    print("7. Borrowed Books")
    print("8. Exit")
    print("="*40)

def main():
    try:
        library = Library("library.json")
        print("Library database loaded successfully!")
    except LibraryDatabaseError as e:
        print(f"Error {e}")
        sys.exit(1)

    while True:
        display_menu()
        choice = input("Select an option (1-8): ").strip()

        if choice == "1":
            print("\n--- ALL BOOKS ---")
            sorted_books = library.get_sorted_books()
            if not sorted_books:
                print("The library is empty :(")
                continue

            for book in sorted_books:
                status = f"Borrowed by {book.borrower_name}" if book.is_borrowed else "Available"
                print(f"[{book.isbn}] '{book.title}' by {book.author} ({status})")

        elif choice == "2":
            print("\n--- AVAILABLE BOOKS ---")
            available_books = library.get_available_books()
            if not available_books:
                print("No books are currently available for borrowing.")
                continue

            for book in available_books:
                print(f"[{book.isbn}] '{book.title}' by {book.author}")

        elif choice == "3":
            print("\n--- ADD A NEW BOOK ---")
            isbn = input("Enter ISBN number (Format: XXX-XX-XXX-XXXX-X): ").strip()
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()

            try:
                new_book = Book(isbn=isbn, title=title, author=author, is_borrowed=False, borrower_name=None)
                library.add_book(new_book)
            except LibraryDatabaseError as e:
                print(f"\nError {e}")

        elif choice == "4":
            print("\n--- REMOVE A BOOK ---")
            isbn_to_remove = input("Enter the ISBN of the book to remove: ").strip()

            try:
                library.remove_book(isbn_to_remove)
            except LibraryDatabaseError as e:
                print(f"\nError {e}")

        elif choice == "5":
            print("\n--- BORROW A BOOK ---")
            isbn = input("Enter book ISBN: ").strip()
            borrower = input("Enter borrower name: ").strip()
            
            try:
                library.borrow_book(isbn, borrower)
            except LibraryDatabaseError as e:
                print(f"\nError {e}")

        elif choice == "6":
            print("\n--- RETURN A BOOK ---")
            isbn = input("Enter book ISBN: ").strip()
            
            try:
                library.return_book(isbn)
            except LibraryDatabaseError as e:
                print(f"\nError {e}")

        elif choice == "7":
            print("\n--- BORROWED BOOKS ---")
            borrowed_gen = library.borrowed_books()
            
            has_records = False
            for book in borrowed_gen:
                has_records = True
                print(f"[{book.isbn}] '{book.title}' has been borrowed by: {book.borrower_name}")
            
            if not has_records:
                print("No books are currently borrowed.")

        elif choice == "8":
            print("\nGoodbye!")
            break

        else:
            print("\nPlease input a valid number.")

if __name__ == "__main__":
    main()