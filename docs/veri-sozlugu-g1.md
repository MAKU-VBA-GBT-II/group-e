# G1 Perakende Satışları Veri Sözlüğü

## Veri Seti Hakkında

Bu veri seti, perakende sektöründeki satış işlemlerini örneklemek amacıyla sentetik olarak oluşturulmuştur.

Veriler gerçek müşterilere veya gerçek satış işlemlerine ait değildir.

Veri seti `src/veri_uretici.py` betiği kullanılarak oluşturulmaktadır. Betikte `random.seed(42)` kullanıldığı için aynı betik tekrar çalıştırıldığında aynı veriler üretilebilir.

## Veri Seti Özellikleri

- Dosya: `data/perakende-satislari.csv`
- Kayıt sayısı: 150
- Alan sayısı: 8
- Ana kategori sayısı: 5
- Veri türü: Sentetik perakende satış verisi
- Sabit seed: 42

## Veri Sözlüğü

| Alan | Veri Tipi | Açıklama | Aralık / Değerler | Birim |
|---|---|---|---|---|
| satis_id | String | Her satış kaydı için benzersiz kimlik numarasıdır. | S0001–S0150 | - |
| tarih | Date | Satışın gerçekleştiği tarihi gösterir. Formatı YYYY-MM-DD şeklindedir. | 2026-01-01–2026-09-28 | Tarih |
| urun | String | Satılan ürünün adını gösterir. | Tanımlı 20 ürün | - |
| kategori | String | Ürünün ait olduğu ana kategoriyi gösterir. | Elektronik, Giyim, Gıda, Ev ve Yaşam, Kozmetik | - |
| adet | Integer | Satılan ürün miktarını gösterir. | 1–5 | adet |
| birim_fiyat | Float | Ürünün bir adet satış fiyatını gösterir. Temel fiyatın %90–%110 aralığında üretilir. | Ürünün temel fiyatına göre %90–%110 | TL |
| toplam_tutar | Float | Satışın toplam tutarıdır. Adet ile birim fiyatın çarpılmasıyla hesaplanır. | adet × birim_fiyat | TL |
| magaza | String | Satış işleminin gerçekleştiği mağazayı gösterir. | Isparta Merkez, Burdur Merkez, Antalya Merkez, Konya Merkez | - |

## Kategoriler

Veri setinde beş farklı ana kategori bulunmaktadır:

- Elektronik
- Giyim
- Gıda
- Ev ve Yaşam
- Kozmetik

## Veri Üretim Yöntemi

Veriler Python kullanılarak sentetik olarak üretilmiştir. Ürün, kategori, satış adedi, fiyat, tarih ve mağaza bilgileri belirlenen seçenekler arasından üretilmektedir.

Tekrarlanabilirlik sağlamak amacıyla `random.seed(42)` kullanılmıştır.

Satış adedi 1–5 arasında üretilir. Birim fiyat, ürünün tanımlı temel fiyatının %90–%110 aralığında belirlenir. Tarih, 2026-01-01 tarihinden başlayarak 0–270 gün aralığından seçilir.

Toplam tutar aşağıdaki şekilde hesaplanmaktadır:

`toplam_tutar = adet × birim_fiyat`

Bu yapı sayesinde veri seti analiz, test ve görselleştirme çalışmalarında kullanılabilir.
