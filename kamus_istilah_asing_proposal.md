# KAMUS & ANALISIS MENDALAM ISTILAH ASING DALAM PROPOSAL TA

> **Acuan Tunggal:** [Proposal TA Achmad Zaki Zaidan (8).pdf](file:///c:/kuliah/TA/TA-ML/Proposal%20TA%20Achmad%20Zaki%20Zaidan%20(8).pdf) (80 Halaman PDF / 66 Halaman Naskah)  
> **Tujuan Dokumen:** Membedah **seluruh istilah asing, akronim teknis, nama ilmiah spesies, pustaka perangkat lunak, dan metrik statistik** yang muncul di dalam proposal Anda—lengkap dengan arti, analisis teknis mendalam (dengan analogi Sistem Informasi/Web), lokasi kemunculannya di PDF, serta perannya saat ditanya dosen penguji Sempro.

---

## Peta Cepat 7 Kategori Istilah di Proposal Anda

1. [Ekologi, Biota & Konteks Lapangan Kariangau](#1-ekologi-biota--konteks-lapangan-kariangau)
2. [Penginderaan Jauh & Satelit Sentinel-2](#2-penginderaan-jauh--satelit-sentinel-2)
3. [Saluran Spektral & 5 Indeks Vegetasi/Air](#3-saluran-spektral--5-indeks-vegetasiair)
4. [Machine Learning, Validasi & Metrik Akurasi](#4-machine-learning-validasi--metrik-akurasi)
5. [Pemodelan Spasio-Temporal (CA-Markov) & Validasi Proyeksi](#5-pemodelan-spasio-temporal-ca-markov--validasi-proyeksi)
6. [Geospasial, Sistem Koordinat & Pustaka Python](#6-geospasial-sistem-koordinat--pustaka-python)
7. [Arsitektur WebGIS, Basis Data Spasial & API](#7-arsitektur-webgis-basis-data-spasial--api)

---

## 1. Ekologi, Biota & Konteks Lapangan Kariangau

| Istilah Asing / Ilmiah | Arti & Analisis Mendalam | Lokasi di PDF |
| :--- | :--- | :--- |
| ***Blue Carbon*** (Karbon Biru) | **Arti:** Karbon yang diserap dari atmosfer dan disimpan oleh ekosistem pesisir & laut (mangrove, lamun, rawa pasang surut).<br>**Analisis:** Berbeda dengan hutan darat yang menyimpan karbon terutama di batang kayu, mangrove menyimpan sebagian besar karbon di **sedimen tanah lumpur anaerobik** hingga beberapa kali lipat lebih besar per hektarnya. Inilah alasan mengapa hilangnya mangrove di Kariangau berdampak besar secara ekologis. | Hlm. 15, 24, 29 |
| ***Estuaria*** (*Estuarine*) | **Arti:** Wilayah perairan muara tempat bercampurnya air tawar sungai dengan air asin laut.<br>**Analisis:** Kawasan Kariangau berada di zona estuaria Teluk Balikpapan yang dipengaruhi pasang surut harian. Kondisi tanah berlumpur dan payau ini yang membuat kandungan air tajuk mangrove berbeda dari hutan darat. | Hlm. 15, 29 |
| ***Boardwalk Canopy Trail*** (*Boardwalk*) | **Arti:** Jalan titian kayu ulin di atas rawa mangrove untuk jalur wisata dan patroli.<br>**Analisis:** Menjadi titik masalah lapangan di Bab 1 & 2.1: pengamatan visual petugas dari *boardwalk* hanya menjangkau radius puluhan meter di kiri-kanan jembatan, tidak bisa melihat keseluruhan hamparan kawasan. | Hlm. 16, 30 |
| ***Ship Wake*** | **Arti:** Gelombang buritan yang ditimbulkan oleh pergerakan kapal bermotor/tongkang.<br>**Analisis:** Lalu lintas kapal tongkang logistik IKN di perairan Teluk Balikpapan depan Kariangau memicu *ship wake* berintensitas tinggi yang mengikis bibir pantai dan merusak bibit mangrove muda (*abrasion*). | Hlm. 16, 30 |
| ***Anthropogenic*** (Antropogenik) | **Arti:** Aktivitas atau dampak yang ditimbulkan oleh ulah manusia (kebalikan dari faktor alamiah).<br>**Analisis:** Di proposal Anda merujuk pada ekspansi Kawasan Industri Kariangau (KIK), galangan kapal (*shipyard*), alih fungsi tambak, dan alur logistik IKN. | Hlm. 16, 30 |
| ***Shipyard*** | **Arti:** Galangan kapal (fasilitas pembuatan dan perbaikan kapal).<br>**Analisis:** Salah satu aktivitas industri berat di pesisir Kariangau yang berbatasan langsung dengan ekosistem mangrove. | Hlm. 16, 30 |
| ***Rhizophora apiculata, Avicennia marina, Sonneratia alba, Nypa fruticans*** | **Arti:** Nama Latin spesies mangrove sejati (bakau, api-api, pedada) serta asosiasi nipah (*Nypa fruticans*).<br>**Analisis:** Menunjukkan bahwa vegetasi mangrove Kariangau bukan satu jenis tanaman seragam, melainkan zonasi multi-spesies pesisir tropis (Noor dkk., 2006). | Hlm. 29 |
| ***Nasalis larvatus*** | **Arti:** Nama ilmiah **Bekantan**, primata endemik Kalimantan berhidung panjang.<br>**Analisis:** Mangrove Kariangau merupakan habitat dan koridor jelajah pakan bekantan (Toulec dkk., 2022). | Hlm. 16, 29 |
| ***Orcaella brevirostris*** | **Arti:** Nama ilmiah **Pesut / Lumba-lumba Irrawaddy** pesisir Teluk Balikpapan.<br>**Analisis:** Ekosistem mangrove menjaga kualitas perairan estuaria tempat mencari makan mamalia pesisir langka ini (Kreb, 2005). | Hlm. 29 |
| ***Scylla serrata*** | **Arti:** Nama ilmiah **Kepiting Bakau**, komoditas perikanan bernilai ekonomi bagi nelayan lokal. | Hlm. 16 |

---

## 2. Penginderaan Jauh & Satelit Sentinel-2

| Istilah Asing / Akronim | Kepanjangan, Arti & Analisis Mendalam | Lokasi di PDF |
| :--- | :--- | :--- |
| **ESA** | *European Space Agency* — Badan Antariksa Eropa pemilik dan pengelola misi satelit **Sentinel-2** (*Copernicus*). | Hlm. 21, 42, 57–59 |
| **CDSE** | *Copernicus Data Space Ecosystem* — Portal dan infrastruktur data resmi ESA tempat mengunduh citra satelit Sentinel-2 secara gratis (*open-access*). Menggantikan portal lama *SciHub*. | Hlm. 21, 51, 64, 66 |
| **STAC API** | *SpatioTemporal Asset Catalog API* — Standar antarmuka API modern untuk mencari dan memfilter metadata citra satelit berdasarkan **lokasi (kotak koordinat)**, **rentang waktu (Juli–Sept)**, dan **persentase awan**, sehingga Anda tidak perlu mengunduh file raksasa secara manual satu per satu lewat browser. | Hlm. 21, 26, 38, 51, 64, 66 |
| **MSI** | *MultiSpectral Instrument* — Nama kamera/sensor optik di satelit Sentinel-2A dan 2B yang merekam 13 saluran gelombang cahaya (dari biru hingga inframerah gelombang pendek). | Hlm. 32, 34, 42, 57, 58, 66 |
| **Level-2A (L2A)** | Tingkat produk citra Sentinel-2 yang **sudah dikoreksi atmosferik** oleh ESA menggunakan algoritma *Sen2Cor* (menghilangkan efek hamburan udara/kabut), berbeda dengan Level-1C (*Top-of-Atmosphere*) yang masih mentah tercampur atmosfer. | Hlm. 21, 42, 57, 59 |
| **ARD** | *Analysis-Ready Data* — Data satelit yang sudah terkalibrasi secara geometris dan radiometris sehingga langsung siap dimasukkan ke analisis/ML tanpa proses koreksi atmosfer yang rumit. | Hlm. 21, 57, 59, 66 |
| **BOA** (*Surface Reflectance*) | *Bottom-of-Atmosphere* — Nilai pantulan cahaya fisik tepat di **permukaan bumi/tajuk daun** (setelah efek atmosfer dihilangkan), bernilai desimal di kisaran `0` s.d. `1`. | Hlm. 11, 21, 42, 57, 59 |
| **Processing Baseline (`PB ≥ 04.00`)** | Versi perangkat lunak pemroses citra milik ESA. Sejak **PB 04.00 (25 Januari 2022)**, ESA menerapkan pergeseran angka **`BOA_ADD_OFFSET = -1000`** pada seluruh produk Sentinel-2 agar nilai piksel permukaan gelap tidak terpotong di angka nol. | Hlm. 11, 21, 26, 42, 52, 58 |
| **DN** (*Digital Number*) | Bilangan bulat (*integer*) mentah yang tersimpan di berkas raster GeoTIFF sebelum dibagi `10000` dan dikoreksi `BOA_ADD_OFFSET = -1000` melalui Persamaan (2.1). | Hlm. 11, 43 |
| **BOA_ADD_OFFSET** | Konstanta penyesuaian radiometrik resmi sebesar **`-1000`** pada produk Sentinel-2 L2A `PB ≥ 04.00`. Wajib ditambahkan (`DN - 1000`) sebelum dibagi `10000`; jika dilupakan, seluruh nilai reflektansi bergeser naik `+0,1` dan merusak rumus rasio indeks. | Hlm. 11, 21, 26, 42, 52, 58 |
| **SCL** | *Scene Classification Layer* — Peta masker klasifikasi bawaan Sentinel-2 L2A yang menandai kondisi setiap piksel (misal: kode `0` & `1` *no-data/saturated*, kode `3` bayangan awan, kode `9` awan tebal, kode `10` sirus tipis) agar piksel awan dapat dibuang otomatis. | Hlm. 26, 43, 51, 52, 58, 69 |
| **LAT** (*Lowest Astronomical Tide*) | Datum/titik acuan muka air laut surut terendah secara astronomis. Di proposal Anda, elevasi pasang surut dibatasi **$\le 1{,}5\text{ m}$ dari LAT** berdasarkan tabel Pushidrosal. | Hlm. 21, 26, 43, 52, 58 |
| ***Spring High Tide*** | Pasang purnama / pasang tertinggi. Air laut menenggelamkan akar dan daun bawah mangrove sehingga menyerap sinar inframerah (**atenuasi optik**) dan mengacaukan klasifikasi. | Hlm. 43 |
| **`nanmedian`** (*Median Composite*) | Teknik menggabungkan beberapa foto satelit dalam jendela kering (Juli–September) dengan mengambil **nilai tengah (median) di tiap piksel sambil mengabaikan nilai kosong (`NaN`)** bekas awan yang sudah dihapus `SCL`. | Hlm. 39, 43, 52 |
| **MGRS** | *Military Grid Reference System* — Sistem penamaan petak (*tile*) global Sentinel-2. Kawasan Kariangau/Balikpapan berada pada petak tile tertentu di sistem MGRS. | Hlm. 51, 57 |
| **VHR** (*Very High Resolution*) | Citra udara/satelit resolusi sangat tinggi (level sub-meter, seperti Google Earth Pro & Esri Wayback) sehingga bentuk tajuk pohon terlihat jelas. Dipakai untuk menggambar *ground truth* baseline 2023. | Hlm. 21, 26, 64, 66 |
| ***Resampling*** (`Bilinear` & `Nearest Neighbor`) | Proses menyamakan ukuran kotak piksel dari `20 m` (band `B05, B8A, B11, B12, SCL`) menjadi `10 m`:<br>• **`Bilinear`**: Merata-ratakan 4 piksel terdekat — dipakai untuk angka pantulan cahaya kontinu.<br>• **`Nearest Neighbor`**: Mengambil nilai kode persis piksel terdekat tanpa merata-rata — wajib dipakai untuk `SCL` karena kode kelas (`3`, `9`, `10`) tidak boleh dirata-ratakan jadi `6,5`. | Hlm. 38, 52 |
| ***Raster Feature Cube*** | Susunan tumpukan 13 matriks 2D (8 band + 5 indeks) yang ukurannya sudah seragam (`10 m`), ibarat 13 lapisan Excel yang ditumpuk sejajar di atas peta Kariangau. | Hlm. 53 |

---

## 3. Saluran Spektral & 5 Indeks Vegetasi/Air

| Istilah Asing / Akronim | Kepanjangan, Arti & Analisis Mendalam | Lokasi di PDF |
| :--- | :--- | :--- |
| ***Spectral Separability*** | Daya pisah spektral — seberapa mudah dua kelas berbeda (misal mangrove vs hutan darat) dipisahkan berdasarkan angka pantulan cahayanya. | Hlm. 43 |
| ***Spectral Confusion*** | Kerancuan/kebingungan spektral — kondisi ketika dua objek berbeda (misal mangrove basah dan hutan darat bukit) punya nilai indeks yang hampir sama sehingga model salah menebak. | Hlm. 23 |
| ***Spectral Thresholding*** | Metode klasik memisahkan kelas hanya memakai satu angka batas (misal: *"jika NDVI > 0,5 maka mangrove"*). Mudah gagal di wilayah batas transisi dibanding *Machine Learning*. | Hlm. 36 |
| **Red Edge 1 (`B05`)** | Saluran di `705 nm`, berada tepat di batas curam antara penyerapan cahaya merah oleh klorofil dan pantulan tinggi NIR. Sangat peka terhadap kesehatan & stres vegetasi. | Hlm. 44, 60 |
| **NIR** (`B08` & `B8A`) | *Near-Infrared* (Inframerah Dekat: `B08` Lebar `842 nm` & `B8A` Sempit `865 nm`). Dipantulkan sangat kuat oleh struktur sel daun sehat, tetapi **diserap habis oleh air**. Menjadi komponen di seluruh 5 indeks spektral Anda. | Hlm. 44, 60 |
| **SWIR** (`B11` & `B12`) | *Short-Wave Infrared* (Inframerah Gelombang Pendek: `1610 nm` & `2190 nm`). **Diserap sangat kuat oleh air dan tanah/lumpur basah**. Inilah kunci pembeda mangrove basah terhadap hutan darat kering. | Hlm. 23, 33, 44, 60 |
| **NDVI** | *Normalized Difference Vegetation Index* (Rouse dkk., 1974) — Mengukur tingkat kehijauan/klorofil vegetasi menggunakan `B08` (NIR) dan `B04` (Merah). Mudah mengalami kejenuhan (*saturation*) di hutan lebat. | Hlm. 11, 17, 44 |
| **EVI** | *Enhanced Vegetation Index* (Huete dkk., 2002) — Versi penyempurnaan NDVI yang menambahkan `B02` (Biru) dan konstanta koreksi agar **tidak cepat jenuh pada kanopi rapat** serta **tahan terhadap kabut/aerosol** dan latar lumpur. | Hlm. 11, 21, 44 |
| **NDWI** | *Normalized Difference Water Index* (McFeeters, 1996) — Menggunakan `B03` (Hijau) dan `B08` (NIR) untuk mendeteksi **badan air terbuka** (teluk/muara/tambak berair). | Hlm. 11, 21, 44 |
| **NDMI** | *Normalized Difference Moisture Index* (Gao, 1996) — Menggunakan `B08` (NIR) dan `B11` (SWIR-1) untuk mengukur **kelembapan internal tajuk daun dan substrat basah**. Fitur pembeda nomor 1 di TA Anda. | Hlm. 5, 6, 11, 18, 21, 44 |
| **RDVI** | *Renormalized Difference Vegetation Index* (Roujean & Breon, 1995) — Menggabungkan sensitivitas indeks selisih (vegetasi jarang) dan indeks rasio (vegetasi rapat) memakai akar kuadrat di penyebut. | Hlm. 11, 21, 44 |

---

## 4. Machine Learning, Validasi & Metrik Akurasi

| Istilah Asing / Akronim | Arti & Analisis Mendalam | Lokasi di PDF |
| :--- | :--- | :--- |
| ***Supervised Machine Learning*** | Pembelajaran mesin terawasi: model dilatih memakai contoh soal yang **sudah ada kunci jawabannya** (*ground truth* label `1` dan `0`). | Hlm. 5, 19, 44 |
| ***Random Forest* (RF)** | Algoritma ansambel karya Breiman (2001) yang menggabungkan **banyak pohon keputusan** (`n_estimators = 200`) untuk melakukan pemungutan suara (*voting*) sehingga jauh lebih akurat dan stabil daripada 1 pohon tunggal. | Hlm. 19, 33, 44–45 |
| ***Ensemble Bagging*** (*Bootstrap Aggregating*) | Teknik melatih ratusan model secara paralel di mana setiap pohon mendapat **sampel data acak dengan pengembalian (*bootstrap*)** sehingga menyisakan sekitar `36,8%` data tidak terpilih (*Out-of-Bag* / **OOB**) untuk uji galat internal. | Hlm. 19, 44, 61 |
| ***Gini Impurity*** | Metrik pengukur "ketidakmurnian" di dalam satu kotak kelompok data saat pohon bercabang (`criterion='gini'`). Pohon memilih batas fitur yang paling efektif membuat isi cabang menjadi murni (dominan `1` semua atau `0` semua). | Hlm. 45, 61 |
| **`max_features = 'sqrt'`** | Aturan bahwa di setiap percabangan pohon, model hanya mengacak **$\lfloor \sqrt{13} \rfloor = 3$ fitur** dari 13 fitur. Tujuannya membuat 200 pohon tidak kembar (***de-correlating trees***) dan mengurangi varians (***variance reduction***). | Hlm. 45, 61 |
| **`max_depth`** & **`min_samples_split`** | Hiperparameter pengatur pertumbuhan pohon (`max_depth=None` membiarkan pohon tumbuh penuh hingga dihentikan batas minimum sampel per cabang). | Hlm. 62 |
| ***Overfitting*** | Kondisi model "menghafal" data latih (termasuk *noise*-nya) sehingga nilainya tinggi di latihan tetapi hancur saat diuji di data baru. | Hlm. 19, 24, 45 |
| ***Noise*** (Derau) | Gangguan acak pada angka piksel citra (sisa kabut tipis, riak air, bayangan) yang dapat mengecoh model klasifikasi. | Hlm. 19, 45 |
| **`predict_proba`** ($P_{ML}$) | Fungsi di `Scikit-Learn` yang mengeluarkan **probabilitas kontinu `0,00`–`1,00`** (proporsi suara pohon yang memilih Mangrove, Persamaan 2.7) alih-alih sekadar label `0`/`1`. Menjadi input utama CA-Markov. | Hlm. 39, 45 |
| **MDI** (*Mean Decrease Impurity*) | Metrik **Feature Importance** bawaan Random Forest: mengukur fitur mana yang paling besar menurunkan *Gini Impurity* di seluruh 200 pohon—digunakan untuk membuktikan peran dominan **NDMI**. | Hlm. 45 |
| ***GridSearchCV*** (*Hyperparameter Tuning*) | Proses mencoba berbagai kombinasi pengaturan model (*hyperparameter*) secara otomatis dengan validasi silang (*Cross-Validation*) untuk mencari kombinasi terbaik. | Hlm. 38, 54 |
| ***Ground Truth*** | Data acuan kebenaran lapangan (*label `1`/`0`* yang digambar manual di **QGIS** berpanduan ortofoto VHR Google Earth Pro & Esri Wayback 2023). | Hlm. 5, 22, 26, 70 |
| ***Spatial Autocorrelation*** | Sifat data geospasial bahwa **piksel yang berdekatan hampir pasti punya nilai dan kelas yang mirip**. | Hlm. 23 |
| ***Spatial Data Leakage*** | Kebocoran data spasial: terjadi jika piksel dari poligon yang sama dipecah acak ke data latih dan data uji. Model seolah-olah mendapat akurasi tinggi karena "menyontek piksel tetangganya". | Hlm. 22, 23, 26, 53 |
| ***5-Fold Stratified Group K-Fold Cross-Validation*** | Protokol validasi silang 5 lipatan (*fold*) yang mengunci pengelompokan **`poly_id`** (**Group** = 1 poligon utuh wajib masuk ke kamar latih ATAU kamar uji saja, mencegah *leakage*) sambil menjaga proporsi kelas mangrove vs non-mangrove tetap seimbang (**Stratified**). | Hlm. 22, 26, 53, 70 |
| ***Confusion Matrix*** | Tabel $2\times 2$ pembanding tebakan model vs kenyataan (`TP, TN, FP, FN`) untuk menghitung `OA`, `PA`, `UA`, `F1-Score`, dan `Kappa`. | Hlm. 38, 47 |
| **OA** (*Overall Accuracy*) | Persentase total piksel yang ditebak benar secara keseluruhan (Persamaan 2.12). Target TA Anda: **$\ge 80\%$**. | Hlm. 13, 47 |
| **PA** (*Producer's Accuracy*) & **UA** (*User's Accuracy*) | • **PA:** Seberapa lengkap objek asli di lapangan berhasil terpetakan (kebalikan kesalahan **Omisi** / lupa terdeteksi).<br>• **UA:** Seberapa dapat dipercaya hasil peta saat dicek ke lapangan (kebalikan kesalahan **Komisi** / salah tuduh). | Hlm. 13 |
| **Cohen's Kappa ($\kappa$)** | Ukuran kesepakatan klasifikasi yang sudah **dikurangi faktor kebetulan acak** (Landis & Koch, 1977; Persamaan 2.13). Target Anda: **$\ge 0{,}70$** (kategori *substantial*). | Hlm. 13, 47, 62 |
| ***F1-Score*** | Rata-rata harmonik antara *Precision* dan *Recall* khusus kelas Mangrove (Persamaan 2.14). Lebih jujur daripada OA saat jumlah piksel non-mangrove jauh lebih luas. Target Anda: **$\ge 0{,}80$**. | Hlm. 13, 47–48 |
| ***Error-Adjusted Area Estimation*** | Estimasi luas area bebas bias menggunakan 100 titik uji acak berstrata + bobot proporsi peta beserta selang kepercayaan 95% mengacu pada protokol **Olofsson dkk. (2014)**. | Hlm. 13, 23, 48 |
| **Pembanding Tabel 2.1** (`CART`, `SVM`, `XGBoost`, `KNN`, `CNN`, `ANN-CA`, `AMMI`, `GMW`, `UAV`) | Algoritma/sistem dari penelitian terdahulu yang dianalisis celahnya: *Classification and Regression Tree* (`CART`), *Support Vector Machine* (`SVM`), *Extreme Gradient Boosting* (`XGBoost`), *K-Nearest Neighbors* (`KNN`), *Convolutional Neural Network* (`CNN`), *Artificial Neural Network* (`ANN-CA`), *Automatic Mangrove Map and Index* (`AMMI`), *Global Mangrove Watch* (`GMW`), dan drone (*UAV*). | Hlm. 32–37 |

---

## 5. Pemodelan Spasio-Temporal (`CA-Markov`) & Validasi Proyeksi

| Istilah Asing / Akronim | Arti & Analisis Mendalam | Lokasi di PDF |
| :--- | :--- | :--- |
| ***Spatio-Temporal*** | Analisis yang menggabungkan dimensi **ruang/lokasi** (*spatial*) dan **waktu/deret tahun** (*temporal*, 2023–2026 $\rightarrow$ 2027). | Hlm. 5, 18, 46 |
| ***Markov Chain*** (Rantai Markov) | Model probabilistik yang menghitung **Matriks Probabilitas Transisi ($P_{ij}$)** dari peta dua tahun berurutan untuk mengestimasi **berapa banyak (kuota)** piksel yang berubah ($N_{trans}$). Bersifat non-spasial (tahu jumlahnya, belum tahu lokasinya). | Hlm. 46 |
| ***Cellular Automata* (CA)** | Model grid seluler di mana keadaan setiap sel piksel pada waktu berikutnya dipengaruhi oleh aturan transisi dan kondisi tetangganya (*bottom-up*). Menentukan **di mana** kuota Markov ditempatkan. | Hlm. 46, 63 |
| **TPM** (*Transition Potential Map*) | Peta Potensi Transisi (skor $S_{gain}$ & $S_{loss}$ di Persamaan 2.10–2.11) yang memeringkat piksel mana yang paling siap bertumbuh atau paling rentan hilang. | Hlm. 46, 51, 55 |
| ***Spatial Drivers*** | Variabel biofisik pendorong perubahan spasial pada TPM Anda: probabilitas **$P_{ML}$**, laju **$\Delta NDMI$**, laju **$\Delta NDVI$**, dan rasio tetangga **$N_{CA}$**. | Hlm. 20, 23, 46 |
| ***Moore Neighborhood 3×3*** ($N_{CA}$) | Pola ketetanggaan 8 sel yang mengelilingi 1 sel pusat dalam kotak $3\times 3$ (Persamaan 2.9). Menerapkan **Hukum Pertama Geografi Tobler (1970)** bahwa objek berdekatan lebih saling berkaitan. | Hlm. 12, 39, 46, 63 |
| ***Noise Floor Filtering*** & ***Connected Component Labeling*** | Operasi morfologi citra yang mengelompokkan piksel bertetangga yang terhubung, lalu membuang bercak terisolasi berukuran $< 4$ piksel agar hasil peta tidak berbintik-bintik. | Hlm. 22, 47, 54 |
| **MMU** (*Minimum Mapping Unit*) | Batas luas minimal agar sebuah bercak poligon dianggap sah. Di proposal Anda **`MMU = 0,04 ha`** = setara **4 piksel** ($4 \times 10\text{ m} \times 10\text{ m}$). | Hlm. 13, 22, 47, 54 |
| ***Hindcasting*** | Uji validasi memprediksi masa lalu yang datanya sudah ada: memakai peta `2023–2024` untuk memproyeksikan `2025`, lalu hasilnya dicocokkan dengan peta klasifikasi riil `2025`. | Hlm. 20, 27, 48, 55 |
| **FoM** (*Figure of Merit*) | Metrik evaluasi proyeksi perubahan lahan (Pontius dkk., 2008; Persamaan 2.15) yang fokus mengukur ketepatan lokasi piksel berubah: **$B / (A + B + C + D)$**.<br>• **$A$ (*Misses*):** Nyatanya berubah, diprediksi diam.<br>• **$B$ (*Hits*):** Nyatanya berubah, diprediksi berubah tepat.<br>• **$C$ (*Wrong Change*):** Salah jenis perubahan (`0` pada biner).<br>• **$D$ (*False Alarms*):** Nyatanya diam, diprediksi berubah. | Hlm. 13, 27, 48, 55 |
| **QD** (*Quantity Disagreement*) & **AD** (*Allocation Disagreement*) | Dekomposisi total kesalahan peta proyeksi:<br>• **QD:** Salah menebak *jumlah total luas* yang berubah.<br>• **AD:** Jumlah luasnya benar, tetapi *salah menaruh lokasinya* di peta. | Hlm. 12–13, 48, 55 |
| ***Null Random Model*** / ***Monte Carlo Simulation*** | Pembanding dasar (*baseline*) di mana kuota piksel perubahan yang sama dilempar **secara acak** diulang **100 kali**. Model CA-Markov Anda wajib menghasilkan $FoM_{CA-Markov} > FoM_{Random}$ pada selang kepercayaan **95% CI**. | Hlm. 20, 48, 55 |
| ***Proof of Concept*** | Bukti konsep — proyeksi tahun **2027** diposisikan sebagai bukti kelayakan metodologis model spasio-temporal apabila kondisi tren historis berlanjut. | Hlm. 20, 22, 27, 55 |

---

## 6. Geospasial, Sistem Koordinat & Pustaka Python

| Istilah Asing / Pustaka | Arti & Analisis Mendalam | Lokasi di PDF |
| :--- | :--- | :--- |
| **UTM Zona 50S (`EPSG:32750`)** | Sistem koordinat **planar/datar bersatuan meter** untuk wilayah Kalimantan Timur. **Wajib** dipakai saat menghitung luas hektar dan jarak spasial agar tidak meleset akibat kelengkungan bumi. | Hlm. 26, 38, 53, 56 |
| **WGS84 (`EPSG:4326`)** | Sistem koordinat geografis **derajat Lintang & Bujur (*Lat/Lon*)** standar GPS dan web. Wajib dipakai saat mengekspor data ke **GeoJSON (RFC 7946)** dan menampilkannya di **Leaflet.js**. | Hlm. 39, 41, 56 |
| ***Bounding Box*** | Kotak pembatas koordinat minimum–maksimum (Utara, Selatan, Timur, Barat) yang memotong citra satelit hanya pada area Kariangau agar komputasi cepat. | Hlm. 38 |
| ***Vector Polygonization*** | Proses mengubah raster klasifikasi (kotak-kotak piksel `1`/`0`) menjadi poligon vektor bermata koordinat dengan batas garis tegas. | Hlm. 39 |
| ***Exploded Polygons*** | Menyimpan setiap bercak mangrove sebagai **1 baris poligon mandiri** (bukan digabung menjadi satu `MultiPolygon` raksasa), sehingga saat pengguna mengklik satu bercak di web, popup langsung menampilkan luas & ID khusus bercak itu. | Hlm. 41, 55 |
| ***Centroid*** | Titik tengah geometris sebuah poligon (disimpan sebagai atribut agar peta mudah memusatkan tampilan atau menaruh penanda). | Hlm. 41 |
| **GeoJSON (`RFC 7946`)** | Standar terbuka berbasis JSON (Butler dkk., 2016) untuk pertukaran data geometri vektor (`Polygon`, `FeatureCollection`) dan atributnya di web. | Hlm. 39, 56 |
| **`PySTAC-Client`, `Rasterio`, `GDAL`** | Pustaka Python untuk mencari & mengunduh citra dari katalog STAC (`PySTAC-Client`) serta membaca, memotong, me-*resample*, dan menulis file raster GeoTIFF (`Rasterio` & `GDAL`). | Hlm. 38 |
| **`NumPy`, `SciPy`, `Scikit-Learn`, `GeoPandas`, `Shapely`** | `NumPy/SciPy` untuk operasi matriks & konvolusi Moore $3\times 3$; `Scikit-Learn` untuk Random Forest & metrik akurasi; `GeoPandas/Shapely` untuk manipulasi poligon, reproyeksi koordinat, dan ekspor GeoJSON. | Hlm. 38–39 |
| **QGIS** | Perangkat lunak GIS *desktop open-source* yang Anda gunakan di tahap awal untuk mendelineasi poligon *ground truth* di atas citra VHR. | Hlm. 17, 33, 51, 70 |

---

## 7. Arsitektur WebGIS, Basis Data Spasial & API

| Istilah Asing / Akronim | Arti & Analisis Mendalam | Lokasi di PDF |
| :--- | :--- | :--- |
| **WebGIS** | Sistem Informasi Geografis berbasis peramban web agar pengelola non-teknis dapat melihat peta dan data tanpa menginstal QGIS/ArcGIS. | Hlm. 18, 24, 40–41 |
| ***Open-Source* vs *Proprietary SaaS*** | *Open-source* = perangkat lunak terbuka bebas biaya lisensi (Python, PostGIS, Next.js, Leaflet); *Proprietary SaaS* = layanan komersial berbayar/tertutup seperti ArcGIS Online (Sunkur dkk., 2024). | Hlm. 24, 36, 38 |
| **GEE** (*Google Earth Engine*) | Platform komputasi awan milik Google. Banyak dipakai penelitian terdahulu, tetapi Anda hindari agar *pipeline* pengolahan data tetap mandiri secara lokal/Google Colab Python tanpa bergantung pada *cloud* tertutup. | Hlm. 16, 18, 32–33 |
| **SIGMEM**, **GeoServer** & **JVM** | **SIGMEM** adalah sistem WebGIS mangrove Kuba (Valero-Jorge dkk., 2024) yang memakai server peta **GeoServer** berbasis **JVM** (*Java Virtual Machine*, butuh RAM besar 4–8 GB). Di TA Anda (versi revisi 2-Tier), fungsi GeoServer digantikan secara lebih ringan oleh kueri `ST_AsGeoJSON` PostGIS + **Next.js API Routes** *(di `(8).pdf` sebelum revisi masih menyebut FastAPI)*. | Hlm. 18–19, 32, 42 |
| ***2-Tier Architecture* & *Offline Processing*** | Pemisahan pemrosesan analitik ML (*offline* di Google Colab) dari sistem WebGIS *online* yang disederhanakan menjadi **2 lapis (*2-Tier*)**: **Tier 1 (Data Tier)** pada PostgreSQL/PostGIS Cloud dan **Tier 2 (Presentation Tier)** pada Next.js 15 + API Routes + Leaflet.js di Vercel *(di `(8).pdf` sebelum revisi masih memakai istilah 4-Tier / Headless)*. | Hlm. 18, 24, 41, 49 |
| ***Presentation Layer*** | Lapisan antarmuka (**Tier 2**) yang fungsinya **murni menyajikan visualisasi data** (bukan mengolah ML atau memproses raster di browser), sehingga mencegah *bottleneck* dan sesuai **Batasan ke-9**. | Hlm. 5, 20, 22, 40, 51, 65 |
| ***Software Stack*** | Tumpukan teknologi perangkat lunak yang saling terhubung dari hulu (*pipeline* data) ke hilir (*frontend* web). | Hlm. 38 |
| **PostgreSQL & PostGIS** | Sistem basis data relasional (*PostgreSQL v17.6*) yang ditambah ekstensi geospasial (**PostGIS v3.5.2**) berstandar **OGC** (*Open Geospatial Consortium*) untuk menyimpan tipe kolom `GEOMETRY(Polygon, 4326)` sebagai **Tier 1 (Data Tier)** pada layanan Cloud (Supabase/Neon). | Hlm. 41, 64–65 |
| **GiST** (*Generalized Search Tree*) & $\mathcal{O}(\log N)$ | Indeks spasial berbasis struktur pohon **R-Tree** di PostGIS. Mengelompokkan poligon ke dalam kotak pembatas agar pencarian lokasi klik pengguna berjalan instan dalam waktu logaritmik $\mathcal{O}(\log N)$ tanpa memindai seluruh tabel. | Hlm. 42, 56, 65 |
| **`ST_AsGeoJSON`** | Fungsi SQL bawaan PostGIS untuk langsung mengubah kolom geometri biner menjadi teks **GeoJSON** agar siap dikirim oleh API Routes ke browser. | Hlm. 42 |
| **Next.js API Routes & `read-only HTTP GET`** | Rute API bawaan **Next.js 15** (dijalankan di **Vercel**) yang menyalurkan permintaan **`read-only HTTP GET`** (hanya baca, tanpa ubah data) langsung ke PostgreSQL/PostGIS tanpa server *backend* terpisah *(di `(8).pdf` sebelum revisi masih menyebut Python FastAPI + Uvicorn ASGI)*. | Hlm. 39, 56, 65 |
| ***HTTP Gzip Compression*** | Teknik memampatkan ukuran teks GeoJSON sebelum dikirim lewat jaringan untuk mengatasi ukuran berkas GeoJSON yang besar (Horbiński & Lorek, 2020) agar peta cepat termuat. | Hlm. 39–40, 56, 65 |
| ***Bottleneck*** | Titik penyempitan kinerja yang membuat sistem lambat (misal jika browser/server web dipaksa menjalankan pelatihan ML saat pengguna membuka peta). | Hlm. 40 |
| **Next.js, Leaflet.js (`L.geoJSON`) & `Page Reload`** | **Next.js** (berbasis komponen React) mengatur antarmuka dinamis tanpa memuat ulang halaman (*page reload*), sedangkan **Leaflet.js** merender poligon GeoJSON ke kanvas peta interaktif di atas ubin peta dasar (**OSM** / Satelit via **Basemap Switcher**) lengkap dengan **Popup Modal** saat poligon diklik. | Hlm. 40–41, 65 |

---

> [!TIP]
> **Cara Efektif Mempelajari Dokumen Ini Sebelum Sidang Sempro:**
> 1. Hafalkan **5 istilah "Bintang Utama"** yang paling sering ditanya penguji: **`BOA_ADD_OFFSET = -1000`**, **`NDMI` (SWIR)**, **`Stratified Group K-Fold` (`poly_id`)**, **`predict_proba` ($P_{ML}$)**, dan **`Hindcasting FoM vs Monte Carlo`**.
> 2. Untuk istilah teknis web (**`PostGIS GiST`**, **`ST_AsGeoJSON`**, **`Gzip`**, **`Presentation Layer`**), gunakan keunggulan Anda sebagai mahasiswa Sistem Informasi dengan menjelaskan bahwa semua desain itu dibuat agar **ringan, cepat, dan aman** tanpa perlu server GeoServer yang berat.
