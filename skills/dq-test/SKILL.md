# Skill: DQ - Test ve Analiz

**Görevi:** Veri kalitesini test etmek ve sonuçları loglamak.

## Girdi
- Veri Dosyası: `data/tedarik_siparisleri.csv`
- Veri Sözlüğü: `docs/veri-sozlugu-g1.md`

## Adım Adım Talimatlar
1. Girdi CSV dosyasını ve veri sözlüğünü pandas ile oku.
2. Kalite kontrollerini yap (En az 5 senaryo: dosya var mı, satır sayısı doğruluğu, sütun adları, veri tipleri/aralıklar, kategori değerleri).
3. Test sonuçlarını değerlendir.
4. Başarılı/Başarısız durumlarını log dosyasına yazdır.

## Çıktı Dosyaları
- `tests/test-cases.md`
- `tests/test-log.md`

## Çalıştırma Komutu
`python src/analiz_g1.py`