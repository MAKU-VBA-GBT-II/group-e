# G2 — Perakende Satış Analizi

**Durum:** BE G2 simülasyon verisi bekleniyor; aşağıdaki metrik sonuçları henüz hesaplanmadı. G1 verisindeki değerler G2 sonucu olarak kullanılmamıştır.

## Veri kaynağı
- G2 veri dosyası: BE PR'ı sonrası doğrulanacak
- G2 veri sürümü / commit: bekleniyor
- Parametreler ve tohum: BE PR'ı sonrası belgelenecek
- Şema ve metrik tanımları: `docs/veri-sozlugu.md`

## Beş metrik

| Kod | Metrik | Sonuç | Birim |
| --- | --- | --- | --- |
| M1 | Toplam satış geliri | BE verisi bekleniyor | TL |
| M2 | Ortalama işlem tutarı | BE verisi bekleniyor | TL/işlem |
| M3 | Toplam satılan ürün adedi | BE verisi bekleniyor | adet |
| M4 | Kategori bazında satış geliri | BE verisi bekleniyor | TL/kategori |
| M5 | Mağaza bazında satış geliri | BE verisi bekleniyor | TL/mağaza |

## Bulgular
G2 verisi doğrulanıp beş metrik hesaplandıktan sonra veriye dayalı gözlemler ve en az bir uygulanabilir öneri buraya eklenecek. Şu aşamada doğrulanmamış sayısal bulgu yazılmamıştır.

## Tamamlama kontrolü
- [ ] BE simülasyon kodu ve G2 CSV doğrulandı
- [ ] Veri sözlüğü G2 alanlarına göre güncellendi
- [ ] Beş metrik G2 CSV üzerinden hesaplandı
- [ ] Kategori ve mağaza kırılımları raporlandı
- [ ] Bulgular ve eylem önerisi yazıldı
- [ ] Test sonuçları ve ilgili commit bağlantıları eklendi

İlgili görev: #27.
