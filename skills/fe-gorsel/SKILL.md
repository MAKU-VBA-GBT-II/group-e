---
name: fe-gorsel
description: Perakende satış verisinden zaman serisi ve kategori grafiklerini üretir.
---

# FE Görselleştirme Skill'i

## Amaç ve kapsam

Bu skill; RetailE projesi kapsamında, BE'nin ürettiği sentetik perakende
satış verisini kullanarak iki grafik üretir:

1. **Zaman serisi grafiği** — aylara göre toplam satış tutarının değişimi.
2. **Kategori kırılım grafiği** — kategorilere göre toplam satış tutarının
   dağılımı ve her kategorinin toplam içindeki yüzde payı.

Görselleştirme ajanı `src/gorsellestirme.py` betiğini proje ana klasöründen
çalıştırır ve `visuals/` klasörü altında iki PNG çıktısını doğrular.
Betiğin yapmadığı işlemler (rapor yazımı, farklı grafik türleri, HTML/video
çıktısı vb.) bu skill'in kapsamına girmez.

## Kullanılan veri kaynağı ve dosyalar

| Dosya | İşlevi |
| --- | --- |
| `data/perakende-satislari.csv` | Girdi — sentetik satış verisi (150 kayıt) |
| `src/gorsellestirme.py` | Grafikleri üreten Python betiği |
| `visuals/zaman-serisi.png` | Çıktı — zaman serisi grafiği |
| `visuals/kategori-kirilimi.png` | Çıktı — kategori kırılım grafiği |

Betiğin kullandığı sütunlar:

- `tarih` — satış tarihi; `pd.to_datetime` ile tarihe çevrilir.
- `kategori` — ürün kategorisi; kırpımda `groupby` anahtarıdır.
- `toplam_tutar` — satış tutarı; sayısal tutulur ve grafiklerde TL birimi
  ile gösterilir.

Kalan sütunlar (`satis_id`, `urun`, `adet`, `birim_fiyat`, `magaza`) betik
tarafından okunmaz, sadece veri dosyasında kalır. Sütunların tam şeması
`docs/veri-sozlugu-g1.md` dosyasında açıklanır.

## CSV'nin okunması ve verinin doğrulanması

Betik, `DATA_PATH` sabitinin gösterdiği dosyayı `pd.read_csv` ile okur.
Okuma sonrası betik kendini doğrular; betikteki denetimler şunlardır:

1. `data/perakende-satislari.csv` dosyası mevcut değilse betik
   `FileNotFoundError` ile durur; dosya yolu hata mesajında gösterilir.
2. `tarih`, `kategori`, `toplam_tutar` sütunlarından biri eksikse betik,
   eksik sütun adlarını içeren bir `ValueError` fırlatır.
3. `tarih` alanı `pd.to_datetime`, `toplam_tutar` alanı `pd.to_numeric`
   ile çevrilir; bu alanlarda `NaT`/`NaN` bırakan satırlar düşürülür.
4. Filtre sonrasında hiç geçerli kayıt kalmadıysa betik `ValueError`
   fırlatır ("Geçerli satış verisi bulunamadı.").

Betiğin son durumu ajanın çıktıyı doğrulaması için iki işaret üretir:
konsoldaki `İki grafik de oluşturuldu.` satırı ve PNG dosyalarının
yenilenmiş zaman damgaları.

## Aylara göre satış tutarlarının gruplanması

Zaman serisi grafiği için betik şu adımları uygular:

1. `tarih` sütunu indeks olarak kullanılır.
2. `toplam_tutar` sütunu `resample("MS")` ile **ay başı** dönemlerine
   toplanır (aylık toplam satış).
3. Sonuç `ax.plot` ile işaretli (`marker="o"`), 2 genişlikte çizgi
   grafiği olarak çizilir.

## Kategorilere göre satış tutarlarının gruplanması

Kategori kırılım grafiği için betik şu adımları uygular:

1. `df.groupby("kategori")["toplam_tutar"].sum()` ile her kategorinin
   toplam satış tutarı hesaplanır.
2. Sonuç `sort_values()` ile artan sıraya dizilir; böylece yatay çubuk
   grafiğinde en yüksek kategori üstte görünür.
