import pandas as pd
import matplotlib.pyplot as plt
import os

# Load data hasil ETL
project_folder = r"D:\APPLY WORK\PORTO\etl_building_store"
file_path = os.path.join(project_folder, 'transformed_sales.csv')
df = pd.read_csv(file_path)

# Buat folder untuk simpan gambar kalau belum ada
output_img_folder = os.path.join(project_folder, 'images')
os.makedirs(output_img_folder, exist_ok=True)

# 1. Total penjualan per kategori
category_sales = df.groupby('category')['total'].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 6))
category_sales.plot(kind='bar', color='skyblue')
plt.title('Total Penjualan per Kategori')
plt.xlabel('Kategori')
plt.ylabel('Total Penjualan (Rp)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(output_img_folder, 'penjualan_per_kategori.png'))
plt.close()

# 2. Penjualan harian
daily_sales = df.groupby('date')['total'].sum()

plt.figure(figsize=(10, 6))
daily_sales.plot(kind='line', marker='o', color='green')
plt.title('Total Penjualan Harian')
plt.xlabel('Tanggal')
plt.ylabel('Total Penjualan (Rp)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(output_img_folder, 'penjualan_harian.png'))
plt.close()

print("Visualisasi berhasil dibuat dan disimpan di folder 'images'!")
