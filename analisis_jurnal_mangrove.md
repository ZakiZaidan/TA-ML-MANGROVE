# 📚 Analisis & Terjemahan Jurnal Mangrove + Machine Learning
> **Sumber:** 4 jurnal PDF dari folder `C:\kuliah\TA\TA-ML\jurnal`  
> **Fokus:** Tools yang dipakai, cara pengolahan data, dan cara tampil di web  
> **Catatan:** Jurnal ke-3 (`forests-14-01831.pdf`) berisi tentang kayu karet, **bukan mangrove** — kemungkinan salah upload.

---

## 📋 Daftar Jurnal

| No | Kode | Judul | Jurnal | Tahun | Lokasi |
|---|---|---|---|---|---|
| 1 | **J1** | Pemodelan perubahan tutupan lahan berbasis ANN pada mangrove di Teluk Bintuni | Agricola (SINTA) | 2025 | Papua Barat, Indonesia |
| 2 | **J2** | Deep learning for mangrove change prediction: Gaoqiao Mangrove, China | Frontiers in Marine Science | 2026 | Guangdong, China |
| 3 | **J3** | An Innovative Tool for Monitoring Mangrove Forest Dynamics in Cuba: SIGMEM | Remote Sensing (MDPI) | 2024 | Kuba, Karibia |
| 4 | **J4** | Prediksi Perubahan Lahan Hutan Mangrove dengan ANN berbasis Landsat (Teluk Ambon) | Prosiding FTSP ITENAS | 2023 | Maluku, Indonesia |
| 5 | **J5** | Mangrove Forest Detection in Balikpapan Using YOLOv8 and Google Earth Satellite Imagery | IIAIR (ITK) | 2024 | Kalimantan Timur, Indonesia |

---

---

## 🇮🇩 J1 — Agricola 2025: ANN Mangrove Teluk Bintuni

### Identitas Jurnal
| Field | Detail |
|---|---|
| **Judul** | Pemodelan perubahan tutupan lahan berbasis Artificial Neural Network (ANN) pada mangrove di Kabupaten Teluk Bintuni |
| **Penulis** | Awalludin Ramdhan, Obed N. Lense, Renny Purnawati |
| **Jurnal** | *Agricola* Vol. 15(1): 11–20 |
| **DOI** | 10.35724/ag.v15i1.6572 |
| **Tahun** | Februari 2025 |
| **Institusi** | Pascasarjana Universitas Papua; Fakultas Kehutanan Universitas Papua |

### 📖 Terjemahan Abstrak
> Penelitian ini membahas perubahan tutupan lahan hutan mangrove di Kabupaten Teluk Bintuni menggunakan pemodelan *Artificial Neural Network* (ANN). Teluk Bintuni memiliki salah satu ekosistem mangrove terbesar di dunia (>220.000 ha), sangat penting untuk penyimpanan karbon dan mitigasi perubahan iklim. Penelitian menggunakan data geospasial dari Kementerian LHK yang dikombinasikan dengan faktor pendorong seperti jarak dari jalan, permukiman, sungai, dan topografi. Model ANN mencapai **Kappa Index = 0,94** dan **Akurasi Keseluruhan = 95,85%**. Prediksi 2022–2030 menunjukkan mangrove primer berkurang 10,29%, sementara mangrove sekunder meningkat 5,36%. Total cadangan karbon diperkirakan turun 6,51% (~2,2 juta Mg C).

### 🔧 Tools & Software yang Digunakan

| Kategori | Tools/Software |
|---|---|
| **Pengolahan Spasial Utama** | **QGIS versi 3.36.3 "Maidenhead"** |
| **Plugin ML Utama** | **MOLUSCE** (Modules for Land Use Change Simulations) |
| **Sumber Data Tutupan Lahan** | Geoportal KLHK — geoportal.menlhk.go.id |
| **Sumber Data Faktor Pendorong** | BIG (Badan Informasi Geospasial) — tanahair.indonesia.go.id |
| **Sumber DEM** | SRTM via USGS EarthExplorer — earthexplorer.usgs.gov |
| **Analisis Korelasi** | Pearson's Correlation (dalam MOLUSCE) |
| **Validasi** | Kappa Statistic (dalam MOLUSCE) |

### 📦 Data Input

| Jenis Data | Detail | Sumber |
|---|---|---|
| Peta tutupan mangrove | Shapefile primer & sekunder (2014, 2018, 2022) | KLHK Geoportal |
| Faktor pendorong | Jarak ke jalan, permukiman, sungai (shapefile) | BIG |
| DEM & Kemiringan lahan | Raster SRTM | USGS EarthExplorer |
| Resolusi raster | 100 m × 100 m | — |

### 🔄 Tahapan Pengerjaan (Workflow)

