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
# CUSTOM CSS (PORTFOLIO STYLE)
# =========================
st.markdown("""
<style>
.main {
    background-color: #f4f6f9;
}
h1 {
    color: #1f4e79;
}
.metric-box {
    background-color: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.05);
}
</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================
st.sidebar.title("🧭 Navigation")
page = st.sidebar.radio("Go to:", ["Dashboard Overview", "Category Analysis"])

st.sidebar.markdown("---")
st.sidebar.write("👩‍💻 Created by: **Angelina Wijaya**")
st.sidebar.write("📊 Project: E-Commerce Data Analysis")

# =========================
# LOAD DATA
# =========================
df = pd.read_csv("dashboard/main_data.csv")

# =========================
# PAGE 1: OVERVIEW
# =========================
if page == "Dashboard Overview":

    st.title("🛒 E-Commerce Analytics Dashboard")
    st.markdown("### Business Performance Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Categories", len(df))
    col2.metric("Total Sales", f"{df['total_sales'].sum():,}")
    col3.metric("Top Category", df.loc[df['total_sales'].idxmax(), 'category'])

    st.markdown("---")

    st.subheader("Top 10 Categories by Sales")

    df_sorted = df.sort_values(by="total_sales", ascending=True)

    fig, ax = plt.subplots(figsize=(8,6))
    ax.barh(df_sorted["category"], df_sorted["total_sales"])
    ax.set_xlabel("Total Sales")
    ax.set_ylabel("Category")

    st.pyplot(fig)

    st.markdown("### 📌 Business Insight")
    st.write("""
    Kategori dengan total penjualan tertinggi menunjukkan preferensi utama pelanggan 
    terhadap produk tertentu. Strategi bisnis dapat difokuskan pada kategori unggulan 
    untuk meningkatkan revenue dan mempertahankan market share.
    """)

# =========================
# PAGE 2: CATEGORY DETAIL
# =========================
elif page == "Category Analysis":

    st.title("📦 Category Analysis")

    selected_category = st.selectbox(
        "Select Product Category",
        df["category"]
    )

    filtered = df[df["category"] == selected_category]

    col1, col2 = st.columns(2)

    col1.metric("Selected Category", selected_category)
    col2.metric("Total Sales", f"{int(filtered['total_sales'].values[0]):,}")

    st.markdown("---")

    fig2, ax2 = plt.subplots(figsize=(6,4))
    ax2.bar(filtered["category"], filtered["total_sales"])
    ax2.set_ylabel("Total Sales")

    st.pyplot(fig2)

    st.markdown("### 📌 Insight")
    st.write(f"""
    Kategori **{selected_category}** merupakan salah satu kontributor penjualan 
    dalam platform e-commerce. Optimalisasi promosi dan pengelolaan stok pada 
    kategori ini dapat meningkatkan performa bisnis secara keseluruhan.

    """)
