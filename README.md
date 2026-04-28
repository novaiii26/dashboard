# E-Commerce Data Analysis Dashboard

Dashboard ini dibuat menggunakan Streamlit untuk memvisualisasikan performa transaksi e-commerce, tren bulanan, dan analisis kategori produk berdasarkan dataset yang telah dibersihkan

## Fitur Utama
- KPI Metrics : Menampilkan total transaksi, jumlah customer unik, dan total pendapatan
- Trend Analysis : Grafik garis untuk melihat pergerakan transaksi bulanan
- Category Analysis : Grafik batang untuk 10 kategori produk pada sidebar
- Data Preview : Menampilkan cuplikan data yang digunakan

## Struktur File
- Dashboard.py : File utama aplikasi Streamlit
- main_data.csv : Dataset hasil pembersihan (cleaned data)
- README.md : Dokumentasi proyek ini 

## Cara Menjalankan di Lokal

### 1. Clone Repositori
Pertama, salin repositori ini ke kompotuer anda: ```bash
git clone [https://github.com/novaiii26/dashboard.git](https://github.com/novaiii26/dashboard.git)
cd dashboard

### 2. Buat Virtual Environment
python -m venv venv
# Untuk Windows:
venv\Scripts\activate
# Untuk Mac/Linux:
source venv/bin/activate

### 3. Install Library yang Dibutuhkan
Install semua depedensi menggunakan pip:
pip install -r requirements.txt

### 4. Jalankan Aplikasi
streamlit run dashboard.py

# Cara Deploy ke Streamlit Cloud
- Pastikan semua file (dashboard.py, main_data.csv, requirements.txt) sudah di-push ke GitHub.
- Masuk ke Streamlit Cloud.
- Hubungkan akun GitHub Anda.
- Pilih repositori dashboard dan branch main.
- Masukkan Main file path: dashboard.py.
- Klik Deploy.

# Library yang Digunakan
- Pandas : Untuk manipulasi dan analisis data
- Streamlit : Untuk membuat interface dashboard web
- Matplotlib/Seaborn : Untuk visualisasi tambahan