```
TAHAP 1: PENGUMPULAN DATA
├── Download peta tutupan mangrove 2014, 2018, 2022 dari geoportal.menlhk.go.id
├── Download data jalan, pemukiman, sungai dari BIG (tanahair.indonesia.go.id)
└── Download DEM SRTM dari USGS EarthExplorer

TAHAP 2: PRE-PROCESSING DI QGIS
├── Konversi semua data ke format raster 100m x 100m
├── Hitung jarak Euclidean dari setiap piksel ke fitur (jalan/sungai/permukiman)
└── Standardisasi proyeksi koordinat

TAHAP 3: ANALISIS KORELASI (MOLUSCE)
├── Input: peta tutupan lahan 2014 + 2018 + faktor pendorong
├── Hitung Pearson's Correlation antar faktor pendorong
└── Filter faktor yang berkorelasi tinggi (jarak jalan-bangunan = 0.82 → salah satu dieleminasi)

TAHAP 4: TRAINING MODEL ANN (MOLUSCE)
├── Input: tutupan lahan 2014 (t0) dan 2018 (t1)
├── Konfigurasi hyperparameter:
│   ├── Neighbourhood size
│   ├── Maximum iteration
│   ├── Learning rate
│   ├── Hidden layer
│   └── Faktor momentum
├── Training menggunakan backpropagation
└── Matriks transisi (probabilitas 0–1 per kelas)

TAHAP 5: SIMULASI CELLULAR AUTOMATA
├── Simulasi perubahan tutupan lahan tahun 2022 berdasarkan pola 2014–2018
└── Output: Peta prediksi tutupan lahan 2022

TAHAP 6: VALIDASI MODEL
├── Bandingkan peta prediksi 2022 vs peta aktual 2022 (dari KLHK)
├── Hitung Kappa Index → Hasil: 0.94 (>0.8 = VALID)
└── Hitung Overall Accuracy → Hasil: 95.85%

TAHAP 7: PREDIKSI 2030
├── Jalankan simulasi CA-ANN untuk proyeksi tahun 2030
└── Output: Peta tutupan lahan mangrove prediksi 2030

TAHAP 8: ANALISIS CADANGAN KARBON
└── Kalkulasi: Luas mangrove × Nilai C per hektar (dari FRL 2022)

TAHAP 9: OUTPUT/VISUALISASI
└── Layout peta di QGIS → Ekspor PNG/PDF
    (Tidak ada komponen web — output desktop)
```

### 📊 Hasil Utama

| Indikator | Nilai |
|---|---|
| Kappa Index Validasi | **0.94** (Hampir sempurna, >0.8) |
| Overall Accuracy | **95.85%** |
| Mangrove primer 2022 | 184.754 ha |
| Mangrove primer 2030 (prediksi) | 167.524 ha (turun 10,29%) |
| Mangrove sekunder 2030 (prediksi) | 87.033 ha (naik 5,36%) |
| Kehilangan stok karbon 2022→2030 | 2.206.344,54 Mg C (−6,5%) |

### 🌐 Apakah Ada Komponen Web?
> **❌ TIDAK** — Penelitian ini murni berbasis desktop QGIS. Output berupa peta statis (gambar/PDF). Tidak ada web interface.

---

---

## 🇨🇳 J2 — Frontiers in Marine Science 2026: Deep Learning Gaoqiao

### Identitas Jurnal
| Field | Detail |
|---|---|
| **Judul** | Deep learning for mangrove change prediction: Gaoqiao Mangrove, China |
| **Penulis** | Jiajun Yuan, Yongze Li, Zhaohui Cheng, Xiong Sun*, Dazhao Liu* |
| **Jurnal** | *Frontiers in Marine Science*, Vol. 13 |
| **DOI** | 10.3389/fmars.2026.1632093 |
| **Tahun** | 6 Februari 2026 |
| **Institusi** | Guangdong Ocean University, Zhanjiang, China |

### 📖 Terjemahan Abstrak
> Hutan mangrove di Cagar Alam Nasional Mangrove Gaoqiao (perbatasan Guangdong–Guangxi) telah mengalami penurunan signifikan dan kemudian pemulihan sebagian, akibat aktivitas manusia dan upaya konservasi. Studi ini mengembangkan framework deep learning dua tahap yang praktis:
> 1. **Enhanced U-Net** (dengan modul SE dan CBAM) mengekstrak peta mangrove tahunan dari citra Landsat multitemporal (1993–2023) → IoU = 0.815, F1-score = 0.928
> 2. **U-Net–ConvLSTM** untuk prediksi spasio-temporal → direkomendasikan karena keseimbangan akurasi, kesederhanaan, dan efisiensi komputasi
> 
> Prediksi 2024–2026 menunjukkan pemulihan lambat yang berkelanjutan di bawah manajemen saat ini.

### 🔧 Tools & Software yang Digunakan

| Kategori | Tools/Software |
|---|---|
| **Bahasa Pemrograman** | **Python** |
| **Framework Deep Learning** | **PyTorch** |
| **GPU** | NVIDIA 4090D (16 GB VRAM) |
| **Preprocessing Citra** | **ENVI 5.6** + Python scripts |
| **Platform Citra Satelit** | USGS EarthExplorer |
| **Drone Survey** | DJI Matrice M300 (verifikasi lapangan) |
| **Visualisasi Hasil** | Line graphs (matplotlib Python) |
| **Koordinat/Proyeksi** | UTM Zone 49N |

### 📦 Data Input

| Jenis Data | Detail | Sumber |
|---|---|---|
| Citra Landsat 5 TM | 1993–2012 (68 scene terpilih dari 75) | USGS EarthExplorer |
| Citra Landsat 8 OLI | 2013–2023 (43 scene terpilih dari 52) | USGS EarthExplorer |
| Drone imagery | 3 cm/pixel, RGB+NIR, 4.35 km², Nov 2023 | DJI Matrice M300 |
| Reference masks | Manual dari Google Earth historis + Global Mangrove Watch | — |
| Band yang digunakan | Blue, Green, Red saja (tidak pakai NIR/SWIR) | — |
| Patch size | 256 × 256 pixel, 50% overlap → 1.280 patches | — |

### 🔄 Tahapan Pengerjaan (Workflow)

