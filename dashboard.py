import pandas as pd
import streamlit as st

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="Dashboard E-Commerce", layout="wide")

st.title("📊 Dashboard Analisis E-Commerce")
st.markdown("Analisis performa transaksi, kategori produk, dan segmentasi customer")

# =========================
# LOAD DATA
# =========================
@st.cache_data
def load_data():
    df = pd.read_csv('cleaned_data_sample.csv')
    rfm = pd.read_csv('rfm_data.csv')
    return df, rfm

try:
    df, rfm = load_data()
except:
    st.error("❌ File tidak ditemukan. Pastikan CSV ada di folder yang sama.")
    st.stop()

# =========================
# PREPROCESSING
# =========================
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
df['Month'] = df['order_purchase_timestamp'].dt.to_period('M').astype(str)

# =========================
# SIDEBAR FILTER
# =========================
st.sidebar.header("🔍 Filter Data")

selected_category = st.sidebar.selectbox(
    "Pilih Kategori",
    ["Semua"] + list(df['product_category_name_english'].dropna().unique())
)

if selected_category != "Semua":
    df = df[df['product_category_name_english'] == selected_category]

# =========================
# KPI / METRICS
# =========================
st.subheader("📌 Ringkasan Utama")

col1, col2, col3 = st.columns(3)

total_transaksi = len(df)
total_customer = df['customer_id'].nunique()
total_revenue = df['TotalPrice'].sum()

col1.metric("Total Transaksi", total_transaksi)
col2.metric("Total Customer", total_customer)
col3.metric("Total Revenue", f"{total_revenue:,.0f}")

# =========================
# TREND TRANSAKSI
# =========================
st.subheader("📈 Trend Transaksi Bulanan")

monthly = df.groupby('Month').size()

st.line_chart(monthly)

# =========================
# TOP KATEGORI
# =========================
st.subheader("🏆 Top 10 Kategori Produk")

top_category = df['product_category_name_english'].value_counts().head(10)

st.bar_chart(top_category)

# =========================
# CUSTOMER SEGMENT
# =========================
st.subheader("👥 Segmentasi Customer (RFM)")

segment = rfm['Segment'].value_counts()

st.bar_chart(segment)

# =========================
# INSIGHT OTOMATIS
# =========================
st.subheader("🧠 Insight")

top_cat = top_category.idxmax()
top_value = top_category.max()

top_segment = segment.idxmax()

st.markdown(f"""
- 📦 Kategori paling populer adalah **{top_cat}** dengan {top_value} transaksi  
- 👥 Mayoritas customer berada pada segment **{top_segment}**  
- 💰 Total revenue mencapai **{total_revenue:,.0f}**
""")

# =========================
# DATA PREVIEW
# =========================
st.subheader("📄 Preview Data")

st.dataframe(df.head(10))