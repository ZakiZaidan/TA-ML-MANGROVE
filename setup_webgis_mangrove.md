# 🚀 Panduan Setup Sistem WebGIS Mangrove
> **Tujuan:** Membangun sistem seperti SIGMEM (Jurnal Remote Sensing, 2024)  
> **Stack:** Django + Machine Learning + Peta Leaflet Interaktif  
> **OS:** Windows 10/11 | Python 3.10

---

## 🗺️ Gambaran Sistem yang Akan Dibangun

```
┌──────────────────────────────────────────────────────────┐
│                 WEBGIS MANGROVE (TA)                    │
├──────────┬───────────────────┬──────────────────────────┤
│ FRONTEND │   Peta interaktif │ Leaflet.js + HTML/CSS/JS │
│          │   Grafik hasil    │ Chart.js                 │
├──────────┼───────────────────┼──────────────────────────┤
│ BACKEND  │   Web server      │ Django (Python)          │
│          │   REST API        │ Django REST Framework    │
│          │   Task ML         │ Celery + Redis           │
├──────────┼───────────────────┼──────────────────────────┤
│ ML       │   Klasifikasi     │ Random Forest (sklearn)  │
│          │   Prediksi        │ ANN/CA (seperti MOLUSCE) │
│          │   Indeks vegetasi │ NDVI, EVI (rasterio)     │
├──────────┼───────────────────┼──────────────────────────┤
│ DATA     │   Peta mangrove   │ GeoJSON / Shapefile      │
│          │   Database        │ PostgreSQL + PostGIS      │
│          │   Citra satelit   │ GeoTIFF (Sentinel/Landsat)│
└──────────┴───────────────────┴──────────────────────────┘
```

---

## 📥 BAGIAN 1: SOFTWARE YANG HARUS DIINSTALL

### A. Software Wajib (Install Dulu Sebelum Apapun)

