# Test Senaryoları (Test Cases) - Grup E

| Test ID | Senaryo | Girdi | Adımlar | Beklenen Sonuç |
|---|---|---|---|---|
| TC-01 | Analiz betiğinin çalıştırılması | `python src/analiz_g1.py` | 1. Terminali aç. 2. Komutu çalıştır. | Betiğin hatasız çalışması ve metrikleri ekrana yazdırması |
| TC-02 | CSV verisinin okunması | `data/perakende-satislari.csv` | 1. Veri yolunu kontrol et. 2. Betiği çalıştır. | Dosyanın okunması ve hata vermemesi |
| TC-03 | Toplam satış tutarının doğruluğu | CSV `toplam_tutar` sütunu | 1. Veriyi topla. 2. Çıktıyı kontrol et. | Toplam satışın doğru görünmesi |
| TC-04 | Veri tipleri ve aralık kontrolü | `data/perakende-satislari.csv` | 1. Sütun tiplerini incele. 2. Negatif değer var mı bak. | Veri tiplerinin uygun ve aralıkların mantıklı olması |
| TC-05 | Kategori değerleri kontrolü | Kategorik sütunlar | 1. Benzersiz değerleri listele. | Beklenen kategori kümesi dışında değer olmaması |

## G2 — Parametreli simülasyon test sonuçları (Issue #29)

**İnceleme tarihi:** 2026-11-08. **Kaynak:** `main` dalındaki `data/perakende-satislari-g2.csv` (blob `924d744b35ed1cd97ca8dfc0bd4a7636a23e0df0`) ve `src/simulasyon_g2.py` (blob `ec691c697a501cf027327c66addee5a3814b508d`). G1 testleri yukarıda korunmuştur.

**Yöntem ve sınır:** GitHub'dan okunan gerçek CSV'nin 150 satırı bağımsız olarak ayrıştırılıp şema, kimlik, tarih, sayı, tutar ve metrik kontrolleri çalıştırıldı. Python üretim betiği bu ortamda çalıştırılamadığı için betik çalıştırma, iki parametrenin farklı değerlerle denenmesi ve aynı seed ile iki çıktı hash'inin karşılaştırılması **çalıştırılmış gibi gösterilmemiştir**. PR #37'nin diff'i ile mevcut `main` betiği ayrıca karşılaştırıldı.

| Test ID | Senaryo | Uygulama / girdi | Beklenen sonuç | Gerçekleşen sonuç | Durum |
| --- | --- | --- | --- | --- | --- |
| G2-TC-01 | Simülasyonun çalışması | `python src/simulasyon_g2.py` | Betik hatasız çalışır, CSV üretir. | Ana dalda CSV mevcut; Python betiği bu inceleme ortamında fiilen çalıştırılamadı. | Çalıştırılmadı |
| G2-TC-02 | CSV şema kontrolü | `data/perakende-satislari-g2.csv` | CSV okunur; 8 zorunlu sütun eksiksizdir. | 150 veri satırı, 8 sütun; başlıklar `satis_id,tarih,urun,kategori,adet,birim_fiyat,toplam_tutar,magaza` ile tam eşleşiyor. | Geçti |
| G2-TC-03 | En az iki ayarlanabilir parametre | `src/simulasyon_g2.py`, PR #37 | İki parametre değiştirilebilir ve çıktı etkisi gözlenir. | Mevcut ana dalda `veri_uret(kayit_sayisi=150, seed=42)` fonksiyon parametreleri var; fakat `main()` bunları sabit değerle çağırıyor ve CLI `argparse` yok. PR #37 diff'inde CLI seçenekleri var, ana daldaki kodla uyumsuz. Değişik parametrelerle fiili çalıştırma yapılmadı. | Doğrulama gerekli / sürüm uyumsuzluğu |
| G2-TC-04 | Veri tipleri ve iş kuralları | CSV'nin 150 satırı | Geçerli tarihler, pozitif tam sayı adet, negatif olmayan fiyat ve tutar, boş/tekrarlı ID olmaması; `adet × birim_fiyat` tutarlılığı. | 150/150 satırda sayısal ve tarih biçimi kontrolleri başarılı; 150 benzersiz ID; 150/150 tutar çarpımı 0,01 TL toleransta uyumlu. Tarihler 2026-01-01–2026-03-31. | Geçti (mevcut CSV) |
| G2-TC-05 | Tekrarlanabilirlik | Aynı `kayit_sayisi` ve `seed` ile iki Python çalıştırması | Aynı girdiler aynı CSV'yi üretir. | Kodda `random.seed(seed)` var; ancak iki gerçek Python çalıştırması ve çıktı hash karşılaştırması yapılamadı. | Çalıştırılmadı |
| G2-TC-06 | DQ metrik doğrulaması | CSV ve `docs/analiz-g2.md` | M1–M5 bağımsız hesapla raporla eşleşir. | M1 = **140.131,25 TL**; M2 = **934,21 TL/işlem**; M3 = **305 adet**; M4: Giyim 40.680,00; Elektronik 37.235,00; Ev ve Yaşam 32.437,00; Kozmetik 19.564,75; Gıda 10.214,50 TL. M5: Antalya 41.819,00; Burdur 35.034,75; Konya Merkez 32.417,00; Isparta 30.860,50 TL. Analiz raporuyla eşleşiyor. | Geçti |

### BE PR incelemesi — iki gönderilmiş satır içi yorum

1. **Parametre / sürüm uyuşmazlığı:** [PR #37 inceleme yorumu 1](https://github.com/MAKU-VBA-GBT-II/group-e/pull/37#discussion_r4506326676). PR'da bulunan CLI parametrelerinin `main` sürümünde bulunmaması ve parametre değişim testinin gerekliliği belirtildi.
2. **Veri kalitesi / sürüm eşleştirme:** [PR #37 inceleme yorumu 2](https://github.com/MAKU-VBA-GBT-II/group-e/pull/37#discussion_r4506326678). CSV kalite kontrolleri ve PR'daki CSV ile `main` CSV farkının çözülmesi istendi.

**Açık kalan doğrulamalar:** Betiği Python ortamında iki farklı parametre setiyle çalıştırmak, aynı seed ile iki çıktının hash'ini karşılaştırmak ve PR #37 ile `main` arasındaki veri/kod sürüm farkını BE ekibiyle netleştirmek. Bu maddeler tamamlanmadan tüm G2 testleri geçti denmemelidir.

İlgili görevler: #26 (BE), #29 (DQ test), #25 (şema), #27 (analiz).
