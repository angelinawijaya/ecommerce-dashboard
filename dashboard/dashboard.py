import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="E-Commerce Analytics Dashboard",
    page_icon="🛒",
    layout="wide"
)

# =========================
# LOAD DATA
# =========================
main_df = pd.read_csv("dashboard/main_data.csv")
rfm_df = pd.read_csv("dashboard/rfm_data.csv")

main_df['order_purchase_timestamp'] = pd.to_datetime(main_df['order_purchase_timestamp'])

# =========================
# SIDEBAR FILTER (INTERACTIVE FEATURE)
# =========================
st.sidebar.title("📅 Filter Periode")

min_date = main_df['order_purchase_timestamp'].min()
max_date = main_df['order_purchase_timestamp'].max()

start_date = st.sidebar.date_input("Start Date", min_date)
end_date = st.sidebar.date_input("End Date", max_date)

filtered_df = main_df[
    (main_df['order_purchase_timestamp'] >= pd.to_datetime(start_date)) &
    (main_df['order_purchase_timestamp'] <= pd.to_datetime(end_date))
]

st.sidebar.markdown("---")
st.sidebar.write("👩‍💻 Created by: Angelina Wijaya")

# =========================
# PAGE TITLE
# =========================
st.title("🛒 E-Commerce Data Analysis Dashboard")
st.markdown("### September 2016 – October 2018")

# ==========================================================
# 📌 PERTANYAAN 1
# ==========================================================
st.header("1️⃣ Kategori Produk dengan Jumlah Penjualan Tertinggi")

category_sales = (
    filtered_df
    .groupby('category')['price']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"{int(filtered_df['price'].sum()):,}")
col2.metric("Total Transactions", filtered_df['order_id'].nunique())
col3.metric("Top Category", category_sales.index[0] if len(category_sales)>0 else "-")

fig, ax = plt.subplots()
category_sales.sort_values().plot(kind='barh', ax=ax)
ax.set_xlabel("Total Sales")
ax.set_ylabel("Category")
st.pyplot(fig)

st.markdown("**Insight:** Kategori dengan total revenue tertinggi menunjukkan preferensi utama pelanggan dalam periode terpilih.")

# ==========================================================
# 📌 PERTANYAAN 2
# ==========================================================
st.header("2️⃣ Segmentasi Pelanggan Berdasarkan RFM Analysis")

segment_count = rfm_df['Segment'].value_counts()

col1, col2 = st.columns(2)

col1.metric("Total Customers", rfm_df.shape[0])
col2.metric("Dominant Segment", segment_count.index[0])

fig2, ax2 = plt.subplots()
segment_count.plot(kind='bar', ax=ax2)
ax2.set_xlabel("Segment")
ax2.set_ylabel("Number of Customers")
st.pyplot(fig2)

st.markdown("""
**Karakteristik Segmen:**

- **Loyal Customer** → Frequency & Monetary tinggi, Recency rendah  
- **New Customer** → Recency rendah tetapi transaksi masih sedikit  
- **At Risk** → Sudah lama tidak bertransaksi  
- **Potential Customer** → Perlu strategi retargeting  
""")