```
TAHAP 1: AKUISISI DAN PRE-PROCESSING DATA
├── Download 127 scene Landsat dari USGS (dipilih 111 yang bersih dari cloud)
├── Clipping ke batas wilayah + buffer 2 km
├── Co-registration ke UTM Zone 49N (RMSE < 0.5 pixel) — menggunakan ENVI 5.6 + Python
├── Komposit citra tahunan (pilih scene terbaik per tahun)
└── Ekstrak band Blue, Green, Red saja sebagai input

TAHAP 2: PEMBUATAN DATASET TRAINING (STAGE 1)
├── Buat 1.280 overlapping patches (256×256 px, 50% overlap)
├── Manual delineation mangrove sebagai ground truth dari setiap patch
├── Data augmentation: rotasi acak, flip horizontal/vertikal, brightness ±25%, kontras
└── Split data: 70% training (896 patch) / 20% validasi (256 patch) / 10% test (128 patch)

TAHAP 3: TRAINING MODEL EKSTRAKSI (U-Net+SE+CBAM)
├── Arsitektur: U-Net encoder-decoder
│   ├── SE Module: channel-wise recalibration (tekan noise spektral)
│   └── CBAM Module: spatial attention (tingkatkan akurasi tepi/batas mangrove)
├── Loss: Binary Cross-Entropy
├── Optimizer: Adam (learning rate = 0.001)
├── Max epoch: 100 (dengan early stopping, patience=10)
└── Hardware: NVIDIA 4090D GPU, 16GB VRAM

TAHAP 4: GENERATE ANNUAL MANGROVE MASKS
├── Terapkan U-Net+SE+CBAM ke 111 scene (1993–2023)
├── Output: 31 peta biner mangrove tahunan (binary masks)
└── Validasi dengan citra drone Nov 2023 → OA = 98.55%, Kappa = 0.9708

TAHAP 5: TRAINING MODEL PREDIKSI SPASIO-TEMPORAL (Stage 2)
├── Input: 31 annual masks dibagi secara kronologis:
│   ├── Training: 1993–2015 (23 tahun)
│   ├── Validasi: 2016–2018 (3 tahun)
│   └── Test: 2019–2023 (5 tahun)
├── Arsitektur UTAMA yang direkomendasikan: U-Net–ConvLSTM
│   ├── Sliding window: 5 tahun berturut-turut → prediksi tahun berikutnya
│   ├── U-Net: ekstraksi spatial feature dari binary masks
│   └── ConvLSTM: 2 layer, 64 hidden units — tangkap temporal dependency
├── OPSIONAL: ConvLSTM + ECOLOSS (Ecological Constraint Loss)
│   └── Penalti jika prediksi pertumbuhan < -5%/tahun atau > +10%/tahun
├── Loss: Dice Loss + λ×ECOLOSS (λ=0.5)
└── Optimizer: Adam (learning rate = 10⁻⁴, batch size = 2)

TAHAP 6: EVALUASI DAN PERBANDINGAN MODEL
├── Metrik: IoU, F1-Score, MAE (%), RMSE (%)
├── Bandingkan: U-Net-ConvLSTM vs ConvLSTM+ECOLOSS vs ConvLSTM vs LSTM vs RNN vs 3DCNN
└── Hasil terbaik: ConvLSTM+ECOLOSS (IoU=0.793, MAE=6.70%)

TAHAP 7: PREDIKSI 2024–2026
├── Recursive forecasting: gunakan 5-year window (2019–2023) → prediksi 2024
├── Gunakan prediksi 2024 untuk prediksi 2025, dan seterusnya
└── Output: Area mangrove (hektar) per tahun 2024, 2025, 2026

TAHAP 8: VISUALISASI
└── Line graph time-series 1993–2026 (Python matplotlib)
    (Tidak ada komponen web — output akademis)
```

### 📊 Hasil Perbandingan Model

| Model | IoU | F1-Score | MAE (%) | RMSE (%) |
|---|---|---|---|---|
| **ConvLSTM+ECOLOSS** | **0.793** | **0.877** | **6.70** | 9.11 |
| U-Net+ConvLSTM | 0.787 | 0.874 | 6.83 | 9.03 |
| ConvLSTM+Self-Attention | 0.790 | 0.877 | 7.34 | 10.30 |
| 3DCNN | 0.786 | 0.873 | 7.87 | 10.77 |
| ConvLSTM (baseline) | 0.776 | 0.867 | 7.32 | 10.00 |
| LSTM | 0.577 | 0.731 | 10.03 | 11.43 |
| RNN | 0.646 | 0.784 | 15.81 | 17.24 |

### 📈 Prediksi Area Mangrove 2024–2026

| Tahun | U-Net–ConvLSTM | ConvLSTM+ECOLOSS | Pure ConvLSTM |
|---|---|---|---|
| Historis 2023 | 693.45 ha | — | — |
| **2024** | 700.38 ha | 682.83 ha | 681.21 ha |
| **2025** | 708.30 ha | 697.77 ha | 702.63 ha |
| **2026** | 710.46 ha | 701.37 ha | 710.19 ha |

### 🌐 Apakah Ada Komponen Web?
> **❌ TIDAK ADA** — Penelitian ini murni berbasis Python/PyTorch untuk keperluan akademis. Hasil divisualisasikan sebagai grafik ilmiah. **Namun**, framework ini sangat ideal untuk diintegrasikan ke dalam sistem web di masa depan.

---

---

## 🌐 J3 — Remote Sensing MDPI 2024: SIGMEM WebGIS Kuba ⭐ PALING RELEVAN

### Identitas Jurnal
| Field | Detail |
|---|---|
| **Judul** | An Innovative Tool for Monitoring Mangrove Forest Dynamics in Cuba Using Remote Sensing and WebGIS Technologies: SIGMEM |
| **Penulis** | Alexey Valero-Jorge, Raúl González-Lozano, Roberto González-De Zayas, Felipe Matos-Pupo, Rogert Sorí, Milica Stojanovic |
| **Jurnal** | *Remote Sensing* (MDPI), Vol. 16, No. 20 |
| **DOI** | 10.3390/rs16203802 |
| **Tahun** | 12 Oktober 2024 |
| **Lokasi** | Gran Humedal del Norte de Ciego de Ávila (GHNCA), Kuba |

