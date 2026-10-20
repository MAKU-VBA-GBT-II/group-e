# Hafta 3 Sprint Raporu (RetailE - Grup E)

**Dönem:** Hafta 3 (Görev 1 - Sprint Kapanışı)  
**Proje Lideri (PM):** Umut Kılıç  
**Tarih:** 20 Ekim 2026  

---

## 1. Planlanan İşler
- [x] Görev 1 kapsamında 4 ana Issue'nun açılması (`G1-veri`, `G1-analiz`, `G1-gorsel`, `G1-test`).
- [x] Görev kartlarının `RetailE-Grup E Panosu` Todo sütununa eklenmesi ve üyelere atanması.
- [x] Reponun kök dizinine ajan skill envanteri olan `AGENTS.md` dosyasının eklenmesi.
- [x] PM rolü için `skills/pm-rapor/SKILL.md` dosyasının hazırlanması.
- [x] BE: Sabit tohumlu sentetik perakende satış verisi (`data/perakende-satislari.csv`), veri sözlüğü (`docs/veri-sozlugu-g1.md`) ve üretim betiğinin hazırlanması.
- [x] FE: Grafik taslaklarının Issue üzerinde paylaşılması ve görselleştirme çıktılarının (`visuals/`) üretilmesi.
- [x] DQ: Keşifçi veri analiz raporunun (`docs/analiz-g1.md`) hazırlanması.
- [x] DQ: Veri doğrulama test senaryolarının (`tests/test-cases.md`) tamamlanması.

---

## 2. Yapılan İşler (Sprint Sonu Çıktıları)
- Tüm ekip üyeleri kendilerine tanımlanan Issue kabul kriterlerini eksiksiz yerine getirdi.
- Devir teslim zinciri GitHub Issue yorumları üzerinden işletildi (BE -> DQ ve BE -> FE devirleri sağlandı).
- Bütün roller kendi ajan skill (`SKILL.md`) dosyalarını oluşturarak teslim etti.
- Panodaki tüm görev kartları başarıyla **Done** sütununa taşındı ve kapatıldı.

---

## 3. Kim Ne Yaptı? (Devir Teslim Zinciri Kanıtları)
- **PM (Umut Kılıç):** Sprint planlaması, issue & pano yönetimi, `AGENTS.md` envanteri, `skills/pm-rapor` ve sprint kapanış raporunu tamamladı.
- **BE (Yaşar Coşkun):** `src/veri_uretici.py` ile sabit tohumlu sentetik veriyi (`data/perakende-satislari.csv`), `docs/veri-sozlugu-g1.md` dokümanını ve `skills/be-veri/SKILL.md` skill'ini tamamladı; G1-analiz ve G1-gorsel Issue'larına devir teslim yorumlarını ekledi.
- **FE (Burak Talha Demir):** Kodlama öncesi 2 adet görsel taslağını `G1-gorsel` Issue'sunda paylaştı. Ardından `src/gorsellestirme.py` betiğini çalıştırarak grafikleri `visuals/` klasörüne aktardı ve `skills/fe-gorsel/SKILL.md` dosyasını oluşturdu.
- **DQ (Sena Çiftçi):** Veri şeması için `tests/test-cases.md` ve `skills/dq-test/SKILL.md` testlerini hazırladı. BE'nin veri teslimi sonrası `docs/analiz-g1.md` keşifçi analiz raporunu ve `skills/dq-analiz/SKILL.md` dosyasını teslim etti.

---

## 4. Tıkanan Noktalar (Blokajlar)
- Sprint süresince kritik bir blokaj yaşanmamış olup, devir teslim zinciri son teslim tarihi olan 20 Ekim 23:59 öncesinde başarıyla tamamlanmıştır.