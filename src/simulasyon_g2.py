import csv
from datetime import datetime, timedelta
import random

# Ayarlanabilir parametreler (G2 gereksinimi için)
KAYIT_SAYISI = 150
BASLANGIC_TARIHI = datetime(2026, 1, 1)

KATEGORILER = {
    "Elektronik": ["Kulaklık", "Powerbank", "Akıllı Saat", "Şarj Kablosu"],
    "Giyim": ["T-Shirt", "Mont", "Pantolon", "Sweatshirt"],
    "Gıda": ["Kahve", "Çikolata", "Zeytinyağı", "Çay"],
    "Ev ve Yaşam": ["Kupa", "Masa Lambası", "Yastık", "Organizer"],
    "Kozmetik": ["Parfüm", "Yüz Kremi", "Şampuan", "Diş Macunu"],
}

MAGAZALAR = ["Isparta", "Burdur", "Antalya", "Konya Merkez"]


def veri_uret(kayit_sayisi=KAYIT_SAYISI):
  veriler = []
  sim_tarihi = BASLANGIC_TARIHI

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


def csv_kaydet(dosya_yolu, veriler):
  alanlar = [
      "satis_id",
      "tarih",
      "urun",
      "kategori",
      "adet",
      "birim_fiyat",
      "toplam_tutar",
      "magaza",
  ]
  with open(dosya_yolu, mode="w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=alanlar)
    writer.writeheader()
    writer.writerows(veriler)


if __name__ == "__main__":
  uretilen_veri = veri_uret()
  csv_kaydet("data/perakende-satislari-g2.csv", uretilen_veri)
