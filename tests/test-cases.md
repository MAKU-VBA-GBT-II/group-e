# Hafta 3: Sentetik Veri Test Senaryoları

| No | Kriter | Test Senaryosu | Beklenen Sonuç | Gerçekleşen Sonuç | Durum |
|---|---|---|---|---|---|
| TC-01 | Dosya | CSV dosyasının var olup olmadığını kontrol et. | `data/perakende-satislari.csv` mevcut olmalı. | | Beklemede |
| TC-02 | Satır Sayısı | Veri setinin satır sayısını say. | Satır sayısı en az 100 olmalı. | | Beklemede |
| TC-03 | Sütunlar | Veri sözlüğündeki zorunlu alanları kontrol et. | Belirlenen sütun başlıkları bulunmalı. | | Beklemede |
| TC-04 | Veri Tipleri | Fiyat alanının tipini kontrol et. | Fiyat > 0 ve sayısal olmalı. | | Beklemede |
| TC-05 | Kategori Değerleri | Kategori çeşitliliğini kontrol et. | Kategorik alanda en az 4 farklı değer olmalı. | | Beklemede |