### 📖 Terjemahan Abstrak
> Tujuan utama pekerjaan ini adalah mengembangkan **viewer berbasis web** yang memungkinkan evaluasi perubahan yang dialami mangrove di GHNCA dari sensor jarak jauh, berkontribusi pada pemahaman variabilitas spasio-temporal dinamika vegetasinya. Pencapaian tujuan ini didukung oleh penggunaan teknologi *open-source* seperti **MapStore, GeoServer, Django**, serta **Google Earth Engine**. Evaluasi *machine learning classifier* Random Forest dan Naive Bayes untuk pemetaan otomatis mangrove menunjukkan RF lebih unggul dengan **OA = 94,11%**. Perubahan neto menunjukkan penurunan 5.138,17 ha (2023) dan 2.831,76 ha (2022) dibandingkan tahun 2020.

### 🔧 Tools & Software yang Digunakan

| Kategori | Tools/Software | Fungsi |
|---|---|---|
| **Cloud Computing** | **Google Earth Engine (GEE)** | Pre-processing citra, klasifikasi, hitung indeks vegetasi |
| **Bahasa Pemrograman** | **Python 3.12.7** | Script otomasi, koneksi ke GEE, manajemen data |
| **Library Python (GEE)** | **earthengine-api** | Eksekusi algoritma di GEE dari Python |
| **Library Python** | **PyDrive2** | Manajemen Google Drive untuk download hasil GEE |
| **Library Python** | **geoserver-rest** | Publish data ke GeoServer via REST API |
| **Web Framework** | **Django** | Web server, API, scheduling tugas otomatis |
| **Task Scheduler** | **Celery** | Eksekusi tugas asynchronous (otomatis tiap 3 bulan) |
| **Map Server** | **GeoServer** | Menyajikan data geospasial via WMS/WFS/WCS |
| **Database Spasial** | **PostgreSQL + PostGIS** | Penyimpanan metadata dan data geospasial |
| **Web GIS Frontend** | **MapStore** | Antarmuka web interaktif untuk visualisasi peta |
| **Metadata Catalog** | **GeoNetwork** | Manajemen dan katalog metadata peta |
| **ML Training** | **R 4.2.3 (CARET library)** | Optimasi hyperparameter RF dan Naive Bayes |
| **Deteksi Cloud** | **s2cloudless (Python)** | Masking awan pada citra Sentinel-2 |

### 📦 Data Input

| Jenis Data | Detail | Sumber |
|---|---|---|
| Citra Satelit | Sentinel-2 Surface Reflectance Level-2A (2020–2023) | Copernicus/GEE |
| Band yang digunakan | B2–B8A, B11, B12 (10 band) | — |
| Resolusi spasial | 10 m (semua band di-resample ke 10 m) | — |
| Indeks vegetasi | NDVI, EVI, CCCI, NDMI + 50 indeks spektral | Dihitung di GEE |
| Indeks terpilih (top 3) | **NDVI, RDVI, NDWI** (via recursive variable elimination) | — |
| Ground truth | 5.517 titik GPS (2020–2023), GNSS receiver Topcon HiPer SR | Survei lapangan |
| Dataset ML | 4.413 training + 1.104 validasi | — |

### 🔄 Tahapan Pengerjaan (Workflow) — DETAIL LENGKAP

```
═══════════════════════════════════════════════════════════════
           ARSITEKTUR SISTEM SIGMEM — WEBGIS MANGROVE
═══════════════════════════════════════════════════════════════

JALUR A: KLASIFIKASI (Dieksekusi setiap 12 bulan)
│
├─ [GEE] 1. Download citra Sentinel-2 SR (COPERNICUS/S2_SR_HARMONIZED)
│         Filter: tanggal + region + cloud < 30%
│
├─ [GEE] 2. Cloud Masking dengan s2cloudless
│         - Gunakan COPERNICUS/S2_CLOUD_PROBABILITY
│         - Identifikasi & masking awan dan bayangan awan
│         - Output: citra bersih tanpa awan
│
├─ [R/CARET] 3. Training model ML (dilakukan sekali, hasil di-export ke GEE)
│         - Input: 5.517 titik ground truth + band Sentinel-2 + 50 indeks
│         - Feature selection: Recursive Variable Elimination (RFE)
│           → pilih 3 indeks terbaik: NDVI, RDVI, NDWI
│         - Split: 80% training, 20% validasi
│         - Cross-validation: 3-fold, 10 repetisi
│         - Bandingkan Random Forest vs Naive Bayes
│         - RF menang: OA=94.11%, Kappa=0.94, F1=0.90
│
├─ [GEE] 4. Klasifikasi otomatis di GEE menggunakan model RF terbaik
│         - Prediksi per piksel: mangrove / non-mangrove
│         - Output: peta klasifikasi mangrove (GeoTIFF)
│
├─ [Python/PyDrive2] 5. Download hasil GeoTIFF dari GEE ke Google Drive
│
├─ [Python/geoserver-rest] 6. Upload GeoTIFF ke GeoServer via REST API
│         - Buat workspace, datastore, layer baru
│         - Atur style & simbologi
│
└─ [GeoServer] 7. Layanan peta tersedia via standar OGC:
              WMS / WFS / WCS / CSW

JALUR B: INDEKS VEGETASI (Dieksekusi setiap 3 bulan / kuartalan)
│
├─ [GEE] 1. Ambil citra Sentinel-2 periode 3 bulan terakhir
│         Filter awan → komposit median → cloud-free composite
│
├─ [GEE] 2. Hitung 4 indeks vegetasi:
│         - NDVI = (B8−B4)/(B8+B4)
│         - EVI = 2.5 × ((B8−B4)/(B8+6×B4−7.5×B2+1))
│         - CCCI = ((B9−B5)/(B9+B5)) / ((B9−B4)/(B9+B4))
│         - NDMI = (B8−B11)/(B11+B8)
│
├─ [Python/PyDrive2] 3. Download indeks vegetasi (GeoTIFF) ke server
│
└─ [Python/geoserver-rest] 4. Publish ke GeoServer → tersedia di WebGIS

═══════════════════════════════════════════════════════════════
              ARSITEKTUR WEB (FRONT-END & BACK-END)
═══════════════════════════════════════════════════════════════

USER (Browser)
    ↕ HTTP Request
MapStore [Web GIS Frontend]  ←──────────────────┐
    ↕ WMS/WFS/WCS (standar OGC)                  │
GeoServer [Map Server]                           │
    ↕ Data Query                                 │
PostgreSQL + PostGIS [Database]                  │
    ↑ Data Insert                                │
Django [Web Server + Task Scheduler]  ←──────────┘
    ↕ earthengine-api                            
Google Earth Engine [Cloud Processing]           
    ↑ Sentinel-2 Data                            
Copernicus Hub / GEE Data Catalog                

═══════════════════════════════════════════════════════════════

OTOMASI WORKFLOW (via Django + Celery):
├── Setiap 12 bulan: Update peta klasifikasi mangrove
├── Setiap 3 bulan: Update indeks vegetasi (NDVI, EVI, CCCI, NDMI)
└── Semua log tersimpan di Django admin interface
```

