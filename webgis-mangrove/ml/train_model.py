"""
ml/train_model.py
Training model Random Forest untuk klasifikasi mangrove
Referensi: Jurnal SIGMEM (OA=94.11%) & Jurnal Bintuni (Kappa=0.94)

Cara pakai:
    python train_model.py --demo        (demo dengan data sintetis)
    python train_model.py --shapefile data/raw/mangrove_2023.shp
"""

import numpy as np
import pandas as pd
import geopandas as gpd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.metrics import (accuracy_score, classification_report,
                             confusion_matrix, cohen_kappa_score)
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import argparse
import os


def kappa_index(y_true, y_pred):
    """Hitung Cohen's Kappa Index (metrik utama di jurnal mangrove)."""
    return cohen_kappa_score(y_true, y_pred)


def train_random_forest(X_train, y_train, n_estimators=100, random_state=42):
    """
    Training Random Forest dengan pipeline (scaler + RF).
    Sesuai metodologi SIGMEM: RF lebih unggul dari Naive Bayes (OA=94.11%)
    """
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('rf', RandomForestClassifier(
            n_estimators=n_estimators,
            max_depth=None,           # Biarkan pohon tumbuh penuh
            min_samples_split=2,
            min_samples_leaf=1,
            max_features='sqrt',      # sqrt(n_features) per split
            bootstrap=True,
            random_state=random_state,
            n_jobs=-1,                # Pakai semua CPU core
            verbose=0
        ))
    ])

    print(f"[TRAIN] Training Random Forest ({n_estimators} trees)...")
    pipeline.fit(X_train, y_train)
    print("[TRAIN] Selesai!")
    return pipeline


def evaluate_model(model, X_test, y_test, class_names=None):
    """Evaluasi model — hitung semua metrik seperti di jurnal."""
    y_pred = model.predict(X_test)

    oa = accuracy_score(y_test, y_pred) * 100
    kappa = kappa_index(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)

    print("\n" + "="*55)
    print("  HASIL EVALUASI MODEL")
    print("="*55)
    print(f"  Overall Accuracy (OA) : {oa:.2f}%")
    print(f"  Kappa Index           : {kappa:.4f}")
    print(f"\n  Interpretasi Kappa:")
    if   kappa > 0.80: print(f"    → Hampir sempurna (>0.80) ✅")
    elif kappa > 0.60: print(f"    → Substansial (0.60–0.80) ✅")
    elif kappa > 0.40: print(f"    → Moderat (0.40–0.60) ⚠️")
    else:               print(f"    → Lemah (<0.40) ❌")

    if class_names:
        print(f"\n  Classification Report:")
        print(classification_report(y_test, y_pred, target_names=class_names))

    print("="*55)

    return {"OA": oa, "Kappa": kappa, "confusion_matrix": cm, "y_pred": y_pred}


def plot_feature_importance(model, feature_names, output_path="data/output/feature_importance.png"):
    """Visualisasi fitur paling penting (seperti jurnal SIGMEM — NDVI, RDVI, NDWI)."""
    rf = model.named_steps['rf']
    importances = rf.feature_importances_
    indices = np.argsort(importances)[::-1]

    plt.figure(figsize=(10, 6))
    plt.title('Feature Importance — Seleksi Fitur Seperti SIGMEM\n(Top features yang dipilih: NDVI, RDVI, NDWI)', fontsize=12)
    bars = plt.bar(range(len(feature_names)), importances[indices], color='steelblue', edgecolor='black')
    plt.xticks(range(len(feature_names)), [feature_names[i] for i in indices], rotation=45, ha='right')
    plt.ylabel('Importance Score')
    plt.xlabel('Fitur')
    plt.tight_layout()

    os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else ".", exist_ok=True)
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    print(f"[PLOT] Feature importance disimpan: {output_path}")
    plt.show()


def plot_confusion_matrix(cm, class_names, output_path="data/output/confusion_matrix.png"):
    """Visualisasi confusion matrix."""
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=class_names, yticklabels=class_names)
    plt.title('Confusion Matrix — Evaluasi Klasifikasi Mangrove', fontsize=12)
    plt.ylabel('Aktual')
    plt.xlabel('Prediksi')
    plt.tight_layout()
    os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else ".", exist_ok=True)
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    print(f"[PLOT] Confusion matrix disimpan: {output_path}")
    plt.show()


