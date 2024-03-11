import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

# Sidebar
st.sidebar.title('Pengaturan Visualisasi')
selected_visualization = st.sidebar.radio('Pilih Visualisasi', ['Penggunaan Sepeda per Jam', 'Penggunaan Sepeda per Musim'])

# Visualisasi Penggunaan Sepeda berdasarkan Jam
url = "https://raw.githubusercontent.com/idhamrobani/dataset-bike-sharing/main/Bike-sharing-dataset/hour.csv"
hour_df = pd.read_csv(url)

selected_columns = ['dteday', 'hr', 'casual', 'registered']
selected_df = hour_df[selected_columns]

grouped_df = selected_df.groupby('hr')

usage_by_hour = grouped_df[['casual', 'registered']].sum().reset_index()

# Visualisasi Penggunaan Sepeda berdasarkan Musim
url = "https://raw.githubusercontent.com/idhamrobani/dataset-bike-sharing/main/Bike-sharing-dataset/hour.csv"
hour_df = pd.read_csv(url)

# Pilih kolom yang dibutuhkan
selected_columns = ['season', 'cnt']

# Buat dataframe baru dengan kolom yang dipilih
selected_df = hour_df[selected_columns]

# Kelompokkan berdasarkan musim
grouped_df = selected_df.groupby('season')

# Hitung total penggunaan sepeda pada setiap musim
usage_by_season = grouped_df['cnt'].sum().reset_index()

# Streamlit App
st.title('Visualisasi Pola Penggunaan Sepeda')

# Tampilkan kedua grafik dalam satu subplot
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 16))

# Grafik Penggunaan Sepeda berdasarkan Jam
ax1.plot(usage_by_hour['hr'], usage_by_hour['casual'], label='Casual Users')
ax1.plot(usage_by_hour['hr'], usage_by_hour['registered'], label='Registered Users')
ax1.set_title('Pola Penggunaan Sepeda per Jam - Casual vs Registered Users')
ax1.set_xlabel('Jumlah Jam dalam Sehari')
ax1.set_ylabel('Banyak User')
ax1.legend()
ax1.grid(True)

# Grafik Penggunaan Sepeda berdasarkan Musim
ax2.bar(usage_by_season['season'], usage_by_season['cnt'], color=['springgreen', 'gold', 'orange', 'slateblue'])
ax2.set_title('Penggunaan Sepeda berdasarkan Musim')
ax2.set_xlabel('Season')
ax2.set_ylabel('Number of Users')
ax2.set_xticks(usage_by_season['season'])
ax2.set_xticklabels(['Spring', 'Summer', 'Fall', 'Winter'])

# Tampilkan grafik di Streamlit
st.pyplot(fig)
