# PANDUAN BELAJAR LENGKAP 7 HARI: PROPOSAL TUGAS AKHIR (ACUAN FINAL PDF V8)

> **Dokumen Acuan Tunggal:** `Proposal TA Achmad Zaki Zaidan (8).pdf` (80 Halaman PDF / 66 Halaman Naskah)  
> **Judul Proposal:** *Proyeksi Perubahan Tutupan Lahan Mangrove Berbasis Machine Learning Terintegrasi Sistem WebGIS*  
> **Penyusun:** Achmad Zaki Zaidan (NIM 10231002) — Program Studi Sistem Informasi, ITK  
> **Dosen Pembimbing:**  
> 1. Arif Wicaksono Septyanto, M.Kom. (Pembimbing Utama)  
> 2. Ir. Bimo Aji Widyantoro, S.T., M.Eng. (Pembimbing Pendamping)  
> **Pendekatan Belajar:** Dirancang khusus untuk **Mahasiswa Sistem Informasi (Web Developer)** — menjelaskan konsep *Penginderaan Jauh* dan *Machine Learning* dari dasar menggunakan analogi *Database SQL, JSON, dan Pemrograman Web*, lengkap dengan bedah tahapan dan **15 Rumus Matematis (Persamaan 2.1 s.d. 2.15)**.

---

## DAFTAR ISI PANDUAN BELAJAR

