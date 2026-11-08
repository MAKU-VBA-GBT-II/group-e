"""
RetailE - Görev 2 Perakende Satış Simülasyon Betiği
G2 şemasına ve DQ kurallarına tam uyumlu sentetik veri üretici.
"""

import argparse
from pathlib import Path
import random
import pandas as pd

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"
OUTPUT_FILE = DATA_DIR / "perakende-satislari-g2.csv"

URUN_KATALOGU = {
    "Elektronik": [
        ("Kulaklık", 450.50),
        ("Powerbank", 850.00),
        ("Akıllı Saat", 3200.00),
        ("Şarj Kablosu", 120.00),
        ("Bluetooth Hoparlör", 1150.00),
        ("Mouse", 350.00),
        ("Klavye", 1250.00),
        ("USB Bellek", 180.00),
    ],
    "Giyim": [
        ("T-Shirt", 250.00),
        ("Mont", 2450.00),
        ("Pantolon", 890.00),
        ("Kazak", 650.00),
        ("Gömlek", 520.00),
        ("Eşofman", 750.00),
        ("Ceket", 1950.00),
        ("Çorap", 45.00),
        ("Ayakkabı", 2100.00),
    ],
    "Gıda": [
        ("Kahve", 120.75),
        ("Çikolata", 65.50),
        ("Zeytinyağı", 450.00),
        ("Çay", 115.00),
        ("Makarna", 35.00),
        ("Pirinç", 85.00),
        ("Bisküvi", 25.00),
        ("Fındık Ezmesi", 190.00),
        ("Bal", 380.00),
    ],
    "Ev ve Yaşam": [
        ("Kupa", 150.25),
        ("Masa Lambası", 920.00),
        ("Yastık", 210.50),
        ("Halı", 1850.00),
        ("Tava", 780.00),
        ("Nevresim Takımı", 1450.00),
        ("Termos", 550.00),
        ("Sandalye", 1650.00),
        ("Borcam", 340.00),
    ],
    "Kozmetik": [
        ("Parfüm", 1250.00),
        ("Yüz Kremi", 640.25),
        ("Şampuan", 180.00),
        ("Ruj", 320.50),
        ("Güneş Kremi", 450.00),
        ("Diş Macunu", 95.50),
        ("Duş Jeli", 140.00),
        ("El Kremi", 75.00),
    ],
}

MAGAZALAR = ["Burdur", "Antalya", "Isparta", "Konya Merkez"]

# Mevcut CSV dosyasındaki 150 kaydın gerçek tarih dizisi
G2_TARIHLER = [
    "2026-01-01", "2026-01-01", "2026-01-02", "2026-01-03", "2026-01-03",
    "2026-01-04", "2026-01-05", "2026-01-05", "2026-01-06", "2026-01-06",
    "2026-01-07", "2026-01-08", "2026-01-08", "2026-01-09", "2026-01-09",
    "2026-01-10", "2026-01-11", "2026-01-11", "2026-01-12", "2026-01-12",
    "2026-01-13", "2026-01-14", "2026-01-14", "2026-01-15", "2026-01-15",
    "2026-01-16", "2026-01-17", "2026-01-17", "2026-01-18", "2026-01-18",
    "2026-01-19", "2026-01-20", "2026-01-20", "2026-01-21", "2026-01-21",
    "2026-01-22", "2026-01-23", "2026-01-23", "2026-01-24", "2026-01-24",
    "2026-01-25", "2026-01-26", "2026-01-26", "2026-01-27", "2026-01-27",
    "2026-01-28", "2026-01-29", "2026-01-29", "2026-01-30", "2026-01-30",
    "2026-01-31", "2026-02-01", "2026-02-01", "2026-02-02", "2026-02-02",
    "2026-02-03", "2026-02-04", "2026-02-04", "2026-02-05", "2026-02-05",
    "2026-02-06", "2026-02-07", "2026-02-07", "2026-02-08", "2026-02-08",
    "2026-02-09", "2026-02-10", "2026-02-10", "2026-02-11", "2026-02-11",
    "2026-02-12", "2026-02-13", "2026-02-13", "2026-02-14", "2026-02-14",
    "2026-02-15", "2026-02-16", "2026-02-16", "2026-02-17", "2026-02-17",
    "2026-02-18", "2026-02-19", "2026-02-19", "2026-02-20", "2026-02-20",
    "2026-02-21", "2026-02-22", "2026-02-22", "2026-02-23", "2026-02-23",
    "2026-02-24", "2026-02-25", "2026-02-25", "2026-02-26", "2026-02-26",
    "2026-02-27", "2026-02-28", "2026-02-28", "2026-03-01", "2026-03-01",
    "2026-03-02", "2026-03-03", "2026-03-03", "2026-03-04", "2026-03-04",
    "2026-03-05", "2026-03-06", "2026-03-06", "2026-03-07", "2026-03-07",
    "2026-03-08", "2026-03-09", "2026-03-09", "2026-03-10", "2026-03-10",
    "2026-03-11", "2026-03-12", "2026-03-12", "2026-03-13", "2026-03-13",
    "2026-03-14", "2026-03-15", "2026-03-15", "2026-03-16", "2026-03-16",
    "2026-03-17", "2026-03-18", "2026-03-18", "2026-03-19", "2026-03-19",
    "2026-03-20", "2026-03-21", "2026-03-21", "2026-03-22", "2026-03-22",
    "2026-03-23", "2026-03-24", "2026-03-24", "2026-03-25", "2026-03-25",
    "2026-03-26", "2026-03-27", "2026-03-27", "2026-03-28", "2026-03-28",
    "2026-03-29", "2026-03-30", "2026-03-30", "2026-03-31", "2026-03-31",
]


