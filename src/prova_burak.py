
import csv
import random
from pathlib import Path

# Projenin ana klasörünü bul
proje_klasoru = Path(__file__).resolve().parent.parent

# Çıktı klasörünü ve dosya yolunu belirle
data_klasoru = proje_klasoru / "data"
data_klasoru.mkdir(parents=True, exist_ok=True)

csv_dosyasi = data_klasoru / "prova-burak.csv"

# 1 ile 100 arasında 10 rastgele sayı üret
sayilar = [random.randint(1, 100) for _ in range(10)]

# Sayıları tek sütunlu CSV dosyasına yaz
with csv_dosyasi.open("w", newline="", encoding="utf-8") as dosya:
    yazici = csv.writer(dosya)
    yazici.writerow(["deger"])
    for sayi in sayilar:
        yazici.writerow([sayi])

print(f"CSV dosyası oluşturuldu: {csv_dosyasi}")
print(f"Üretilen sayı adedi: {len(sayilar)}")
