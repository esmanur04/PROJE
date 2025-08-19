from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_get_books_empty():
    response = client.get("/books")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_add_invalid_book():
    response = client.post("/books", json={"isbn": "0000000000"})  # geçersiz ISBN
    assert response.status_code == 404

def test_add_and_delete_book():
    # 1. Kitap ekle
    response = client.post("/books", json={"isbn": "9780140328721"})  # Charlie and the Chocolate Factory
    assert response.status_code == 200
    book = response.json()
    assert "title" in book
    assert "author" in book
    assert "isbn" in book

    # 2. Kitap listede var mı kontrol et
    response = client.get("/books")
    assert response.status_code == 200
    books = response.json()
    assert any(b["isbn"] == "9780140328721" for b in books)

    # 3. Kitabı sil
    response = client.delete("/books/9780140328721")
    assert response.status_code == 200
    assert response.json()["message"] == "9780140328721 numaralı kitap silindi"