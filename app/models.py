import utils
import os
import json

class Library: 
    def __init__(self) :
        self.books = []
        self.load_libary()

    @utils.logger
    def add_book(self, book):
        self.books.append(book)
        print(f'Book {book.name} added!')
        self.save_library()
    
    @utils.logger
    def remove_book(self, book):
        self.books.remove(book)
        print(f'Book {book.name} deleted!')
    
    @utils.logger
    def load_libary(self):
        if os.path.exists("library.json"):
            with open("library.json", "r", encoding="utf-8") as file:
                self.books = json.load(file)

class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f"Book(name='{self.name}')"
    
    def to_dict(self):
        return {"name": self.name}
    
    @classmethod
    def from_dict(cls, data):
        return cls(name=data["name"])