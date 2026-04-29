# Proyek Analisis Data: E-Commerce Public Dataset 🛍️

## Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis data publik dari sebuah platform e-commerce guna mendapatkan wawasan (insight) mendalam mengenai perilaku pelanggan dan efisiensi operasional. Analisis difokuskan pada dua aspek utama: **retensi pelanggan di kota-kota besar** dan **dampak performa logistik terhadap kepuasan pelanggan** pada kategori produk tertentu.

## Pertanyaan Bisnis (SMART Framework)
1. **Pertanyaan 1 (Retensi):** Bagaimana perbandingan jumlah pelanggan yang melakukan pembelian ulang (repeat order) dibandingkan dengan pembeli baru di 5 kota besar dalam periode terakhir?
2. **Pertanyaan 2 (Logistik):** Sejauh mana keterlambatan pengiriman memengaruhi skor ulasan pelanggan, khususnya pada kategori produk 'Health & Beauty'?

## Struktur Dataset
Dataset yang digunakan mencakup informasi mengenai:
- `customers`: Lokasi dan identitas unik pelanggan.
- `orders`: Status pesanan dan stempel waktu (timestamps) proses pengiriman.
- `order_items`: Detail produk, harga, dan biaya logistik.
- `order_reviews`: Skor ulasan dan komentar dari pelanggan.
- `products`: Informasi kategori produk (dalam bahasa Portugis dan Inggris).

## Tahapan Proyek
1. **Data Wrangling**:
   - **Gathering Data**: Memuat seluruh file CSV.
   - **Assessing Data**: Mengidentifikasi *missing values*, duplikasi, dan kesalahan tipe data.
   - **Cleaning Data**: Menangani data kosong, memperbaiki tipe data datetime, dan melakukan *filtering* pada pesanan yang sukses.
2. **Exploratory Data Analysis (EDA)**: Mengeksplorasi hubungan antar variabel untuk menjawab pertanyaan bisnis.
3. **Visualization & Explanatory Analysis**: Membuat grafik batang, scatter plot, dan heatmap untuk memvisualisasikan temuan.
4. **Analisis Lanjutan**: Melakukan analisis distribusi untuk melihat korelasi antara variabel logistik dan kepuasan.

## Library yang Digunakan
- Pandas
- Numpy
- Matplotlib
- Seaborn

## Temuan Utama (Insights)
- **Rendahnya Loyalitas:** Mayoritas pelanggan di kota-kota besar merupakan pembeli satu kali (*single order*). Hal ini menunjukkan potensi besar untuk program loyalitas.
- **Sensitivitas Waktu:** Pada kategori *Health & Beauty*, keterlambatan pengiriman lebih dari 3 hari dari estimasi menyebabkan penurunan drastis pada rata-rata skor ulasan (di bawah 3.0).

## Cara Menjalankan Proyek
1. Pastikan Python sudah terinstal di sistem Anda.
2. Instal library yang dibutuhkan:
   ```bash
   pip install pandas numpy matplotlib seaborn
3. Buka file Jupyter Notebook (notebook.ipynb) atau jalankan skrip Python.
4. Pastikan semua file dataset (.csv) berada dalam direktori yang sama dengan kode.

Rekomendasi Action Item
Marketing: Implementasi program next-purchase discount untuk pelanggan di kota besar.

Operasional: Menambah buffer time pada estimasi pengiriman untuk mengelola ekspektasi pelanggan.

Logistik: Prioritas pengiriman (SLA ketat) untuk kategori produk dengan sensitivitas tinggi.
