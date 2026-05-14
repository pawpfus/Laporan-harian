import streamlit as st
import pandas as pd
import json
import os
from datetime import date

FILE_DATA = "laporan.json"

# FUNGSI

# buat file jika belum ada
if not os.path.exists(FILE_DATA):
    with open(FILE_DATA, "w") as f:
        json.dump([], f)

# baca data
def baca_data():
    try:
        with open(FILE_DATA, "r") as f:
            return json.load(f)
    except:
        return []

# simpan data
def simpan_data(data):
    with open(FILE_DATA, "w") as f:
        json.dump(data, f, indent=4)

# HALAMAN

st.set_page_config(
    page_title="Pelaporan Pertanian",
    page_icon="🌾",
    layout="centered"
)

st.title("🌾 Pelaporan Pertanian")

st.write("Input laporan harian pertanian")

# FORM INPUT

with st.form("form_laporan"):

    tanggal = st.date_input("Tanggal", date.today())

    desa = st.text_input("Desa")

    kelompok_tani = st.text_input("Kelompok Tani")

    jenis_LTT = st.selectbox(
        "Jenis LTT",
        [
            "Reguler",
            "Oplah Rawa",
            "Oplah Non Rawa",
            "CSR"
        ]
    )

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

    submit = st.form_submit_button("💾 Simpan")

# SIMPAN DATA

if submit:

    # validasi
    if desa == "" or kelompok_tani == "" or user == "":
        st.warning("Semua data wajib diisi")
    else:

        data = baca_data()

        data.append({
            "tanggal": str(tanggal),
            "desa": desa,
            "kelompok_tani": kelompok_tani,
            "jenis_LTT": jenis_LTT,
            "kegiatan": kegiatan,
            "komoditas": komoditas,
            "luas": luas,
            "user": user
        })

        simpan_data(data)

        st.success("Laporan berhasil disimpan")

# TAMPIL DATA

st.subheader("📋 Data Laporan")

data = baca_data()

if data:

    df = pd.DataFrame(data)

    # HEADER
    header = st.columns([1,2,2,2,2,2,1])

    header[0].write("No")
    header[1].write("Tanggal")
    header[2].write("Desa")
    header[3].write("Poktan")
    header[4].write("Kegiatan")
    header[5].write("Luas")
    header[6].write("Aksi")

    st.divider()

    # DATA
    for i, row in df.iterrows():

        col = st.columns([1,2,2,2,2,2,1])

        col[0].write(i)
        col[1].write(row["tanggal"])
        col[2].write(row["desa"])
        col[3].write(row["kelompok_tani"])
        col[4].write(row["kegiatan"])
        col[5].write(f"{row['luas']} Ha")

        if col[6].button("🗑", key=f"hapus_{i}"):

            data.pop(i)

            simpan_data(data)

            st.success("Data berhasil dihapus")

            st.rerun()

else:
    st.info("Belum ada data")