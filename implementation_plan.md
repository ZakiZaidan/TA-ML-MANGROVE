# Implementasi Sistem WebGIS Prediksi Mangrove (TA)

Dokumen ini adalah rencana implementasi bertahap untuk Tugas Akhir (TA) membangun WebGIS Prediksi Mangrove. Rencana ini mengacu pada *best practice* dari analisis 5 jurnal, terutama J3 (SIGMEM) untuk arsitektur web dan J5 (YOLOv8) & J1/J4 untuk metrik evaluasi.

## User Review Required
> [!IMPORTANT]
> **Mohon periksa rencana di bawah ini.** Sebelum kita melanjutkan ke tahap pengumpulan data dan penulisan kode backend/ML, saya perlu persetujuan Anda mengenai urutan kerjanya.

## Open Questions
> [!WARNING]
> 1. **Wilayah Studi:** TA Anda berlokasi di daerah mana? (Misalnya: Teluk Bintuni, Teluk Ambon, Teluk Balikpapan, atau daerah lain?). Ini penting untuk saya buatkan script otomatis yang mendownload koordinat satelit yang tepat.
> 2. **Ketersediaan Data Aktual:** Apakah Anda sudah memiliki data *shapefile* batas hutan mangrove dari instansi terkait (seperti KLHK / Bappeda setempat)? Ataukah kita akan mengandalkan murni deteksi satelit + *Machine Learning*?

---

## Proposed Changes / Tahapan Implementasi

Implementasi akan dibagi menjadi 4 tahap utama:

### Tahap 1: Persiapan Data & Akuisisi Satelit (Fokus Berikutnya)
Tahap ini berfokus pada pengumpulan data nyata untuk area studi Anda.
- **[NEW] `data_pipeline/download_gee.py`**: Script opsional untuk mengunduh citra Landsat/Sentinel otomatis via Google Earth Engine API (jika ada akun).
- **[NEW] `data_pipeline/preprocess_shapefile.py`**: Memotong (clip) citra satelit sesuai dengan batas administrasi wilayah menggunakan `GeoPandas` dan `Rasterio`.
- **[NEW] `data/raw/`**: Folder untuk menampung data mentah citra satelit dan data sekunder (DEM, Jarak ke Jalan, Jarak ke Sungai).

### Tahap 2: Pipeline Machine Learning (Klasifikasi & Prediksi)
Tahap ini mengubah script ML demo kita menjadi script yang memproses data spasial `.tif` dan `.shp`.
- **[MODIFY] `ml/train_model.py`**: Menambahkan fitur membaca data latih dari ekstraksi nilai piksel citra vs data ground truth (shapefile). 
- **[NEW] `ml/predict_map.py`**: Script yang menerima citra satelit seluruh wilayah, melakukan prediksi menggunakan model `Random Forest` yang sudah dilatih, dan menghasilkan peta probabilitas mangrove (`GeoTIFF`).
- **[MODIFY] `ml/vegetation_index.py`**: Penyesuaian agar script bisa memproses *batch* data multi-temporal (misal data 2014, 2018, 2023).

### Tahap 3: Database & Backend WebGIS (Django + PostGIS)
Tahap ini membangun server web untuk melayani data spasial ke antarmuka peta.
- **[MODIFY] `backend/mangrove/models.py`**: Pembuatan tabel PostgreSQL/PostGIS untuk menyimpan poligon area mangrove.
- **[NEW] `backend/mangrove/management/commands/load_data.py`**: Script utilitas untuk mengimpor otomatis data GeoJSON hasil prediksi ML ke dalam database PostGIS.
- **[MODIFY] `backend/mangrove/views.py`**: Pembuatan API Endpoint berbasis *Django REST Framework (DRF)* yang menghasilkan output berformat GeoJSON.
- **[MODIFY] `backend/config/urls.py`**: Registrasi API endpoint.

### Tahap 4: Frontend WebGIS Interaktif (Leaflet)
Tahap ini menghubungkan UI yang sudah kita buat dengan data dinamis dari server Django.
- **[MODIFY] `frontend/index.html`**: Menghapus data *dummy* dan menghubungkannya dengan API endpoint (menggunakan `fetch()`).
- **[NEW] `frontend/map_logic.js`**: Memisahkan logika JavaScript (seperti pewarnaan poligon berdasarkan NDVI/Probabilitas dan *Year Switcher*) ke dalam file terpisah agar kode HTML lebih bersih.

---

## Verification Plan

Bagaimana kita memvalidasi bahwa sistem berfungsi sesuai harapan:

### Automated Tests
- Menjalankan *Cross Validation* (K-Fold) pada model *Random Forest* untuk memastikan model tidak *overfitting* dan skor Kappa Index berada di rentang **> 0.80**.
- Menjalankan `python manage.py test` pada Django untuk memvalidasi bahwa endpoint REST API dapat memancarkan `GeoJSON` dengan benar.

### Manual Verification
- Melakukan pengecekan visual dengan meng-*overlay* hasil prediksi dengan citra *Google Earth High Resolution* (seperti metode J5 YOLOv8) langsung di dalam WebGIS.
- Menjalankan *Year Switcher* di WebGIS untuk memastikan data multi-temporal dirender dengan cepat.
