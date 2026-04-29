# 🛒 E-Commerce Analytics Dashboard

Proyek Analisis Data Akhir — Fundamental Analisis Data (Dicoding)

**Nama:** Dhinda Oktavia Ramadhansi  
**Email:** cdcc308d6x0974@student.devacademy.id  
**ID Dicoding:** CDCC308D6X0974  
**Dataset:** Brazilian E-Commerce Public Dataset by Olist (2016–2018)

---

## 📋 Pertanyaan Bisnis

1. **Bagaimana tren jumlah pesanan dan total pendapatan per bulan selama tahun 2017–2018**, dan bulan mana yang mencatatkan performa pesanan tertinggi serta terendah?
2. **Kategori produk apa yang menghasilkan total pendapatan tertinggi namun memiliki rata-rata skor ulasan pelanggan paling rendah (< 4,0)** selama periode 2016–2018, sehingga menjadi prioritas perbaikan kualitas layanan?

---

## 📁 Struktur Proyek

```
submission/
├── dashboard/
│   ├── main_data.csv          # Data utama gabungan untuk dashboard
│   ├── category_data.csv      # Data agregasi per kategori produk
│   └── dashboard.py           # Aplikasi Streamlit
├── data/
│   ├── orders_dataset.csv
│   ├── order_items_dataset.csv
│   ├── order_payments_dataset.csv
│   ├── order_reviews_dataset.csv
│   ├── customers_dataset.csv
│   ├── products_dataset.csv
│   ├── sellers_dataset.csv
│   └── product_category_name_translation.csv
├── notebook.ipynb             # Notebook analisis lengkap (sudah dijalankan)
├── requirements.txt           # Daftar library yang digunakan
└── README.md                  # Dokumentasi ini
```

---

## 🚀 Cara Menjalankan Dashboard

### 1. Clone / Ekstrak Submission

```bash
unzip submission.zip
cd submission
```

### 2. Buat Virtual Environment (Disarankan)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Jalankan Dashboard Streamlit

```bash
streamlit run dashboard/dashboard.py
```

Dashboard akan otomatis terbuka di browser pada alamat:  
**`http://localhost:8501`**

> **Catatan:** Jalankan perintah dari dalam folder `submission/` agar path ke `dashboard/main_data.csv` dan `dashboard/category_data.csv` terdeteksi dengan benar.

---

## 📊 Fitur Dashboard

| Halaman | Konten |
|---------|--------|
| 🏠 **Overview** | KPI utama, distribusi status order, top 5 kategori revenue |
| 📈 **Tren Penjualan** | Grafik tren bulanan pesanan & pendapatan 2017–2018 |
| 🏷️ **Kategori Produk** | Revenue vs. review score per kategori, zona prioritas perbaikan |
| 💳 **Metode Pembayaran** | Distribusi revenue & order per negara bagian pelanggan |

Dashboard juga dilengkapi dengan:
- **Filter tahun** (2016, 2017, 2018)
- **Filter negara bagian pelanggan**
- **Anotasi insight** di setiap visualisasi
- **Tombol download** data CSV

---

## 📦 Library yang Digunakan

| Library | Versi | Kegunaan |
|---------|-------|----------|
| pandas | 2.2.2 | Manipulasi dan analisis data |
| numpy | 1.26.4 | Komputasi numerik |
| matplotlib | 3.9.0 | Visualisasi data statis |
| seaborn | 0.13.2 | Visualisasi statistik |
| streamlit | 1.35.0 | Pembuatan dashboard interaktif |

---

## 💡 Kesimpulan Utama

1. **November 2017** adalah bulan dengan pesanan tertinggi, menunjukkan dampak signifikan dari kampanye harbolnas/Black Friday. Pertumbuhan revenue digerakkan oleh **volume transaksi**, bukan kenaikan harga.

2. Kategori **bed_bath_table** dan **computers_accessories** memiliki review score di bawah 4.0 meski menghasilkan revenue besar — menjadi prioritas perbaikan kualitas layanan.

---

*Proyek ini dibuat untuk memenuhi syarat submission Proyek Akhir Kelas Fundamental Analisis Data — Dicoding Indonesia.*
