import pandas as pd
import os

# Path folder proyek
project_folder = r"D:\APPLY WORK\PORTO\etl_building_store"  # Sesuaikan dengan path folder kamu

# Step 1: Extract
# Membaca data dari file CSV
data_path = os.path.join(project_folder, 'data', 'sales_data.csv')
df = pd.read_csv(data_path)  # Membaca data ke dalam DataFrame df

# Step 2: Transform
# Menghitung kolom 'total' jika kosong (quantity * price)
df['total'] = df['quantity'] * df['price']

# Mengubah kategori menjadi huruf kecil semua
df['category'] = df['category'].str.lower()

# Menghapus data yang masih kosong (missing data)
df.dropna(inplace=True)

# Step 3: Load
# Menyimpan data yang sudah diproses ke file baru
output_path = os.path.join(project_folder, 'transformed_sales.csv')
df.to_csv(output_path, index=False)

print("ETL selesai! Data telah disimpan ke", output_path)

