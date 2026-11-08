---
name: dq-analiz
description: Grup E perakende satış verilerinin G1 ve G2 analiz metriklerini hesaplar, veri kalitesini kontrol eder, FE grafiklerini doğrular ve kanıta dayalı analiz raporu hazırlar.
---

# DQ Analiz Skill — Grup E

## Amaç
DQ rolünde sentetik perakende satış verilerinden tekrarlanabilir ve doğrulanabilir analiz üret. G1 ve G2 veri kaynaklarını karıştırma. Analiz raporunu yalnızca gerçek hesaplamalar ve kayıtlı kanıtlarla güncelle; test edilmemiş bir kontrolü tamamlanmış gösterme.

## Girdiler ve çıktılar
- G1 kaynak: `data/perakende-satislari.csv`; analiz betiği: `src/analiz_g1.py`; rapor: `docs/analiz-g1.md`.
- G2 kaynak: `data/perakende-satislari-g2.csv`; üretici: `src/simulasyon_g2.py`; veri sözlüğü: `docs/veri-sozlugu.md`; rapor: `docs/analiz-g2.md`.
- Kalite kanıtı: `tests/test-cases.md`; FE çıktıları: `visuals/g2-zaman-serisi.png`, `visuals/g2-kategori-kirilimi.png`, `visuals/g2-magaza-dagilimi.png`.
- Analiz değişikliği sırasında BE kodunu, CSV'leri, FE görsellerini ve PM raporunu değiştirme.

## Adım adım çalışma
1. GitHub `main` dalındaki güncel kaynak dosyaları, veri sözlüğünü ve ilgili commitleri kontrol et.
2. CSV'yi UTF-8 olarak oku; başlık, satır sayısı, eksik alanlar, benzersiz `satis_id`, ISO `tarih`, pozitif `adet` ve `birim_fiyat` değerlerini doğrula.
3. `toplam_tutar` ile `adet × birim_fiyat` hesabını kuruş düzeyinde (0,01 TL tolerans) karşılaştır. Hataları raporla; kaynak veriyi sessizce değiştirme.
4. Aşağıdaki M1–M5 metriklerini **aynı doğrulanmış G2 CSV** üzerinden hesapla.
5. Kategori ve mağaza gelirlerini azalan sırada göster; her grubun işlem sayısını ve toplam gelir içindeki yüzdesini de belirt.
6. Her metrik için 1–2 cümle açıklama, en az üç kanıta dayalı bulgu ve bir uygulanabilir eylem önerisi yaz. G1 görevindeki top-3 gereksinimini ayrıca koru; G2'nin M1–M5 tanımlarını bununla değiştirme.
7. FE grafiklerindeki ay toplamlarını, kategori ve mağaza tutarlarını ve yüzdeleri CSV ile karşılaştır. Görselde yuvarlanan değerleri uygun hassasiyetle değerlendir; etiket bulunmayan noktalar için kesin etiket varmış gibi yazma.
8. Sonuçları `docs/analiz-g2.md` içinde kaynak sürümü, yöntem, birim, kanıt ve sınırlılıklarıyla belgele. G1 raporunun geçmişini koru.
9. GitHub'a yazmadan önce yalnızca izin verilen dosyaları değiştirdiğini doğrula.

## G2 metrik tanımları

| Kod | Metrik | Formül / yöntem | Birim |
| --- | --- | --- | --- |
| M1 | Toplam satış geliri | `SUM(toplam_tutar)` | TL |
| M2 | Ortalama işlem tutarı | `SUM(toplam_tutar) / kayıt sayısı` | TL/işlem |
| M3 | Toplam satılan ürün adedi | `SUM(adet)` | adet |
| M4 | Kategori bazında satış geliri | `kategori` gruplarında `SUM(toplam_tutar)` | TL/kategori |
| M5 | Mağaza bazında satış geliri | `magaza` gruplarında `SUM(toplam_tutar)` | TL/mağaza |

Her CSV satırı bir işlem kabul edilir. Para biriminde iki ondalık basamak, yüzde paylarında uygun yuvarlama kullan. Yuvarlanan yüzdelerin toplamı tam %100 olmayabilir.

## Referans sonuçlar ve doğrulama
`docs/analiz-g2.md` belgesinde 2026-11-08 tarihinde kayıtlı G2 referans sonuçları: **150 kayıt, 8 sütun; M1 140.131,25 TL; M2 934,21 TL/işlem; M3 305 adet**. M4'te en yüksek kategori Giyim (40.680,00 TL), M5'te en yüksek mağaza Antalya (41.819,00 TL) olarak belgelenmiştir. Bu değerler gelecekteki başka parametrelerle üretilen CSV'ye otomatik uygulanmaz; her yeni kaynak için yeniden hesaplanır.

Üç FE görseli için önceki DQ kabulü `docs/analiz-g2.md` içinde kayıtlıdır. Aylık toplamlar: Ocak 51.158,75 TL; Şubat 43.105,00 TL; Mart 45.867,50 TL. Bu üç değerin toplamı M1 ile eşleşmelidir. Kategori ve mağaza grafiklerinin TL ve yüzde gösterimleri M4/M5 ile karşılaştırılmalıdır.

## Sınırlar ve test kanıtları
- `tests/test-cases.md` dosyasındaki G2-TC-01–G2-TC-09 sonuçlarına atıf yap; geçmiş sonuçları yeni çalıştırılmış gibi gösterme.
- G2 üretiminde 300 kayıt ve özel tarih, aynı gün, ters tarih ve farklı seed kontrolleri belgelenmiştir. Aynı seed ile iki bağımsız dinamik üretimin birebir eşitliği ayrıca test edilmemiştir.
- Referans CSV CRLF, yeniden üretilen CSV LF satır sonları kullandığından ham SHA-256 değerleri farklıdır; normalize edilmiş satır içerikleri eşleşmiştir. İçerik eşitliğini bayt eşitliği olarak sunma.
- Sentetik veri sonuçları gerçek mağaza performansına ilişkin çıkarım olarak sunulamaz.

## Kabul kriterleri
- G1: en az beş metrik (toplam, ortalama, iki kırılım, top-3), metrik açıklamaları, üç gözlem ve bir eylem.
- G2: M1–M5 doğru hesaplanır, birimler ve kırılımlar açıklanır; FE görselleriyle karşılaştırma kanıtı ve sınırlılıklar belgelenir.
- Test başarısı yalnızca mevcut kanıtlarla ifade edilir; hatalı veya eksik kanıt açıkça belirtilir.

## Kısa bilgi istemi özeti
"Güncel Grup E G1/G2 perakende satış CSV'lerini ve veri sözlüklerini incele. Veri kalitesini doğrula; G2 M1–M5 metriklerini, kategori ve mağaza kırılımlarını hesapla. FE görsellerini karşılaştır, üç bulgu ve bir eylem önerisi hazırla. Kaynak commitini ve kanıtları belirt; çalıştırılmamış kontrolleri başarılı sayma. BE, CSV, FE ve PM dosyalarını değiştirme."
