# G2 — Perakende Satış Analizi

**Durum:** G2 verisi üzerinden beş metrik hesaplandı. Sonuçlar sentetik satış verisine aittir; gerçek ticari performansı temsil etmez.

## Veri kaynağı ve yöntem
- Kaynak: `data/perakende-satislari-g2.csv` (GitHub `main` dalındaki sürüm)
- Kaynak CSV blob SHA: `924d744b35ed1cd97ca8dfc0bd4a7636a23e0df0`
- Kayıt sayısı: **150**, alan sayısı: **8**
- Tarih aralığı (mevcut CSV'de doğrulandı): **2026-01-01 – 2026-03-31**
- Veri sözlüğü: `docs/veri-sozlugu.md`
- Hesaplama: CSV'deki `toplam_tutar` değerleri toplandı; ortalama işlem tutarı toplam gelirin satır sayısına bölünmesiyle hesaplandı. Her satır bir satış işlemi sayıldı.
- Veri kontrolü: satış kimlikleri benzersiz; satır tutarları `adet × birim_fiyat` hesabıyla uyumlu (0,01 TL tolerans).
- **Güncel BE kodu / referans CSV karşılaştırması (2026-11-08):** Umut'un [bf040ac](https://github.com/MAKU-VBA-GBT-II/group-e/commit/bf040ac458fffffb920b5e53495940cacb915aab) düzeltmesinden sonraki `src/simulasyon_g2.py` (Git blob `bc3fd2fc63ed3fac9433a3e2d2498f47588b7966`) varsayılan 150 kayıt/2026-01-01–2026-03-31/seed 42 için kod içindeki referans veriyi döndürür. Diğer parametrelerde `random.seed` ve `datetime/timedelta` kullanılarak dinamik veri üretilir. Önceki `pd.date_range` sürümündeki 103/150 tarih uyuşmazlığı artık güncel bir açık hata değildir.
- **DQ çalıştırma kanıtı:** Kullanıcı PowerShell'de 300 kayıt ve 2026-02-01–2026-02-28 tarih aralığını doğruladı. `bf040ac` sonrasında başlangıç ve bitiş tarihi 2026-02-01 seçilerek üretilen 10 kaydın tamamı aynı tarihte çıktı. Varsayılan 150 kayıt için UTF-8 satır karşılaştırmasında fark görülmedi; **SHA-256 eşitliği ise `False`** çıktı. Bayt düzeyinde farkın nedeni henüz kesinleştirilmedi; satır eşitliği ile dosya hash eşitliği karıştırılmamalıdır.
- **Kaynak sürümü:** Referans CSV Git blob SHA `924d744b35ed1cd97ca8dfc0bd4a7636a23e0df0` değerindedir. Bu değer Git blob kimliğidir, PowerShell SHA-256 sonucu değildir. Test dosyaları ayrı `--cikti` yollarında üretildi; BE kodu ve referans CSV bu DQ belge güncellemesinde değiştirilmedi.
- **Test sınırları:** Ters tarih aralığını reddetme kontrolü kodda vardır; son sürümde CLI üzerinden çalıştırma kanıtı yoktur. Farklı seed çıktılarının son sürümde yeniden karşılaştırılması ve SHA-256 farkının açıklığa kavuşturulması takip maddeleridir.

## Beş metrik

| Kod | Metrik | Sonuç | Birim |
| --- | --- | ---: | --- |
| M1 | Toplam satış geliri | 140.131,25 | TL |
| M2 | Ortalama işlem tutarı | 934,21 | TL/işlem |
| M3 | Toplam satılan ürün adedi | 305 | adet |
| M4 | Kategori bazında satış geliri | Aşağıdaki kategori tablosu | TL/kategori |
| M5 | Mağaza bazında satış geliri | Aşağıdaki mağaza tablosu | TL/mağaza |

### M4 — Kategori bazında satış geliri

| Sıra | Kategori | Gelir | İşlem sayısı | Gelir payı |
| --- | --- | ---: | ---: | ---: |
| 1 | Giyim | 40.680,00 TL | 30 | 29,03% |
| 2 | Elektronik | 37.235,00 TL | 30 | 26,57% |
| 3 | Ev ve Yaşam | 32.437,00 TL | 30 | 23,15% |
| 4 | Kozmetik | 19.564,75 TL | 30 | 13,96% |
| 5 | Gıda | 10.214,50 TL | 30 | 7,29% |

### M5 — Mağaza bazında satış geliri

| Sıra | Mağaza | Gelir | İşlem sayısı | Gelir payı |
| --- | --- | ---: | ---: | ---: |
| 1 | Antalya | 41.819,00 TL | 38 | 29,84% |
| 2 | Burdur | 35.034,75 TL | 38 | 25,00% |
| 3 | Konya Merkez | 32.417,00 TL | 37 | 23,13% |
| 4 | Isparta | 30.860,50 TL | 37 | 22,02% |

## Bulgular

1. **Genel satış:** 150 işlemde toplam **140.131,25 TL** gelir ve **305 adet** ürün satışı oluşmuştur. İşlem başına ortalama **934,21 TL** gelir düşmektedir.
2. **Kategori karşılaştırması:** En yüksek gelire sahip kategori **Giyim** (**40.680,00 TL**, toplamın **%29,03**'i); en düşük gelirli kategori **Gıda** (**10.214,50 TL**). Bu fark, işlem sayısından ziyade ürün fiyatları ve miktarlarıyla birlikte yorumlanmalıdır.
3. **Mağaza karşılaştırması:** En yüksek gelir **Antalya** mağazasında (**41.819,00 TL**), en düşük gelir **Isparta** mağazasında (**30.860,50 TL**) oluşmuştur. Bu veri sentetik olduğundan farklar gerçek mağaza başarısına ilişkin kanıt değildir.

## Eylem önerisi

Kategori ve mağaza gelirlerinin yanında **işlem sayısı, satılan adet ve ortalama birim fiyat** da izlenmelidir. Özellikle Giyim kategorisinin gelir liderliğinin yüksek fiyatlardan mı yoksa satış hacminden mi kaynaklandığını görmek için sonraki analizde adet ve işlem başına gelir karşılaştırması yapılması önerilir.

## Tamamlama kontrolü
- [x] G2 CSV'nin satır/sütun yapısı ve temel tutar tutarlılığı kontrol edildi
- [x] Veri sözlüğü G2 alanlarına göre güncellendi
- [x] Beş metrik G2 CSV üzerinden hesaplandı
- [x] Kategori ve mağaza kırılımları raporlandı
- [x] Üç bulgu ve uygulanabilir eylem önerisi yazıldı
- [x] #29 kapsamındaki kullanıcı tarafından bildirilen simülasyon/CSV testleri ve BE PR inceleme yorumları kaydedildi
- [x] PR #34 `main` dalına birleştirildi (merge commit: `ad381688ee85d54940b5e17c7b947a1212909666`)
- [x] BE: Güncel betiğin varsayılan bitiş tarihi 2026-03-31 olarak düzeltildi
- [x] BE/DQ: Önceki tarih uyuşmazlığı ve aynı gün sınır durumu düzeltildi; 10/10 aynı gün testi geçti.
- [x] DQ: 300 kayıt ve özel tarih aralığı CLI testi geçti; varsayılan CSV satır içeriği eşleşti.
- [ ] DQ: SHA-256 bayt farkının nedeni ve son sürümde ters tarih aralığı/farklı seed CLI testleri ayrıca doğrulanacak.

İlgili görevler: #27 (analiz), #25 (şema), #29 (test).
