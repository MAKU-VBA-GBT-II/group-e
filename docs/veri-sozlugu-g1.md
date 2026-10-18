\# G1 Perakende Satışları Veri Sözlüğü



\## Veri Seti Hakkında



Bu veri seti, perakende sektöründeki satış işlemlerini örneklemek amacıyla sentetik olarak oluşturulmuştur.



Veriler gerçek müşterilere veya gerçek satış işlemlerine ait değildir.



Veri seti `src/veri\_uretici.py` betiği kullanılarak oluşturulmaktadır. Betikte `random.seed(42)` kullanıldığı için aynı betik tekrar çalıştırıldığında aynı veriler üretilebilir.



\## Veri Seti Özellikleri



\- Dosya: `data/perakende-satislari.csv`

\- Kayıt sayısı: 150

\- Alan sayısı: 8

\- Ana kategori sayısı: 5

\- Veri türü: Sentetik perakende satış verisi

\- Sabit seed: 42



\## Veri Sözlüğü



| Alan | Veri Tipi | Açıklama |

|---|---|---|

| satis\_id | String | Her satış kaydı için benzersiz kimlik numarasıdır. |

| tarih | Date | Satışın gerçekleştiği tarihi gösterir. Formatı YYYY-MM-DD şeklindedir. |

| urun | String | Satılan ürünün adını gösterir. |

| kategori | String | Ürünün ait olduğu ana kategoriyi gösterir. |

| adet | Integer | Satılan ürün miktarını gösterir. |

| birim\_fiyat | Float | Ürünün bir adet fiyatını TL cinsinden gösterir. |

| toplam\_tutar | Float | Satışın toplam tutarıdır. Adet ile birim fiyatın çarpılmasıyla hesaplanır. |

| magaza | String | Satış işleminin gerçekleştiği mağazayı gösterir. |



\## Kategoriler



Veri setinde beş farklı ana kategori bulunmaktadır:



\- Elektronik

\- Giyim

\- Gıda

\- Ev ve Yaşam

\- Kozmetik



\## Veri Üretim Yöntemi



Veriler Python kullanılarak sentetik olarak üretilmiştir. Ürün, kategori, satış adedi, fiyat, tarih ve mağaza bilgileri belirlenen seçenekler arasından üretilmektedir.



Tekrarlanabilirlik sağlamak amacıyla `random.seed(42)` kullanılmıştır.



Toplam tutar aşağıdaki şekilde hesaplanmaktadır:



`toplam\_tutar = adet × birim\_fiyat`



Bu yapı sayesinde veri seti analiz ve görselleştirme çalışmalarında kullanılabilir.