1. [Hasil Pemeriksaan PDF Final `(8).pdf` vs `ta_proyek.md`](#-1-hasil-pemeriksaan-pdf-final-8pdf-vs-ta_proyekmd)
2. [Peta Struktur Dokumen PDF Final Anda (Halaman demi Halaman)](#-2-peta-struktur-dokumen-pdf-final-anda-halaman-demi-halaman)
3. [Fondasi Paling Dasar: Kamus Analogi Anak Web & Sistem Informasi](#-3-fondasi-paling-dasar-kamus-analogi-anak-web--sistem-informasi)
4. [Bedah Alur 8 Tahap Kerangka Penelitian (Bab 1.6) & 4 Tahap Teknis (Bab 3.3)](#-4-bedah-alur-8-tahap-kerangka-penelitian-bab-16--4-tahap-teknis-bab-33)
5. [Bedah Tuntas Seluruh 15 Rumus (Persamaan 2.1 s.d. 2.15) dengan Contoh Angka](#-5-bedah-tuntas-seluruh-15-rumus-persamaan-21-sd-215-dengan-contoh-angka)
6. [Bedah Arsitektur Sistem 4-Tier & Database WebGIS (Bab 2.3 & Bab 3.4.5)](#-6-bedah-arsitektur-sistem-4-tier--database-webgis-bab-23--bab-345)
7. [Metode & Kurikulum Belajar 7 Hari (1 Minggu Menguasai Seluruh Proposal)](#-7-metode--kurikulum-belajar-7-hari-1-minggu-menguasai-seluruh-proposal)
8. [Bank Simulasi Tanya-Jawab Dosen Penguji Sempro (Beserta Jawaban Kunci)](#-8-bank-simulasi-tanya-jawab-dosen-penguji-sempro-beserta-jawaban-kunci)

---

## 🔍 1. Hasil Pemeriksaan PDF Final `(8).pdf` vs `ta_proyek.md`

Berdasarkan pemeriksaan menyeluruh terhadap berkas **`Proposal TA Achmad Zaki Zaidan (8).pdf`**, berikut adalah status validasi dan perbedaan antara PDF Final Anda dengan berkas lama `ta_proyek.md`:

### A. Status Daftar Pustaka di PDF Final `(8).pdf`: **100% COCOK & TERPAKAI**
- Seluruh **39 referensi** yang tercetak pada **Daftar Pustaka (Hal. 74–79 PDF / Hal. 60–65 dokumen)** kini **100% terpakai di dalam teks tubuh proposal**.
- Empat jurnal CA-Markov (**Subedi dkk., 2013; Hamad dkk., 2018; Guan dkk., 2019; Wang dkk., 2021**) sudah masuk dengan tepat di **Sub-bab 2.4.4 (Hal. 46 PDF / Hal. 32 dokumen)**.
- Tiga referensi yang sebelumnya tidak terpakai (`Agafonkin 2023`, `Chen & Guestrin 2016`, `Cortes & Vapnik 1995`) sudah bersih dari Daftar Pustaka.

### B. Daftar Perbedaan antara PDF Final `(8).pdf` dan `ta_proyek.md` (Acuan Kita Sekarang Adalah PDF Final `(8).pdf`)
1. **Struktur Bab (3 Bab Proposal Murni):** PDF Final `(8).pdf` terdiri atas **BAB 1 (Pendahuluan)**, **BAB 2 (Metodologi)**, dan **BAB 3 (Rancangan Proyek)**, tanpa Bab 4 yang ada di `ta_proyek.md`.
2. **Latar Belakang Pemilihan Random Forest (Bab 1.1, Hal. 19 PDF):** Di PDF Final `(8).pdf`, alasan pemilihan *Random Forest* langsung berfokus pada keunggulan *ensemble bagging* (Breiman, 2001), ketahanan terhadap *overfitting* dan multikolinearitas (Simarmata dkk., 2024), serta preseden keberhasilan sistem WebGIS mangrove **SIGMEM di Kuba (Valero-Jorge dkk., 2024)** yang mencapai OA 94,11% dan Kappa 0,94.
3. **Sumber Data Pasang Surut Tunggal (Pushidrosal, 2024):** Di PDF Final `(8).pdf` (Hal. 21, 43, 52, 58, 64, 66 PDF), verifikasi pasang surut ($\le 1{,}5\text{ m}$ LAT) mengacu tunggal pada **Tabel Pasang Surut Stasiun Teluk Balikpapan dari Pusat Hidro-Oseanografi TNI Angkatan Laut (Pushidrosal, 2024)** (tidak lagi menyebut BIG).
4. **Sub-bab 2.2 Penelitian Terdahulu (Hal. 32–37 PDF):** Hanya menggunakan **Tabel 2.1 Penelitian Terdahulu (10 Jurnal)** tanpa Tabel 2.2 Matriks Keputusan.
5. **Akhir Bab 2 (Hal. 48 PDF):** Bab 2 berakhir langsung pada **Sub-bab 2.4.5 Metrik Evaluasi Kinerja Model Klasifikasi & Validasi Spasial** (tanpa Sub-bab 2.5 Standar Regulasi).
6. **Sub-bab 3.4 Konseptual Proyek (Hal. 57–65 PDF):** Terdiri atas 5 sub-bagian (`3.4.1 Dataset Sentinel-2`, `3.4.2 Atribut Fitur Spektral`, `3.4.3 Konseptual Random Forest`, `3.4.4 Konseptual CA-Markov`, dan `3.4.5 Konseptual Arsitektur 4-Tier WebGIS`), di mana tabel kaku 78 poligon sudah dihapus sepenuhnya sesuai revisi proposal.

> **Catatan Kecil pada PDF `(8).pdf` untuk Anda Ketahui Saat Sidang:**
> - Pada **Daftar Isi (Hal. 7 PDF)**, baris `2.3 Teknologi` belum tercantum di antara `2.2 Penelitian Terdahulu` dan `2.4 Metode` (meskipun isi **Sub-bab 2.3 Teknologi** ada lengkap di **Hal. 38–42 PDF / Hal. 24–27 dokumen**).
> - Pada **Tabel 3.2 (Hal. 59–60 PDF)**, baris tabel yang tercetak baru nomor `1 s.d. 7` (`B02 s.d. B11`), sedangkan `B12` dan 5 indeks (`NDVI, EVI, NDWI, NDMI, RDVI`) sudah tertulis lengkap di **Sub-bab 2.4.2 (Hal. 43–44 PDF)** dan **Sub-bab 3.3.1 (Hal. 53 PDF)**.

---

## 🗺️ 2. Peta Struktur Dokumen PDF Final Anda (Halaman demi Halaman)

Gunakan peta ini saat membuka `Proposal TA Achmad Zaki Zaidan (8).pdf` agar Anda bisa langsung melompat ke halaman yang tepat:

| Bagian / Sub-bab di PDF Final `(8).pdf` | Hal. PDF | Hal. Naskah | Inti Isi yang Wajib Anda Kuasai |
| :--- | :---: | :---: | :--- |
| **Abstrak & Abstract** | 5–6 | ii–iii | Ringkasan masalah Kariangau, data Sentinel-2 (2023–2026), 13 fitur (NDMI kunci), RF 200 pohon, CA-Markov 2027, dan WebGIS *presentation layer*. |
| **Daftar Notasi** | 11–14 | vii–x | Kamus seluruh simbol rumus ($\rho, DN, NDVI, NDMI, P_{ML}, N_{CA}, S_{gain}, S_{loss}, P_{ij}, FoM, OA, \kappa, F1, MMU$). |
| **BAB 1 PENDAHULUAN** | **15–28** | **1–14** | |
| — `1.1 Latar Belakang` | 15–19 | 1–5 | Fungsi mangrove, ancaman KIK & tongkang IKN, 4 kendala pemantauan di Kariangau, *gap* riset terdahulu, solusi 3 komponen, alasan pilih *Random Forest*. |
| — `1.2 Rumusan Masalah` & `1.3 Tujuan` | 19–20 | 5–6 | **4 Rumusan Masalah (RM-1 s.d. RM-4)** dan **4 Tujuan** yang saling berpasangan 1-lawan-1. |
| — `1.4 Batasan Proyek` | 21–22 | 7–8 | **9 Batasan Proyek** (lokasi Kariangau, Sentinel-2 L2A 2023–2026, Juli–Sept & pasut $\le 1{,}5\text{ m}$, offset `-1000` & 13 fitur, kelas biner `1`/`0`, *ground truth* VHR 2023, RF 200 pohon + *Group K-Fold* `poly_id`, CA-Markov MMU 0,04 ha + *hindcasting* 2025 $\rightarrow$ 2027, WebGIS murni *presentation layer*). |
| — `1.5 Relevansi Industri/Akademik` | 22–24 | 8–10 | Kontribusi akademik (NDMI atasi kebingungan NDVI, anti-*leakage* `poly_id`, $P_{ML}$ di CA-Markov) & praktis (pantau dampak KIK & logistik IKN tanpa lisensi GIS berbayar). |
| — `1.6 Kerangka Penelitian` | 25–28 | 11–14 | **Gambar 1.1 Flowchart Kerangka TA** (8 Tahap dari Identifikasi Masalah sampai Kesimpulan). |
| **BAB 2 METODOLOGI** | **29–48** | **15–34** | |
| — `2.1 Domain Penelitian` | 29–30 | 15–16 | Lokasi Kariangau, spesies mangrove (*Rhizophora, Avicennia, Sonneratia, Nypa*), habitat bekantan & pesut, 3 ancaman utama (KIK, logistik IKN, pantauan titian kayu). |
| — `2.2 Penelitian Terdahulu` | 32–37 | 18–23 | **Tabel 2.1 (10 Jurnal)** dari Valero-Jorge (2024) hingga Bunting (2022) beserta kelemahan masing-masing yang disempurnakan oleh TA Anda. |
| — `2.3 Teknologi` (`2.3.1` s.d. `2.3.4`) | 38–42 | 24–27 | Narasi teknologi: Python Data Science (`2.3.1`), FastAPI & GeoJSON (`2.3.2`), Next.js & Leaflet.js (`2.3.3`), serta Arsitektur 4-Tier & PostGIS GiST (`2.3.4`). |
| — `2.4 Metode` (`2.4.1` s.d. `2.4.5`) | 42–48 | 28–34 | **Tempat seluruh 15 Rumus berada!** Koreksi BOA (`Pers. 2.1`), 5 Indeks Spektral (`Pers. 2.2–2.6`), Random Forest (`Pers. 2.7`), CA-Markov (`Pers. 2.8–2.11`), Evaluasi Akurasi & FoM (`Pers. 2.12–2.15`). |
| **BAB 3 RANCANGAN PROYEK** | **49–73** | **35–59** | |
| — `3.1 Garis Besar` & `3.2 Flowchart` | 49–51 | 35–37 | Ringkasan eksekutif proyek & **Gambar 3.1 Flowchart Teknis Pembuatan Prototipe**. |
| — `3.3 Prosedur` (`3.3.1` s.d. `3.3.4`) | 51–56 | 37–42 | Langkah kerja teknis **Tahap 1** (Pra-pemrosesan), **Tahap 2** (Ground Truth & RF), **Tahap 3** (CA-Markov & Hindcasting), **Tahap 4** (PostGIS, FastAPI, Leaflet). |
| — `3.4 Konseptual Proyek` (`3.4.1`–`3.4.5`) | 57–65 | 43–51 | Spesifikasi dataset (**Tabel 3.1**), fitur spektral (**Tabel 3.2**), hiperparameter RF (**Tabel 3.3**), variabel CA-Markov (**Tabel 3.5**), & **Gambar 3.2 Arsitektur 4-Tier WebGIS**. |
| — `3.5 Sumber Daya` & `3.6 Jadwal` | 66–73 | 52–59 | SDM, 5 material data, spesifikasi laptop Intel Core i7-14650HX (**Tabel 3.5**), & Jadwal proyek (**Tabel 3.8**). |

---

## 💡 3. Fondasi Paling Dasar: Kamus Analogi Anak Web & Sistem Informasi

Karena Anda berlatar belakang Sistem Informasi dan terbiasa membuat *website*, jangan membayangkan *Machine Learning* dan *Penginderaan Jauh* sebagai sesuatu yang asing. Gunakan **6 jembatan logika** ini:

### 1. Citra Satelit Raster = Tabel HTML / Spreadsheet Raksasa
- Saat Anda mendengar kata **"Citra Raster Sentinel-2 Resolusi 10 meter"**, bayangkan sebuah tabel `<table border="1">` raksasa yang digelar menutupi Kawasan Wisata Mangrove Kariangau.
- Setiap **1 kotak sel (`<td>`)** di tabel itu disebut **1 Piksel**, dan ukurannya di dunia nyata adalah **$10 \text{ meter} \times 10 \text{ meter} = 100 \text{ m}^2 = 0{,}01 \text{ hektar}$**.
- Jadi kalau di proposal tertulis **"Minimum Mapping Unit (MMU) 0,04 ha (4 piksel)"**, artinya sebuah poligon mangrove baru dianggap sah kalau minimal terdiri dari **4 kotak piksel yang saling menempel** ($4 \times 0{,}01 \text{ ha} = 0{,}04 \text{ ha}$). Kalau ada 1 piksel sendirian di tengah air, itu cuma *noise* (bintik salah tebak) dan langsung dihapus.

### 2. Band Spektral & 13 Fitur = 13 Kolom di Tabel Database SQL
- Foto biasa dari kamera HP hanya menyimpan **3 angka warna** di setiap piksel: `Red`, `Green`, `Blue` (RGB).
- Kamera satelit Sentinel-2 (*MultiSpectral Instrument* / MSI) menyimpan **8 angka saluran cahaya (8 Band BOA)** di setiap piksel:
  1. `B02` (Biru - 490 nm) $\rightarrow$ peka terhadap air & hamburan langit.
  2. `B03` (Hijau - 560 nm) $\rightarrow$ memantulkan warna hijau daun & air dangkal.
  3. `B04` (Merah - 665 nm) $\rightarrow$ **diserap habis oleh klorofil daun** untuk fotosintesis.
  4. `B05` (*Red Edge 1* - 705 nm) $\rightarrow$ batas transisi tajam antara merah dan inframerah; peka stres tanaman.
  5. `B08` (*Near-Infrared* / NIR Lebar - 842 nm) $\rightarrow$ **dipantulkan sangat kuat oleh jaringan sel daun yang sehat/tebal**.
  6. `B8A` (*Narrow NIR* - 865 nm) $\rightarrow$ inframerah dekat sempit yang bebas gangguan uap air.
  7. `B11` (*Short-Wave Infrared 1* / SWIR-1 - 1610 nm) $\rightarrow$ **diserap sangat kuat oleh air dan lumpur basah**!
  8. `B12` (*Short-Wave Infrared 2* / SWIR-2 - 2190 nm) $\rightarrow$ peka terhadap kelembapan tajuk dan lumpur organik pesisir.
- Dari 8 kolom asli itu, kita membuat **5 kolom rumus tambahan (*computed columns*)**: `NDVI`, `EVI`, `NDWI`, `NDMI`, dan `RDVI`.
- **Analogi Database:** Bayangkan Anda punya tabel SQL bernama `piksel_kariangau`. Setiap baris (`row`) adalah 1 kotak $10\times 10\text{ m}$, dan baris tersebut punya **13 kolom angka (`8 Band + 5 Indeks = 13 Fitur`)**!

### 3. Kenapa `NDVI` Bisa Tertipu dan Kenapa `NDMI` Jadi Pahlawan?
Ini adalah **pertanyaan nomor 1 yang paling sering ditanyakan dosen penguji** dari Bab 1 dan Bab 2:
- **Masalah di Kariangau:** Di belakang hutan mangrove Kariangau, terdapat **hutan darat perbukitan** (pohon karet, akasia, semak belukar bukit).
- Kalau kita hanya memakai indeks kehijauan daun standar (**`NDVI`**), baik **pohon mangrove** maupun **pohon hutan bukit** sama-sama berdaun hijau lebat! Akibatnya, nilai `NDVI` keduanya hampir kembar ($\approx 0{,}75 - 0{,}80$). Ini yang di proposal disebut **kerancuan spektral (*spectral confusion*)**.
- **Solusi di Proposal Anda (`NDMI`):**
  - Pohon mangrove tumbuh di **zona pasang surut berlumpur basah** dan daunnya tebal menyimpan air (*sukulen*), sedangkan pohon hutan bukit tumbuh di **tanah daratan kering**.
  - Sinar **`B11` (SWIR-1)** memiliki sifat fisik **diserap oleh air**.
  - Di area mangrove yang basah, sinar `B11` diserap habis oleh air sehingga pantulan `B11` sangat kecil. Ketika dimasukkan ke rumus **`NDMI = (B08 - B11) / (B08 + B11)`**, nilai `NDMI` mangrove menjadi **tinggi positif ($> +0{,}35$)**, sedangkan hutan darat bukit nilainya **rendah ($< +0{,}15$)**.

### 4. *Spatial Data Leakage* & `poly_id` = Mencegah Contekan Saat Ujian
- Dalam *Machine Learning*, kita membagi data menjadi **Data Latih (*Training*)** untuk belajar dan **Data Uji (*Testing*)** untuk ujian.
- **Bahaya jika dibagi acak per piksel:** Bayangkan ada 1 poligon hutan mangrove berisi 100 piksel yang saling berdempetan. Kalau kita acak per piksel, Piksel A masuk ke *Training* (soal latihan) dan Piksel B yang persis di sebelahnya (jaraknya cuma 10 meter, pohonnya sama!) masuk ke *Testing* (soal ujian).
- Akibatnya, model mendapat nilai akurasi 99% palsu karena **"menyontek tetangga sebelahnya"**! Di bahasa ilmiah, ini disebut **kebocoran data spasial (*spatial data leakage*) akibat autokorelasi spasial**.
- **Solusi di Proposal Anda (`5-Fold Stratified Group K-Fold` berbasis `poly_id`):**
  - Setiap poligon *ground truth* diberi atribut ID kelompok bernama **`poly_id`** (misal `poly_id = 1` s.d. `N`).
  - Saat dibagi menjadi 5 lipatan (*5-Fold*), aturan **`Group K-Fold`** mengunci agar **seluruh piksel yang memiliki `poly_id` yang sama wajib masuk ke kamar yang sama** (kalau `poly_id = 5` masuk ke Data Uji, maka tidak boleh ada satu piksel pun dari `poly_id = 5` di Data Latih!).
  - Kata **`Stratified`** artinya rasio persentase kelas Mangrove (50%) dan Non-Mangrove (50%) dijaga tetap seimbang di setiap lipatan.

### 5. Proyeksi UTM Zona 50S (`EPSG:32750`) vs WGS84 (`EPSG:4326`)
Kenapa di proposal selalu disebut dua kode koordinat ini?
- **`EPSG:32750` (UTM Zona 50S):** Sistem koordinat **bidang datar (planar)** khusus wilayah Kalimantan Timur yang satuannya adalah **Meter ($m$)**. Kita **wajib** memakai ini saat memproses piksel $10\times 10\text{ m}$ dan saat **menghitung luas hektar ($\text{ha}$)**, karena menghitung luas di bidang datar meter persegi jauh lebih akurat daripada di bola bumi yang melengkung.
- **`EPSG:4326` (WGS84):** Sistem koordinat **derajat Lintang & Bujur (*Latitude/Longitude*)** standar GPS dan web. Kita mengubah poligon ke `EPSG:4326` pada tahap paling akhir karena standar internasional **GeoJSON (RFC 7946)** dan pustaka **Leaflet.js** di browser mewajibkan koordinat derajat WGS84.

---

## ⚙️ 4. Bedah Alur 8 Tahap Kerangka Penelitian (Bab 1.6) & 4 Tahap Teknis (Bab 3.3)

Di proposal Anda terdapat dua diagram alir (*flowchart*):
- **Gambar 1.1 (Hal. 25 PDF / Bab 1.6):** Kerangka Penelitian Tugas Akhir dari awal sampai penarikan kesimpulan (**8 Tahap Umum**).
- **Gambar 3.1 (Hal. 50 PDF / Bab 3.2 & 3.3):** Diagram Alir Teknis Pembuatan Sistem (**4 Tahap Teknis Inti**, yang sebenarnya adalah rincian dari Tahap 3, 4, 5, 6, dan 7 pada Gambar 1.1).

Mari kita bedah **4 Tahap Teknis Inti di Bab 3.3 (Hal. 51–56 PDF)** langkah demi langkah:

---

### TAHAP 1: Akuisisi dan Pra-pemrosesan Data Citra Sentinel-2 (13 Fitur)
*(Hal. 51–53 PDF / Sub-bab 3.3.1)*

Tujuan Tahap 1 adalah mengubah citra satelit mentah dari internet menjadi **"Kubus Data Bersih 13 Fitur (*Raster Feature Cube*)"** untuk tahun **2023, 2024, 2025, dan 2026**. Ada **6 langkah berurutan**:

1. **Pencarian & Unduh Citra via API (`pystac-client`):**
   - Mengambil citra **Sentinel-2 Level-2A (L2A)** dari server Eropa **CDSE STAC API** pada kotak wilayah (*Tile* `50MNL`) yang memotong koordinat Kariangau (`01°10'00"–01°13'00" LS` dan `116°48'00"–116°51'00" BT`).
   - Hanya mengambil bulan **Juli–September** (musim kemarau/kering di Balikpapan menurut data **BMKG Sepinggan**) dengan tutupan awan $< 60\%$.
2. **Sinkronisasi Pasang Surut Air Laut (`Pushidrosal, 2024`):**
   - Jam satelit memotret dicocokkan dengan **Tabel Pasang Surut Stasiun Teluk Balikpapan (Pushidrosal, 2024)**.
   - Foto satelit saat air pasang tinggi ($> 1{,}8\text{ m}$ LAT) **dibuang**, dan hanya dipilih saat air surut/sedang (**$\le 1{,}5\text{ m}$ LAT**) supaya akar dan daun mangrove bawah tidak tenggelam oleh air laut.
3. **Koreksi Radiometrik Offset (`BOA_ADD_OFFSET = -1000`):**
   - Menerapkan **Persamaan (2.1)**: $\rho = (DN - 1000) / 10000$ pada semua saluran citra karena citra tahun 2023–2026 memakai *Processing Baseline* $\text{PB} \ge 04.00$.
4. **Penyeragaman Ukuran Piksel (*Resampling* ke 10 meter):**
   - Saluran `B02, B03, B04, B08` sudah berukuran $10\text{ m}$.
   - Saluran `B05, B8A, B11, B12` yang aslinya berukuran $20\text{ m}$ diperkecil kotaknya menjadi **$10\text{ m}$** menggunakan metode **Bilinear** (rata-rata halus 4 piksel terdekat) agar gradasi angka pantulan daunnya mulus.
   - Saluran **SCL (*Scene Classification Layer*)** yang berisi kode angka bulat awan juga diubah dari $20\text{ m}$ ke **$10\text{ m}$**, tetapi wajib memakai metode **Nearest Neighbor** (salin bulat-bulat angka terdekat) agar kode kategori awan (misal kode `3` atau `9`) tidak berubah menjadi angka koma/desimal!
5. **Penapisan Awan (*Cloud Masking* SCL) & Komposit Median (`nanmedian`):**
   - Piksel yang punya kode SCL `9` (awan tebal), `10` (awan tipis sirus), `3` (bayangan awan), serta `0` dan `1` (piksel rusak/tepi kosong) dilubangi/dihapus (*Boolean mask* menjadi `NaN`).
   - Dari kumpulan beberapa citra bersih selama bulan Juli–September di tahun yang sama, dihitung **nilai tengahnya (`nanmedian`)** per piksel, sehingga menghasilkan **1 citra tahunan yang bersih tanpa bolong awan** untuk tahun 2023, 2024, 2025, dan 2026.
6. **Ekstraksi 13 Dimensi Fitur Spektral:**
   - Menghitung 5 indeks (`NDVI, EVI, NDWI, NDMI, RDVI`) dengan **Persamaan (2.2)–(2.6)** dan menggabungkannya dengan 8 band BOA menjadi 13 fitur per piksel pada proyeksi **UTM Zona 50S (`EPSG:32750`)**.

---

### TAHAP 2: Pembuatan Ground Truth, Pelatihan, dan Evaluasi Model Klasifikasi
*(Hal. 53–54 PDF / Sub-bab 3.3.2)*

Tujuan Tahap 2 adalah melatih otak **Random Forest** dan memastikan akurasinya lulus syarat sebelum dipakai memetakan seluruh tahun. Ada **5 langkah berurutan**:

1. **Delineasi *Ground Truth* Terstandar (Baseline 2023):**
   - Menggambar poligon sampel referensi di QGIS pada citra tahun 2023 dengan melihat citra satelit resolusi sangat tajam (*Google Earth Pro Historical Imagery* & *Esri World Imagery Wayback 2023*) serta peta batas KLHK & Kelurahan Kariangau.
   - Mencakup kelas **Mangrove (`1`)** dan **Non-Mangrove (`0`)** (hutan darat bukit, air teluk/muara, lahan terbuka industri KIK, permukiman). Setiap poligon diberi kode unik **`poly_id`**.
2. **Partisi Data dengan `5-Fold Stratified Group K-Fold Cross-Validation`:**
   - Membagi data menjadi 5 lipatan pengujian dengan mengunci kelompok **`poly_id`** (agar piksel dari 1 poligon yang sama tidak bocor menyeberang antara data latih dan data uji).
3. **Pelatihan Model *Random Forest Classifier*:**
   - Melatih model di `scikit-learn` dengan **200 pohon keputusan (`n_estimators = 200`)**, kriteria cabang **`gini` (*Gini Impurity*)**, fitur acak per cabang **`max_features = 'sqrt'`** ($\sqrt{13} \approx 3$ fitur), dan `bootstrap = True`, disertai *tuning* via `GridSearchCV`.
4. **Evaluasi Akurasi Dua Lapis (Gerbang Keputusan):**
   - **Evaluasi Validasi Silang:** Wajib mencapai **$\text{F1-Score} \ge 0{,}80$**, **$\text{Overall Accuracy (OA)} \ge 80\%$**, dan **$\text{Kappa } (\kappa) \ge 0{,}70$** (Persamaan 2.12–2.14). *Jika belum tercapai, alur kembali melakukan re-tuning hiperparameter.*
   - **Validasi Independen Bebas Bias Area (Olofsson dkk., 2014):** Menyebar **100 titik uji acak terstratifikasi** (50 titik di kelas mangrove, 50 titik di kelas non-mangrove) per tahun untuk menghitung estimasi luas hektar bebas bias beserta selang kepercayaan 95% (target standar error $S(\hat{O}) \le 0{,}03$).
5. **Klasifikasi Lanskap 2023–2026 & Ekstraksi Peta Probabilitas ($P_{ML}$):**
   - Model Random Forest terbaik digunakan untuk menebak seluruh piksel di Kariangau pada tahun **2023, 2024, 2025, dan 2026**.
   - Menghasilkan 2 luaran per tahun:
     1. **Peta Klasifikasi Biner** (`1` = Mangrove, `0` = Non-Mangrove).
     2. **Peta Probabilitas $P_{ML}$** (nilai $0{,}00$ s.d. $1{,}00$ dari fungsi `predict_proba`, Persamaan 2.7).

---

### TAHAP 3: Pemodelan Proyeksi Tutupan Lahan (CA-Markov) & Validasi Hindcasting
*(Hal. 54–55 PDF / Sub-bab 3.3.3)*

Tujuan Tahap 3 adalah memprediksi peta tutupan mangrove masa depan (**Tahun 2027**) dan membuktikan secara ilmiah bahwa prediksinya akurat. Ada **4 langkah berurutan**:

1. **Penapisan Derau Spasial (*Minimum Mapping Unit* / MMU 0,04 ha):**
   - Menghapus bintik-bintik poligon yang luasnya **kurang dari 4 piksel ($< 0{,}04\text{ ha}$)** menggunakan *connected component labeling* agar kedipan salah tebak tidak merusak perhitungan matriks transisi.
2. **Kalkulasi Matriks Probabilitas Transisi Markov ($P_{ij}$):**
   - Membandingkan perubahan peta antar-tahun (`2023→2024`, `2024→2025`, `2025→2026`) menggunakan **Persamaan (2.8)** untuk menentukan **kuota jumlah piksel ($N_{trans}$)** yang akan bertambah (*gain*) atau hilang (*loss*).
3. **Penyusunan *Transition Potential Map* (TPM):**
   - Menghitung skor kesesuaian tumbuh mangrove baru (**$S_{gain}$**, Persamaan 2.10) dan skor kerentanan hilang mangrove (**$S_{loss}$**, Persamaan 2.11) di setiap piksel berdasarkan 4 variabel pendorong berbobot sama ($0{,}25$):
     - $P_{ML}$ (keyakinan Random Forest),
     - $\Delta NDMI$ (perubahan kelembapan tajuk),
     - $\Delta NDVI$ (perubahan kehijauan daun),
     - $N_{CA}$ (rasio tetangga mangrove pada kotak **Moore $3 \times 3$**, Persamaan 2.9).
4. **Validasi *Hindcasting* 2025 & Proyeksi *Proof of Concept* 2027:**
   - **Uji *Hindcasting*:** Model diminta memproyeksikan tahun **2025** hanya dengan berbekal data **2023–2024**. Hasil tebakan 2025 itu diadu dengan **peta klasifikasi riil 2025** menggunakan rumus **Figure of Merit (`FoM`, Persamaan 2.15)** serta galat kuantitas (`QD`) dan galat lokasi (`AD`) (Pontius dkk., 2008).
   - **Syarat Lulus:** Nilai $FoM_{\text{CA-Markov}}$ wajib lebih besar daripada nilai $FoM_{\text{Random}}$ dari **100 kali simulasi tebakan acak *Monte Carlo*** pada selang kepercayaan 95%.
   - Setelah dinyatakan valid, model dijalankan pada data terakhir untuk menghasilkan **Peta Proyeksi Tutupan Mangrove Tahun 2027**.

---

### TAHAP 4: Pengembangan Basis Data Spasial dan Sistem WebGIS
*(Hal. 55–56 PDF / Sub-bab 3.3.4)*

Tujuan Tahap 4 adalah menyajikan hasil pemetaan (2023–2026) dan proyeksi (2027) ke dalam **antarmuka WebGIS interaktif sebagai *presentation layer***. Ada **4 langkah berurutan**:

1. **Vektorisasi & Hitung Luas Hektar Riil:**
   - Mengubah piksel raster hasil klasifikasi (2023–2026) dan proyeksi (2027) menjadi poligon vektor terpisah (*exploded polygons*) menggunakan `GeoPandas` dan `GDAL`.
   - Menghitung luas tiap poligon dalam satuan **hektar ($\text{ha}$)** pada proyeksi datar **UTM Zona 50S (`EPSG:32750`)**, lalu mengubah koordinatnya ke **WGS84 (`EPSG:4326`)** sesuai standar **GeoJSON RFC 7946**.
2. **Penyimpanan ke Basis Data Spasial (`PostgreSQL 17 + PostGIS 3.x`):**
   - Memasukkan poligon ke tabel **`klasifikasi_mangrove`** yang dilengkapi indeks spasial **GiST (*Generalized Search Tree*)** berkecepatan $\mathcal{O}(\log N)$, serta menyimpan rekapitulasi tahunan ke tabel **`statistik_luas`**.
3. **Pembuatan *Backend* RESTful API (`Python FastAPI + Uvicorn ASGI`):**
   - Menyediakan 5 *endpoint* `GET` *read-only* berfitur kompresi **HTTP Gzip** (`/api/mangrove/years`, `/api/mangrove/geojson/{tahun}`, `/api/mangrove/proyeksi/{tahun}`, `/api/mangrove/statistik`, dan `/docs`).
4. **Pembuatan *Frontend* Peta Interaktif (`Next.js 15 + Leaflet.js`):**
   - Menampilkan kanvas peta interaktif `L.geoJSON`, tombol pilih tahun, *toggle* layer proyeksi 2027, grafik garis tren luasan hektar, kartu metrik akurasi (`OA, Kappa, F1, FoM`), dan *popup* detail poligon saat diklik.

---

## 📐 5. Bedah Tuntas Seluruh 15 Rumus (Persamaan 2.1 s.d. 2.15) dengan Contoh Angka

Semua rumus di proposal Anda terletak di **BAB 2 $\rightarrow$ Sub-bab 2.4 Metode (Hal. 42–48 PDF / Hal. 28–34 dokumen)**. Berikut penjelasan lengkap dari dasar untuk setiap rumus:

---

### 5.1. Rumus Pra-pemrosesan & 5 Indeks Spektral (Hal. 42–44 PDF)

#### 🔹 Persamaan (2.1): Kalibrasi Radiometrik Nilai Piksel Mentah ke Reflektansi ($\rho$)
$$\rho = \frac{DN + BOA\_ADD\_OFFSET}{QUANTIFICATION\_VALUE} = \frac{DN - 1000}{10000} \tag{2.1}$$
- **Letak di PDF:** Hal. 42–43 PDF (Sub-bab 2.4.1).
- **Arti Simbol:**
  - $DN$ (*Digital Number*): Angka bulat mentah yang tersimpan di file gambar satelit (contoh: `4400`).
  - $BOA\_ADD\_OFFSET = -1000$: Angka koreksi wajib dari ESA untuk citra Sentinel-2 sejak *Processing Baseline* 04.00 (25 Januari 2022).
  - $QUANTIFICATION\_VALUE = 10000$: Faktor pembagi agar angka ribuan berubah menjadi angka desimal skala $0$ s.d. $1$.
  - $\rho$ (*Rho*): Nilai pantulan cahaya fisik permukaan (*Surface Reflectance*), berada di rentang $[-0{,}1 \text{ s.d. } 1{,}5]$.
- **Contoh Angka:** Piksel memiliki nilai mentah $DN = 4400$ pada band `B08`:
  $$\rho = \frac{4400 - 1000}{10000} = 0{,}34$$

---

#### 🔹 Persamaan (2.2): *Normalized Difference Vegetation Index* (`NDVI` — Rouse dkk., 1974)
$$NDVI = \frac{B08 - B04}{B08 + B04 + \varepsilon} \tag{2.2}$$
- **Letak di PDF:** Hal. 44 PDF (Sub-bab 2.4.2).
- **Arti Simbol:**
  - $B08$: Nilai pantulan inframerah dekat (*NIR*) — tinggi jika daun rimbun.
  - $B04$: Nilai pantulan cahaya Merah (*Red*) — rendah jika klorofil daun aktif berfotosintesis.
  - $\varepsilon = 10^{-6}$ ($0{,}000001$): Angka sangat kecil yang ditambahkan di bagian bawah pecahan semata-mata agar komputer tidak mengalami *error division by zero* jika $B08 + B04 = 0$.
- **Cara Baca Hasil:** Rentang $-1$ sampai $+1$. Nilai $> 0{,}6$ menandakan vegetasi hijau rapat.

---

#### 🔹 Persamaan (2.3): *Enhanced Vegetation Index* (`EVI` — Huete dkk., 2002)
$$EVI = \frac{2{,}5 \times (B08 - B04)}{B08 + 6 \times B04 - 7{,}5 \times B02 + 1 + \varepsilon} \tag{2.3}$$
- **Letak di PDF:** Hal. 44 PDF (Sub-bab 2.4.2).
- **Arti konstanta di dalam rumus:**
  - $2{,}5$: Faktor penguat (*gain factor*).
  - $6 \times B04$ dan $-7{,}5 \times B02$: Koefisien koreksi aerosol atmosfer menggunakan saluran Biru (`B02`) untuk menembus kabut tipis.
  - $+1$: Konstanta penyesuaian latar belakang kanopi (*canopy background adjustment*) agar pantulan lumpur di sela pohon tidak mengganggu nilai kehijauan.
- **Fungsi Utama:** Mencegah kejenuhan (*saturasi*) yang dialami `NDVI` ketika kanopi mangrove sangat lebat.

---

#### 🔹 Persamaan (2.4): *Normalized Difference Water Index* (`NDWI` — McFeeters, 1996)
$$NDWI = \frac{B03 - B08}{B03 + B08 + \varepsilon} \tag{2.4}$$
- **Letak di PDF:** Hal. 44 PDF (Sub-bab 2.4.2).
- **Logika Rumus:** Mengadu saluran Hijau (`B03`) melawan saluran Inframerah Daun (`B08`).
- **Fungsi Utama:** Memisahkan **badan air terbuka** (laut Teluk Balikpapan, muara sungai, tambak) dari vegetasi. Karena air menyerap habis `B08`, maka di atas air nilai $B03 > B08$ sehingga **`NDWI` bernilai positif ($> 0$)**.

---

#### 🔹 Persamaan (2.5): *Normalized Difference Moisture Index* (`NDMI` — Gao, 1996) ★ *Kunci Utama!*
$$NDMI = \frac{B08 - B11}{B08 + B11 + \varepsilon} \tag{2.5}$$
- **Letak di PDF:** Hal. 44 PDF (Sub-bab 2.4.2).
- **Logika Rumus:** Mengadu struktur sel daun (`B08` NIR) melawan serapan air gelombang pendek (`B11` SWIR-1).
- **Fungsi Utama (Wajib Hafal untuk Sidang!):** Menjadi **pembeda utama (*rank 1 feature importance*) antara mangrove basah vs hutan darat perbukitan kering**. Karena air pada daun mangrove dan substrat lumpur pasang surut menyerap `B11`, maka nilai `B11` mangrove menjadi kecil dan nilai **`NDMI` mangrove tinggi positif**, sedangkan hutan darat perbukitan nilai `B11`-nya tinggi sehingga **`NDMI`-nya rendah**.

---

#### 🔹 Persamaan (2.6): *Renormalized Difference Vegetation Index* (`RDVI` — Roujean & Breon, 1995)
$$RDVI = \frac{B08 - B04}{\sqrt{B08 + B04 + \varepsilon}} \tag{2.6}$$
- **Letak di PDF:** Hal. 44 PDF (Sub-bab 2.4.2).
- **Logika Rumus:** Menggunakan akar kuadrat ($\sqrt{B08 + B04}$) pada penyebut untuk menggabungkan kepekaan pada vegetasi jarang sekaligus mencegah kejenuhan pada kanopi mangrove yang sangat rapat.

---

### 5.2. Rumus Random Forest & Proyeksi CA-Markov (Hal. 45–47 PDF)

#### 🔹 Persamaan (2.7): Estimasi Probabilitas Keanggotaan Kelas Random Forest ($P_{ML}$)
$$P_{ML}(y=1 \mid x) = \frac{1}{B} \sum_{b=1}^{B} I(h_b(x) = 1) \tag{2.7}$$
- **Letak di PDF:** Hal. 45 PDF (Sub-bab 2.4.3).
- **Terjemahan Simbol:**
  - $P_{ML}(y=1 \mid x)$: Peluang piksel $x$ berkelas Mangrove (`1`) menurut model *Machine Learning*.
  - $B = 200$: Total jumlah pohon keputusan di dalam *Random Forest*.
  - $h_b(x)$: Hasil tebakan pohon ke-$b$ terhadap piksel $x$.
  - $I(h_b(x) = 1)$: Fungsi indikator (bernilai `1` jika pohon ke-$b$ menebak Mangrove, `0` jika menebak Non-Mangrove).
- **Intinya:** Proporsi pohon dari 200 pohon yang memilih Mangrove. Jika 180 dari 200 pohon memilih Mangrove, maka $P_{ML} = 180 / 200 = 0{,}90$. Nilai kontinu $[0, 1]$ inilah yang disetor ke model proyeksi CA-Markov!

---

#### 🔹 Persamaan (2.8): Matriks Probabilitas Transisi Rantai Markov ($P$)
$$P = \begin{bmatrix} P_{00} & P_{01} \\ P_{10} & P_{11} \end{bmatrix}, \quad \sum_{j} P_{ij} = 1 \tag{2.8}$$
- **Letak di PDF:** Hal. 46 PDF (Sub-bab 2.4.4).
- **Cara Membaca Matriks $2 \times 2$ ini:**
  - Baris atas adalah nasib piksel yang awalnya **Non-Mangrove (`0`)**:
    - $P_{00}$: Peluang tetap Non-Mangrove (`0 → 0`).
    - $P_{01}$: Peluang tumbuh menjadi Mangrove baru (`0 → 1`, *rekolonisasi/gain*).
  - Baris bawah adalah nasib piksel yang awalnya **Mangrove (`1`)**:
    - $P_{10}$: Peluang berubah menjadi Non-Mangrove (`1 → 0`, *degradasi/loss*).
    - $P_{11}$: Peluang bertahan tetap Mangrove (`1 → 1`, *persistensi*).
- **Fungsi Utama:** Mengalikan proporsi $P_{01}$ dan $P_{10}$ dengan jumlah piksel awal untuk mendapatkan **kuota jumlah piksel yang berubah ($N_{trans}$)**.

---

#### 🔹 Persamaan (2.9): Rasio Ketetanggaan Spasial Seluler Kernel Moore $3 \times 3$ ($N_{CA}$)
$$N_{CA}(x, y) = \frac{1}{8} \sum_{u=-1}^{1} \sum_{v=-1}^{1} I(tutupan(x+u, y+v) = 1), \quad (u, v) \neq (0, 0) \tag{2.9}$$
- **Letak di PDF:** Hal. 46 PDF (Sub-bab 2.4.4).
- **Terjemahan Simbol:**
  - $(x, y)$: Koordinat piksel tengah yang sedang dihitung.
  - $u \in \{-1, 0, 1\}$ dan $v \in \{-1, 0, 1\}$ dengan $(u, v) \neq (0, 0)$: Mengiterasi **8 piksel tetangga** yang mengelilingi piksel tengah pada kotak berukuran $3 \times 3$.
  - $\frac{1}{8} \sum I(\dots)$: Menghitung berapa banyak dari 8 tetangga tersebut yang bertutupan Mangrove (`1`), lalu dibagi 8.
- **Contoh Angka:** Kalau 4 dari 8 tetangganya adalah mangrove, maka $N_{CA} = 4/8 = 0{,}50$.

---

#### 🔹 Persamaan (2.10) & (2.11): Skor Kesesuaian Tumbuh ($S_{gain}$) & Skor Kerentanan Hilang ($S_{loss}$)
$$S_{gain}(x, y) = 0{,}25 \cdot P_{ML} + 0{,}25 \cdot \Delta NDMI_{norm} + 0{,}25 \cdot \Delta NDVI_{norm} + 0{,}25 \cdot N_{CA} \tag{2.10}$$
$$S_{loss}(x, y) = 0{,}25 \cdot (1 - P_{ML}) + 0{,}25 \cdot (-\Delta NDMI_{norm}) + 0{,}25 \cdot (-\Delta NDVI_{norm}) + 0{,}25 \cdot (1 - N_{CA}) \tag{2.11}$$
- **Letak di PDF:** Hal. 47 PDF (Sub-bab 2.4.4).
- **Logika Kedua Rumus Ini:**
  - Keduanya adalah **rata-rata berbobot seimbang ($w_1 = w_2 = w_3 = w_4 = 0{,}25$)** dari 4 pendorong spasial.
  - **Kapan piksel Non-Mangrove mudah tumbuh jadi Mangrove ($S_{gain}$ tinggi)?** Saat nilai $P_{ML}$ tinggi, kelembapan $\Delta NDMI$ naik, kehijauan $\Delta NDVI$ naik, dan dikelilingi banyak tetangga mangrove ($N_{CA}$ tinggi).
  - **Kapan piksel Mangrove rawan rusak/hilang jadi Non-Mangrove ($S_{loss}$ tinggi)?** Kebalikannya! Saat keyakinan mangrove rendah ($(1 - P_{ML})$ tinggi), mengalami kekeringan ($-\Delta NDMI_{norm}$ positif), daunnya rontok ($-\Delta NDVI_{norm}$ positif), dan berada di pinggiran yang dikelilingi non-mangrove ($(1 - N_{CA})$ tinggi).

---

### 5.3. Rumus Evaluasi Akurasi Klasifikasi & Validasi Proyeksi (Hal. 47–48 PDF)

#### 🔹 Persamaan (2.12): *Overall Accuracy* (`OA`)
$$OA = \frac{TP + TN}{TP + TN + FP + FN} \times 100\% \tag{2.12}$$
- **Letak di PDF:** Hal. 47 PDF (Sub-bab 2.4.5).
- **Arti:** Total piksel yang ditebak benar ($TP$ Mangrove benar + $TN$ Non-Mangrove benar) dibagi total seluruh piksel uji. **Target: $\ge 80\%$**.

---

#### 🔹 Persamaan (2.13): Koefisien Kesepakatan Cohen's Kappa ($\kappa$ — Landis & Koch, 1977)
$$\kappa = \frac{p_o - p_e}{1 - p_e} \tag{2.13}$$
- **Letak di PDF:** Hal. 47 PDF (Sub-bab 2.4.5).
- **Arti Simbol:**
  - $p_o$: Proporsi kesepakatan aktual yang teramati (sama dengan nilai `OA` dalam desimal, misal $0{,}90$).
  - $p_e$: Proporsi kesepakatan yang diharapkan terjadi secara kebetulan/acak (*expected agreement by chance*), dihitung dari perkalian total baris dan kolom matriks konfusi.
- **Fungsi Utama:** Mengukur ketepatan model setelah dikurangi faktor kebetulan. **Target: $\ge 0{,}70$**.

---

#### 🔹 Persamaan (2.14): *F1-Score* Kelas Mangrove
$$F1 = 2 \times \frac{Precision \times Recall}{Precision + Recall} = \frac{2 \cdot TP}{2 \cdot TP + FP + FN} \tag{2.14}$$
- **Letak di PDF:** Hal. 47–48 PDF (Sub-bab 2.4.5).
- **Arti Simbol:**
  - $Precision = \frac{TP}{TP + FP}$ (*User's Accuracy* / UA): Dari semua yang ditebak Mangrove oleh model, berapa persen yang benar-benar Mangrove?
  - $Recall = \frac{TP}{TP + FN}$ (*Producer's Accuracy* / PA): Dari semua Mangrove asli di lapangan, berapa persen yang berhasil ditemukan oleh model?
  - $F1$: Rata-rata harmonik dari *Precision* dan *Recall*. **Target utama: $\ge 0{,}80$**.

---

#### 🔹 Persamaan (2.15): *Figure of Merit* (`FoM` — Pontius dkk., 2008)
$$FoM = \frac{B}{A + B + C + D} \times 100\% \tag{2.15}$$
- **Letak di PDF:** Hal. 48 PDF (Sub-bab 2.4.5).
- **Digunakan pada tahap apa?** Pada tahap **Validasi *Hindcasting*** (memproyeksikan tahun 2025 dari data 2023–2024, lalu membandingkan peta proyeksi 2025 dengan peta riil 2025).
- **Arti 4 Huruf ($A, B, C, D$):**
  - **$A$ (*Misses*):** Di peta asli 2025 **berubah**, tetapi model memprediksi **diam/tidak berubah**.
  - **$B$ (*Hits*):** Di peta asli 2025 **berubah**, dan model **tepat memprediksi berubah**.
  - **$C$ (*Wrong Change*):** Berubah tetapi salah kelas tujuan (pada klasifikasi biner 2 kelas, $C = 0$).
  - **$D$ (*False Alarms*):** Di peta asli 2025 **diam**, tetapi model salah memprediksi **berubah**.
- **Kriteria Lulus:** $FoM_{\text{CA-Markov}} > FoM_{\text{Random}}$ (mengalahkan 100 simulasi acak *Monte Carlo* pada selang kepercayaan 95%).

---

## 🖥️ 6. Bedah Arsitektur Sistem 4-Tier & Database WebGIS (Bab 2.3 & Bab 3.4.5)

Bagian ini adalah **kekuatan utama Anda sebagai mahasiswa Sistem Informasi** (lihat **Gambar 3.2 di Hal. 64–65 PDF / Hal. 50–51 dokumen**):

```
┌─────────────────────────────────────────────────────────────────────────┐
│ LAPISAN 1: SUMBER DATA (Data Source Layer)                              │
│ • Sentinel-2 L2A (CDSE STAC API)    • Tabel Pasut Pushidrosal (2024)    │
│ • Iklim BMKG Sepinggan (2024)       • Ortofoto VHR Google Earth & Esri  │
└───────────────────────────────────┬─────────────────────────────────────┘
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ LAPISAN 2: PIPELINE ANALITIK OFFLINE PYTHON (Analytical Processing)     │
│ • Rasterio/GDAL + NumPy/SciPy (Pra-pemrosesan & 13 Fitur + Moore 3x3)   │
│ • Scikit-Learn (Random Forest 200 Pohon) + Simulasi Proyeksi CA-Markov  │
│ • GeoPandas/Shapely: Hitung Hektar di UTM 50S (EPSG:32750) → WGS84      │
└───────────────────────────────────┬─────────────────────────────────────┘
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ LAPISAN 3: BASIS DATA SPASIAL (Spatial Data Layer — PostgreSQL/PostGIS) │
│ 1. Tabel `klasifikasi_mangrove`:                                        │
│    • GEOMETRY(Polygon, 4326) (exploded polygons) + Indeks Spasial GiST  │
│    • Kolom: kode_poligon, tahun, tipe ('klasifikasi'/'proyeksi'),       │
│             luas_ha, centroid                                           │
│ 2. Tabel `statistik_luas`:                                              │
│    • Kolom: tahun, luas_total_ha, jumlah_poligon, f1_score, oa_persen,  │
│             kappa, fom (agar grafik dimuat dalam hitungan milidetik!)   │
└───────────────────────────────────┬─────────────────────────────────────┘
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ LAPISAN 4: LAYANAN API & PRESENTASI WEB (Service & Presentation Layer)  │
│ • Backend Python FastAPI (Uvicorn ASGI + Kompresi HTTP Gzip):           │
│   1. GET /api/mangrove/years                                            │
│   2. GET /api/mangrove/geojson/{tahun}                                  │
│   3. GET /api/mangrove/proyeksi/{tahun}                                 │
│   4. GET /api/mangrove/statistik                                        │
│   5. GET /docs (Swagger UI)                                             │
│ • Frontend Next.js 15 & Leaflet.js (Presentation Layer):                │
│   Kanvas Peta L.geoJSON, Pemilih Tahun (2023–2026 & Proyeksi 2027),     │
│   Grafik Tren Luasan, Kartu Metrik Akurasi, dan Popup Klik Poligon.     │
└─────────────────────────────────────────────────────────────────────────┘
```

### Tiga Poin Kunci Arsitektur WebGIS yang Wajib Anda Tekankan Saat Sidang:
1. **Kenapa Disebut *Decoupled Presentation Layer*?**
   - Karena proses *training Machine Learning* dan simulasi *CA-Markov* yang berat **tidak dijalankan saat user mengklik tombol di web**, melainkan diselesaikan di **Lapisan 2 (Offline Python Pipeline)**. WebGIS (FastAPI + Leaflet.js) fokus 100% menampilkan hasil yang sudah tervalidasi dari PostGIS (mengacu pada Orlandini dkk., 2026).
2. **Kenapa Tidak Pakai *GeoServer* seperti Penelitian Valero-Jorge dkk. (2024)?**
   - GeoServer berjalan di atas *Java Virtual Machine* (JVM) yang memakan RAM server sangat besar (4–8 GB). Dengan mengekspor poligon langsung dari PostGIS (`ST_AsGeoJSON`) melalui **FastAPI + kompresi Gzip** ke **Leaflet.js**, arsitektur menjadi jauh lebih ringan dan cepat.
3. **Kenapa Pakai *Exploded Polygons* + Indeks *GiST* di PostGIS?**
   - *Exploded polygons* artinya setiap bercak poligon mangrove disimpan sebagai **1 baris (`row`) mandiri** bertipe `GEOMETRY(Polygon, 4326)` (bukan digabung jadi 1 `MultiPolygon` raksasa se-Kariangau). Dengan begitu, saat user mengklik 1 bercak mangrove di peta, indeks pohon pencarian **GiST (*Generalized Search Tree*)** (Peng dkk., 2024) langsung menemukan poligon tersebut dengan kecepatan logaritmik $\mathcal{O}(\log N)$ dan menampilkan luas hektarnya di *popup*.

---

## 📅 7. Metode & Kurikulum Belajar 7 Hari (1 Minggu Menguasai Seluruh Proposal)

Gunakan metode **Feynman Technique** (baca 30 menit $\rightarrow$ tutup PDF $\rightarrow$ jelaskan kembali dengan bahasa sendiri selama 15 menit):

### 🗓️ HARI 1: Menguasai Cerita Besar, Latar Belakang, & Rumusan Masalah
- **Halaman PDF yang Dibaca:** Hal. 5 (Abstrak) dan Hal. 15–28 PDF (Bab 1 Lengkap).
- **Target Hafal di Luar Kepala:**
  1. **3 Ancaman Utama di Kariangau:** (a) Ekspansi Kawasan Industri Kariangau (KIK) & galangan kapal, (b) Gelombang kapal tongkang logistik IKN di Teluk Balikpapan, (c) Patroli visual pengelola hanya sebatas jembatan titian kayu ulin (*boardwalk*).
  2. **4 Kendala Operasional (Hal. 17 PDF):** Keterbatasan keahlian GIS desktop, tidak ada database spasial terpusat, jangkauan pantau visual sempit & belum ada alat prediksi masa depan, serta kemiripan nilai `NDVI` antara mangrove dan hutan bukit + gangguan awan tropis.
  3. **4 Rumusan Masalah (Hal. 19–20 PDF):** (1) Kinerja RF 13 fitur, (2) Tren luas hektar 2023–2026 di UTM 50S, (3) Formulasi & validasi *hindcasting* CA-Markov 2027, (4) Penyajian ke *presentation layer* WebGIS.

### 🗓️ HARI 2: Menguasai Data Sentinel-2, Tahap 1, & Rumus (2.1)–(2.6)
- **Halaman PDF yang Dibaca:** Hal. 42–44 PDF (Sub-bab 2.4.1–2.4.2), Hal. 51–53 PDF (Tahap 1), dan Hal. 57–60 PDF (Tabel 3.1 & 3.2).
- **Target Paham Logika:**
  1. Kenapa bulan **Juli–September**? (Musim kering Balikpapan menurut BMKG Sepinggan, awan paling sedikit).
  2. Kenapa filter pasang surut **$\le 1{,}5\text{ m}$ LAT**? (Mengacu tabel **Pushidrosal 2024**, agar air pasang tidak menenggelamkan tajuk bawah mangrove yang bikin nilai NIR turun).
  3. Kenapa band 20 m di-*resample* ke 10 m pakai **Bilinear**, sedangkan pita awan SCL pakai **Nearest Neighbor**?
  4. Paham rumus **Persamaan (2.1)** (`BOA_ADD_OFFSET = -1000`) dan **Persamaan (2.2)–(2.6)**, terutama kenapa **`NDMI` (Pers. 2.5)** mampu membedakan mangrove basah vs hutan bukit kering.

### 🗓️ HARI 3: Menguasai *Ground Truth*, *Random Forest*, & Rumus (2.7)
- **Halaman PDF yang Dibaca:** Hal. 44–45 PDF (Sub-bab 2.4.3), Hal. 53–54 PDF (Tahap 2), dan Hal. 61–62 PDF (Tabel 3.3).
- **Target Paham Logika:**
  1. Cara bikin *Ground Truth* 2023 tanpa survei fisik (pakai ortofoto resolusi sangat tinggi *Google Earth Pro Historical Imagery* & *Esri Wayback 2023* + batas KLHK).
  2. Cara kerja **`5-Fold Stratified Group K-Fold` berbasis `poly_id`** untuk mencegah *spatial data leakage*.
  3. Makna parameter RF: `n_estimators = 200`, `criterion = 'gini'`, `max_features = 'sqrt'` ($\sqrt{13} \approx 3$ fitur), `bootstrap = True` (menyisakan $\sim 36{,}8\%$ data *Out-of-Bag* / OOB), dan cara kerja rumus **`predict_proba` ($P_{ML}$, Pers. 2.7)**.

### 🗓️ HARI 4: Menguasai Proyeksi CA-Markov & Rumus (2.8)–(2.11)
- **Halaman PDF yang Dibaca:** Hal. 45–47 PDF (Sub-bab 2.4.4), Hal. 54–55 PDF (Tahap 3), dan Hal. 62–63 PDF (Tabel 3.5).
- **Target Paham Logika:**
  1. Fungsi filter **MMU 0,04 ha (4 piksel $10\times 10\text{ m}$)** sebelum masuk ke CA-Markov.
  2. Perbedaan tugas **Rantai Markov** (menghitung matriks transisi $P_{ij}$ Pers. 2.8 & kuota jumlah piksel berubah $N_{trans}$) dengan **Cellular Automata** (mengalokasikan lokasi piksel yang berubah).
  3. Empat variabel pendorong spasial pada *Transition Potential Map* (TPM) berbobot masing-masing $0{,}25$: $P_{ML}$, $\Delta NDMI$, $\Delta NDVI$, dan **rasio 8 tetangga Moore $3\times 3$ ($N_{CA}$, Pers. 2.9)** untuk menghitung skor **$S_{gain}$ (Pers. 2.10)** dan **$S_{loss}$ (Pers. 2.11)**.

### 🗓️ HARI 5: Menguasai Evaluasi Akurasi, Olofsson (2014), & Hindcasting `FoM` (2.12)–(2.15)
- **Halaman PDF yang Dibaca:** Hal. 47–48 PDF (Sub-bab 2.4.5).
- **Target Paham Logika:**
  1. Tiga metrik matriks konfusi: **OA ($\ge 80\%$, Pers. 2.12)**, **Kappa ($\ge 0{,}70$, Pers. 2.13)**, dan **F1-Score ($\ge 0{,}80$, Pers. 2.14)**.
  2. Apa itu **Validasi Independen 100 Titik Acak Terstratifikasi (Olofsson dkk., 2014)**? (50 titik di kelas mangrove, 50 titik di non-mangrove pada tiap peta tahunan untuk mengoreksi bias luas hektar pada selang kepercayaan 95% dengan target standar error $S(\hat{O}) \le 0{,}03$).
  3. Apa itu **Validasi *Hindcasting* 2025** dan bagaimana cara kerja rumus **Figure of Merit (`FoM`, Pers. 2.15)** ($A, B, C, D$) melawan 100 simulasi acak *Monte Carlo*?

### 🗓️ HARI 6: Menguasai Teknologi & Arsitektur WebGIS 4-Tier
- **Halaman PDF yang Dibaca:** Hal. 32–42 PDF (Tabel 2.1 Penelitian Terdahulu & Sub-bab 2.3 Teknologi) dan Hal. 55–56, 64–65 PDF (Tahap 4 & Sub-bab 3.4.5).
- **Target Paham Logika:**
  1. Peran masing-masing jurnal di Sub-bab 2.3 (`Seydi 2024`, `Valero-Jorge 2024`, `Orlandini 2026`, `Popa 2026`, `Butler 2016`, `Horbiński & Lorek 2020/2022`, `Geng 2026`, `Peng 2024`).
  2. Struktur 2 tabel di PostgreSQL/PostGIS (`klasifikasi_mangrove` & `statistik_luas`), 5 *endpoint* FastAPI, kompresi Gzip, dan batasan WebGIS sebagai *presentation layer*.

### 🗓️ HARI 7: Gladi Bersih Presentasi & Tanya-Jawab Penguji
- Latihan presentasi 10–12 menit dari Bab 1 s.d. Bab 3, lalu jawab 8 pertanyaan penguji di Bagian 8 di bawah ini tanpa melihat catatan!

---

## 🎯 8. Bank Simulasi Tanya-Jawab Dosen Penguji Sempro (Beserta Jawaban Kunci)

Berikut adalah **8 pertanyaan tersulit yang paling sering ditanyakan dosen penguji** pada sidang proposal topik *Machine Learning Geospasial + WebGIS*, lengkap dengan jawaban singkat dan padat sesuai PDF Final `(8).pdf`:

1. **Penguji:** *"Kenapa kamu memilih algoritma Random Forest, padahal di Tabel 2.1 ada CNN (Seydi dkk., 2024) dan XGBoost (Minati dkk., 2023)?"*
   - **Jawaban Anda:** *"Ada tiga alasan utama, Pak/Bu. Pertama, secara teoretis Random Forest menggunakan mekanisme ensemble bagging 200 pohon dengan pemilihan sub-fitur acak ($\sqrt{13} \approx 3$ fitur), sehingga sangat tahan terhadap derau spektral awan tropis dan tidak rentan overfitting maupun multikolinearitas antar-indeks vegetasi dibanding pohon tunggal. Kedua, berbeda dengan CNN yang membutuhkan infrastruktur GPU server berbiaya tinggi, Random Forest sangat efisien dijalankan pada perangkat standar dan mampu menghasilkan probabilitas kontinu $P_{ML}$ via fungsi `predict_proba` yang menjadi variabel pendorong utama untuk model proyeksi CA-Markov. Ketiga, pemilihan ini didukung preseden sistem WebGIS mangrove SIGMEM karya Valero-Jorge dkk. (2024) yang membuktikan Random Forest mencapai Overall Accuracy 94,11% dan Kappa 0,94 pada citra Sentinel-2."*

2. **Penguji:** *"Di Kariangau banyak hutan darat di perbukitan belakang mangrove. Bagaimana modelmu tidak salah mengenali hutan bukit sebagai mangrove?"*
   - **Jawaban Anda:** *"Itulah alasan utama penelitian ini mengekstraksi 13 fitur spektral dan menempatkan indeks kelembapan **NDMI (Persamaan 2.5)** berbasis pita gelombang pendek **SWIR-1 (`B11`)** sebagai pembeda kunci. Jika hanya mengandalkan NDVI, nilai kehijauan tajuk mangrove dan hutan bukit memang mirip. Namun, karena mangrove tumbuh di zona lumpur pasang surut yang basah dan berdaun sukulen, radiasi SWIR `B11` diserap kuat oleh air sehingga nilai NDMI mangrove tinggi positif, berbeda tegas dengan hutan daratan perbukitan yang kering dan memiliki nilai NDMI rendah."*

3. **Penguji:** *"Mengapa jam perekaman satelit harus disinkronkan dengan data pasang surut Pushidrosal ($\le 1{,}5\text{ m}$ LAT)?"*
   - **Jawaban Anda:** *"Karena mangrove tumbuh di zona intertidal pasang surut. Apabila citra Sentinel-2 diambil saat pasang tertinggi (> 1,8 m LAT), air laut akan menenggelamkan perakaran dan tajuk mangrove strata bawah. Air memiliki sifat menyerap habis radiasi inframerah dekat (NIR `B08`), sehingga pantulan vegetasi mangrove akan teredam (mengalami atenuasi optik) dan berisiko salah terklasifikasi sebagai badan air."*

4. **Penguji:** *"Apa maksud dari `5-Fold Stratified Group K-Fold` berbasis `poly_id` pada Tahap 2? Kenapa tidak pakai `train_test_split` acak biasa?"*
   - **Jawaban Anda:** *"Jika kita membagi data latih dan uji secara acak per piksel, piksel-piksel yang bersebelahan di dalam satu poligon pohon yang sama akan terpisah sebagian ke data latih dan sebagian ke data uji. Karena piksel bertetangga memiliki kemiripan nilai spektral yang sangat tinggi (autokorelasi spasial), model akan mengalami **kebocoran data spasial (spatial data leakage)** dan menghasilkan akurasi yang tampak tinggi secara semu. Dengan `Group K-Fold` berbasis `poly_id`, seluruh piksel yang berasal dari satu poligon yang sama dikunci dalam satu lipatan (fold) yang sama sehingga pengujian benar-benar objektif."*

5. **Penguji:** *"Jelaskan bagaimana Random Forest dan CA-Markov bekerja sama memproyeksikan tutupan mangrove tahun 2027!"*
   - **Jawaban Anda:** *"Keduanya terhubung secara berurutan. Pertama, Random Forest memetakan tutupan mangrove tahunan 2023–2026 sekaligus mengeluarkan peta probabilitas kelas $P_{ML}$ (Persamaan 2.7). Setelah bercak derau < 0,04 ha (4 piksel) dibersihkan, **Rantai Markov** menghitung matriks transisi antar-tahun (Persamaan 2.8) untuk menentukan **kuota jumlah piksel** yang akan bertambah atau berkurang. Selanjutnya, **Cellular Automata (CA)** menentukan **lokasi spasial** piksel mana yang bertransisi menggunakan Transition Potential Map (Persamaan 2.10 & 2.11) yang menggabungkan 4 pendorong berbobot 0,25: probabilitas $P_{ML}$, perubahan kelembapan $\Delta NDMI$, perubahan kehijauan $\Delta NDVI$, dan proporsi 8 tetangga mangrove pada kernel Moore $3 \times 3$ ($N_{CA}$, Persamaan 2.9)."*

6. **Penguji:** *"Bagaimana kamu membuktikan bahwa hasil proyeksi tahun 2027 itu tidak asal menebak?"*
   - **Jawaban Anda:** *"Melalui pengujian **validasi hindcasting** pada Tahap 3. Sebelum memproyeksikan tahun 2027, model dikalibrasi menggunakan data 2023–2024 untuk memproyeksikan tahun **2025**. Peta hasil proyeksi 2025 tersebut kemudian dibandingkan secara piksel-demi-piksel terhadap peta klasifikasi riil tahun 2025 menggunakan metrik **Figure of Merit (FoM, Persamaan 2.15)** dari Pontius dkk. (2008) yang khusus menilai ketepatan pada piksel yang berubah. Model dinyatakan valid apabila nilai FoM-nya melampaui 100 simulasi alokasi acak Monte Carlo pada selang kepercayaan 95%."*

7. **Penguji:** *"Mengapa sudah ada matriks konfusi (OA, Kappa, F1) pada validasi silang, tetapi masih ditambah uji 100 titik acak Olofsson dkk. (2014)?"*
   - **Jawaban Anda:** *"Validasi silang 5-Fold menguji kinerja algoritma pada poligon sampel tahun baseline 2023. Sedangkan protokol Olofsson dkk. (2014) menggunakan 100 titik acak terstratifikasi (50 mangrove, 50 non-mangrove) pada peta hasil klasifikasi tiap tahun (2023–2026) untuk mengoreksi potensi bias luasan peta dan menghasilkan estimasi luas hektar yang bebas bias beserta rentang interval kepercayaan 95%."*

8. **Penguji:** *"Karena kamu mahasiswa Sistem Informasi, jelaskan bagaimana desain arsitektur WebGIS dan basis datamu!"*
   - **Jawaban Anda:** *"Sistem dirancang dengan pola **4-Tier Decoupled Architecture** (Gambar 3.2). Pemrosesan berat citra dan ML dipisahkan pada pipeline offline Python agar tidak membebani web server. Hasilnya dikonversi menjadi poligon vektor berluas hektar akurat (dihitung pada proyeksi meter UTM Zona 50S `EPSG:32750` lalu direproyeksi ke WGS84 `EPSG:4326`), kemudian disimpan ke basis data **PostgreSQL 17 / PostGIS 3.5** pada tabel `klasifikasi_mangrove` (dengan struktur exploded polygons berindeks pohon spasial **GiST** berkecepatan $\mathcal{O}(\log N)$) dan tabel `statistik_luas`. Data disajikan melalui RESTful API asinkron **Python FastAPI** yang dikompresi **HTTP Gzip** menuju antarmuka peta **Next.js 15 & Leaflet.js** sebagai presentation layer mandiri tanpa memerlukan middleware berat seperti GeoServer."*

