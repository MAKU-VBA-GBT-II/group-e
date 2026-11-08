# Görev 2 Raporu — RetailE (Grup E)
**Tarih:** 8 Kasım 2026  
**Proje Yöneticisi (PM):** Umut Kılıç (@Umutklcc)  
**Kapsam:** Görev 2 Simülasyon, Veri Kalitesi, Görselleştirme ve Süreç Metrikleri  

---

## 1. Yönetici Özeti
Grup E (RetailE) olarak Görev 2 kapsamındaki sentetik perakende simülasyonu, veri kalitesi (DQ) testleri ve frontend (FE) görselleştirme süreçleri tamamlanmıştır. Backend (BE) rolü sorumluluğundaki parametreli simülasyon kodunun gereksinimleri karşılamaması ve devir zincirini tıkaması sebebiyle; projenin aksamaması adına çalışan nihai kod (`src/simulasyon_g2.py`), CLI altyapısı ve 150 satırlık referans veri kümesi doğrudan Proje Yöneticisi (PM) tarafından kodlanarak sisteme kazandırılmıştır (PR #37, `bf040ac`). Ayrıca BE rolü yönergede zorunlu kılınan `skills/be-simulasyon/SKILL.md` dosyasını teslim etmemiştir. Yaşar (DQ) ve Sena (FE) kendi teslimatlarını başarıyla tamamlamış; tüm çıktılar test edilerek `main` dalına entegre edilmiştir.

---

## 2. Teslim Edilenler
Görev 1 kapanışından bu yana ana dala (`main`) kazandırılan somut çıktılar:
- **G2 Parametreli Simülasyon Betiği ve Referans Veri (PM Katkısıyla):** `argparse`, deterministik `seed=42` ve `ROOT_DIR` yapısıyla çalışan dinamik simülasyon kodu (`src/simulasyon_g2.py`) ve 150 satırlık referans veri kümesi (`data/perakende-satislari-g2.csv`) doğrudan PM (@Umutklcc) tarafından geliştirilerek sisteme alındı (PR #37, `bf040ac`).
- **DQ Veri Sözlüğü ve Analiz Raporu:** M1–M5 kurumsal metrik hesaplamaları, alan kuralları ve test özetleri belgelendi (`docs/veri-sozlugu.md`, `docs/analiz-g2.md`).
- **Uç Durum Test Senaryoları:** 300 kayıt, özel tarih aralıkları ve negatif test senaryoları uygulandı (`tests/test-cases.md`).
- **FE Görselleştirme Paketi:** Doğru G2 verisiyle üretilen kategori kırılımı, mağaza dağılımı ve zaman serisi grafikleri depoya işlendi (`visuals/g2-*.png`, `src/gorsellestirme_g2.py`, PR #39).

---

## 3. Sayılarla Süreç (Süreç KPI'ları)

| Metrik | Değer | Açıklama |
| :--- | :---: | :--- |
| **Toplam Açılan Issue** | 7 | Görev 2 rolleri, alt iş paketleri ve takım veri toplama (#25, #26, #27, #28, #29, #32, #35) |
| **Kapatılan Issue** | 7 | Tüm iş paketleri teslim yorumlarıyla tamamlandı |
| **Merge Edilen PR Sayısı** | 4 | Altyapı, BE simülasyon (#37) ve FE görselleştirme (#39) dahil |
| **PR Başına İlk İnceleme Süresi** | ~25 dk | PM tarafından PR açılışından ilk teknik incelemeye kadar geçen süre |
| **Geciken İş Sayısı** | 0 | PM müdahalesi sayesinde teslimler son teslim tarihinden önce tamamlandı |

### Üye Bazında Süreç Katkısı

| Üye | Rol | Commit Sayısı | Fiili Durum / Kapatılan Görevler |
| :--- | :--- | :---: | :--- |
| **Umut Kılıç** (@Umutklcc) | PM (ve Fiili BE) | 18+ | Proje koordinasyonu, PR incelemeleri/merge, simülasyon kodunun bizzat yazımı (`bf040ac`), referans veri üretimi ve Görev 2 raporu (#35) |
| **Burak Talha Demir** (@buraktalhademir) | BE | 1-2 | Görev 2 simülasyon isterlerini ve kodunu tamamlayamadı (PR #31 eski taslaktır); zorunlu `skills/be-simulasyon/SKILL.md` dosyasını teslim etmedi. |
| **Sena Çiftçi** (@senacifci5-prog) | FE | 14+ | Veri görselleştirme grafikleri ve betiğini eksiksiz teslim etti (#28, PR #39) |
| **Yaşar Coşkun** (@yasar07488) | DQ | 22+ | Şema tanımı, metrik analizi, CLI testleri ve görsel onayını eksiksiz teslim etti (#25, #27, #29) |

---

## 4. Tıkananlar ve Çözümler
1. **BE Rolünün Görevi Yapamaması ve Süreci Tıkaması:**
   - *Sorun:* Backend sorumluluğundaki parametreli simülasyon kodu zamanında ve çalışır vaziyette çıkmadı, devir zincirindeki DQ ve FE adımları tıkanma noktasına geldi.
   - *Çözüm:* PM (@Umutklcc) inisiyatif alarak bizzat kodlamayı üstlendi; `src/simulasyon_g2.py` kodunu çalışır hale getirdi (`bf040ac`), referans CSV dosyasını üretti ve PR #37 ile depoya kattı.
2. **BE Rolünün Zorunlu Skill Dosyasını Teslim Etmemesi:**
   - *Sorun:* Görev 2 Kural 2 kapsamında zorunlu olan `skills/be-simulasyon/SKILL.md` dosyası Burak tarafından repoya eklenmedi.
   - *Çözüm:* Durum takım raporuna olgusal bir eksiklik olarak yansıtıldı.
3. **Dinamik Simülasyonda Tarih Aralığı Sapması:**
   - *Sorun:* İlk simülasyon denemesinde son kayıt tarihi bitiş tarihini aşıyordu.
   - *Çözüm:* PM tarafından `(bitis - baslangic).days` ve ofset yuvarlama formülü düzeltilerek DQ referansıyla tam eşleşme sağlandı (`bf040ac`).
4. **SHA-256 Bayt Düzeyinde Hash Farkı:**
   - *Sorun:* Referans dosya ile test çıktısının ham hash değerleri eşleşmedi.
   - *Çözüm:* Windows (CRLF) ve Unix/Linux (LF) satır sonu biçimlerinden kaynaklandığı kanıtlandı; metin normalizasyonu yapılarak doğrulandı.
5. **Görselleştirmede Hatalı Veri Yolu:**
   - *Sorun:* FE ilk betikte eski G1 referans verisini okumuştu.
   - *Çözüm:* PM yönlendirmesiyle veri yolu `data/perakende-satislari-g2.csv` olarak güncellendi ve grafikler PR #39 ile doğru üretildi.

---

## 5. Kim Ne Yaptı (Olgusal Teslimat Tablosu)

| Üye | Teslim Ettikleri (Kanıt Bağlantıları) | Karşılaşılan Engel ve Gerçekleşen Çözüm | Gelecek Dönem Hedefi |
| :--- | :--- | :--- | :--- |
| **Burak Talha Demir** (BE) | Kapsam dahilinde geçerli ve çalışan bir simülasyon kodu teslim edemedi. PR #31 eski taslaktır; PR #37 nihai kodu Umut tarafından yazıldı. `skills/be-simulasyon/SKILL.md` teslim edilmedi. | Görev 2 simülasyon isterlerini ve skill zorunluluğunu tamamlayamadı; iş PM tarafından yapıldı. | Kendi rol sorumluluğunu bizzat üstlenmesi gerekmektedir. |
| **Umut Kılıç** (PM & Fiili BE) | Proje koordinasyonu (`AGENTS.md`), PR #37 ve #39 inceleme/yönetimi, fiilen `src/simulasyon_g2.py` kodlaması (`bf040ac`), referans veri üretimi ve Görev 2 raporu ([Issue #35](https://github.com/MAKU-VBA-GBT-II/group-e/issues/35), [PR #37](https://github.com/MAKU-VBA-GBT-II/group-e/pull/37)) | BE teslimatının aksaması ve skill açığı; kodlama ve kurtarma PM tarafından yapılarak devir zinciri işletildi. | Görev 3'te her üyenin kendi sorumluluğunu teslim etmesini sağlamak. |
| **Sena Çiftçi** (FE) | `src/gorsellestirme_g2.py`, 3 adet analiz grafiği (`visuals/g2-*.png`), `skills/fe-gorsel/SKILL.md` ([PR #39](https://github.com/MAKU-VBA-GBT-II/group-e/pull/39), [Issue #28](https://github.com/MAKU-VBA-GBT-II/group-e/issues/28)) | İlk aşamada G1 verisinin okunması; PM uyarısıyla doğru dosya yolu entegre edilerek aşıldı. | Raporlama ve grafik çeşitliliğini artırmak, takım içi koordinasyonu sürdürmek. |
| **Yaşar Coşkun** (DQ) | `docs/veri-sozlugu.md`, `docs/analiz-g2.md`, `tests/test-cases.md`, FE görsel onayı, `skills/dq-*/SKILL.md` ([Commit db16357](https://github.com/MAKU-VBA-GBT-II/group-e/commit/db16357), [Commit b771f95](https://github.com/MAKU-VBA-GBT-II/group-e/commit/b771f95), [Issue #29](https://github.com/MAKU-VBA-GBT-II/group-e/issues/29)) | Tarih sapması ve SHA-256 CRLF/LF uyumsuzluğu incelenerek metin normalizasyonuyla çözüldü. | Testleri otomatikleştirmek, veri kalitesi denetimlerini CI/CD ortamına taşımak. |

---

## 6. Dersler (Retrospektif)
1. **Rol Sorumluluğu ve Yedekleme:** Bir rol çalışmadığında PM'in teknik müdahalesinin projeyi kurtardığı, ancak takım disiplini açısından sürdürülemez olduğu görüldü.
2. **Kural ve Skill Takibi:** Her rolün kendi skill dosyasını teslim etme zorunluluğunun takım içi denetimlerde daha erken takip edilmesi gerektiği anlaşıldı.
3. **Format ve Çapraz Platform:** Dosya hash denetimlerinde işletim sistemlerinin satır sonu (CRLF/LF) farklılıklarının test adımlarında önceden kurala bağlanması gerektiği öğrenildi.

---

## 7. Görev 3 Hazırlığı (Veri Değişimi Planı)
Duyuru-5 kapsamında eşleşilen partner takım ile veri entegrasyonu hazırlıkları:
- **Şema Eşleme:** Partner takımla veri şemaları (kolon isimleri, tipler, para birimleri ve tarih biçimleri) karşılıklı incelenecek.
- **Dönüşüm / Köprü Katmanı:** Gelen harici veri setinin kendi iç veri yapımıza uyması için ETL/mapping fonksiyonu kurgulanacak.
- **Entegrasyon Testi:** Partnerden gelen verinin eksik/hatalı değer kontrolleri DQ tarafından `tests/` altında otomatik senaryolara bağlanacak.

---

### Araç ve Prompt Özeti (Görev 2 Kuralı)
*Bu rapor, proje yöneticisi koordinesinde takım içi teslim verileri ve git log kayıtları toplanarak `pm-rapor` yönergeleri doğrultusunda hazırlanmıştır.*  
**Prompt Özeti:** `"Görev 2 Raporu formatına uygun olarak; BE rolünün işi tamamlayamadığı ve skill teslim etmediği olgusu, PM'in fiilen simülasyonu kodlayarak projeyi kurtardığı gerçeği, Sena (FE) ve Yaşar (DQ) teslim kanıtları, PR #31/#37/#39 kayıtları, CRLF/LF ve tarih sapması tıkanıklıkları ile süreç KPI'larını içeren olgusal reports/rapor-g2.md dosyasını üret."`