@echo off
REM FastAPI server’ını arka planda başlat
start "" python -m uvicorn api:app --reload

REM Server açılana kadar beklemek için birkaç saniye
timeout /t 5 /nobreak >nul

REM Tarayıcıyı aç /docs sayfasına git
start "" http://127.0.0.1:8000/docs

exit
