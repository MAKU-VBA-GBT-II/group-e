# Hafta 3 Sprint Raporu — Grup E (RetailE)

**Hazırlayan:** Umut Kılıç (PM) · **Dönem:** Hafta 3 (Görev 1 Sprint Sonu ve PM Denetimi) · **İlk Sürüm:** 18 Ekim 2026 · **Revizyon Tarihi:** 25 Ekim 2026

---

## 1. Planlanan İşler
- [x] Görev 1 geliştirme Issue'larının (#11, #12, #13, #14) son tarih ve kabul kriterleriyle açılıp panoya işlenmesi.
- [x] Reponun kök dizinine merkezi ajan envanterinin (`AGENTS.md`) ve `skills/pm-rapor/SKILL.md` yönergesinin eklenmesi.
- [ ] BE: 150 satırlık sentetik veri, veri sözlüğü ve devir teslim yorumlarının tamamlanması.
- [ ] DQ: Sentetik CSV ile birebir tutarlı keşifçi analiz raporunun hazırlanması.
- [ ] DQ: 5 adet kalite kontrol/şema test senaryosunun kanıt yorumlarıyla doğrulanması.
- [ ] FE: Taslak çizim ve veri görselleştirme betiğinin eksiksiz bir `SKILL.md` ile teslim edilmesi.

---

## 2. Kim Ne Yaptı? (Teslimat ve Kanıt Tablosu)

| Rol | Kişi | Görev Kodu | Issue | Teslim Edilen Dosyalar | Commit Hash | Durum |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **PM** | Umut Kılıç | PM-Planlama | #10 | `reports/report-w03.md`, `AGENTS.md`, `skills/pm-rapor/SKILL.md` | `7cbbf8b` | Tamamlandı |
| **BE** | Yaşar Coşkun | G1-veri | #11 | `src/veri_ureticisi.py`, `data/perakende-satislari.csv`, `docs/veri-sozlugu-g1.md` | `3558818` | Tamamlandı (Sözlük ve devir yorumu güncellendi) |
| **DQ** | Sena Çiftçi | G1-analiz | #12 | `src/analiz_g1.py`, `docs/analiz-g1.md` | `6c7807c` | Tamamlandı (Dinamik analiz betiği ve rapor eklendi) |
| **DQ** | Sena Çiftçi | G1-test | #14 | `tests/test-cases.md`, `skills/dq-test/SKILL.md` | `6c7807c` | Tamamlandı (Test tablosuna Girdi ve Adımlar eklendi) |
| **FE** | Burak T. Demir | G1-gorsel | #13 | `src/gorsellestirme.py`, `visuals/*.png`, `skills/fe-gorsel/SKILL.md` | `4e97699`, `1cbb3ce` | Tamamlandı (Grafikler üretildi, skill dolduruldu) |
---

## 3. Tıkanan / Sorunlu Noktalar (Blokajlar)
Hafta 3 sprint kapanışında gerçekleştirilen fiziksel dosya ve Issue denetimleri sonucunda tespit edilen 3 temel blokaj aşağıdadır:

1. **FE Skill Dosyasının Boş Olması ve Taslak Eksikliği:**  
   `skills/fe-gorsel/SKILL.md` dosyası depoda bulunmasına karşın içeriği 0 bayttır[cite: 8]. Ayrıca kod yazımından önce Issue'ya eklenmesi zorunlu olan tel çerçeve/taslak çizim yer almamış; görseller kodla üretildikten sonra yüklenmiştir[cite: 8].

2. **Kırılan Devir Teslim Zinciri:**  
   BE rolü veri üretimini tamamlamasına rağmen #13 numaralı FE Issue kartı altına beklenen `"Veri hazır — commit 3558818"` devir yorumunu girmemiştir[cite: 7]. Bu durum, FE rolünün iş başlama resmi onayını kayıtsız bırakmış ve süreç izlenebilirliğini koparmıştır[cite: 7].

3. **DQ Analizindeki Ciddi Veri Uyuşmazlığı ve Betik Eksikliği:**  
   `docs/analiz-g1.md` raporunda toplam ciro 145.000 TL olarak belirtilmiş; ancak BE'nin ürettiği `data/perakende-satislari.csv` dosyasında gerçek cironun 239.182,23 TL olduğu saptanmıştır. Raporda olmayan şehirler (İstanbul, Ankara) listelenmiş, kategori oranları çelişmiş ve bu sayıları hesaplayan herhangi bir analiz betiği depoya eklenmemiştir.

---

## 4. Gelecek Hafta Planı (Hafta 4)
- [ ] **FE Düzeltmeleri:** Burak Talha Demir'in `skills/fe-gorsel/SKILL.md` dosyasını doldurması, taslak çizim fotoğrafını #13'e eklemesi ve en az 2 commit kuralını sağlaması[cite: 8].
- [ ] **BE Düzeltmeleri:** Yaşar Coşkun'un #13 kartına devir yorumunu girmesi, #11 kapanışındaki commit yer tutucusunu güncellemesi ve `docs/veri-sozlugu-g1.md` tablosuna aralık/birim sütunlarını eklemesi[cite: 7].
- [ ] **DQ Düzeltmeleri:** Sena Çiftçi'nin analiz betiğini yazması, `docs/analiz-g1.md` dosyasını gerçek veriyle (239.182,23 TL) güncellemesi ve #12 ile #14 kartlarına kanıt yorumlarını eklemesi.
- [ ] **Test Koşumu:** DQ tarafından `tests/test-cases.md` senaryolarının gerçek veri üzerinde koşturularak `tests/test-log.md` dosyasının üretilmesi.
- [ ] **Sürüm Yayını:** Tüm blokajlar giderildikten ve düzeltme commit'leri tamamlandıktan sonra `gorev1-final` etiketinin (release) yayımlanması.
- [ ] **Çapraz İnceleme:** Yan Görev 3 kapsamında Grup Z reposunda `skills/pm-rapor/SKILL.md` için açılan geliştirme Issue'sunun takip edilmesi[cite: 3].