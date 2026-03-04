# 🛒 E-Commerce Data Analysis Dashboard

## 📌 Project Overview
Project ini merupakan analisis data e-commerce untuk memahami:
- Kategori produk dengan penjualan tertinggi
- Segmentasi pelanggan menggunakan metode RFM (Recency, Frequency, Monetary)

Dashboard interaktif dibuat menggunakan Streamlit untuk memvisualisasikan insight bisnis.

---

## 📊 Business Questions

1. Kategori produk apa yang memiliki penjualan tertinggi?
2. Bagaimana segmentasi pelanggan berdasarkan RFM Analysis?

---

## 📈 Key Insights

- Kategori **bed_bath_table** merupakan kategori dengan total penjualan tertinggi.
- Mayoritas pelanggan memiliki frequency rendah (1 transaksi).
- Segmentasi RFM membantu mengidentifikasi pelanggan bernilai tinggi dan pelanggan berisiko churn.

---

## 📁 Project Structure
submission/
│
├── dashboard/
│ ├── dashboard.py
│ ├── main_data.csv
│
├── notebook.ipynb
├── requirements.txt
├── README.md


---

## ⚙️ Setup Virtual Environment

### 1️⃣ Create Virtual Environment

```bash
python -m venv venv
2️⃣ Activate Virtual Environment

Windows: venv\Scripts\activate

📦 Install Dependencies

Disarankan untuk menginstall library melalui file requirements.txt:

pip install -r requirements.txt
▶️ Run Dashboard Locally

Masuk ke folder dashboard:

cd dashboard

Jalankan Streamlit:

streamlit run dashboard.py

Dashboard akan terbuka di browser pada:

http://localhost:8501
🌐 Online Deployment (Optional)

Dashboard juga dapat diakses melalui Streamlit Cloud:
https://ecommerce-dashboard-9mqdw4tfjrzqyisby9awmf.streamlit.app/

🛠️ Tools & Technologies

Python

Pandas

Matplotlib

Streamlit

👩‍💻 Author

Angelina Wijaya
E-Commerce Data Analysis Project
