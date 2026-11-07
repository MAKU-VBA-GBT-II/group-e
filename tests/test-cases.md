# Test Senaryoları (Test Cases) - Grup E

| Test ID | Senaryo | Girdi | Adımlar | Beklenen Sonuç |
|---|---|---|---|---|
| TC-01 | Analiz betiğinin çalıştırılması | `python src/analiz_g1.py` | 1. Terminali aç. 2. Komutu çalıştır. | Betiğin hatasız çalışması ve metrikleri ekrana yazdırması |
| TC-02 | CSV verisinin okunması | `data/perakende-satislari.csv` | 1. Veri yolunu kontrol et. 2. Betiği çalıştır. | Dosyanın okunması ve hata vermemesi |
| TC-03 | Toplam satış tutarının doğruluğu | CSV `toplam_tutar` sütunu | 1. Veriyi topla. 2. Çıktıyı kontrol et. | Toplam satışın doğru görünmesi |
| TC-04 | Veri tipleri ve aralık kontrolü | `data/perakende-satislari.csv` | 1. Sütun tiplerini incele. 2. Negatif değer var mı bak. | Veri tiplerinin uygun ve aralıkların mantıklı olması |
| TC-05 | Kategori değerleri kontrolü | Kategorik sütunlar | 1. Benzersiz değerleri listele. | Beklenen kategori kümesi dışında değer olmaması |

## G2 — Parametreli simülasyon test planı (Issue #29)

**Durum:** Testler hazırlanmıştır; BE G2 simülasyon kodu ve çıktı dosyası henüz ana dalda doğrulanmadığı için gerçekleşen sonuçlar beklemededir. Test girdileri ve dosya yolu BE PR'ına göre kesinleştirilecektir. G1 testleri yukarıda korunmuştur.

| Test ID | Senaryo | Uygulama adımları | Beklenen sonuç | Gerçekleşen sonuç | Durum |
| --- | --- | --- | --- | --- | --- |
| G2-TC-01 | Simülasyonun çalışması | BE'nin G2 betiğini belgelenen komutla çalıştır. | Hatasız çalışır ve çıktı üretir. | BE PR'ı bekleniyor | Beklemede |
| G2-TC-02 | CSV şema kontrolü | Üretilen CSV başlıklarını `docs/veri-sozlugu.md` ile karşılaştır. | Zorunlu sütunlar eksiksizdir, dosya okunabilir. | BE PR'ı bekleniyor | Beklemede |
| G2-TC-03 | En az iki ayarlanabilir parametre | BE kodunda en az iki parametreyi tespit et; her birini ayrı ayrı değiştirip çıktıyı karşılaştır. | İki parametre gerçekten değiştirilebilir ve belgelenen etkiyi gösterir. | BE PR'ı bekleniyor | Beklemede |
| G2-TC-04 | Veri tipleri ve iş kuralları | Sayısal alanları, tarihleri, boş ve yinelenen kimlikleri, `adet × birim_fiyat` tutarlılığını denetle. | Geçerli türler, pozitif miktar, geçerli tarihler, tutarlı tutarlar ve benzersiz kimlikler. | BE PR'ı bekleniyor | Beklemede |
| G2-TC-05 | Tekrarlanabilirlik | Aynı parametreler ve aynı tohumla simülasyonu iki kez çalıştır; çıktıları karşılaştır. | Simülasyon deterministik olarak tasarlandıysa iki çıktı aynıdır; değilse tohum politikası açıkça belgelenmiştir. | BE PR'ı bekleniyor | Beklemede |
| G2-TC-06 | DQ metrik doğrulaması | G2 CSV üzerinden M1–M5'i bağımsız hesapla ve `docs/analiz-g2.md` ile karşılaştır. | Beş metriğin sonuçları raporla eşleşir. | BE verisi ve DQ analizi bekleniyor | Beklemede |

### BE Pull Request incelemesi (zorunlu 2 yorum)
- **Yorum 1 — Parametreler:** Kodun hangi iki parametreyi kabul ettiğini, varsayılanlarını ve değiştirilince çıktının nasıl etkilendiğini gerçek satırlara bakarak yorumla.
- **Yorum 2 — Veri kalitesi:** Üretilen verinin şemaya uygunluğu ve doğrulanan iş kurallarına dair gerçek kod/satır üzerinde yorum bırak.
- Bu iki yorum, BE PR'ı açılmadan gönderilmiş sayılmaz; gerçek inceleme yapıldıktan sonra PR bağlantıları ve test sonuçları bu bölüme işlenmelidir.

İlgili görevler: #26 (BE), #29 (DQ test), #25 (şema), #27 (analiz).