### 📊 Hasil Utama

| Metrik | Random Forest (RF) | Naive Bayes (NB) |
|---|---|---|
| **Overall Accuracy (OA)** | **94.11%** | 89.85% |
| **Kappa** | **0.94** | 0.86 |
| **F1-Score** | **0.90** | 0.80 |
| Producer Accuracy (Mangrove) | 96.16% | 92.01% |

**Perubahan Luas Mangrove GHNCA:**
| Tahun | Area (ha) | Perubahan vs 2020 |
|---|---|---|
| 2020 (baseline) | ~27.238 ha | — |
| 2021 | ~27.811 ha | — |
| 2022 | 24.408 ha | −2.831,76 ha |
| 2023 | 22.100 ha | −5.138,17 ha |

### 🌐 Komponen Web — SIGMEM

> **✅ YA — SISTEM WEBGIS LENGKAP**

**Fitur Web Interface (MapStore):**
- Visualisasi peta mangrove interaktif per tahun
- Layer switching antar tahun (2020–2023)
- Display indeks vegetasi (NDVI, EVI, CCCI, NDMI) per kuartal
- Tampilan spatial berbasis standar OGC (WMS/WFS)
- Aksesibilitas untuk peneliti, pengambil keputusan, dan mahasiswa

---

---

## 🇮🇩 J4 — Prosiding ITENAS 2023: ANN Teluk Ambon

### Identitas Jurnal
| Field | Detail |
|---|---|
| **Judul** | Prediksi Perubahan Lahan Hutan Mangrove dengan Metode ANN berbasis Citra Satelit Landsat (Studi Kasus: Teluk Ambon) |
| **Penulis** | Ramadhany Nurfajar Lukman, Soni Darmawan |
| **Prosiding** | FTSP Series: Seminar Nasional dan Diseminasi Tugas Akhir 2023, ITENAS Bandung |
| **Tahun** | 2023 |
| **Institusi** | Program Studi Teknik Geodesi, ITENAS Bandung |

### 📖 Terjemahan Abstrak
> Hutan mangrove di Teluk Ambon telah mengalami degradasi signifikan. Penelitian bertujuan menganalisis perubahan lahan mangrove menggunakan metode *Artificial Neural Network* (ANN) dalam plugin MOLUSCE di QGIS. Data: Landsat 5 (2003), Landsat 8 (2013, 2023), serta jaringan jalan dan garis pantai sebagai faktor pendorong. Formula prediksi MOLUSCE: t1+(t1−t0) → 2013+(2013−2003) = **prediksi 2023**. Luas mangrove bertambah ~7,38 ha dari 2003 hingga 2033. **Kappa Index = 0.79** (kesesuaian 86,3%). Prediksi 2033: area mangrove bertambah ~46,98 ha.

### 🔧 Tools & Software yang Digunakan

| Kategori | Tools/Software | Fungsi |
|---|---|---|
| **GIS Utama** | **QGIS** | Analisis spasial & plugin MOLUSCE |
| **Plugin ML** | **MOLUSCE** | Pemodelan ANN perubahan lahan |
| **GIS Sekunder** | **ArcMap 10.8** | Klasifikasi citra, layout peta, hitung faktor pendorong |
| **Sumber Citra** | USGS EarthExplorer | Download Landsat 5 & 8 (gratis) |
| **Sumber Faktor Pendorong** | InaGeoPortal | Jaringan jalan & garis pantai |
| **Metode Klasifikasi** | Maximum Likelihood (dalam ArcMap) | Klasifikasi tutupan lahan |
| **Validasi** | Kappa Statistic + Confusion Matrix | Evaluasi akurasi |

### 📦 Data Input

| Jenis Data | Detail | Sumber |
|---|---|---|
| Landsat 5 TM | 2003 | USGS EarthExplorer |
| Landsat 8 OLI | 2013 dan 2023 | USGS EarthExplorer |
| Band yang digunakan | Near Infrared (NIR), SWIR1, Red | Landsat 5 & 8 |
| Jaringan jalan | Shapefile | InaGeoPortal |
| Garis pantai | Shapefile | InaGeoPortal |
| Kelas tutupan lahan | Mangrove, Urban, Hutan, Perairan | Klasifikasi manual |

### 🔄 Tahapan Pengerjaan (Workflow)

