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
- **Yeniden üretilebilirlik kontrolü (8 Kasım 2026, güncel BE sürümü):** `src/simulasyon_g2.py` artık `pd.date_range(start=baslangic_tarihi, end=bitis_tarihi, periods=kayit_sayisi)` kullanıyor ve varsayılan bitiş tarihi **2026-03-31**. Böylece önceki **2026-05-30** bitiş hatası giderildi. Ancak **tarih aralığının aynı olması, CSV'nin birebir aynı üretildiğini kanıtlamaz**: mevcut CSV'nin ilk tarihleri `2026-01-01, 2026-01-01, 2026-01-02, 2026-01-03` iken güncel betiğin eşit aralıklı ilk tarihleri `2026-01-01, 2026-01-01, 2026-01-02, 2026-01-02` olur. Dolayısıyla tarih dağılımı farklıdır; varsayılan betik çalıştırılarak mevcut CSV'nin üzerine yazılmamalıdır. BE ekibi referans CSV'nin üretim kuralını netleştirmeli, ardından yeniden üretim ve SHA eşitliği test edilmelidir.
- **SHA kontrolü:** `924d744b35ed1cd97ca8dfc0bd4a7636a23e0df0` değeri 8 Kasım 2026 tarihinde `main` dalındaki `data/perakende-satislari-g2.csv` dosyasının Git blob SHA değeriyle eşleşti. Bu bir CSV içerik sürümü referansıdır; dosya değişirse değişebilir.
- **Test kapsamı:** #29 kapsamında kullanıcının bildirdiği Python fonksiyonu, farklı kayıt sayısı/seed ve CSV tekrarlanabilirlik testleri kaydedildi; bu testler mevcut CSV ile güncel betiğin **birebir aynı dosyayı ürettiğini kanıtlamaz**.

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
- [ ] BE/DQ: Betiğin tarih dağılımı referans CSV ile eşitlenecek, yeniden üretim ve SHA doğrulaması yapılacak; veri değişirse M1–M5 tekrar hesaplanacak

İlgili görevler: #27 (analiz), #25 (şema), #29 (test).
