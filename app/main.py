from models import Library, Book

lib = Library()
book = Book("Old Man and the Sea")

lib.add_book(book)
print(lib.books)

lib.remove_book(book)
print(lib.books)