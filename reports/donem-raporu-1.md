# Dönem Raporu 1 — RetailE (Grup E)
**Tarih:** 8 Kasım 2026  
**Proje Yöneticisi (PM):** Umut Kılıç (@Umutklcc)  
**Dönem Kapsamı:** Görev 1 Kapanışından Bugüne (Görev 2 Süreci ve Dönem Sonu Değerlendirmesi)  

---

## 1. Yönetici Özeti
Grup E (RetailE) olarak bu dönemde Görev 2 kapsamındaki sentetik perakende simülasyonu, veri kalitesi (DQ) testleri ve frontend (FE) görselleştirme süreçleri devir zinciri kuralına uygun şekilde tamamlanmıştır. Backend (BE) rolü sorumluluğundaki parametreli simülasyon kodunun ara sürümü incelenmiş; devir zincirinin aksamaması ve şema/tarih uyumsuzluğunun giderilmesi adına çalışan nihai kod (`src/simulasyon_g2.py`), CLI altyapısı ve 150 satırlık referans veri kümesi doğrudan Proje Yöneticisi (PM) tarafından kod refaktörü ile tamamlanarak sisteme kazandırılmıştır (PR #37, `bf040ac`). Ayrıca BE rolü yönergede zorunlu kılınan `skills/be-simulasyon/SKILL.md` dosyasını teslim etmemiştir. Yaşar (DQ) ve Sena (FE) kendi teslimatlarını başarıyla tamamlamış; tüm çıktılar test edilerek `main` dalına entegre edilmiştir.

---

## 2. Teslim Edilenler
Görev 1 kapanışından bu yana ana dala (`main`) kazandırılan somut çıktılar ve doğrulanabilir GitHub kanıtları:
- **G2 Parametreli Simülasyon Betiği ve Referans Veri (BE & PM):** CLI argümanlarıyla yönetilebilen dinamik veri üretim kodu (`src/simulasyon_g2.py`) ve 150 satırlık referans veri kümesi (`data/perakende-satislari-g2.csv`) BE ara sürümü üzerine PM (@Umutklcc) refaktörü ile sisteme alındı (PR #37, `bf040ac`).
- **DQ Veri Sözlüğü ve Analiz Raporu:** M1–M5 kurumsal metrik hesaplamaları, 150 kayıt ve 8 sütunluk şema tanımı ve test özetleri belgelendi (`docs/veri-sozlugu.md`, `docs/analiz-g2.md`, Commit `b771f95`, Commit `db16357`).
- **Uç Durum Test Senaryoları:** 300 kayıt, özel tarih aralığı, aynı gün kayıt, ters tarih ve farklı seed testleri uygulandı (`tests/test-cases.md`, Issue #29).
- **FE Görselleştirme Paketi:** Doğru G2 verisiyle üretilen kategori kırılımı, mağaza dağılımı ve zaman serisi grafikleri depoya işlendi (`visuals/g2-*.png`, `src/gorsellestirme_g2.py`, PR #39, Issue #28).
- **Grup Z Çapraz İnceleme:** Grup Z analiz betiği incelendi ve gelen inceleme yanıtı kapatıldı (#21, #24).
- **Yönetim ve Koordinasyon:** Rol şablonu güncellendi (`AGENTS.md`, `32c1a48`), Görev 2 teknik raporu (`reports/rapor-g2.md`) ve Dönem Raporu 1 (`reports/donem-raporu-1.md`) hazırlandı (Issue #32, Issue #35).

---

## 3. Sayılarla Dönem (Süreç KPI'ları)

| Metrik | Değer | Açıklama |
| :--- | :---: | :--- |
| **Toplam Açılan Issue Sayısı** | 7 | Görev 2 rolleri, alt iş paketleri ve takım veri toplama (#25, #26, #27, #28, #29, #32, #35) |
| **Kapatılan Issue Sayısı** | 7 | Tüm iş paketleri ve takım veri toplama konusu kapatıldı |
| **Merge Edilen PR Sayısı** | 4 | Altyapı, BE simülasyon (#37) ve FE görselleştirme (#39) dahil |
| **PR Başına İlk İnceleme Süresi** | ~25 dk | PM tarafından PR açılışından ilk teknik incelemeye kadar geçen süre |
| **Geciken İş Sayısı** | 0 | PM müdahalesi ve hızlı devir sayesinde teslimler zamanında tamamlandı |

### Üye Bazında Süreç Katkısı

| Üye | Rol | Commit Sayısı | Fiili Durum / Kapatılan Görevler |
| :--- | :--- | :---: | :--- |
| **Umut Kılıç** (@Umutklcc) | PM (ve Fiili BE) | 18+ | Proje koordinasyonu, PR incelemeleri/merge, simülasyon kodunun bizzat yazımı (`bf040ac`), referans veri üretimi ve dönem raporu (#32, #35) |
| **Burak Talha Demir** (@buraktalhademir) | BE | 11 | Simülasyon ara sürümü (PR #37, `8e05940`), eski altyapı taslağı (PR #31); zorunlu `skills/be-simulasyon/SKILL.md` dosyasını teslim etmedi. |
| **Sena Çiftçi** (@senacifci5-prog) | FE | 14+ | Veri görselleştirme grafikleri ve betiğini eksiksiz teslim etti (#28, PR #39) |
| **Yaşar Coşkun** (@yasar07488) | DQ | 22+ | Şema tanımı, metrik analizi, CLI testleri ve görsel onayını eksiksiz teslim etti (#25, #27, #29) |

---

## 4. Tıkananlar ve Çözümler
1. **BE Simülasyonunda Şema ve Kod Gecikmesi:**
   - *Sorun:* Şema belirsizliği ve tarih ofset sapması sebebiyle BE simülasyon kodu ara sürümde kaldı (`8e05940`), devir zincirindeki test adımları tıkanma noktasına geldi.
   - *Çözüm:* PM devreye girerek kod refaktörünü bizzat üstlendi (`bf040ac`), dinamik tarih ofset mantığı düzeltilerek referans CSV üretildi ve PR #37 ile depoya merge edildi.
2. **BE Rolünün Zorunlu Skill Dosyasını Teslim Etmemesi:**
   - *Sorun:* Görev 2 Kural 2 kapsamında zorunlu olan `skills/be-simulasyon/SKILL.md` dosyası Burak tarafından repoya eklenmedi.
   - *Çözüm:* Durum takım raporuna olgusal bir eksiklik olarak yansıtıldı.
3. **SHA-256 Bayt Düzeyinde Hash Farkı:**
   - *Sorun:* Referans dosya ile betik çıktısının ham SHA-256 hash değerleri eşleşmedi.
   - *Çözüm:* DQ tarafından incelenerek farkın Windows (CRLF) ile Linux (LF) satır sonu biçimlerinden kaynaklandığı kanıtlandı; metin normalizasyonu yapılarak G2-TC-05 ile doğrulandı.
4. **FE Görselleştirmede Hatalı Veri Yolu:**
   - *Sorun:* FE ilk betikte yanlışlıkla eski Görev 1 verisini okumuştu.
   - *Çözüm:* PM yönlendirmesiyle veri yolu `data/perakende-satislari-g2.csv` olarak güncellendi ve grafikler PR #39 ile doğru üretildi.
5. **Roller Arası Bağımlılık Sıralaması:**
   - *Sorun:* Simülasyon -> DQ test -> Görselleştirme zincirinde zamanlama baskısı yaşandı.
   - *Çözüm:* Takım içi hızlı geri bildirim döngüleriyle koordinasyon sağlandı.

---

## 5. Kim Ne Yaptı (Olgusal Teslimat Tablosu)

| Üye | Teslim Ettikleri (Kanıt Bağlantıları) | Karşılaşılan Engel ve Gerçekleşen Çözüm | Gelecek Dönem Hedefi |
| :--- | :--- | :--- | :--- |
| **Burak Talha Demir** (BE) | `src/simulasyon_g2.py` ara sürümü ([PR #37](https://github.com/MAKU-VBA-GBT-II/group-e/pull/37), `8e05940`), eski altyapı çalışması ([PR #31](https://github.com/MAKU-VBA-GBT-II/group-e/pull/31)), Grup Z incelemesi ([#21](https://github.com/MAKU-VBA-GBT-II/group-e/issues/21), [#24](https://github.com/MAKU-VBA-GBT-II/group-e/issues/24)), `AGENTS.md` G2 dağılımı (`32c1a48`). `skills/be-simulasyon/SKILL.md` teslim edilmedi. | Şema belirsizliği ve tarih uyuşmazlığı; nihai G2-veri PM refaktörüyle (`bf040ac`) kurtarıldı. | G3 veri değişimi için şema ve handover'ı erken netleştirmek; ek parametreler eklemek. |
| **Yaşar Coşkun** (DQ) | G2 veri seti testleri (150 kayıt, 8 kolon), 300 kayıt/özel tarih/farklı seed testleri, M1–M5 analiz metrikleri, FE görsel onayı, `docs/veri-sozlugu.md` ([Commit b771f95](https://github.com/MAKU-VBA-GBT-II/group-e/commit/b771f95)), `docs/analiz-g2.md` ([Commit db16357](https://github.com/MAKU-VBA-GBT-II/group-e/commit/db16357)), [Issue #29](https://github.com/MAKU-VBA-GBT-II/group-e/issues/29). | Tarih sapması ve SHA-256 CRLF/LF uyumsuzluğu tespit edildi; metin normalizasyonuyla çözüldü. | DQ testlerini daha fazla otomatikleştirmek ve veri kalitesi kontrollerini geliştirmek. |
| **Sena Çiftçi** (FE) | `src/gorsellestirme_g2.py` veri yolu güncellemesi, 3 adet analiz grafiği (`visuals/g2-*.png`), [PR #39](https://github.com/MAKU-VBA-GBT-II/group-e/pull/39), [Issue #28](https://github.com/MAKU-VBA-GBT-II/group-e/issues/28). | Başlangıçta eski G1 verisinin okunması; liderin yönlendirmesiyle doğru veri yolu verilerek aşıldı. | Takım içi koordinasyonu aynı dilde sürdürmek ve analiz çeşitliliğini artırmak. |
| **Umut Kılıç** (PM & Fiili BE) | Proje planlaması (`AGENTS.md`), PR #37 ve #39 teknik inceleme ve merge, fiilen `src/simulasyon_g2.py` refaktörü (`bf040ac`), referans veri üretimi, Görev 2 teknik raporu (`reports/rapor-g2.md`), Dönem Raporu 1 ([Issue #32](https://github.com/MAKU-VBA-GBT-II/group-e/issues/32), [Issue #35](https://github.com/MAKU-VBA-GBT-II/group-e/issues/35)). | BE ara sürümünün devir zincirini tıkaması ve BE skill eksikliği; teknik müdahale yapılarak devir zinciri kuralı korundu. | Partner takımla veri değişiminde şema eşleme ve devir adımlarını erken netleştirmek. |

---

## 6. Dersler (Retrospektif)
1. **Rol Sorumluluğu ve Müdahale Sınırı:** Bir rol takıldığında PM'in teknik müdahalesinin projeyi kurtardığı, ancak takım disiplini ve rol devir zinciri açısından erken aşamada şemaların dondurulması gerektiği görüldü.
2. **Kural ve Skill Takibi:** Her rolün kendi skill dosyasını teslim etme kuralının erken aşamada kontrol edilmesi gerektiği anlaşıldı.
3. **Format ve Çapraz Platform Standardı:** Dosya hash denetimlerinde işletim sistemlerinin satır sonu (CRLF/LF) farklılıklarının test adımlarında önceden kurala bağlanması gerektiği somut olarak tecrübe edildi.

---

## 7. Görev 3 Hazırlığı (Veri Değişimi Planı)
Duyuru-5 kapsamında eşleşilen partner takım ile veri entegrasyonu hazırlıkları:
- **Şema Eşleme:** Partner takımla veri şemaları (kolon isimleri, tipler, para birimleri ve tarih biçimleri) karşılıklı incelenecek.
- **Dönüşüm / Köprü Katmanı:** Gelen harici veri setinin kendi iç veri yapımıza uyması için ETL/mapping fonksiyonu kurgulanacak.
- **Entegrasyon Testi:** Partnerden gelen verinin eksik/hatalı değer kontrolleri DQ tarafından `tests/` altında otomatik senaryolara bağlanacak.

---

### Araç ve Prompt Özeti (Dönem Raporu 1 Kuralı)
*Bu rapor, proje yöneticisi koordinesinde takım içi Issue #32 veri toplama başlığındaki üye beyanları ve git log kayıtları derlenerek `pm-rapor` yönergeleri doğrultusunda hazırlanmıştır.*  
**Prompt Özeti:** `"Dönem Raporu 1 formatına uygun olarak; Issue #32 altındaki Umut, Burak, Yaşar ve Sena beyanlarını, PR #31/#37/#39 kayıtlarını, CRLF/LF ve tarih sapması tıkanıklıklarını, BE skill eksikliğini ve süreç KPI'larını içeren olgusal reports/donem-raporu-1.md dosyasını üret."`