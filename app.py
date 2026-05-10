import streamlit as st
import requests
from datetime import date

# Judul aplikasi
st.title("📋 Pelaporan Pertanian")

st.write("Input laporan harian kegiatan pertanian")

# Form input
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

# Tombol simpan
if st.button("💾 Simpan Laporan"):

    data = {
        "tanggal": str(tanggal),
        "desa": desa,
        "kelompok_tani": kelompok_tani,
        "kegiatan": kegiatan,
        "komoditas": komoditas,
        "luas": luas,
        "user": user
    }

    response = requests.post(
        "http://127.0.0.1:8000/laporan",
        json=data
    )

    if response.status_code == 200:
        st.success("Laporan berhasil disimpan")
    else:
        st.error("Gagal menyimpan laporan")