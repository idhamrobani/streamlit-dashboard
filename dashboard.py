import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')
st.title('Belajar Analisis Data')
 

# Data untuk visualisasi pertama
data_season = {'season': ['Spring', 'Summer', 'Fall', 'Winter'],
               'cnt': [100, 150, 120, 80]}
all_data_df_season = pd.DataFrame(data_season)

# Data untuk visualisasi kedua (contoh dummy data, ganti dengan data yang sesuai)
data_hour = {'hr': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
             'casual': [10, 15, 8, 12, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115],
             'registered': [5, 10, 6, 8, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110]}

usage_by_hour = pd.DataFrame(data_hour)

# Visualisasi pertama
st.sidebar.header("Visualisasi 1: Bike Usage by Season")
st.sidebar.text("Ini adalah visualisasi penggunaan sepeda berdasarkan musim.")
st.sidebar.subheader("Data:")
st.sidebar.write(all_data_df_season)

# Tanpa col1, visualisasi akan ditampilkan di area utama


# Visualisasi pertama
fig_season, ax_season = plt.subplots(figsize=(10, 6))
ax_season.bar(all_data_df_season['season'], all_data_df_season['cnt'], color=['springgreen', 'gold', 'orange', 'slateblue'])
ax_season.set_title('Bike Usage by Season')
ax_season.set_xlabel('Season')
ax_season.set_ylabel('Number of Users')
ax_season.set_xticks(all_data_df_season['season'])
ax_season.set_xticklabels(['Spring', 'Summer', 'Fall', 'Winter'])

# Menampilkan visualisasi pertama di Streamlit
st.pyplot(fig_season)

# Teks yang diatur menjadi pusat untuk visualisasi pertama
st.write("<div style='text-align:center'>Ini adalah visualisasi penggunaan sepeda berdasarkan musim.</div>", unsafe_allow_html=True)

# Visualisasi kedua
# Visualisasi kedua
fig_hour, ax_hour = plt.subplots(figsize=(12, 8))
ax_hour.plot(usage_by_hour['hr'], usage_by_hour['casual'], label='Casual Users')
ax_hour.plot(usage_by_hour['hr'], usage_by_hour['registered'], label='Registered Users')
ax_hour.set_title('Visualisasi 2: Jam yang Digunakan oleh Casual dan Registered Users')
ax_hour.set_xlabel('Jumlah Jam dalam Sehari')
ax_hour.set_ylabel('Banyak Pengguna')
ax_hour.legend()
ax_hour.grid(True)

# Menampilkan visualisasi kedua di Streamlit
st.sidebar.header("Visualisasi 2: Jam yang Digunakan oleh Casual dan Registered Users")
st.sidebar.text("Ini adalah visualisasi jam yang digunakan oleh pengguna casual dan terdaftar.")
st.sidebar.subheader("Data:")
st.sidebar.write(usage_by_hour)
st.pyplot(fig_hour)

