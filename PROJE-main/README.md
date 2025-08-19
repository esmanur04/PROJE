# 📚 Python 202 Bootcamp - Kütüphane Yönetim Sistemi

Bu proje, **Global AI Hub Python 202 Bootcamp** kapsamında geliştirilmiş
bir kütüphane yönetim sistemidir.\
Projenin amacı, **OOP**, **harici API kullanımı** ve **FastAPI ile kendi
API'nizi geliştirme** adımlarını birleştirerek, gerçek hayata
uyarlanabilir bir yazılım geliştirmektir.

Proje üç aşamadan oluşmaktadır:\
1. **OOP ile Terminal Uygulaması** -- Konsol üzerinden kitap ekleme,
silme, arama ve listeleme.\
2. **Harici API Entegrasyonu** -- Open Library API kullanarak ISBN
numarasıyla kitap bilgilerini otomatik çekme.\
3. **FastAPI ile Web Servisi** -- Kütüphane işlevlerini RESTful API
olarak dışarıya açma.

------------------------------------------------------------------------

## 🚀 Kurulum

# 1️ Git sürümünü kontrol et
git --version

# 2️ Repo’yu klonla
git clone https://github.com/esmanur04/PROJE.git

# 3️ Klonlanan klasöre gir
cd PROJE

# 4️ Sanal ortam oluştur ve aktif et
# Windows:
-python -m venv venv


-venv\Scripts\activate
# Mac/Linux:
 python -m venv venv
 source venv/bin/activate

# 5️ Gerekli paketleri yükle
# Eğer requirements.txt varsa:
pip install -r requirements.txt
# Yoksa manuel:
pip install fastapi uvicorn httpx

# 6️ Projeyi çalıştır
python -m uvicorn api:app --reload

# Tarayıcıda açmak için: http://127.0.0.1:8000/docs




------------------------------------------------------------------------

## 📂 Proje Yapısı

    .
    ├── __pycache__/          # Python derlenmiş dosyaları (otomatik oluşur, silinebilir)
    │   └── *.pyc
    ├── tests/                # Pytest test dosyaları
    │   ├── test_api.py       # API endpoint testleri
    │   ├── test_book.py      # Book sınıfı testleri
    │   ├── test_library.py   # Library sınıfı testleri
    │   └── test_main.py      # main.py terminal akışı testleri
    ├── api.py                # FastAPI ile REST API oluşturma
    ├── book.py               # Book sınıfı (kitap nesnesi)
    ├── library.json          # Kitapların saklandığı JSON dosyası
    ├── library.py            # Library sınıfı (kütüphane yönetimi)
    ├── main.py               # Terminal uygulaması (CLI arayüzü)
    ├── requirements.txt      # Gerekli kütüphaneler listesi
    └── start_server.bat      # Windows için hızlı API başlatma scripti

------------------------------------------------------------------------

## 📌 Dosya Açıklamaları

### 🔹 `book.py`

-   `Book` sınıfını içerir.\
-   Her kitabın `title`, `author`, `isbn` bilgilerini tutar.\
-   `__str__` metodu ile kitabı okunaklı biçimde döndürür.

### 🔹 `library.py`

-   `Library` sınıfını içerir.\
-   Kitap ekleme, silme, listeleme, arama gibi temel işlevleri sağlar.\
-   Kitap bilgilerini **`library.json`** dosyasında saklar.

### 🔹 `library.json`

-   Kitapların kalıcı olarak saklandığı JSON dosyasıdır.\
-   Uygulama kapatılıp açılsa bile veriler korunur.

### 🔹 `main.py`

-   Konsol tabanlı kullanıcı arayüzünü içerir.\

-   Kullanıcıya şu menüyü sunar:

        1. Kitap Ekle
        2. Kitap Sil
        3. Kitapları Listele
        4. Kitap Ara
        5. Çıkış

### 🔹 `api.py`

-   `FastAPI` tabanlı web servisidir.\
-   Endpoint'ler:
    -   `GET /books` → Tüm kitapları listeler.
    -   `POST /books` → ISBN ile kitap ekler (Open Library API'den veri
        çeker).
    -   `DELETE /books/{isbn}` → ISBN'e göre kitabı siler.

### 🔹 `tests/`

-   Projedeki sınıflar ve API için **pytest** test dosyaları.\
-   Kodun doğru çalışıp çalışmadığını otomatik kontrol eder.

### 🔹 `requirements.txt`

-   Projede kullanılan kütüphaneler listesi.
    -   `fastapi`
    -   `uvicorn`
    -   `httpx`
    -   `pytest`

### 🔹 `start_server.bat`

-   Windows kullanıcıları için tek tıkla FastAPI sunucusunu başlatır.

### 🔹 `__pycache__/`

-   Python tarafından otomatik oluşturulur.\
-   Kodların daha hızlı çalışması için derlenmiş `.pyc` dosyalarını
    içerir.\
-   Silinmesi **kodun çalışmasını bozmaz**, Python tekrar oluşturur.

------------------------------------------------------------------------

## 🛠 Kullanılan Teknolojiler

-   **Python 3.12+**
-   **FastAPI** -- Modern ve hızlı web framework
-   **Uvicorn** -- ASGI server
-   **httpx** -- HTTP istekleri için
-   **Pytest** -- Test otomasyonu
-   **JSON** -- Veri saklama formatı

------------------------------------------------------------------------

## 📖 Örnek Kullanım

### 📌 Terminal

``` bash
python main.py
```

👉 Kullanıcı `ISBN` girerek kitap ekler, listeyi görebilir veya kitap
silebilir.

### 📌 API

``` http
POST /books
Content-Type: application/json
Body: {"isbn": "9780140328721"}
```

Döndürür:

``` json
{
  "title": "Matilda",
  "author": "Roald Dahl",
  "isbn": "9780140328721"
}
```

------------------------------------------------------------------------

## ✅ Testler

Testleri çalıştırmak için:

``` bash
pytest
```

------------------------------------------------------------------------

## 💡 Geliştirme Önerileri

-   SQLite veya PostgreSQL gibi bir veritabanı desteği eklenebilir.\
-   PUT endpoint ile kitap güncelleme özelliği eklenebilir.\
-   Basit bir HTML/CSS/JS arayüzü ile API'ye görsel arayüz yapılabilir.\
-   Docker ile containerize edilebilir.
