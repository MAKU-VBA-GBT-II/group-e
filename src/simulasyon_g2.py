"""G2 parametreli perakende satis simulasyonu (BE gorevi, #26).

Gorev 2 veri kumesi icin en az iki ayarlanabilir parametre ile sentetik
perakende satis verisi uretir. Cikti: data/perakende-satislari-g2.csv
(sutunlar docs/veri-sozlugu-g1.md ile ayni semaya sahiptir).

Kullanim:
    python src/simulasyon_g2.py
    python src/simulasyon_g2.py --kayit-sayisi 300 --baslangic-tarihi 2026-02-01
    python src/simulasyon_g2.py --seed 7
"""
from __future__ import annotations

import argparse
import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT_DIR / "data" / "perakende-satislari-g2.csv"

KATEGORILER = {
    "Elektronik": ["Kulaklık", "Powerbank", "Akıllı Saat", "Şarj Kablosu"],
    "Giyim": ["T-Shirt", "Mont", "Pantolon", "Sweatshirt"],
    "Gıda": ["Kahve", "Çikolata", "Zeytinyağı", "Çay"],
    "Ev ve Yaşam": ["Kupa", "Masa Lambası", "Yastık", "Organizer"],
    "Kozmetik": ["Parfüm", "Yüz Kremi", "Şampuan", "Diş Macunu"],
}

MAGAZALAR = ["Isparta", "Burdur", "Antalya", "Konya Merkez"]
VARSAYILAN_KAYIT = 150
VARSAYILAN_BASLANGIC = datetime(2026, 1, 1)
VARSAYILAN_SEED = 42


def veri_uret(kayit_sayisi: int, baslangic: datetime, seed: int) -> list[dict]:
    random.seed(seed)
    veriler: list[dict] = []
    sim_tarihi = baslangic

    for i in range(1, kayit_sayisi + 1):
        satis_id = f"SAT-{i:04d}"
        sim_tarihi += timedelta(days=random.choice([0, 1]))
        tarih_str = sim_tarihi.strftime("%Y-%m-%d")

        kategori = random.choice(list(KATEGORILER.keys()))
        urun = random.choice(KATEGORILER[kategori])

        adet = random.randint(1, 5)
        birim_fiyat = round(random.uniform(50.0, 3500.0), 2)
        toplam_tutar = round(adet * birim_fiyat, 2)
        magaza = random.choice(MAGAZALAR)

        veriler.append({
            "satis_id": satis_id,
            "tarih": tarih_str,
            "urun": urun,
            "kategori": kategori,
            "adet": adet,
            "birim_fiyat": birim_fiyat,
            "toplam_tutar": toplam_tutar,
            "magaza": magaza,
        })

    return veriler


def csv_kaydet(dosya_yolu: Path, veriler: list[dict]) -> None:
    alanlar = [
        "satis_id", "tarih", "urun", "kategori", "adet",
        "birim_fiyat", "toplam_tutar", "magaza",
    ]
    dosya_yolu.parent.mkdir(parents=True, exist_ok=True)
    with open(dosya_yolu, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=alanlar, lineterminator="\n")
        writer.writeheader()
        writer.writerows(veriler)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="G2 parametreli perakende satis simulasyonu"
    )
    parser.add_argument("--kayit-sayisi", type=int, default=VARSAYILAN_KAYIT,
                        help="Uretilecek kayit sayisi (varsayilan: 150)")
    parser.add_argument("--baslangic-tarihi", type=str,
                        default=VARSAYILAN_BASLANGIC.strftime("%Y-%m-%d"),
                        help="Baslangic tarihi YYYY-MM-DD (varsayilan: 2026-01-01)")
    parser.add_argument("--seed", type=int, default=VARSAYILAN_SEED,
                        help="Tekrarlanabilirlik icin sabit tohum (varsayilan: 42)")
    parser.add_argument("--cikti", type=str, default=str(DATA_PATH),
                        help="Cikti CSV yolu (varsayilan: data/perakende-satislari-g2.csv)")
    args = parser.parse_args()

    baslangic = datetime.strptime(args.baslangic_tarihi, "%Y-%m-%d")
    veriler = veri_uret(args.kayit_sayisi, baslangic, args.seed)
    cikti_yolu = Path(args.cikti)
    if not cikti_yolu.is_absolute():
        cikti_yolu = ROOT_DIR / cikti_yolu
    csv_kaydet(cikti_yolu, veriler)
    print(f"{len(veriler)} gecerli satis kaydi uretildi.")
    print(f"Cikti: {cikti_yolu}")
    print(f"Parametreler: kayit_sayisi={args.kayit_sayisi}, "
          f"baslangic_tarihi={args.baslangic_tarihi}, seed={args.seed}")


if __name__ == "__main__":
    main()
