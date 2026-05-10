from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date
import json
import os

app = FastAPI()

FILE_DATA = "laporan.json"

# buat file json jika belum ada
if not os.path.exists(FILE_DATA):
    with open(FILE_DATA, "w") as f:
        json.dump([], f)

# model data
class Laporan(BaseModel):
    tanggal: date
    desa: str
    kelompok_tani: str
    kegiatan: str
    komoditas: str
    luas: float
    user: str

# baca data
def baca_data():
    with open(FILE_DATA, "r") as f:
        return json.load(f)

# simpan data
def simpan_data(data):
    with open(FILE_DATA, "w") as f:
        json.dump(data, f, indent=4)

# input laporan
@app.post("/laporan")
def tambah_laporan(laporan: Laporan):

    data = baca_data()

    data.append({
        "tanggal": str(laporan.tanggal),
        "desa": laporan.desa,
        "kelompok_tani": laporan.kelompok_tani,
        "kegiatan": laporan.kegiatan,
        "komoditas": laporan.komoditas,
        "luas": laporan.luas,
        "user": laporan.user
    })

    simpan_data(data)

    return {"message": "Data berhasil disimpan"}

# tampil semua laporan
@app.get("/laporan")
def lihat_laporan():
    return baca_data()