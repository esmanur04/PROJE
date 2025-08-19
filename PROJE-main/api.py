from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from library import Library

app = FastAPI()
library = Library("library.json")

# Pydantic model: sadece ISBN alacak
class ISBNRequest(BaseModel):
    isbn: str

# Pydantic model: JSON dönerken Book formatı
class BookResponse(BaseModel):
    title: str
    author: str
    isbn: str

@app.get("/books", response_model=list[BookResponse])
def get_books():
    """Kütüphanedeki tüm kitapları döner."""
    return [vars(book) for book in library.books]

@app.post("/books", response_model=BookResponse)
def add_book(req: ISBNRequest):
    """ISBN ile kitap ekler."""
    book = library.add_book(req.isbn)
    if not book:
        raise HTTPException(status_code=404, detail="Kitap bulunamadı veya eklenemedi")
    return vars(book)

@app.delete("/books/{isbn}")
def delete_book(isbn: str):
    """ISBN ile kitabı siler."""
    book = library.find_book(isbn)
    if not book:
        raise HTTPException(status_code=404, detail="Kitap bulunamadı")
    library.remove_book(isbn)
    return {"message": f"{isbn} numaralı kitap silindi"}