3. `ax.barh` ile yatay çubuk grafik çizilir.
4. Her çubuğun ucuna satış tutarı ve toplam içindeki yüzde payı
   yazılır, örneğin: `123.456 TL (%17.8)`.

## Grafiklerin oluşturulması ve etiketlendirilmesi

`main()` fonksiyonu başında `VISUALS_DIR.mkdir(parents=True,
exist_ok=True)` çağrısı ile `visuals/` klasörü yoksa oluşturulur.

Her iki grafikte de `dpi=160` ve `bbox_inches="tight"` ayarı kullanılır.
Grafik dosyaya yazıldıktan sonra `plt.close(fig)` ile figure bellekten
temizlenir ve konsola hedef dosya yolları yazdırılır:

```text
Oluşturuldu: <proje_kökün>\visuals\zaman-serisi.png
Oluşturuldu: <proje_kökün>\visuals\kategori-kirilimi.png
```

## Başlık, eksen etiketleri ve TL birimi kuralları

- Her grafikte `fontsize=15`, `pad=14` ayarlı, açıklayıcı bir başlık
  bulunur:
  - Zaman serisi: **Aylara Göre Toplam Satış Tutarı**
  - Kategori kırılım: **Kategorilere Göre Satış Dağılımı**
- Eksen etiketleri:
  - Zaman serisi: x ekseni → `Aylar`, y ekseni → `Satış tutarı (TL)`.
  - Kategori kırılım: x ekseni → `Satış tutarı (TL)`, y ekseni →
    `Ürün kategorisi`.
- **TL birimi zorunludur** — eksenlere `ticker.FuncFormatter(lambda x,
  _: f"{x:,.0f} TL")` uygulanır; değerler binlik ayraçlı ve `TL` ekli
  gösterilir.
- Kategori grafikinde çubuk ucu notları da tutarı `TL` birimiyle ve
  yüzde payıyla yazar.
- Zaman serisi grafiğinde `fig.autofmt_xdate()` tarih etiketlerini
  hizalar; kategori grafiğinde `ax.set_axisbelow(True)` ile ızgara
  çubukların arkasında kalır.
- Zaman serisi grafiğinde yatay ızgara (`ax.grid(True, ...)`), kategori
  grafiğinde ise sadece x eksenine ızgara (`ax.grid(axis="x", ...)")
  kullanılır.

## PNG çıktı yolları

| Çıktı | Hedef yol |
| --- | --- |
| Zaman serisi grafiği | `visuals/zaman-serisi.png` |
| Kategori kırılım grafiği | `visuals/kategori-kirilimi.png` |

Hedef yollar betikte `ROOT_DIR / "visuals" / "<dosya-adı>"` biçiminde
oluşturulur; `ROOT_DIR`, `src/gorsellestirme.py`'nin bir üst klasörü
(proje kök dizini) olduğu için betik hangi dizinden çalıştırılırsa
çalıştırılsın aynı yere yazar.

## Çalıştırma

Betik proje ana klasöründen aşağıdaki komutla çalıştırılır:

```bash
python src/gorsellestirme.py
```

Gerekli paketler: `pandas` ve `matplotlib`.

Betik başarılı çalıştığında iki PNG de yeniden oluşturulur.

## Çıktıların ve hataların kontrolü

Betiğin çalıştırılmasından sonra ajan şu kontrolleri yapar:

- Konsol çıktısında sırasıyla kayıt sayısı, iki `Oluşturuldu: ...`
  satırı ve `İki grafik de oluşturuldu.` mesajı görünür.
- `visuals/zaman-serisi.png` ve `visuals/kategori-kirilimi.png`
  dosyaları vardır ve boyutları 0 bayt değildir.
- Betik bir istisna fırlattıysa (dosya yok, sütun eksik, veri geçersiz)
  hata mesajı ajan tarafından raporlanır ve PNG çıktısı üretilmediği
  için teslim edilmez.

Betiğin üzerinde değişiklik yapılıyorsa mevcut davranış (veri
denetimleri, TL biçimlendirme, etiketler ve PNG yolları) korunmalıdır;
yapılan grafiklerle `visuals/` altındaki mevcut çıktılar yeniden
üretilmeli ve fark kontrolü yapılmalıdır.
