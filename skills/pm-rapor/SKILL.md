---
name: pm-rapor
description: Proje yöneticisinin haftalık ilerleme raporunu oluşturmasını, devir teslimleri denetlemesini ve ekip durumunu tutanağa geçirmesini sağlar.
---

# PM Raporlama Skill'i

## Amaç ve Kapsam
Bu skill, Proje Yöneticisi (PM) tarafından her sprint veya hafta sonunda `reports/report-wNN.md` (NN = iki basamaklı hafta numarası, örn: w03, w04) raporunu standart, tekrarlanabilir ve kanıta dayalı biçimde üretmek için kullanılır.

## Adım Adım Talimatlar

1. **İlerleme ve Issue Denetimi:**
   - İlgili haftanın sprint Issue kartlarını (#XX) incele.
   - Ekip üyelerinin kartlarındaki kabul kriterlerinin eksiksiz karşılandığını teyit et.

2. **Devir-Teslim Kontrolü:**
   - **BE → FE / DQ Devri:** BE üyesinin veri üretim kartında (#11) ve ilgili geliştirme kartında (#13) "Veri hazır" devir yorumunu, dosya yolunu ve geçerli commit hash'ini denetle.
   - **DQ → FE Devri:** DQ üyesinin analiz kartında (#12) veriyle uyumlu metrikleri ve commit hash'ini doğrula.
   - **FE Kanıtı:** FE üyesinin görselleştirme kartında (#13) üretilen grafik yollarını ve commit hash'ini doğrula.

3. **Engel ve Risklerin Tespiti:**
   - Hafta boyunca yaşanan teknik veya operasyonel blokajları (uyuşmayan veri, eksik devir yorumu, boş skill dosyası vb.) tespit et.

4. **Raporun Üretilmesi (`reports/report-wNN.md`):**
   - Aşağıdaki zorunlu şablon yapısına sadık kalarak raporu oluştur.
   - "Kim Ne Yaptı?" tablosundaki her satıra **mutlaka geçerli bir commit hash'i ve ilgili Issue numarası** yazılmalıdır.

### Rapor Şablonu

```markdown
# Haftalık İlerleme Raporu — Hafta NN

## 1. Planlanan Görevler
(Hafta başında yapılması hedeflenen ana başlıklar)

## 2. Yapılan İşler
(Hafta boyunca tamamlanan görevlerin somut özeti)

## 3. Kim Ne Yaptı?
| Rol | Sorumlu | Tamamlanan Görev | İlgili Issue | Commit Hash |
| :--- | :--- | :--- | :--- | :--- |
| PM | [Ad Soyad] | ... | #... | ... |
| BE | [Ad Soyad] | ... | #... | ... |
| DQ | [Ad Soyad] | ... | #... | ... |
| FE | [Ad Soyad] | ... | #... | ... |

## 4. Karşılaşılan Engeller ve Tıkanıklıklar (Blockers)
(Süreçte yaşanan somut blokajlar ve ekibin geliştirdiği çözümler)

## 5. Gelecek Hafta Planı
(Bir sonraki sprintte yapılacak adımlar)
```

## Kullanılan Dosyalar
- **Girdi:** Depodaki tüm Issue'lar, commit geçmişi, `docs/` ve `skills/` altındaki teslimler.
- **Çıktı:** `reports/report-wNN.md` (Örn: `reports/report-w03.md`)

## Çalıştırma
Bu skill PM rolü tarafından her hafta sonu sprint kapanışında işletilir ve üretilen rapor `reports/` klasörü altına commit edilir.

---

# PM Raporlama ve Koordinasyon Yeteneği (pm-rapor)

## Rol Tanımı
Grup E (RetailE) Proje Yöneticisi (PM) rolü için sprint ve görev kapanış raporlarını, dönem raporlarını ve GitHub teslim issue taslaklarını üreten yetenektir.

## Görev ve Sorumluluklar
1. Takım içi görev dağılımını ve rol devir zincirini koordine etmek (AGENTS.md).
2. PR'ları teknik gereksinimlere göre incelemek, gerektiğinde müdahale edip ana dala (main) birleştirmek.
3. Görev ve dönem sonlarında takım verilerini toplamak, KPI metriklerini derlemek ve şeffaf retrospektif raporları oluşturmak.

## Çıktı ve Rapor Format Kuralları
Raporlar Markdown (.md) formatında üretilir ve şu 7 zorunlu başlığı içerir:
1. Yönetici Özeti
2. Teslim Edilenler (kanıt linkleriyle)
3. Sayılarla Dönem (Süreç KPI'ları: Issue, PR, inceleme süreleri)
4. Tıkananlar ve Çözümler
5. Kim Ne Yaptı (Olgusal teslimat tablosu)
6. Dersler (Retrospektif)
7. Görev 3 Hazırlığı (Veri değişimi planı)

## Prompt Özeti
"pm-rapor kurallarına uygun olarak; takım içi PR kanıtlarını, rol katkılarını ve süreç KPI'larını içeren olgusal raporu üret."