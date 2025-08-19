import pytest
from library import Library

def test_add_book_valid_isbn(tmp_path):
    test_file = tmp_path / "test_library.json"
    library = Library(filename=test_file)

    # Geçerli ISBN (Matilda - Roald Dahl)
    library.add_book("9780140328721")

    assert len(library.books) > 0
    assert library.books[0].title is not None
    assert library.books[0].author is not None

def test_add_book_invalid_isbn(tmp_path):
    test_file = tmp_path / "test_library.json"
    library = Library(filename=test_file)

    # Geçersiz ISBN
    library.add_book("0000000000000")

    # Kitap eklenmemiş olmalı
    assert len(library.books) == 0