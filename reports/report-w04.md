# Hafta 4 Sprint Raporu — Grup E (RetailE)
**Hazırlayan:** Umut Kılıç (PM) · **Dönem:** Hafta 4 (Görev 1 Kapanış, Test & Sürüm) · **Tarih:** 27 Ekim 2026

---

## 1. Planlanan İşler
- Hafta 3 denetiminde tespit edilen tüm blokajların (BE devir teslimi, FE skill/taslak eksikliği, DQ analiz uyuşmazlığı) kapatılması.
- DQ tarafından `tests/test-cases.md` senaryolarının gerçek veri üzerinde koşturulup `tests/test-log.md` günlüğüne işlenmesi.
- DQ tarafından en az 2 adet hata/iyileştirme Issue'su açılması ve ilgili rollere atanması.
- BE ve FE rollerinin kendilerine atanan Issue'ları düzeltme commit'leriyle kapatması.
- DQ'nun nihai veri ve şema uyumunu onaylaması.
- Görev 1'in tüm gereksinimleri tamamlanarak `gorev1-final` resmi sürümünün yayımlanması.

---

## 2. Kim Ne Yaptı? (Teslimat ve Kanıt Tablosu)

| Rol | Kişi | Görev Kodu | Issue | Yapılan İş & Teslim Edilen Dosyalar | Durum |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **PM** | Umut Kılıç | PM-Kapanış | #10, #15 | Rapor revizyonları tamamlandı, `report-w04.md` üretildi, `AGENTS.md` güncellendi ve `gorev1-final` release'i yayımlandı. | Tamamlandı |
| **BE** | Yaşar Coşkun | G1-Düzeltme | #11, #21 | Veri sözlüğü güncellendi, devir yorumu girildi, Python analiz betiği hata/iyileştirmesi kapatıldı (`c2a1db1`). | Tamamlandı |
| **DQ** | Sena Çiftçi | G1-Test & Onay | #12, #14 | `test-cases.md` ve `test-log.md` 5 senaryoyla tamamlandı; #20 ve #21 numaralı Issue'lar açıldı; G1-analiz onay yorumu girildi. | Tamamlandı |
| **FE** | Burak T. Demir | G1-Görsel | #13, #20 | `skills/fe-gorsel/SKILL.md` dolduruldu, grafikler revize edildi, eksen/birim iyileştirmeleri yapıldı (`1cbb3ce`). | Tamamlandı |

---

## 3. Test ve Kalite Süreci (DQ Rapor Özeti)
- `tests/test-cases.md` altında tanımlanan 5 senaryo (TC-01...TC-05) `data/perakende-satislari.csv` ve `src/analiz_g1.py` üzerinde koşturulmuştur.
- Tüm senaryoların başarıyla geçtiği `tests/test-log.md` dosyasına tarihli olarak işlenmiştir.
- Süreçte açılan geliştirme Issue'ları (#20 FE, #21 BE) ilgili geliştiriciler tarafından commit mesajı kurallarına uygun biçimde çözülerek kapatılmıştır.
- Analiz verilerinin CSV ile birebir tutarlı olduğu (toplam ciro: 239.182,23 TL) DQ tarafından onaylanmıştır.

---

## 4. Kapanış ve Sürüm
Görev 1 kapsamındaki tüm veri, analiz, görselleştirme, test ve dokümantasyon gereksinimleri eksiksiz tamamlanmış; `gorev1-final` etiketiyle GitHub Releases üzerinden ilk ana kararlı sürüm yayımlanmıştır.