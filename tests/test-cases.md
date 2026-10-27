# Test Senaryoları

| Test ID | Senaryo | Girdi | Adımlar | Beklenen Sonuç |
|---|---|---|---|---|
| TC-01 | Analiz betiğinin çalıştırılması | `python src/analiz_g1.py` | 1. Terminali aç 2. Komutu çalıştır | Betiğin hatasız çalışması ve metrikleri ekrana yazdırması |
| TC-02 | CSV verisinin okunması | `data/perakende-satislari.csv` | 1. Veri yolunu kontrol et 2. Betiği çalıştır | Dosyanın okunması ve hata vermemesi |
| TC-03 | Toplam satış tutarının doğruluğu | CSV `toplam_tutar` sütunu | 1. Veriyi topla 2. Çıktıyı kontrol et | Toplam satışın 239.182,23 TL olarak görünmesi |