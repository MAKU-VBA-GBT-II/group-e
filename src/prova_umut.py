import csv
import os
import random

# data klasörünü garantiye al
os.makedirs("data", exist_ok=True)

# 1 ile 100 arasında 10 rastgele tam sayı üret
sayilar = [random.randint(1, 100) for _ in range(10)]

# data/prova-umut.csv dosyasına yaz
with open("data/prova-umut.csv", mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["deger"])
    for sayi in sayilar:
        writer.writerow([sayi])

print("data/prova-umut.csv başarıyla oluşturuldu!")