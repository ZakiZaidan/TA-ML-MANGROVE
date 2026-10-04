"""
test_setup.py - Jalankan untuk cek semua library terpasang dengan benar
Cara: python test_setup.py
"""
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

print("=" * 50)
print("  TEST SETUP WEBGIS MANGROVE")
print("=" * 50)

tests = []

def check(name, import_fn):
    try:
        version = import_fn()
        print(f"  [OK]  {name:20s} {version}")
        tests.append((name, True))
    except Exception as e:
        print(f"  [!!]  {name:20s} GAGAL - {str(e)[:50]}")
        tests.append((name, False))

check("Django",         lambda: __import__('django').get_version())
check("DRF",            lambda: __import__('rest_framework').__version__)
check("GeoPandas",      lambda: __import__('geopandas').__version__)
check("Rasterio",       lambda: __import__('rasterio').__version__)
check("Shapely",        lambda: __import__('shapely').__version__)
check("Pyproj",         lambda: __import__('pyproj').__version__)
check("NumPy",          lambda: __import__('numpy').__version__)
check("Pandas",         lambda: __import__('pandas').__version__)
check("Scikit-learn",   lambda: __import__('sklearn').__version__)
check("Joblib",         lambda: __import__('joblib').__version__)
check("Folium",         lambda: __import__('folium').__version__)
check("Matplotlib",     lambda: __import__('matplotlib').__version__)
check("Psycopg2",       lambda: __import__('psycopg2').__version__)
check("Celery",         lambda: __import__('celery').__version__)
check("Redis-py",       lambda: __import__('redis').__version__)
check("Requests",       lambda: __import__('requests').__version__)
# FIX: pakai importlib.metadata agar robust di semua versi dotenv
check("Python-dotenv",  lambda: __import__('importlib.metadata', fromlist=['version']).version('python-dotenv'))

# GDAL butuh cara khusus
try:
    from osgeo import gdal
    print(f"  [OK]  {'GDAL':20s} {gdal.__version__}")
    tests.append(("GDAL", True))
except Exception:  # FIX: jangan gunakan bare except tanpa exception class
    print(f"  [!!]  {'GDAL':20s} GAGAL - Install via wheel file!")
    print("         Download: https://github.com/cgohlke/geospatial-wheels/releases")
    print("         Pilih: GDAL-*-cp310-cp310-win_amd64.whl")
    tests.append(("GDAL", False))

# GEE (opsional — tidak dihitung dalam total)
try:
    import ee
    print(f"  [OK]  {'Earth Engine':20s} {ee.__version__}")
except Exception:
    print(f"  [--]  {'Earth Engine':20s} Tidak terinstall (opsional)")

print("\n" + "=" * 50)
passed = sum(1 for _, ok in tests if ok)
total = len(tests)
print(f"  Hasil: {passed}/{total} library berhasil")
if passed == total:
    print("  [**] Semua siap! Kamu bisa mulai coding.")
else:
    failed = [name for name, ok in tests if not ok]
    print(f"  [!]  Yang perlu difix: {', '.join(failed)}")
    print("  Lihat SETUP.md bagian Troubleshooting")
print("=" * 50)