def demo_with_synthetic_data():
    """
    Demo LENGKAP dengan data sintetis.
    Simulasi: klasifikasi mangrove/non-mangrove berdasarkan indeks vegetasi.
    """
    print("=" * 55)
    print("  DEMO: Training Random Forest Mangrove")
    print("  (Data sintetis — ganti dengan data nyata!)")
    print("=" * 55)
    np.random.seed(42)
    n_samples = 5517  # Sama dengan jurnal SIGMEM

    # Simulasi fitur spektral (mirip Sentinel-2)
    # Mangrove: NDVI tinggi (~0.7), NDWI rendah, NDMI tinggi
    # Non-mangrove: NDVI variasi, tergantung kelas

    # Kelas 0 = Non-Mangrove (~50%)
    n_non = n_samples // 2
    ndvi_non  = np.random.normal(0.3,  0.2, n_non)
    evi_non   = np.random.normal(0.25, 0.15, n_non)
    ndwi_non  = np.random.normal(0.1,  0.2, n_non)
    ndmi_non  = np.random.normal(0.1,  0.15, n_non)
    rdvi_non  = np.random.normal(0.2,  0.1, n_non)

    # Kelas 1 = Mangrove (~50%)
    n_man = n_samples - n_non
    ndvi_man  = np.random.normal(0.72, 0.1, n_man)
    evi_man   = np.random.normal(0.55, 0.1, n_man)
    ndwi_man  = np.random.normal(-0.2, 0.15, n_man)
    ndmi_man  = np.random.normal(0.45, 0.1, n_man)
    rdvi_man  = np.random.normal(0.6,  0.1, n_man)

    # Gabungkan
    X = np.column_stack([
        np.concatenate([ndvi_non, ndvi_man]),
        np.concatenate([evi_non,  evi_man]),
        np.concatenate([ndwi_non, ndwi_man]),
        np.concatenate([ndmi_non, ndmi_man]),
        np.concatenate([rdvi_non, rdvi_man]),
    ])
    y = np.array([0]*n_non + [1]*n_man)
    feature_names = ['NDVI', 'EVI', 'NDWI', 'NDMI', 'RDVI']
    class_names   = ['Non-Mangrove', 'Mangrove']

    print(f"\n[DATA] Total sampel: {n_samples}")
    print(f"[DATA] Non-mangrove: {n_non} | Mangrove: {n_man}")
    print(f"[DATA] Fitur: {feature_names}")

    # Split 80% train, 20% validasi (sama dengan SIGMEM)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    print(f"\n[SPLIT] Training: {len(X_train)} | Validasi: {len(X_test)}")

    # Training
    model = train_random_forest(X_train, y_train, n_estimators=100)

    # Evaluasi
    results = evaluate_model(model, X_test, y_test, class_names)

    # Visualisasi
    os.makedirs("data/output", exist_ok=True)
    plot_feature_importance(model, feature_names, "data/output/feature_importance.png")
    plot_confusion_matrix(results['confusion_matrix'], class_names, "data/output/confusion_matrix.png")

    # Simpan model
    os.makedirs("ml/models", exist_ok=True)
    model_path = "ml/models/rf_mangrove.pkl"
    joblib.dump(model, model_path)
    print(f"\n[SAVED] Model disimpan: {model_path}")
    print(f"[LOAD]  Cara load: model = joblib.load('{model_path}')")

    return model, results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Training Random Forest Mangrove")
    parser.add_argument("--demo",       action="store_true", help="Jalankan demo data sintetis")
    parser.add_argument("--shapefile",  type=str, help="Path ke shapefile ground truth")
    parser.add_argument("--output",     type=str, default="ml/models/rf_mangrove.pkl")
    args = parser.parse_args()

    if args.demo or not args.shapefile:
        model, results = demo_with_synthetic_data()
        print("\n✅ Demo selesai! Ganti dengan data nyata dari KLHK/survei lapangan.")
    else:
        print(f"[INFO] Loading shapefile: {args.shapefile}")
        gdf = gpd.read_file(args.shapefile)
        print(f"[INFO] Kolom: {list(gdf.columns)}")
        print(f"[INFO] CRS: {gdf.crs}")
        # Lanjutkan sesuai struktur data kamu...
        print("[TODO] Sesuaikan kode ini dengan kolom shapefile kamu!")
