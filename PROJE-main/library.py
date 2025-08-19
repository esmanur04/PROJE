import json
import os
import httpx
from book import Book

class Library:
    def __init__(self, filename="library.json"):
        self.filename = filename
        self.books = []
        self.load_books()

    def add_book(self, isbn: str):
        """ISBN ile Open Library API'den kitap bilgisi çekerek ekleme yapar."""
        url = f"https://openlibrary.org/isbn/{isbn}.json"
        try:
            response = httpx.get(url, timeout=10.0, follow_redirects=True)
            if response.status_code == 404:
                print("❌ Kitap bulunamadı.")
                return None
            response.raise_for_status()

            data = response.json()
            title = data.get("title", "Bilinmeyen Başlık")

            # Yazar bilgisi çek
            author = "Bilinmeyen Yazar"
            if "authors" in data and data["authors"]:
                author_key = data["authors"][0]["key"]
                author_url = f"https://openlibrary.org{author_key}.json"
                try:
                    author_resp = httpx.get(author_url, timeout=10.0, follow_redirects=True)
                    if author_resp.status_code == 200:
                        author = author_resp.json().get("name", "Bilinmeyen Yazar")
                except Exception:
                    pass

            # Kitap nesnesi oluştur ve kaydet
            new_book = Book(title, author, isbn)
            self.books.append(new_book)
            self.save_books()
            print(f"✅ Kitap eklendi: {new_book}")
            return new_book

        except httpx.RequestError as e:
            print(f"🌐 Ağ bağlantı hatası: {e}")
            return None
        except Exception as e:
            print(f"⚠️ Beklenmeyen hata: {e}")
            return None

    def remove_book(self, isbn: str) -> bool:
        """ISBN ile kitabı siler."""
        before_count = len(self.books)
        self.books = [book for book in self.books if book.isbn != isbn]
        self.save_books()
        return len(self.books) < before_count

    def find_book(self, isbn: str):
        """ISBN ile kitabı bulur."""
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def list_books(self):
        """Kütüphanedeki tüm kitapları yazdırır."""
        if not self.books:
            print("📂 Kütüphane boş.")
        else:
            print("\n📖 Kütüphanedeki Kitaplar:")
            for book in self.books:
                print(f"- {book.title} by {book.author} (ISBN: {book.isbn})")

    def load_books(self):
        """JSON dosyasından kitapları yükler."""
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                    self.books = [Book(**item) for item in data]
                except json.JSONDecodeError:
                    self.books = []

    def save_books(self):
        """Kitap listesini JSON dosyasına kaydeder."""
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump([book.__dict__ for book in self.books], f, ensure_ascii=False, indent=4)