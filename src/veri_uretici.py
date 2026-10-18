import csv
import random
from datetime import datetime, timedelta

# Sabit seed sayesinde her çalıştırmada aynı veriler üretilir.
random.seed(42)

urunler = {
    "Elektronik": [
        ("Kulaklık", 750),
        ("Klavye", 900),
        ("Mouse", 500),
        ("Powerbank", 1200),
    ],
    "Giyim": [
        ("Tişört", 250),
        ("Pantolon", 600),
        ("Gömlek", 450),
        ("Mont", 1500),
    ],
    "Gıda": [
        ("Kahve", 180),
        ("Çikolata", 60),
        ("Makarna", 40),
        ("Süt", 35),
    ],
    "Ev ve Yaşam": [
        ("Masa Lambası", 400),
        ("Yastık", 250),
        ("Havlu", 150),
        ("Bardak Seti", 300),
    ],
    "Kozmetik": [
        ("Şampuan", 180),
        ("Parfüm", 900),
        ("Krem", 250),
        ("Deodorant", 140),
    ],
}

magazalar = [
    "Isparta Merkez",
    "Burdur Merkez",
    "Antalya Merkez",
    "Konya Merkez",
]

baslangic_tarihi = datetime(2026, 1, 1)

with open(
    "data/perakende-satislari.csv",
    "w",
    newline="",
    encoding="utf-8-sig"
) as dosya:

    yazici = csv.writer(dosya)

    yazici.writerow([
        "satis_id",
        "tarih",
        "urun",
        "kategori",
        "adet",
        "birim_fiyat",
        "toplam_tutar",
        "magaza",
    ])

    kategoriler = list(urunler.keys())

    for i in range(1, 151):
        kategori = random.choice(kategoriler)
        urun, temel_fiyat = random.choice(urunler[kategori])

        adet = random.randint(1, 5)

        fiyat_degisim = random.uniform(0.90, 1.10)
        birim_fiyat = round(temel_fiyat * fiyat_degisim, 2)

        toplam_tutar = round(adet * birim_fiyat, 2)

        tarih = baslangic_tarihi + timedelta(
            days=random.randint(0, 270)
        )

        magaza = random.choice(magazalar)

        yazici.writerow([
            f"S{i:04d}",
            tarih.strftime("%Y-%m-%d"),
            urun,
            kategori,
            adet,
            birim_fiyat,
            toplam_tutar,
            magaza,
        ])

print("data/perakende-satislari.csv başarıyla oluşturuldu.")
print("Toplam 150 sentetik satış kaydı üretildi.")
random.seed(42)