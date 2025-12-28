# Backend CYK Parser - Tugas Akhir TBO

Aplikasi backend menggunakan Flask untuk mengecek validitas struktur kalimat Bahasa Indonesia menggunakan **Algoritma CYK (Cocke-Younger-Kasami)**.

## Struktur Folder
- `app/logic/grammar.py`: Kamus kata (Terminal).
- `app/logic/cnf.py`: Aturan tata bahasa (Chomsky Normal Form).
- `app/logic/cyk.py`: Logika utama algoritma CYK.
- `app/routes.py`: API endpoint untuk memproses input.

## Cara Menjalankan
1. Pastikan Python sudah terinstal.
2. Aktifkan virtual environment (venv).
3. Install dependencies:
   ```bash
   pip install -r requirements.txt