```
TAHAP 1: PENGUMPULAN DATA
├── Download Landsat 5 (2003) dari USGS EarthExplorer
├── Download Landsat 8 (2013, 2023) dari USGS EarthExplorer
└── Download shapefile jalan & pantai dari InaGeoPortal

TAHAP 2: KLASIFIKASI TUTUPAN LAHAN (ArcMap 10.8)
├── Pilih kombinasi band: NIR + SWIR1 + Red (Landsat 5 & 8)
├── Klasifikasi supervised: Maximum Likelihood
├── 4 kelas: Mangrove, Urban, Hutan, Perairan
├── Lakukan untuk: Landsat 2003, 2013, 2023
└── Output: 3 peta raster tutupan lahan (2003, 2013, 2023)

TAHAP 3: UJI AKURASI KLASIFIKASI
├── Buat Error Matrix / Confusion Matrix
└── Hitung: Producer Accuracy, User Accuracy, Overall Accuracy, Kappa

TAHAP 4: HITUNG FAKTOR PENDORONG (ArcMap 10.8)
├── Hitung jarak Euclidean dari setiap piksel ke jaringan jalan
└── Hitung jarak Euclidean dari setiap piksel ke garis pantai

TAHAP 5: INPUT MODEL MOLUSCE (QGIS)
├── Tab "Input Model":
│   ├── Initial map: peta tutupan lahan 2003 (t0)
│   └── Final map: peta tutupan lahan 2013 (t1)
├── Tambahkan faktor pendorong: jarak ke jalan + jarak ke garis pantai
└── Cek resolusi & proyeksi semua layer harus sama

TAHAP 6: EVALUATING CORRELATION (MOLUSCE)
└── Hitung korelasi antar faktor pendorong → gunakan hanya faktor bebas korelasi

TAHAP 7: AREA CHANGES (MOLUSCE)
└── Generate matriks transisi (probabilitas 0–1) antar kelas tutupan lahan

TAHAP 8: TRAIN NEURAL-NETWORK (MOLUSCE)
├── Konfigurasi ANN:
│   ├── Neighbourhood size
│   ├── Maximum iteration
│   ├── Learning rate
│   ├── Hidden layer(s)
│   └── Momentum factor
└── Training menggunakan backpropagation

TAHAP 9: VALIDATION (MOLUSCE)
├── Simulasi prediksi tutupan lahan 2023 (= t1+(t1-t0) = 2013+(2013-2003))
├── Bandingkan prediksi 2023 vs aktual 2023 (hasil klasifikasi Landsat 2023)
├── Hitung: % of correctness → 86.3%
└── Hitung: Kappa (overall) → 0.79 (VALID, ≥ ambang batas 0.7)

TAHAP 10: PREDIKSI TAHUN 2033
└── Jalankan simulasi CA-ANN untuk proyeksi 2033 (= 2023+(2023-2013))
    Output: Peta tutupan lahan prediksi 2033

TAHAP 11: LAYOUT DAN OUTPUT
└── Layout peta di ArcMap/QGIS → Ekspor gambar
    (Tidak ada komponen web)
```

### 📊 Hasil Utama

| Indikator | Nilai |
|---|---|
| Kappa Index (validasi model) | **0.79** (Kesepakatan substansial) |
| % of Correctness | **86.3%** |
| Kappa Index (data lapangan 2023) | **0.81** |
| Mangrove 2023 | 46.80 ha |
| Mangrove 2033 (prediksi) | 46.98 ha (+0.18 ha) |
| Periode prediksi | 10 tahun (2023 → 2033) |

### 🌐 Apakah Ada Komponen Web?
> **❌ TIDAK** — Penelitian berbasis desktop (QGIS + ArcMap). Output berupa gambar/layout peta statis.

---

---

---

---

## 🇮🇩 J5 — IIAIR ITK 2024: YOLOv8 Deteksi Mangrove Balikpapan ⭐ BARU

### Identitas Jurnal
| Field | Detail |
|---|---|
| **Judul** | Mangrove Forest Detection in Balikpapan Using YOLOv8 and Google Earth Satellite Imagery |
| **Penulis** | Rayhan Marcello Ananda Purnomo, Miftahul Fauzi Rifai, Muhammad Faisal (Supervisor: Rizky Amelia) |
| **Jurnal** | *Innovative Informatics and Artificial Intelligence Research (IIAIR)*, Vol. 1, Issue 1, pp. 1–8 |
| **DOI** | 10.2478/iiair |
| **Tahun** | Desember 2024 |
| **Institusi** | Departemen Teknik Informatika, Institut Teknologi Kalimantan (ITK), Balikpapan |

### 📖 Terjemahan Abstrak
> Hutan mangrove di Teluk Balikpapan, Kalimantan Timur, mengalami ancaman akibat urbanisasi cepat dan alih fungsi lahan — diperparah oleh pembangunan IKN Nusantara di Penajam Paser Utara. Studi ini mengusulkan pendekatan **deteksi objek berbasis YOLOv8** untuk deteksi otomatis hutan mangrove menggunakan citra satelit Very High Resolution (VHR) dari **Google Earth**. Framework mengintegrasikan preprocessing berbasis **CLAHE** dengan fine-tuning YOLOv8n dari bobot pre-trained COCO selama 250 epoch menggunakan optimizer SGD dengan cosine annealing. Dataset terdiri dari **1.314 citra VHR** dengan anotasi bounding box manual. Model mencapai: Precision **0.687**, Recall **0.652**, F1-Score **0.669**, mAP@50 **0.584**, dan mAP@50-95 **0.309**.

### 🔧 Tools & Software yang Digunakan

| Kategori | Tools/Software | Fungsi |
|---|---|---|
| **Algoritma Utama** | **YOLOv8n** (Ultralytics 2023) | Object detection mangrove |
| **Pre-trained Weights** | **COCO weights** (yolov8n.pt) | Transfer learning |
| **Platform Training** | **Google Colab** (1 GPU) | Komputasi cloud gratis |
| **Anotasi Data** | **LabelImg** | Buat bounding box YOLO format |
| **Library Python** | split-folders | Pembagian dataset train/val |
| **Pre-processing** | **CLAHE** (OpenCV) | Contrast Limited Adaptive Histogram Equalization |
| **Sumber Data** | **Google Earth Pro** (screenshot) | Citra VHR 0.5–1.0 m/piksel |
| **Framework** | **Ultralytics YOLOv8** | Training, evaluasi, inferensi |

### 📦 Data Input

