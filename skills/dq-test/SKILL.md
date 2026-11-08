---
name: dq-test
description: Grup E perakende satış verileri için G1 ve G2 şema, tarih, parametre, hesaplama ve veri kalitesi testlerini kanıtlarıyla yürütür.
---

# DQ Test — Veri Kalitesi ve Doğrulama

## Amaç ve sorumluluk
DQ rolü, perakende satış veri setlerinin yapısal ve mantıksal doğruluğunu ölçülebilir testlerle denetler. Testi çalıştırmadan "Geçti" yazma. BE kodunu, referans CSV'leri veya FE görsellerini değiştirme; tespit edilen sorunları kanıtla bildir.

## Girdiler
- G1: `data/perakende-satislari.csv`, `docs/veri-sozlugu-g1.md`, `src/analiz_g1.py`
- G2: `data/perakende-satislari-g2.csv`, `docs/veri-sozlugu.md`, `src/simulasyon_g2.py`
- Test kayıtları: `tests/test-cases.md`, varsa `tests/test-log.md`
- Analiz doğrulaması: `docs/analiz-g2.md`; grafik etiketleri için ilgili FE PNG dosyaları

Dosyaların mevcut olduğunu ve güncel `main` dalındaki gerçek şemayı önce doğrula. G1 ve G2 gereksinimlerini birbirine karıştırma.

## İş akışı
1. Güncel dal, ilgili commit, CSV, veri sözlüğü ve test belgelerini oku.
2. Başlık hariç satır sayısını, sütun adlarını, veri tiplerini ve eksik değerleri ölç.
3. En az beş temel senaryoyu ve ilgili G2 ek senaryolarını uygula.
4. Her senaryonun beklenen ve gerçekleşen sonucunu, komutunu ve kanıtını kaydet.
5. Hatalarda yeniden üretim adımlarını, beklenen/gözlenen davranışı ve etkilenen dosyayı belirt; gerekiyorsa BE/FE ekibine devret.
6. `tests/test-cases.md` ve `tests/test-log.md` belgelerindeki test kayıtlarını tutarlı hale getir. GitHub'a yazmadan önce değişiklik kapsamını ve kullanıcı onayını kontrol et.

## Zorunlu testler

| ID | Test | Kabul ve doğrulama |
| --- | --- | --- |
| DQ-01 | Dosya varlığı | Hedef CSV mevcut, boş değil ve okunabilir |
| DQ-02 | Kayıt sayısı | Görevde belirtilen minimum sayı ve istenen parametreli sayı ölçülür |
| DQ-03 | Şema | Sütunlar veri sözlüğüyle karşılaştırılır |
| DQ-04 | Tipler ve aralıklar | Tarih/sayı alanları ayrıştırılır; zorunlu alanlar ve pozitif değerler kontrol edilir |
| DQ-05 | Kategoriler | İzin verilen değerler ve gerekli farklı kategori sayısı kontrol edilir |
| DQ-06 | Kimlik ve tutar | Benzersiz `satis_id` ve `adet * birim_fiyat = toplam_tutar` tutarlılığı kontrol edilir |
| DQ-07 | G2 parametreli üretim | `--kayit-sayisi 300` ile gerçekten 300 veri satırı üretildiği doğrulanır |
| DQ-08 | Özel tarih aralığı | Aynı başlangıç/bitiş gününde tüm tarihler o güne eşit olmalı; ters tarih aralığı reddedilmeli; ay sonu/artık yıl sınırları gerektiğinde ayrıca test edilmeli |
| DQ-09 | Seed ve tekrarlanabilirlik | Farklı seed çıktılarının farklılığı ve aynı seed tekrarlarının eşitliği ayrı ayrı ölçülür |
| DQ-10 | CRLF/LF ve kodlama | Ham bayt karşılaştırması ile satır sonları normalize edilmiş metin karşılaştırması ayrı raporlanır; LF/CRLF farkı tek başına veri hatası değildir |
| DQ-11 | Analiz ve FE metrikleri | CSV toplam, ortalama, adet ve kırılımları analiz belgesi ve grafiklerdeki sayısal etiketlerle karşılaştırılır |

## Örnek G2 test komutları
Komutları depo kökünde çalıştır; referans CSV üzerine yazma.

```powershell
python src/simulasyon_g2.py --kayit-sayisi 300 --baslangic-tarihi 2026-02-01 --bitis-tarihi 2026-02-28 --seed 99 --cikti data/g2-test-parametre.csv
python src/simulasyon_g2.py --kayit-sayisi 10 --baslangic-tarihi 2026-02-01 --bitis-tarihi 2026-02-01 --cikti data/g2-tarih-test.csv
python src/simulasyon_g2.py --baslangic-tarihi 2026-03-01 --bitis-tarihi 2026-02-01
```

Son komutun hata vermesi beklenir. Test çıktıları geçici amaçlıdır; yalnızca onaylanan dosyalar commit edilir.

## Mevcut doğrulama kanıtlarının kullanımı
`tests/test-cases.md` içindeki G2-TC-01–G2-TC-09 kayıtları ve ilgili kanıt bağlantıları esas alınır. Bu belgede yer alan geçmiş sonuçlar yeniden çalıştırılmış gibi sunulmaz. 2026-11-08 kayıtlarında 300 kayıt ve özel tarih testi başarılı bildirilmiştir; farklı seed karşılaştırması yapılmıştır. Aynı seed ile iki bağımsız tekrarın birebir eşitliği ayrıca ölçülmemiştir. Referans CSV ile yeniden üretilen CSV'nin satır içerikleri LF'ye normalize edilince eşleşmiştir; ham SHA-256 değerleri CRLF/LF farkı nedeniyle eşit değildir. Bu ayrımı raporda koru.

## Sonuç kaydı
Her test için:
- Test ID, kaynak dosya ve commit
- Kullanılan komut veya yöntem
- Beklenen sonuç
- Gerçekleşen sonuç
- Durum: Geçti / Kaldı / Çalıştırılmadı / Kısmen doğrulandı
- Kanıt bağlantısı veya ölçüm
- Hata varsa yeniden üretim adımları ve sorumlu ekibe devir

## Kabul ölçütleri
G1'in en az beş temel kalite senaryosu korunur. G2'de parametreli 300 kayıt, tarih sınırları, seed, CRLF/LF ve analiz tutarlılığı ayrı test edilir. Doğrulanmamış hiçbir kontrol başarılı ilan edilmez. Kaynak kod, referans CSV, görseller ve PM raporu bu skill güncellemesiyle değiştirilmez.

## Kısa bilgi istemi özeti
"Güncel Grup E G1/G2 perakende satış CSV'lerini, veri sözlüklerini ve test kayıtlarını incele. Temel veri kalitesi, 300 kayıt, özel tarih, seed, CRLF/LF ve analiz/grafik metrik testlerini ölçülebilir kanıtlarla raporla. G1 geçmişini koru; çalıştırılmayan testleri geçti yazma ve BE/FE dosyalarını değiştirme."