| No | Software | Download | Fungsi |
|---|---|---|---|
| 1 | **Python 3.10** | Sudah ada ✅ | Runtime utama |
| 2 | **QGIS 3.36** | [qgis.org/download](https://qgis.org/download/) | Analisis GIS + MOLUSCE |
| 3 | **PostgreSQL 16** | [postgresql.org/download](https://www.postgresql.org/download/windows/) | Database spasial |
| 4 | **PostGIS 3.4** | Paket pgAdmin/StackBuilder | Ekstensi spasial PostgreSQL |
| 5 | **Redis** | [github.com/microsoftarchive/redis/releases](https://github.com/microsoftarchive/redis/releases) | Message broker (Celery) |
| 6 | **Git** | Sudah ada ✅ | Version control |
| 7 | **VS Code** | [code.visualstudio.com](https://code.visualstudio.com/) | Code editor |

### B. Data yang Harus Didownload (Gratis)

| Sumber | URL | Isi |
|---|---|---|
| KLHK Geoportal | [geoportal.menlhk.go.id](https://geoportal.menlhk.go.id) | Peta tutupan mangrove Indonesia |
| BIG Indonesia | [tanahair.indonesia.go.id](http://tanahair.indonesia.go.id/portal-web/) | Shapefile jalan, sungai, permukiman |
| USGS EarthExplorer | [earthexplorer.usgs.gov](https://earthexplorer.usgs.gov/) | Landsat 8/9, Sentinel-2, DEM SRTM |
| Google Earth Engine | [earthengine.google.com](https://earthengine.google.com) | Daftar akun gratis (akademik) |

---

## ⚙️ BAGIAN 2: LANGKAH INSTALASI STEP-BY-STEP

### LANGKAH 1: Install PostgreSQL + PostGIS

```
1. Download PostgreSQL dari: https://www.postgresql.org/download/windows/
2. Saat instalasi, CENTANG "Stack Builder"
3. Buka Stack Builder setelah selesai → pilih PostGIS → install
4. Buka pgAdmin 4 → buat database baru bernama: mangrove_db
5. Klik kanan mangrove_db → Query Tool → jalankan:
   CREATE EXTENSION postgis;
   CREATE EXTENSION postgis_topology;
```

### LANGKAH 2: Buat Virtual Environment Python

```powershell
# Buka PowerShell di folder proyek
cd C:\kuliah\TA\TA-ML\webgis-mangrove

# Buat virtual environment
python -m venv venv

# Aktifkan venv (WAJIB setiap kali kerja!)
.\venv\Scripts\Activate.ps1

# Kalau muncul error execution policy:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### LANGKAH 3: Install GDAL (PALING KRITIKAL di Windows!)

> ⚠️ GDAL adalah library geospasial paling penting. Di Windows, JANGAN pakai `pip install gdal` langsung karena sering error! Gunakan wheel file pre-compiled:

```powershell
# 1. Buka: https://github.com/cgohlke/geospatial-wheels/releases
# 2. Download file untuk Python 3.10 + Windows 64-bit, contoh:
#    GDAL-3.9.1-cp310-cp310-win_amd64.whl

# 3. Install wheel-nya (ganti nama file sesuai yang kamu download):
pip install C:\Users\ahmad\Downloads\GDAL-3.9.1-cp310-cp310-win_amd64.whl

# 4. Cek berhasil:
python -c "from osgeo import gdal; print('GDAL OK:', gdal.__version__)"
```

### LANGKAH 4: Install Semua Library Python

```powershell
# Pastikan venv sudah aktif (ada tulisan (venv) di prompt)

# Install semua sekaligus:
pip install Django==4.2.16 djangorestframework==3.15.2 django-cors-headers==4.4.0
pip install geopandas scikit-learn numpy pandas matplotlib folium joblib
pip install psycopg2-binary celery redis python-dotenv requests
pip install rasterio
```

**Status Instalasi (Final - 18/18 Berhasil!):**

| Library | Status |
|---|---|
| Django 4.2.16 | OK |
| GeoPandas 1.1.4 | OK |
| Rasterio 1.4.4 | OK |
| Scikit-learn 1.7.2 | OK |
| Celery 5.6.3 | OK |
| Redis 8.1.0 | OK |
| Psycopg2 2.9.13 | OK |
| Folium, NumPy, Pandas, Matplotlib, dkk. | OK |
| **GDAL 3.10.1** | **OK (via wheel)** |

### LANGKAH 5: Setup Proyek Django

```powershell
cd C:\kuliah\TA\TA-ML\webgis-mangrove\backend

# Buat proyek Django
django-admin startproject config .

# Buat app mangrove
python manage.py startapp mangrove

# Test Django berjalan:
python manage.py runserver
# Buka browser: http://127.0.0.1:8000/
```

### LANGKAH 6: Install Redis (untuk Celery)

```
1. Download: https://github.com/microsoftarchive/redis/releases
2. Install Redis → akan berjalan sebagai Windows Service otomatis
3. Test di PowerShell: redis-cli ping
   → Harus output: PONG
```

---

## 📦 BAGIAN 3: PENJELASAN SETIAP LIBRARY

### Kategori Web Framework
| Library | Fungsi di Sistem Kamu |
|---|---|
| `Django` | Server web utama — handle request, routing, database |
| `djangorestframework` | Buat REST API agar frontend bisa minta data dari backend |
| `django-cors-headers` | Izinkan browser akses API dari domain berbeda |

### Kategori Geospasial
| Library | Fungsi di Sistem Kamu |
|---|---|
| `GDAL` | Engine geospasial utama — dasar semua library geospasial |
| `geopandas` | Baca/tulis shapefile dan GeoJSON di Python |
| `rasterio` | Baca citra satelit GeoTIFF piksel per piksel |
| `Shapely` | Operasi geometri: potong area, hitung luas, overlap |
| `pyproj` | Konversi proyeksi koordinat (WGS84 ↔ UTM ↔ dll) |
| `Fiona` | Backend I/O untuk geopandas (auto-dipakai) |

### Kategori Machine Learning
| Library | Fungsi di Sistem Kamu |
|---|---|
| `scikit-learn` | Random Forest, preprocessing, split dataset, akurasi |
| `numpy` | Operasi array/matriks piksel citra satelit |
| `scipy` | Hitung Pearson Correlation (seleksi faktor pendorong) |
| `joblib` | Simpan/load model ML ke file `.pkl` |
| `pandas` | Manipulasi data tabular |

### Kategori Database & Task
| Library | Fungsi di Sistem Kamu |
|---|---|
| `psycopg2-binary` | Koneksi Python ↔ PostgreSQL+PostGIS |
| `celery` | Jalankan task ML di background secara terjadwal |
| `redis` | Antrian pesan untuk Celery |

### Kategori Visualisasi
| Library | Fungsi di Sistem Kamu |
|---|---|
| `folium` | Generate peta Leaflet interaktif dari Python |
| `matplotlib` | Plot grafik perubahan luas mangrove |

---

## 📁 BAGIAN 4: STRUKTUR FOLDER PROYEK

```
webgis-mangrove/
│
├── requirements.txt             ← Semua library Python
├── .env                         ← Password DB, API keys (jangan di-commit!)
│
├── backend/                     ← Aplikasi Django
│   ├── manage.py
│   ├── config/                  ← Settings, routing
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── celery.py
│   │
│   └── mangrove/                ← App utama
│       ├── models.py            ← Model database
│       ├── views.py             ← API logic
│       ├── serializers.py       ← Data → JSON
│       ├── urls.py              ← URL routing
│       └── tasks.py             ← Task ML (Celery)
│
├── ml/                          ← Script Machine Learning
│   ├── train_model.py           ← Training Random Forest
│   ├── predict.py               ← Prediksi tutupan lahan
│   ├── preprocess.py            ← Preprocessing citra
│   ├── vegetation_index.py      ← Hitung NDVI, EVI, NDWI, NDMI
│   └── models/                  ← File model terlatih (.pkl)
│
├── data/                        ← Data geospasial
│   ├── raw/                     ← Download dari KLHK/BIG
│   ├── processed/               ← Setelah preprocessing
│   └── output/                  ← Hasil prediksi (GeoJSON)
│
└── frontend/                    ← Web Interface
    ├── index.html               ← Halaman utama
    ├── map.js                   ← Peta Leaflet interaktif
    └── style.css                ← Styling
```

---

## 🏗️ BAGIAN 5: RENCANA PENGERJAAN (8 TAHAP)

```
Tahap 1 — Setup Lingkungan (Minggu 1)
   Install PostgreSQL, PostGIS, GDAL, semua library Python

Tahap 2 — Persiapan Data (Minggu 2)
   Download shapefile KLHK, BIG, DEM dari USGS

Tahap 3 — Machine Learning (Minggu 3-4)
   Preprocessing → Training Random Forest → Prediksi → Validasi Kappa

Tahap 4 — Database Setup (Minggu 5)
   Import data ke PostgreSQL+PostGIS, buat tabel spasial

Tahap 5 — Backend API Django (Minggu 6-7)
   Buat endpoint: /api/mangrove/, /api/prediction/, /api/vegetation-index/

Tahap 6 — Peta Interaktif (Minggu 8)
   Leaflet.js + GeoJSON dari API + layer switcher + popup info

Tahap 7 — Grafik & Dashboard (Minggu 9)
   Chart.js untuk grafik luas mangrove per tahun

Tahap 8 — Polish & Presentasi (Minggu 10)
   Responsive design, dokumentasi, demo
```

---

## ⚡ BAGIAN 6: QUICK TEST — Cek Semua Library Berfungsi

Simpan sebagai `test_setup.py` dan jalankan:

```python
# test_setup.py — jalankan dengan: python test_setup.py
print("Testing semua library...")

try:
    import django; print(f"  ✅ Django {django.__version__}")
except: print("  ❌ Django GAGAL")

try:
    import geopandas; print(f"  ✅ GeoPandas {geopandas.__version__}")
except: print("  ❌ GeoPandas GAGAL")

try:
    import rasterio; print(f"  ✅ Rasterio {rasterio.__version__}")
except: print("  ❌ Rasterio GAGAL")

try:
    import sklearn; print(f"  ✅ Scikit-learn {sklearn.__version__}")
except: print("  ❌ Scikit-learn GAGAL")

try:
    import folium; print(f"  ✅ Folium {folium.__version__}")
except: print("  ❌ Folium GAGAL")

try:
    import psycopg2; print(f"  ✅ Psycopg2 {psycopg2.__version__}")
except: print("  ❌ Psycopg2 GAGAL")

try:
    import celery; print(f"  ✅ Celery {celery.__version__}")
except: print("  ❌ Celery GAGAL")

try:
    from osgeo import gdal; print(f"  ✅ GDAL {gdal.__version__}")
except: print("  ❌ GDAL GAGAL — install via wheel file!")

print("\nDone! Fix semua yang ❌ sebelum lanjut.")
```

---

## 🆘 Troubleshooting Umum di Windows

| Error | Penyebab | Solusi |
|---|---|---|
| `GDAL not found` | GDAL belum install | Install via wheel pre-compiled |
| `psycopg2 error` | PostgreSQL tidak jalan | Start service di Windows Services |
| `redis connection refused` | Redis tidak jalan | Jalankan `redis-server` di terminal terpisah |
| `ExecutionPolicy error` | PowerShell policy | `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` |
| `CRS mismatch / shapefile error` | Proyeksi berbeda | `gdf.to_crs('EPSG:4326')` untuk reproject |
| `ModuleNotFoundError` | venv tidak aktif | Jalankan `.\venv\Scripts\Activate.ps1` dulu |

---

*Referensi arsitektur: Valero-Jorge et al. (2024), SIGMEM — DOI: 10.3390/rs16203802*
