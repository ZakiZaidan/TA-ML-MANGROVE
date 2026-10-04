"""Demo singkat Random Forest tanpa geopandas — bisa langsung jalan."""
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, cohen_kappa_score, confusion_matrix
import joblib, os

print("=" * 55)
print("  DEMO: Random Forest Klasifikasi Mangrove")
print("  Referensi: SIGMEM OA=94.11%, Kappa=0.94")
print("=" * 55)

np.random.seed(42)
n = 5517
n_non = n // 2
n_man = n - n_non

# Simulasi fitur indeks vegetasi 5 kolom: NDVI, EVI, NDWI, NDMI, RDVI
X = np.column_stack([
    np.concatenate([np.random.normal(0.30, 0.20, n_non), np.random.normal(0.72, 0.10, n_man)]),
    np.concatenate([np.random.normal(0.25, 0.15, n_non), np.random.normal(0.55, 0.10, n_man)]),
    np.concatenate([np.random.normal(0.10, 0.20, n_non), np.random.normal(-0.20, 0.15, n_man)]),
    np.concatenate([np.random.normal(0.10, 0.15, n_non), np.random.normal(0.45, 0.10, n_man)]),
    np.concatenate([np.random.normal(0.20, 0.10, n_non), np.random.normal(0.60, 0.10, n_man)]),
])
y = np.array([0] * n_non + [1] * n_man)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print(f"\nData: {len(X_train)} training / {len(X_test)} validasi")
print("Fitur: NDVI, EVI, NDWI, NDMI, RDVI")

# Training
rf = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)

# Evaluasi
oa    = accuracy_score(y_test, y_pred) * 100
kappa = cohen_kappa_score(y_test, y_pred)
cm    = confusion_matrix(y_test, y_pred)

print(f"\nHASIL EVALUASI:")
print(f"  Overall Accuracy (OA) : {oa:.2f}%")
print(f"  Kappa Index           : {kappa:.4f}")

if kappa > 0.80:
    interp = "Hampir Sempurna (>0.80) - target jurnal SIGMEM/Bintuni"
elif kappa > 0.60:
    interp = "Substansial (0.60-0.80)"
else:
    interp = "Moderat (<0.60)"
print(f"  Interpretasi Kappa    : {interp}")

print(f"\nConfusion Matrix:")
print(f"  {'':15s}  Pred Non-Mangrove  Pred Mangrove")
print(f"  {'Aktual Non-Mang':15s}  {cm[0][0]:17d}  {cm[0][1]:12d}")
print(f"  {'Aktual Mangrove':15s}  {cm[1][0]:17d}  {cm[1][1]:12d}")

# Feature importance
features = ['NDVI', 'EVI', 'NDWI', 'NDMI', 'RDVI']
importances = rf.feature_importances_
ranked = sorted(zip(features, importances), key=lambda x: x[1], reverse=True)
print(f"\nFeature Importance (seperti SIGMEM pakai NDVI, RDVI, NDWI):")
for name, imp in ranked:
    bar = "#" * int(imp * 40)
    print(f"  {name:6s}  {bar:40s}  {imp:.4f}")

# Simpan model
os.makedirs("ml/models", exist_ok=True)
joblib.dump(rf, "ml/models/rf_mangrove.pkl")
print(f"\n[SAVED] Model tersimpan: ml/models/rf_mangrove.pkl")
print("[DONE]  Demo berhasil! Ganti data dengan shapefile KLHK untuk TA nyata.")
