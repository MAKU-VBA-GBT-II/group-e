# G2 — RetailE Veri Sözlüğü ve Analiz Planı

## 1. Amaç ve kapsam
Bu belge, RetailE perakende mini veri kümesinin alanlarını ve DQ rolünün hesaplayacağı beş metriği tanımlar. G2 veri kümesi `data/perakende-satislari-g2.csv` ve `src/simulasyon_g2.py` temel alınmıştır. Ana daldaki G2 CSV dosyasında 150 satış kaydı ve 8 sütun bulunmaktadır. G1 veri kümesi `data/perakende-satislari.csv` yalnızca önceki aşamanın referansıdır.

## 2. Referans veri kümesi
- Mevcut referans: `data/perakende-satislari.csv` (G1)
- Kayıt türü: sentetik perakende satış işlemi
- G1 kayıt sayısı: 150
- G1 alan sayısı: 8
- G2 veri dosyası: `data/perakende-satislari-g2.csv` (ana dalda mevcut)
- G2 kayıt sayısı: 150
- G2 alan sayısı: 8
- G2 üretim betiği: `src/simulasyon_g2.py`
- Üretim fonksiyonu parametreleri: `kayit_sayisi` (150), `baslangic_tarihi` (2026-01-01), `bitis_tarihi` (2026-03-31), `seed` (42). `main()` bu değerleri CLI'dan alır; `--cikti` ile dosya yolu değiştirilebilir.
- Tarih aralığı (betikte): 2026-01-01–2026-03-31.

## 3. Alan sözlüğü (G2 şeması)

| Alan | Veri türü | Açıklama | Kural / örnek | Birim |
| --- | --- | --- | --- | --- |
| `satis_id` | Metin | İşlemin benzersiz kimliği | Boş ve tekrarlı olmamalı | — |
| `tarih` | Tarih | İşlem tarihi | `YYYY-MM-DD`, geçerli tarih | — |
| `urun` | Metin | Satılan ürün | Boş olmamalı | — |
| `kategori` | Metin | Ürün ana kategorisi | Elektronik, Giyim, Gıda, Ev ve Yaşam, Kozmetik | — |
| `adet` | Tamsayı | Satılan miktar | G2 betiğinde 1–5 | adet |
| `birim_fiyat` | Ondalıklı sayı | Birim satış fiyatı | Sıfırdan büyük | TL/adet |
| `toplam_tutar` | Ondalıklı sayı | Satır satış tutarı | `adet × birim_fiyat` (kuruş yuvarlamasıyla) | TL |
| `magaza` | Metin | Satışın gerçekleştiği mağaza | G2 betiğinde Isparta, Burdur, Antalya, Konya Merkez | — |

## 4. Hesaplanacak beş metrik

| No | Metrik | Hesaplama | Birim | Kullanılan alanlar |
| --- | --- | --- | --- | --- |
| M1 | Toplam satış geliri | `SUM(toplam_tutar)` | TL | `toplam_tutar` |
| M2 | Ortalama işlem tutarı | `SUM(toplam_tutar) / satış kaydı sayısı` | TL/işlem | `toplam_tutar`, kayıt sayısı |
| M3 | Toplam satılan ürün adedi | `SUM(adet)` | adet | `adet` |
| M4 | Kategori bazında satış geliri | `kategori` bazında `SUM(toplam_tutar)`; büyükten küçüğe sırala | TL/kategori | `kategori`, `toplam_tutar` |
| M5 | Mağaza bazında satış geliri | `magaza` bazında `SUM(toplam_tutar)`; büyükten küçüğe sırala | TL/mağaza | `magaza`, `toplam_tutar` |

Not: Her CSV satırı bir satış işlemi kabul edilmiştir; aynı sepetin birden fazla satıra bölündüğü farklı bir G2 modeli gelirse M2'nin tanımı yeniden gözden geçirilmelidir.

## 5. Kalite ve analiz kuralları
1. CSV dosyası okunabilmeli; başlıklar G2 BE şemasıyla eşleşmeli.
2. `satis_id` boş veya tekrarlı olmamalı.
3. `tarih` geçerli ISO tarih biçiminde olmalı.
4. `adet` pozitif tamsayı; `birim_fiyat` ve `toplam_tutar` negatif olmayan sayılar olmalı.
5. `toplam_tutar` değeri `adet × birim_fiyat` ile 0,01 TL tolerans içinde uyuşmalı.
6. Metrikler aynı doğrulanmış G2 dosyası üzerinden hesaplanmalı; G1 sayıları G2 sonucu olarak sunulmamalı.

## 6. G2 üretim parametreleri ve sonraki kontroller
- `kayit_sayisi`: Üretilecek satış satırı sayısını belirler; `satis_id` sayısını ve oluşturulan tarih dizisini etkiler.
- `seed`: Rastgele ürün, kategori, adet ve mağaza seçimlerinin tekrarlanabilirliğini kontrol eder.
- `baslangic_tarihi` / `bitis_tarihi`: Üretilecek tarih aralığını belirler; güncel kodda 150 kayıt bu aralığa `pd.date_range(..., periods=kayit_sayisi)` ile dağıtılır.
- `--cikti`: CLI üzerinden CSV çıktı dosyasının yolunu belirler; doğrulama için mevcut referans CSV'nin üzerine yazmadan ayrı dosya kullanılmalıdır.
- CLI seçenekleri: `--kayit-sayisi`, `--baslangic-tarihi`, `--bitis-tarihi`, `--seed`, `--cikti`.
- G2 CSV'nin 150 satırı, 8 sütunu, alan tipleri, tutar tutarlılığı ve benzersiz satış ID'leri kontrol edildi; M1–M5 hesaplanıp `docs/analiz-g2.md` dosyasına yazıldı. #29 kapsamında test senaryoları ve BE PR #37'ye iki inceleme yorumu tamamlandı.
- **Açık uyumsuzluk:** Güncel BE kodunun tarih formülü ile referans CSV'nin 150 satırından **103'ünün tarihi farklıdır**. Bu yüzden referans CSV'nin güncel betikle birebir üretimi doğrulanmış değildir. BE düzeltmesinden sonra ayrı çıktı dosyasıyla SHA ve analiz metrikleri yeniden kontrol edilmelidir.

İlgili görevler: #25 (şema), #27 (analiz), #29 (test); BE bağımlılığı: #26.
