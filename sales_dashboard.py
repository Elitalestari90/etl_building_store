import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import os

# Path relatif ke file CSV
data_path = os.path.join("data", "transformed_sales.csv")
df = pd.read_csv(data_path)


st.title("📈 Dashboard Penjualan Toko Bangunan")

# Sidebar filter
st.sidebar.header("Filter Data")
kategori = st.sidebar.multiselect(
    "Pilih Kategori:",
    options=df['category'].unique(),
    default=df['category'].unique()
)

# Filter berdasarkan kategori
filtered_df = df[df['category'].isin(kategori)]

# Tampilkan data
st.subheader("🧾 Data Penjualan")
st.dataframe(filtered_df)

# Total penjualan per kategori
st.subheader("📊 Total Penjualan per Kategori")
total_per_category = filtered_df.groupby('category')['total'].sum().sort_values(ascending=False)
st.bar_chart(total_per_category)

# Penjualan per tanggal
st.subheader("📆 Penjualan per Tanggal")
filtered_df['date'] = pd.to_datetime(filtered_df['date'], errors='coerce')
sales_per_date = filtered_df.groupby('date')['total'].sum().sort_index()
st.line_chart(sales_per_date)

st.markdown("---")
st.caption("Dashboard oleh Elita • Dibuat dengan Streamlit")
