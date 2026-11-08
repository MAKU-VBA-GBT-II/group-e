# Görev 2 Raporu — RetailE (Grup E)
**Tarih:** 8 Kasım 2026  
**Proje Yöneticisi (PM):** Umut Kılıç (@Umutklcc)  
**Kapsam:** Görev 2 Simülasyon, Veri Kalitesi, Görselleştirme ve Süreç Metrikleri  

---

## 1. Yönetici Özeti
Grup E (RetailE) olarak Görev 2 kapsamındaki sentetik perakende simülasyonu, veri kalitesi (DQ) testleri ve frontend (FE) görselleştirme adımlarını "devir zinciri" kuralına tam uyumla tamamladık. Backend (BE) rolü kapsamındaki simülasyon kodu ve referans veri üretimi gereksinimi, sürecin aksamaması adına doğrudan Proje Yöneticisi (PM) tarafından üstlenilerek geliştirilmiş ve sisteme kazandırılmıştır. Karşılaşılan dinamik tarih hesaplama sapması, satır sonu kaynaklı SHA-256 hash farkı ve hatalı veri yolu eşleşmeleri ekip içi hızlı inceleme döngüleriyle çözülmüştür. Tüm bileşenler `main` dalına entegre edilmiş, test senaryoları belgelenmiş ve takım teslimatları kapatılan görevlerle mühürlenmiştir.

---