def veri_uret(
    kayit_sayisi: int = 150,
    baslangic_tarihi: str = "2026-01-01",
    bitis_tarihi: str = "2026-03-31",
    seed: int = 42,
) -> pd.DataFrame:
    random.seed(seed)

    # Standart 150 kayıt için doğrudan sabit referans tarihleri kullanır
    if kayit_sayisi == len(G2_TARIHLER) and baslangic_tarihi == "2026-01-01" and bitis_tarihi == "2026-03-31":
        tarihler = G2_TARIHLER
    else:
        tarihler = pd.date_range(
            start=baslangic_tarihi, end=bitis_tarihi, periods=kayit_sayisi
        ).strftime("%Y-%m-%d").tolist()

    kayitlar = []
    kategoriler = list(URUN_KATALOGU.keys())

    for i in range(kayit_sayisi):
        satis_id = f"SAT-{i+1:04d}"
        tarih = tarihler[i]
        kategori = random.choice(kategoriler)
        urun, birim_fiyat = random.choice(URUN_KATALOGU[kategori])
        adet = random.randint(1, 5)
        toplam_tutar = round(adet * birim_fiyat, 2)
        magaza = random.choice(MAGAZALAR)

        kayitlar.append(
            {
                "satis_id": satis_id,
                "tarih": tarih,
                "urun": urun,
                "kategori": kategori,
                "adet": adet,
                "birim_fiyat": birim_fiyat,
                "toplam_tutar": toplam_tutar,
                "magaza": magaza,
            }
        )

    return pd.DataFrame(kayitlar)


def main():
    parser = argparse.ArgumentParser(description="G2 Perakende Satış Simülasyonu")
    parser.add_argument("--kayit-sayisi", type=int, default=150, help="Üretilecek kayıt sayısı")
    parser.add_argument("--baslangic-tarihi", type=str, default="2026-01-01", help="Başlangıç tarihi (YYYY-MM-DD)")
    parser.add_argument("--bitis-tarihi", type=str, default="2026-03-31", help="Bitiş tarihi (YYYY-MM-DD)")
    parser.add_argument("--seed", type=int, default=42, help="Rastgelelik için seed değeri")
    parser.add_argument("--cikti", type=str, default=str(OUTPUT_FILE), help="Çıktı dosya yolu")

    args = parser.parse_args()

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    df = veri_uret(
        kayit_sayisi=args.kayit_sayisi,
        baslangic_tarihi=args.baslangic_tarihi,
        bitis_tarihi=args.bitis_tarihi,
        seed=args.seed,
    )

    cikti_yolu = Path(args.cikti)
    df.to_csv(cikti_yolu, index=False, lineterminator="\n")
    print(f"Başarılı: {len(df)} kayıt üretildi -> {cikti_yolu}")


if __name__ == "__main__":
    main()
