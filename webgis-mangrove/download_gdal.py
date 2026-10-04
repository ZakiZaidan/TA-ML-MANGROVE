"""Cari dan download GDAL wheel untuk Python 3.10 Windows 64-bit."""
import urllib.request
import json
import os

print("Mencari GDAL wheel untuk Python 3.10 Windows 64-bit...")

try:
    url = "https://api.github.com/repos/cgohlke/geospatial-wheels/releases"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=15) as r:
        releases = json.loads(r.read())

    gdal_url = None
    gdal_name = None

    for release in releases[:5]:  # cek 5 release terbaru
        tag = release.get("tag_name", "")
        assets = release.get("assets", [])
        for asset in assets:
            name = asset["name"]
            if "GDAL" in name and "cp310" in name and "win_amd64" in name and name.endswith(".whl"):
                gdal_url = asset["browser_download_url"]
                gdal_name = name
                print(f"Ditemukan di release {tag}: {name}")
                break
        if gdal_url:
            break

    if gdal_url:
        dest = os.path.join(os.path.expanduser("~"), "Downloads", gdal_name)
        print(f"\nMulai download ke: {dest}")
        print("(Ini mungkin butuh 1-2 menit tergantung kecepatan internet...)")

        def progress(count, block_size, total_size):
            if total_size > 0:
                pct = count * block_size * 100 // total_size
                mb_done = count * block_size / 1_000_000
                mb_total = total_size / 1_000_000
                print(f"\r  {pct}% ({mb_done:.1f}/{mb_total:.1f} MB)", end="", flush=True)

        urllib.request.urlretrieve(gdal_url, dest, reporthook=progress)
        print(f"\n\nDownload selesai!")
        print(f"\nSekarang install dengan perintah:")
        print(f'  pip install "{dest}"')
    else:
        print("\nTidak ditemukan otomatis. Download manual dari:")
        print("  https://github.com/cgohlke/geospatial-wheels/releases")
        print("  Cari: GDAL-*-cp310-cp310-win_amd64.whl")

except Exception as e:
    print(f"Error: {e}")
    print("\nDownload manual dari:")
    print("  https://github.com/cgohlke/geospatial-wheels/releases")