## 2. Teslim Edilenler
Görev 1 kapanışından bu yana ana dala (`main`) kazandırılan temel çıktılar:
- **G2 Parametreli Simülasyon Betiği ve Veri (PM Katkısıyla):** CLI argümanlarıyla yönetilebilen dinamik veri üretim kodu (`src/simulasyon_g2.py`) ve 150 satırlık referans veri kümesi (`data/perakende-satislari-g2.csv`) doğrudan PM (@Umutklcc) tarafından geliştirilerek sisteme alındı (PR #37).
- **DQ Veri Sözlüğü ve Analiz Raporu:** M1–M5 kurumsal metrik hesaplamaları, alan kuralları ve test özetleri belgelendi (`docs/veri-sozlugu.md`, `docs/analiz-g2.md`).
- **Uç Durum Test Senaryoları:** 300 kayıt, özel tarih aralıkları ve negatif test senaryoları uygulandı (`tests/test-cases.md`).
- **FE Görselleştirme Paketi:** Doğru G2 verisiyle üretilen kategori kırılımı, mağaza dağılımı ve zaman serisi grafikleri depoya işlendi (`visuals/g2-*.png`, `src/gorsellestirme_g2.py`, PR #39).

---

## 3. Sayılarla Dönem (Süreç KPI'ları)
Görev 2 boyunca GitHub etkinlikleri ve commit/PR izleri üzerinden derlenen metrik tablosu:

| Metrik | Değer | Açıklama |
| :--- | :---: | :--- |
| **Toplam Açılan Issue** | 6 | Görev 2 rolleri ve alt iş paketleri (#25, #26, #27, #28, #29, #35) |
| **Kapatılan Issue** | 6 | Tüm iş paketleri teslim yorumlarıyla tamamlandı |
| **Merge Edilen PR Sayısı** | 4 | Altyapı, BE simülasyon (#37) ve FE görselleştirme (#39) dahil |
| **PR Başına İlk İnceleme Süresi** | ~25 dk | PR açılışından ilk teknik inceleme yorumuna kadar geçen ortalama süre |
| **Geciken İş Sayısı** | 0 | Tüm teslimler belirlenen son teslim tarihinden (8 Kasım 23:59) önce bitti |

### Üye Bazında Süreç Katkısı

| Üye | Rol | Commit Sayısı | İlgili / Kapatılan Görevler |
| :--- | :--- | :---: | :--- |
| **Umut Kılıç** (@Umutklcc) | PM (ve Fiili BE) | 28+ | Proje yönetimi, PR incelemeleri/merge, simülasyon kodu ve referans CSV üretimi (#26, #35, PR #37) |
| **Burak Talha Demir** (@buraktalhademir) | BE (Kayıtlı Rol) | 1-2 | Görev 2 kapsamındaki kod teslimatını tamamlayamadı; ilk aşama altyapı denemesi (PR #31) haricinde kod çıktısı bulunmuyor. |
| **Sena Çiftçi** (@senacifci5-prog) | FE | 14+ | Veri görselleştirme grafikleri ve betik (#28, PR #39) |
| **Yaşar Coşkun** (@yasar07488) | DQ | 22+ | Şema tanımı, metrik analizi, CLI testleri (#25, #27, #29) |

---

## 4. Tıkananlar ve Çözümler
1. **BE Rolü Teslimatının Aksaması:**
   - *Sorun:* Backend sorumluluğundaki parametreli simülasyon kodunun zamanında çıkmaması zincirdeki DQ ve FE adımlarını durma noktasına getirdi.
   - *Çözüm:* PM devreye girerek `src/simulasyon_g2.py` betiğini ve referans `data/perakende-satislari-g2.csv` dosyasını bizzat kodladı ve PR #37 ile depoya kattı.
2. **Dinamik Simülasyonda Tarih Aralığı Sapması:**
   - *Sorun:* İlk simülasyon denemesinde son kayıt tarihi bitişi aşıyor ve 103/150 tarih uyuşmazlığı oluşuyordu.
   - *Çözüm:* DQ'nun inceleme bildirimi doğrultusunda kod tarafında `toplam_gun = (bitis - baslangic).days` ve gün ofseti mantığı düzeltilerek yeniden üretildi (`bf040ac`).
3. **SHA-256 Bayt Düzeyinde Hash Farkı:**
   - *Sorun:* Referans dosya ile test çıktısının ham hash değerleri eşleşmedi.
   - *Çözüm:* Farkın Windows (CRLF) ve Unix/Linux (LF) satır sonu biçimlerinden kaynaklandığı kanıtlandı; metin normalizasyonu yapılarak doğrulaması sağlandı.
4. **Görselleştirmede Hatalı Veri Yolu:**
   - *Sorun:* FE ilk betikte eski G1 referans verisini okumuştu.
   - *Çözüm:* PM yönlendirmesiyle veri yolu `data/perakende-satislari-g2.csv` olarak güncellendi ve grafikler G2 çıktılarıyla yeniden üretildi (PR #39).

---

## 5. Kim Ne Yaptı (Olgusal Teslimat Tablosu)

| Üye | Teslim Ettikleri (Kanıt Bağlantıları) | Karşılaşılan Engel ve Çözüm | Gelecek Dönem Hedefi |
| :--- | :--- | :--- | :--- |
| **Umut Kılıç** (PM & Fiili BE) | Proje koordinasyonu (`AGENTS.md`), PR #37 ve #39 yönetimi, fiili olarak `src/simulasyon_g2.py` CLI simülasyonu ve `data/perakende-satislari-g2.csv` üretimi ([Issue #26](https://github.com/MAKU-VBA-GBT-II/group-e/issues/26), [Issue #35](https://github.com/MAKU-VBA-GBT-II/group-e/issues/35), [PR #37](https://github.com/MAKU-VBA-GBT-II/group-e/pull/37)) | BE teslimatının gecikmesi; kodlama PM tarafından üstlenilerek blokaj çözüldü. | Görev dağılımlarını daha sıkı kontrol ederek herkesin kendi rol teslimatını yapmasını sağlamak. |
| **Burak Talha Demir** (BE) | Kapsam dahilinde geçerli simülasyon veya veri teslimatı bulunmamaktadır; eski taslak çalışması yapılmıştır ([PR #31](https://github.com/MAKU-VBA-GBT-II/group-e/pull/31)). | Görev 2 simülasyon isterlerini teslim edemedi; iş PM tarafından tamamlandı. | Süreç içi sorumlulukları eksiksiz üstlenmek. |
| **Sena Çiftçi** (FE) | `src/gorsellestirme_g2.py`, 3 adet analiz grafiği (`visuals/g2-*.png`) ([PR #39](https://github.com/MAKU-VBA-GBT-II/group-e/pull/39), [Issue #28](https://github.com/MAKU-VBA-GBT-II/group-e/issues/28)) | İlk aşamada G1 verisinin okunması; PM uyarısıyla doğru dosya yolu entegre edilerek aşıldı. | Raporlama ve grafik çeşitliliğini artırmak, takım içi koordinasyonu aynı dilde sürdürmek. |
| **Yaşar Coşkun** (DQ) | `docs/veri-sozlugu.md`, `docs/analiz-g2.md`, `tests/test-cases.md`, FE görsel onayı ([Commit db16357](https://github.com/MAKU-VBA-GBT-II/group-e/commit/db16357), [Commit b771f95](https://github.com/MAKU-VBA-GBT-II/group-e/commit/b771f95), [Issue #29](https://github.com/MAKU-VBA-GBT-II/group-e/issues/29)) | Tarih sapması ve SHA-256 CRLF/LF uyumsuzluğu incelenerek metin normalizasyonuyla çözüldü. | Testleri otomatikleştirmek, veri kalitesi denetimlerini CI/CD ortamına taşımak. |

---

## 6. Dersler (Retrospektif)
1. **Rol Sorumluluğu ve Yedekleme:** Bir rolün aksaması durumunda PM müdahalesinin süreci kurtardığı, ancak her üyenin kendi rolünü teslim etmesinin takım sürdürülebilirliği için şart olduğu görüldü.
2. **Çapraz Platform ve Format Farkındalığı:** Dosya hash denetimlerinde işletim sistemlerinin satır sonu (CRLF/LF) farklılıklarının test adımlarında önceden kurala bağlanması gerektiği öğrenildi.
3. **Devir Sıralaması:** "BE simülasyonu $\rightarrow$ DQ analizi $\rightarrow$ FE görselleştirmesi $\rightarrow$ DQ teyidi" akışının iş tekrarını önlediği kanıtlandı.

---

## 7. Görev 3 Hazırlığı (Veri Değişimi Planı)
Duyuru-5 kapsamında eşleşilen partner takım ile veri entegrasyonu hazırlıkları:
- **Şema Eşleme:** Partner takımla veri şemaları (kolon isimleri, tipler, para birimleri ve tarih biçimleri) karşılıklı incelenecek.
- **Dönüşüm / Köprü Katmanı:** Gelen harici veri setinin kendi iç veri yapımıza uyması için ETL/mapping fonksiyonu kurgulanacak.
- **Entegrasyon Testi:** Partnerden gelen verinin eksik/hatalı değer kontrolleri DQ tarafından `tests/` altında otomatik senaryolara bağlanacak.

---

### Araç ve Prompt Özeti (Görev 2 Kuralı)
*Bu rapor, proje yöneticisi koordinesinde takım içi Issue/PR teslim verileri ve git log kayıtları toplanarak `pm-rapor` yönergeleri doğrultusunda hazırlanmıştır.*  
**Prompt Özeti:** `"Görev 2 Raporu formatına uygun olarak; BE görevinin fiilen PM tarafından tamamlandığı olgusu, Sena (FE) ve Yaşar (DQ) teslim kanıtları, PR #37/#39 kayıtları, CRLF/LF ve tarih sapması tıkanıklıkları ile süreç KPI'larını içeren olgusal reports/rapor-g2.md dosyasını üret."`