| Jenis Data | Detail | Sumber |
|---|---|---|
| Citra VHR | Google Earth screenshot, 0.5–1.0 m/px | Google Earth Pro |
| Jumlah gambar | 1.314 citra | Manual collection |
| Split dataset | 80% training (1.051 img) / 20% validasi (263 img) | split-folders (seed=42) |
| Ukuran input | 960 × 960 piksel | Resize |
| Format anotasi | YOLO bounding box (x_center, y_center, width, height) | LabelImg |
| Kelas | 1 kelas: **mangrove** | — |
| Area studi | Teluk Balikpapan, 1.0°–1.5°LS, 116.7°–117.0°BT | — |

### 🔄 Tahapan Pengerjaan (Workflow)

```
TAHAP 1: PENGUMPULAN DATA (Data Collection)
├── Screenshot citra satelit dari Google Earth Pro
│   - Area: pesisir Teluk Balikpapan yang diketahui ada mangrove
│   - Resolusi: 0.5–1.0 m/piksel (Very High Resolution)
└── Kumpulkan 1.314 citra total

TAHAP 2: ANOTASI DATA (Manual Annotation)
├── Gunakan software LabelImg
├── Buat bounding box di setiap cluster mangrove per gambar
├── Format YOLO: (class_id, x_center, y_center, width, height) — normalized
├── 1 kelas saja: 'mangrove'
└── Dilakukan oleh tim dengan domain expertise mangrove

TAHAP 3: PEMBAGIAN DATASET
├── Gunakan library split-folders (seed tetap = 42 untuk reproducibility)
├── 80% Training → 1.051 citra
└── 20% Validasi → 263 citra

TAHAP 4: IMAGE PREPROCESSING
├── Resize semua gambar ke 960 × 960 piksel
├── Terapkan CLAHE (Contrast Limited Adaptive Histogram Equalization)
│   ├── Color space: LAB → proses channel L (luminance) saja
│   ├── Clip limit: 2.5
│   └── Tile grid size: 6 × 6
└── Normalisasi intensitas piksel ke range [0, 1]

TAHAP 5: TRAINING MODEL YOLOv8n
├── Load pre-trained weights: yolov8n.pt (COCO)
├── Platform: Google Colab (1 GPU, gratis)
├── Konfigurasi hyperparameter:
│   ├── Epochs: 250
│   ├── Batch size: 8
│   ├── Image size: 960 × 960
│   ├── Optimizer: SGD (lr0 = 0.01, lrf = 0.01, momentum = 0.937)
│   ├── LR Scheduler: Cosine Annealing + warm-up 5 epoch
│   ├── Weight decay: 5×10⁻⁴
│   ├── Box loss weight: 9.0 (prioritas lokalisasi)
│   └── Class loss weight: 0.4
├── Online Data Augmentation (real-time saat training):
│   ├── Horizontal & vertical flip (prob 0.5)
│   ├── Random rotation ±5°
│   ├── HSV jitter (hue 0.01, saturation 0.5, brightness 0.3)
│   ├── Random scale ±30% & translation ±10%
│   ├── Mosaic augmentation (prob 0.8, dimatikan di 20 epoch terakhir)
│   ├── MixUp augmentation (prob 0.1)
│   └── Copy-paste augmentation (prob 0.1)
└── Simpan checkpoint terbaik: best.pt (berdasarkan mAP@50 tertinggi)

TAHAP 6: EVALUASI MODEL
├── Inferensi pada validasi set menggunakan best.pt
├── Confidence threshold: 0.25
├── IoU threshold: 0.6
└── Hitung metrik:
    ├── Precision = TP / (TP + FP)
    ├── Recall = TP / (TP + FN)
    ├── F1-Score = 2 × (P × R) / (P + R)
    ├── mAP@50 (IoU = 0.50)
    └── mAP@50-95 (IoU dari 0.50 sampai 0.95, step 0.05)

TAHAP 7: ANALISIS DAN VISUALISASI
├── Plot training curves (box loss, class loss, DFL loss)
├── Visualisasi bounding box: ground truth (hijau) vs prediksi (biru)
└── Analisis kasus sulit: canopy padat, boundary ambigu
    (Tidak ada komponen web — output akademis/penelitian)
```

### 📊 Hasil Utama

| Metrik Evaluasi | Nilai |
|---|---|
| **Precision** | **0.687** |
| **Recall** | **0.652** |
| **F1-Score** | **0.669** |
| **mAP@50** | **0.584** |
| **mAP@50-95** | **0.309** |

### Hyperparameter Training

| Hyperparameter | Nilai |
|---|---|
| Base model | YOLOv8n (COCO-pretrained) |
| Epochs | 250 |
| Image size | 960 × 960 |
| Batch size | 8 |
| Optimizer | SGD |
| Initial LR (lr₀) | 0.01 |
| Final LR factor (lrf) | 0.01 |
| Momentum | 0.937 |
| Warm-up epochs | 5 |
| Weight decay | 5×10⁻⁴ |
| Box loss weight | 9.0 |
| Class loss weight | 0.4 |
| LR Scheduler | Cosine Annealing |
| Early stopping patience | 50 |
| Random seed | 42 |

### 🔍 Analisis Keterbatasan (dari Diskusi Penulis)

> - Gap antara mAP@50 (0.584) vs mAP@50-95 (0.309) menunjukkan model bisa **lokalisasi kasar** mangrove dengan baik, tapi **akurasi batas bounding box** masih rendah
> - Penyebab: batas canopy mangrove tidak beraturan dan saling berhimpitan — berbeda dengan objek geometris seperti tiang listrik
> - Overfitting ringan terdeteksi (dataset VHR relatif kecil = 1.314 gambar)
> - Saran perbaikan: tambah dataset, pakai multispektral/SAR, perbaiki anotasi batas canopy

### 🌐 Apakah Ada Komponen Web?
> **❌ TIDAK** — Penelitian ini berfokus pada pelatihan dan evaluasi model deteksi objek. Output berupa bounding box pada citra. Tidak ada sistem web.

