# Backend CYK Parser - Tugas Akhir TBO

Aplikasi backend menggunakan Flask untuk mengecek validitas struktur kalimat Bahasa Indonesia menggunakan **Algoritma CYK (Cocke-Younger-Kasami)**.

## Teknologi yang Digunakan
- **Python**
- **Flask** (Web Framework)
- **Flask-CORS** (Cross-Origin Resource Sharing)
- **Algoritma CYK** (Parser Logic)

## Struktur Folder
- `app/logic/grammar.py`: Kamus kata (Terminal).
- `app/logic/cnf.py`: Aturan tata bahasa (Chomsky Normal Form).
- `app/logic/cyk.py`: Logika utama algoritma CYK.
- `app/routes.py`: API endpoint untuk memproses input.

## Cara Menjalankan
1. **Clone Repository**
   ```bash
   git clone https://github.com/deandamanik/final-project-tbo-backend.git
   cd final-project-tbo-backend
   ```

2. **Aktifkan virtual environment (venv).**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan Server Backend**
   
   Setelah semua terinstall, jalankan aplikasi dengan perintah:
   ```bash
   python run.py
   ```

5. **Pengujian API**
   
   Berdasarkan konfigurasi, server berjalan di: http://127.0.0.1:8000
   Untuk menguji algoritma CYK, kirimkan request POST ke endpoint yang tersedia (misal /parse) dengan format JSON:

   **Contoh Request:**
   - URL: http://127.0.0.1:8000/parse
   - Method: POST
   - Body(JSON):

   ```bash
      JSON
   {
   "sentence": "saya makan nasi"
   }
   ```