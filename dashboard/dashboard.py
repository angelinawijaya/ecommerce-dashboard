import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="E-Commerce Dashboard", layout="wide")

st.header("E-Commerce Data Analysis Dashboard 🛒")

# =========================
# HELPER FUNCTIONS
# =========================

def create_category_sales_df(df):
    category_sales_df = df.groupby("category")["price"].sum().sort_values(ascending=False).reset_index()
    return category_sales_df


def create_rfm_df(df):
    rfm_df = df.groupby(by="customer_id", as_index=False).agg({
        "order_purchase_timestamp": "max",
        "order_id": "nunique",
        "price": "sum"
    })

    rfm_df.columns = ["customer_id", "max_order_timestamp", "frequency", "monetary"]

    rfm_df["max_order_timestamp"] = pd.to_datetime(rfm_df["max_order_timestamp"])
    recent_date = df["order_purchase_timestamp"].max()
    rfm_df["recency"] = rfm_df["max_order_timestamp"].apply(lambda x: (recent_date - x).days)

    rfm_df.drop("max_order_timestamp", axis=1, inplace=True)

    return rfm_df


# =========================
# LOAD DATA
# =========================

all_df = pd.read_csv("main_data.csv")

all_df["order_purchase_timestamp"] = pd.to_datetime(all_df["order_purchase_timestamp"])
all_df.sort_values(by="order_purchase_timestamp", inplace=True)
all_df.reset_index(drop=True, inplace=True)

# =========================
# FILTER SIDEBAR
# =========================

min_date = all_df["order_purchase_timestamp"].min()
max_date = all_df["order_purchase_timestamp"].max()

with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    start_date, end_date = st.date_input(
        label="Rentang Waktu",
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

# Filter dataframe
main_df = all_df[
    (all_df["order_purchase_timestamp"] >= pd.to_datetime(start_date)) &
    (all_df["order_purchase_timestamp"] <= pd.to_datetime(end_date))
]

# =========================
# BUSINESS QUESTION 1
# =========================

st.subheader("📊 Total Sales by Category")

category_sales_df = create_category_sales_df(main_df)

fig1, ax1 = plt.subplots(figsize=(12,6))
sns.barplot(
    x="price",
    y="category",
    data=category_sales_df.head(10),
    ax=ax1
)
ax1.set_title("Top Categories by Total Sales")
ax1.set_xlabel("Total Sales")
ax1.set_ylabel("Category")

st.pyplot(fig1)

st.markdown("""
**Insight:**
Kategori dengan total penjualan tertinggi menunjukkan produk yang paling diminati 
pelanggan dalam rentang waktu yang dipilih.
""")

st.markdown("---")

# =========================
# BUSINESS QUESTION 2
# =========================

st.subheader("📈 Customer Segmentation Based on RFM")

rfm_df = create_rfm_df(main_df)

# RFM Scoring
rfm_df["R_score"] = pd.qcut(rfm_df["recency"], 4, labels=[4,3,2,1])
rfm_df["F_score"] = pd.qcut(rfm_df["frequency"].rank(method="first"), 4, labels=[1,2,3,4])
rfm_df["M_score"] = pd.qcut(rfm_df["monetary"], 4, labels=[1,2,3,4])

rfm_df["RFM_Total"] = (
    rfm_df["R_score"].astype(int) +
    rfm_df["F_score"].astype(int) +
    rfm_df["M_score"].astype(int)
)

def segment(score):
    if score >= 10:
        return "High Value"
    elif score >= 7:
        return "Loyal"
    elif score >= 5:
        return "Potential"
    else:
        return "At Risk"

rfm_df["Segment"] = rfm_df["RFM_Total"].apply(segment)

segment_counts = rfm_df["Segment"].value_counts().reset_index()
segment_counts.columns = ["Segment", "Customer_Count"]

fig2, ax2 = plt.subplots(figsize=(8,5))
sns.barplot(
    x="Segment",
    y="Customer_Count",
    data=segment_counts,
    ax=ax2
)

ax2.set_title("Customer Segmentation (RFM)")
ax2.set_xlabel("Segment")
ax2.set_ylabel("Number of Customers")

st.pyplot(fig2)

st.markdown("""
**Insight:**
Segmentasi RFM membantu mengidentifikasi pelanggan bernilai tinggi, pelanggan loyal, 
serta pelanggan yang berisiko churn dalam periode yang dipilih.
""")

st.caption("Copyright © 2026")