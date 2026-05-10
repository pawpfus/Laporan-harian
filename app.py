import streamlit as st
import pandas as pd
import json
import os
from datetime import date

FILE_DATA = "laporan.json"

# buat file json jika belum ada
if not os.path.exists(FILE_DATA):
    with open(FILE_DATA, "w") as f:
        json.dump([], f)

# baca data
def baca_data():
    with open(FILE_DATA, "r") as f:
        return json.load(f)

# simpan data
def simpan_data(data):
    with open(FILE_DATA, "w") as f:
        json.dump(data, f, indent=4)

# halaman
st.set_page_config(
    page_title="Pelaporan Pertanian",
    page_icon="🌾",
    layout="centered"
)

st.title("🌾 Pelaporan Pertanian")

st.write("Input laporan harian")

# form input
tanggal = st.date_input("Tanggal", date.today())

desa = st.text_input("Desa")

kelompok_tani = st.text_input("Kelompok Tani")

kegiatan = st.selectbox(
    "Kegiatan",
    [
        "Bera",
        "Olah Lahan",
        "Tanam",
        "Panen"
    ]
)

komoditas = st.selectbox(
    "Komoditas",
    [
        "Padi",
        "Jagung",
        "Kedelai"
    ]
)

luas = st.number_input(
    "Luas (Ha)",
    min_value=0.0,
    step=0.1
)

user = st.text_input("Nama User")

# simpan
if st.button("💾 Simpan"):

    data = baca_data()

    data.append({
        "tanggal": str(tanggal),
        "desa": desa,
        "kelompok_tani": kelompok_tani,
        "kegiatan": kegiatan,
        "komoditas": komoditas,
        "luas": luas,
        "user": user
    })

    simpan_data(data)

    st.success("Laporan berhasil disimpan")

# tampil data
st.subheader("📋 Data Laporan")

data = baca_data()

if data:
    df = pd.DataFrame(data)
    st.dataframe(df)
else:
    st.info("Belum ada data")

st.subheader("📋 Data Laporan")

response = requests.get(
    "http://127.0.0.1:8000/laporan"
)

if response.status_code == 200:
    data = response.json()
    st.dataframe(data)

st.subheader("📊 Rekap Luas")

rekap = requests.get(
    "http://127.0.0.1:8000/rekap"
).json()

st.json(rekap)