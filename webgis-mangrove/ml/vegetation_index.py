"""
ml/vegetation_index.py
Menghitung indeks vegetasi dari citra satelit (GeoTIFF)
Referensi: Jurnal SIGMEM (Remote Sensing, 2024) — NDVI, EVI, CCCI, NDMI

Cara pakai:
    python vegetation_index.py --input data/raw/sentinel2_2023.tif --output data/output/
"""

import numpy as np
import rasterio
from rasterio.plot import show
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import argparse
import os


def load_sentinel2_bands(tif_path):
    """
    Load band Sentinel-2 dari file GeoTIFF.
    Asumsi urutan band: B2(Blue), B3(Green), B4(Red), B8(NIR), B8a(nNIR),
                        B9(WV), B11(SWIR1), B12(SWIR2)
    Sesuaikan dengan urutan band di file kamu!
    """
    with rasterio.open(tif_path) as src:
        print(f"[INFO] Membaca: {tif_path}")
        print(f"[INFO] Jumlah band: {src.count}, Ukuran: {src.width}x{src.height}")
        meta = src.meta.copy()

        # Baca band (index mulai dari 1 di rasterio)
        # SESUAIKAN angka band ini dengan file GeoTIFF kamu!
        B4  = src.read(3).astype(float)   # Red
        B8  = src.read(4).astype(float)   # NIR
        B8a = src.read(5).astype(float)   # Narrow NIR
        B2  = src.read(1).astype(float)   # Blue
        B9  = src.read(6).astype(float)   # Water Vapor
        B11 = src.read(7).astype(float)   # SWIR1
        B5  = src.read(None)              # Red Edge 1 (kalau ada)

    return B2, B4, B8, B8a, B9, B11, meta


def compute_ndvi(B4, B8):
    """
    NDVI = (NIR - Red) / (NIR + Red)
    Range: -1 to 1 | Mangrove biasanya > 0.5
    """
    with np.errstate(divide='ignore', invalid='ignore'):
        ndvi = np.where(
            (B8 + B4) == 0, 0,
            (B8 - B4) / (B8 + B4)
        )
    print(f"[NDVI] Min={ndvi.min():.3f}, Max={ndvi.max():.3f}, Mean={ndvi.mean():.3f}")
    return ndvi.astype(np.float32)


def compute_evi(B2, B4, B8):
    """
    EVI = 2.5 * ((NIR - Red) / (NIR + 6*Red - 7.5*Blue + 1))
    Lebih stabil dari NDVI di area vegetasi padat
    """
    with np.errstate(divide='ignore', invalid='ignore'):
        evi = np.where(
            (B8 + 6*B4 - 7.5*B2 + 1) == 0, 0,
            2.5 * ((B8 - B4) / (B8 + 6*B4 - 7.5*B2 + 1))
        )
    evi = np.clip(evi, -1, 1)
    print(f"[EVI]  Min={evi.min():.3f}, Max={evi.max():.3f}, Mean={evi.mean():.3f}")
    return evi.astype(np.float32)


def compute_ndwi(B3_green, B8):
    """
    NDWI = (Green - NIR) / (Green + NIR)
    Deteksi kandungan air / area basah
    Positif = air/basah, Negatif = vegetasi kering
    """
    with np.errstate(divide='ignore', invalid='ignore'):
        ndwi = np.where(
            (B3_green + B8) == 0, 0,
            (B3_green - B8) / (B3_green + B8)
        )
    print(f"[NDWI] Min={ndwi.min():.3f}, Max={ndwi.max():.3f}, Mean={ndwi.mean():.3f}")
    return ndwi.astype(np.float32)


def compute_ndmi(B8, B11):
    """
    NDMI = (NIR - SWIR1) / (NIR + SWIR1)
    Kandungan kelembaban vegetasi
    """
    with np.errstate(divide='ignore', invalid='ignore'):
        ndmi = np.where(
            (B8 + B11) == 0, 0,
            (B8 - B11) / (B8 + B11)
        )
    print(f"[NDMI] Min={ndmi.min():.3f}, Max={ndmi.max():.3f}, Mean={ndmi.mean():.3f}")
    return ndmi.astype(np.float32)


def save_index(index_array, meta, output_path):
    """Simpan indeks vegetasi sebagai GeoTIFF single-band."""
    meta.update(count=1, dtype='float32', nodata=-9999)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with rasterio.open(output_path, 'w', **meta) as dst:
        dst.write(index_array, 1)
    print(f"[SAVED] {output_path}")


