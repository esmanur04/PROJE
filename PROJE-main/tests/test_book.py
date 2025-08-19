import pytest
from book import Book

def test_book_str():
    book = Book("Test Title", "Test Author", "1234567890")
    assert str(book) == "Test Title by Test Author (ISBN: 1234567890)"
