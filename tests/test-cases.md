# Test Senaryoları (Test Cases) - Grup E

| Test ID | Senaryo | Girdi | Adımlar | Beklenen Sonuç |
|---|---|---|---|---|
| TC-01 | Analiz betiğinin çalıştırılması | `python src/analiz_g1.py` | 1. Terminali aç. 2. Komutu çalıştır. | Betiğin hatasız çalışması ve metrikleri ekrana yazdırması |
| TC-02 | CSV verisinin okunması | `data/perakende-satislari.csv` | 1. Veri yolunu kontrol et. 2. Betiği çalıştır. | Dosyanın okunması ve hata vermemesi |
| TC-03 | Toplam satış tutarının doğruluğu | CSV `toplam_tutar` sütunu | 1. Veriyi topla. 2. Çıktıyı kontrol et. | Toplam satışın doğru görünmesi |
| TC-04 | Veri tipleri ve aralık kontrolü | `data/perakende-satislari.csv` | 1. Sütun tiplerini incele. 2. Negatif değer var mı bak. | Veri tiplerinin uygun ve aralıkların mantıklı olması |
| TC-05 | Kategori değerleri kontrolü | Kategorik sütunlar | 1. Benzersiz değerleri listele. | Beklenen kategori kümesi dışında değer olmaması |

## G2 — Parametreli simülasyon test sonuçları (Issue #29)

**Güncelleme:** 2026-11-08. **BE düzeltmesi:** [bf040ac](https://github.com/MAKU-VBA-GBT-II/group-e/commit/bf040ac458fffffb920b5e53495940cacb915aab). **Kaynak:** `main` dalındaki `src/simulasyon_g2.py` (blob `bc3fd2fc63ed3fac9433a3e2d2498f47588b7966`) ve `data/perakende-satislari-g2.csv` (blob `924d744b35ed1cd97ca8dfc0bd4a7636a23e0df0`). Yukarıdaki G1 testleri korunmuştur.

**Kanıt yöntemi:** BE kodu ve referans CSV GitHub üzerinden incelendi. Komut çalıştırma sonuçları kullanıcının Windows PowerShell ekran görüntülerinden ve ilettiği sonuçlardan alındı. Referans CSV'nin `Get-Content -Encoding UTF8` ile yapılan satır bazlı karşılaştırmasında fark çıkmadı; buna karşılık SHA-256 karşılaştırması `False` verdi. Bu nedenle **satır içerikleri eşleşiyor, bayt düzeyinde dosya eşitliği doğrulanmış değil**. SHA farkının nedeni kesinleştirilmedi.

| Test ID | Senaryo | Uygulama / girdi | Beklenen sonuç | Gerçekleşen sonuç | Durum |
| --- | --- | --- | --- | --- | --- |
| G2-TC-01 | CSV oluşturma ve kayıt sayısı | `python src/simulasyon_g2.py --kayit-sayisi 150 --cikti data/g2-test-150.csv` | 150 kayıt yazılması | Kullanıcı test dosyasını üretti; referans CSV ile UTF-8 satır karşılaştırması fark göstermedi. | Geçti (satır içeriği) |
| G2-TC-02 | Referans CSV şeması | `data/perakende-satislari-g2.csv` | 150 kayıt, 8 sütun | 150 kayıt ve `satis_id,tarih,urun,kategori,adet,birim_fiyat,toplam_tutar,magaza` başlıkları doğrulandı. | Geçti |
| G2-TC-03 | Parametreli kayıt ve tarih üretimi | `--kayit-sayisi 300 --baslangic-tarihi 2026-02-01 --bitis-tarihi 2026-02-28 --seed 99 --cikti data/g2-test-parametre.csv` | 300 kayıt, ilk tarih 2026-02-01, son tarih 2026-02-28 | Kullanıcı PowerShell çıktısında 300 kayıt ve beklenen ilk/son tarihleri gösterdi. | Geçti |
| G2-TC-04 | Referans veri iş kuralları | Referans CSV | Benzersiz ID, geçerli tarih, pozitif adet ve tutar uyumu | Önceki DQ kontrolünde 150 benzersiz ID, 150/150 tutar uyumu ve 2026-01-01–2026-03-31 tarih aralığı doğrulandı. | Geçti (referans CSV) |
| G2-TC-05 | Tekrarlanabilirlik ve dosya eşitliği | Varsayılan 150 kayıt, `seed=42` | Tekrar üretimde aynı satır içeriği; bayt eşitliği ayrı kontrol | UTF-8 satır karşılaştırması fark göstermedi. SHA-256 karşılaştırması `False` verdi; dosya biçimi/sonlandırma farkı olasılığı henüz kesinleştirilmedi. | Satır içeriği geçti; SHA açık |
| G2-TC-06 | DQ metrik doğrulaması | Referans CSV ve `docs/analiz-g2.md` | M1–M5 eşleşmeli | M1 **140.131,25 TL**; M2 **934,21 TL/işlem**; M3 **305 adet**. M4 ve M5 kırılımları analiz belgesiyle eşleşiyor. | Geçti |
| G2-TC-07 | Aynı başlangıç ve bitiş tarihi | `--kayit-sayisi 10 --baslangic-tarihi 2026-02-01 --bitis-tarihi 2026-02-01 --cikti data/g2-tarih-test.csv` | 10 tarihin tamamı 2026-02-01 | Önceki sürümde 5 kayıt 2026-02-02 idi. BE `bf040ac` düzeltmesinden sonra kullanıcı ekran görüntüsünde 10/10 kaydın 2026-02-01 olduğunu gösterdi. | Geçti (düzeltme sonrası) |
| G2-TC-08 | Ters tarih aralığının reddi | `--baslangic-tarihi 2026-03-01 --bitis-tarihi 2026-02-01` | Hata verilmesi | Güncel kodda `if baslangic > bitis: raise ValueError(...)` kontrolü var; bu sürümde fiili CLI testi sunulmadı. | Kodda mevcut; çalıştırma bekliyor |
| G2-TC-09 | Farklı seed ile farklı çıktı | Aynı parametreler, `--seed 42` ve `--seed 99` | Farklı veri, aynı seed ile tekrar üretimde aynı veri | Güncel kod `random.seed(seed)` kullanıyor; son BE commitinden sonra ayrı karşılaştırma çıktısı sunulmadı. | Yeniden test önerilir |

### BE PR inceleme kayıtları

- [PR #37 satır içi yorum 1](https://github.com/MAKU-VBA-GBT-II/group-e/pull/37#discussion_r4506326676) ve [yorum 2](https://github.com/MAKU-VBA-GBT-II/group-e/pull/37#discussion_r4506326678) önceki sürümlere ilişkin tarihsel inceleme kayıtlarıdır.
- Önceki `pd.date_range` sürümünde raporlanan **103/150 tarih uyuşmazlığı**, güncel `bf040ac` sürümünün açık hatası değildir. Güncel kod varsayılan parametrelerde 150 sabit referans kaydını döndürür; farklı parametrelerde dinamik simülasyon uygular.
- **Açık takip:** SHA-256 dosya eşitliğinin neden sağlanmadığı, ters tarih aralığı CLI testi ve son sürümde farklı seed karşılaştırması ayrıca doğrulanabilir. Referans CSV ve BE kodu değiştirilmemiştir.

İlgili görevler: #26 (BE), #29 (DQ test), #25 (şema), #27 (analiz).