---

---

## 📊 Tabel Perbandingan Kelima Jurnal

| Aspek | J1 (Bintuni, 2025) | J2 (Gaoqiao, 2026) | J3 (SIGMEM, 2024) | J4 (Ambon, 2023) | J5 (Balikpapan, 2024) |
|---|---|---|---|---|---|
| **Algoritma ML** | ANN (backprop) | U-Net+CBAM + ConvLSTM | Random Forest | ANN (backprop) | **YOLOv8n** (object detection) |
| **Pendekatan** | Prediksi perubahan lahan | Prediksi spasio-temporal | Klasifikasi + WebGIS | Prediksi perubahan lahan | **Deteksi objek real-time** |
| **Tool Utama** | QGIS + MOLUSCE | Python + PyTorch | GEE + Django + GeoServer | QGIS + ArcMap | Google Colab + Ultralytics |
| **Data Citra** | Shapefile KLHK | Landsat 5 & 8 | Sentinel-2 | Landsat 5 & 8 | **Google Earth VHR (0.5m)** |
| **Resolusi Data** | Vector/shapefile | 30 m (Landsat) | 10 m (Sentinel-2) | 30 m (Landsat) | **0.5–1.0 m (VHR)** |
| **Validasi Utama** | Kappa = 0.94 | IoU = 0.815 | OA = 94.11% | Kappa = 0.79 | mAP@50 = 0.584 |
| **Output** | Peta prediksi 2030 | Peta piksel 2024–2026 | WebGIS real-time | Peta prediksi 2033 | **Bounding box mangrove** |
| **Berbasis Web?** | ❌ Desktop | ❌ Python/CLI | ✅ **WebGIS Penuh** | ❌ Desktop | ❌ Lokal/Colab |
| **Konteks Lokal?** | ✅ Indonesia | ❌ China | ❌ Kuba | ✅ Indonesia | ✅ **Indonesia (ITK)** |

---

## 🏗️ Arsitektur Referensi untuk Tugas Akhir

Berdasarkan analisis keempat jurnal, berikut arsitektur sistem yang direkomendasikan untuk TA berbasis web:

```
┌─────────────────────────────────────────────────────────────────┐
│              ARSITEKTUR SISTEM WebGIS MANGROVE                  │
│     (Gabungan pendekatan J1/J4 + arsitektur web J3)            │
├─────────────────┬───────────────────────────────────────────────┤
│  DATA LAYER     │ Citra Landsat/Sentinel-2 (USGS/Copernicus)   │
│                 │ Data KLHK (peta mangrove existing)            │
│                 │ Data BIG (jalan, sungai, permukiman)          │
│                 │ DEM SRTM                                      │
├─────────────────┼───────────────────────────────────────────────┤
│  PROCESSING     │ QGIS → Klasifikasi + Faktor Pendorong        │
│  LAYER          │ MOLUSCE Plugin → ANN + CA (prediksi)         │
│  (Desktop/      │    ATAU                                       │
│   Backend)      │ Python + GEE → Random Forest / Deep Learning  │
├─────────────────┼───────────────────────────────────────────────┤
│  STORAGE        │ PostgreSQL + PostGIS (data spasial)          │
│  LAYER          │ File system (GeoTIFF, Shapefile)             │
├─────────────────┼───────────────────────────────────────────────┤
│  SERVICE        │ GeoServer / QGIS Server                      │
│  LAYER          │ → WMS (tampilkan peta di web)                │
│                 │ → WFS (download fitur vektor)                │
├─────────────────┼───────────────────────────────────────────────┤
│  API LAYER      │ Django / Flask (Python)                      │
│                 │ REST API untuk komunikasi frontend-backend    │
├─────────────────┼───────────────────────────────────────────────┤
│  FRONTEND       │ Leaflet.js / OpenLayers (peta interaktif)    │
│  (Web)          │ HTML + CSS + JavaScript                      │
│                 │ Tampilan: peta klasifikasi + prediksi        │
└─────────────────┴───────────────────────────────────────────────┘
```

### Referensi Spesifik per Komponen Sistem

| Komponen Sistem TA | Ambil dari Jurnal | Detail |
|---|---|---|
| **Metodologi ML (ANN+MOLUSCE)** | J1 + J4 | QGIS plugin MOLUSCE, faktor pendorong, validasi Kappa |
| **Arsitektur WebGIS** | J3 (SIGMEM) | Django + GeoServer + MapStore + PostgreSQL |
| **Teknologi Stack Web** | J3 (SIGMEM) | earthengine-api, geoserver-rest, Celery, Django |
| **Metrik Evaluasi** | J1 + J2 + J3 + J5 | Kappa, OA, F1-Score, IoU, mAP@50 |
| **Indeks Vegetasi** | J3 | NDVI, EVI, NDMI, NDWI (dihitung di GEE atau QGIS) |
| **Prediksi Deep Learning** | J2 | ConvLSTM untuk prediksi temporal (opsional, lebih canggih) |
| **Deteksi Objek Resolusi Tinggi** | J5 (YOLOv8) | YOLOv8 + Google Earth VHR, bounding box mangrove |
| **Transfer Learning** | J5 (YOLOv8) | Fine-tune dari COCO weights, teknik augmentasi |

---

> **💡 Catatan Khusus J5:** Jurnal YOLOv8 ini menggunakan pendekatan **object detection** (bukan segmentasi/klasifikasi piksel). Ini cocok sebagai komponen tambahan untuk **deteksi patch mangrove** secara visual dari citra resolusi tinggi — bisa diintegrasikan ke sistem web sebagai fitur analisis on-demand.

---

*Dokumen ini dibuat secara otomatis dari pembacaan PDF menggunakan Python pdfplumber — September 2026.*
*Semua konten merupakan terjemahan dan analisis dari jurnal asli yang tercantum.*