def visualize_all(ndvi, evi, ndwi, ndmi, output_path):
    """Buat visualisasi 4-panel semua indeks."""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Indeks Vegetasi Mangrove\n(Referensi: SIGMEM, Remote Sensing 2024)',
                 fontsize=14, fontweight='bold')

    cmap = 'RdYlGn'  # Merah=rendah, Hijau=tinggi

    im1 = axes[0, 0].imshow(ndvi, cmap=cmap, vmin=-1, vmax=1)
    axes[0, 0].set_title('NDVI (Normalized Difference Vegetation Index)')
    axes[0, 0].axis('off')
    plt.colorbar(im1, ax=axes[0, 0], fraction=0.046)

    im2 = axes[0, 1].imshow(evi, cmap=cmap, vmin=-1, vmax=1)
    axes[0, 1].set_title('EVI (Enhanced Vegetation Index)')
    axes[0, 1].axis('off')
    plt.colorbar(im2, ax=axes[0, 1], fraction=0.046)

    im3 = axes[1, 0].imshow(ndwi, cmap='Blues', vmin=-1, vmax=1)
    axes[1, 0].set_title('NDWI (Normalized Difference Water Index)')
    axes[1, 0].axis('off')
    plt.colorbar(im3, ax=axes[1, 0], fraction=0.046)

    im4 = axes[1, 1].imshow(ndmi, cmap=cmap, vmin=-1, vmax=1)
    axes[1, 1].set_title('NDMI (Normalized Difference Moisture Index)')
    axes[1, 1].axis('off')
    plt.colorbar(im4, ax=axes[1, 1], fraction=0.046)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    print(f"[PLOT] Disimpan ke: {output_path}")
    plt.show()


def run_demo():
    """Demo dengan data sintetis (tanpa file GeoTIFF nyata)."""
    print("[DEMO] Menggunakan data acak — ganti dengan GeoTIFF Sentinel-2 asli!\n")
    np.random.seed(42)
    size = (256, 256)

    # Simulasi band Sentinel-2 (nilai 0-10000, surface reflectance)
    B2  = np.random.uniform(200, 800,  size)  # Blue
    B3  = np.random.uniform(300, 900,  size)  # Green
    B4  = np.random.uniform(200, 700,  size)  # Red
    B8  = np.random.uniform(800, 4000, size)  # NIR (tinggi untuk vegetasi)
    B11 = np.random.uniform(300, 1500, size)  # SWIR1

    # Normalisasi ke 0-1 (sudah surface reflectance ÷ 10000)
    B2 /= 10000; B3 /= 10000; B4 /= 10000
    B8 /= 10000; B11 /= 10000

    ndvi = compute_ndvi(B4, B8)
    evi  = compute_evi(B2, B4, B8)
    ndwi = compute_ndwi(B3, B8)
    ndmi = compute_ndmi(B8, B11)

    os.makedirs("data/output", exist_ok=True)
    visualize_all(ndvi, evi, ndwi, ndmi, "data/output/vegetation_indices_demo.png")
    print("\n✅ Demo selesai! Lihat: data/output/vegetation_indices_demo.png")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Hitung Indeks Vegetasi Mangrove")
    parser.add_argument("--input",  type=str, help="Path ke file GeoTIFF Sentinel-2")
    parser.add_argument("--output", type=str, default="data/output/", help="Folder output")
    parser.add_argument("--demo",   action="store_true", help="Jalankan dengan data demo")
    args = parser.parse_args()

    if args.demo or not args.input:
        run_demo()
    else:
        print(f"[INFO] Memproses: {args.input}")
        B2, B4, B8, B8a, B9, B11, meta = load_sentinel2_bands(args.input)

        # Normalisasi Sentinel-2 Level-2A (divide by 10000)
        B2 = B2 / 10000.0
        B4 = B4 / 10000.0
        B8 = B8 / 10000.0
        B11= B11 / 10000.0

        ndvi = compute_ndvi(B4, B8)
        evi  = compute_evi(B2, B4, B8)
        ndwi = compute_ndwi(B8a, B8)  # pakai B8a sebagai proxy Green
        ndmi = compute_ndmi(B8, B11)

        save_index(ndvi, meta, os.path.join(args.output, "ndvi.tif"))
        save_index(evi,  meta, os.path.join(args.output, "evi.tif"))
        save_index(ndwi, meta, os.path.join(args.output, "ndwi.tif"))
        save_index(ndmi, meta, os.path.join(args.output, "ndmi.tif"))

        visualize_all(ndvi, evi, ndwi, ndmi,
                      os.path.join(args.output, "vegetation_indices.png"))
