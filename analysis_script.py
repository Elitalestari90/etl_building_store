import pandas as pd
import os
import matplotlib.pyplot as plt

# Path ke file hasil ETL
project_folder = r"D:\APPLY WORK\PORTO\etl_building_store"
data_path = os.path.join(project_folder, 'transformed_sales.csv')

# Load data
df = pd.read_csv(data_path)

# Total penjualan per kategori
total_per_category = df.groupby('category')['total'].sum().sort_values(ascending=False)
print("\n📊 Total penjualan per kategori:")
print(total_per_category)

# Penjualan per tanggal
sales_per_date = df.groupby('date')['total'].sum()

# Visualisasi total penjualan per kategori
plt.figure(figsize=(8, 5))
total_per_category.plot(kind='bar', color='skyblue', title='Total Penjualan per Kategori')
plt.xlabel('Kategori')
plt.ylabel('Total Penjualan')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Visualisasi penjualan per tanggal
plt.figure(figsize=(10, 5))
sales_per_date.plot(kind='line', marker='o', color='salmon', title='Penjualan per Tanggal')
plt.xlabel('Tanggal')
plt.ylabel('Total Penjualan')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
