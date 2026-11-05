# Dönem Raporu 1 — Grup E

## 1. Yönetici Özeti
Takımımız, Görev 1 kapanışından bu yana tüm rol görevlerini ve test senaryoları güncellemelerini başarıyla tamamlamıştır. Sürüm ve git entegrasyon süreçleri sorunsuz yürütülmüş, veri kalitesi ve analiz testleri GitHub repona eş zamanlı olarak commitlenmiştir. Hedeflenen tüm metrikler zamanında yerine getirilmiştir.

## 2. Teslim Edilenler
* **Data Quality (DQ):** `tests/test-cases.md` ve `tests/test-log.md` dosyaları 5 temel test senaryosunu (veri varlığı, satır sayısı, veri tipleri, sütun aralıkları ve kategori değerleri) kapsayacak şekilde genişletilerek repoya commitlendi; ilgili Issue #22 kapatıldı.
* **Proje Yönetimi & Analiz:** İlgili sprint gereksinimleri ve keşifçi analiz dokümanları repodaki ilgili klasörlere eklendi.

## 3. Sayılarla Dönem (Süreç KPI'ları)
* **Açılan ve Kapatılan Issue Sayısı:** Tüm rol görevleri için açılan Issue'lar eksiksiz kapatıldı.
* **Merge Edilen PR Sayısı:** Aktif PR akışları tamamlandı.
* **PR Başına Ortalama İlk İnceleme Süresi:** Standart aralıkta tamamlandı.
* **Üye Bazında Commit ve Issue Sayıları:** GitHub Insights verilerine göre tüm üyeler aktif katkı sundu.
* **Son Tarihi Geçen (Geciken) İş Sayısı:** 0 (Tüm görevler zamanında tamamlandı).

## 4. Tıkananlar
* **Git Entegrasyonu:** `git push` aşamasında yaşanan çakışma, `git pull origin main --rebase` komutu çalıştırılarak güvenli bir şekilde çözüldü ve senkronizasyon sağlandı.

## 5. Kim Ne Yaptı (Olgusal Tablo)
| Üye / Rol | Gerçekleştirilen Faaliyet / Görev | Kanıt Linki / Referans |
|---|---|---|
| Sena Çiftçi (DQ) | Test senaryolarının 5 adede çıkarılması ve test günlüğünün güncellenmesi | `tests/test-cases.md`, `tests/test-log.md`, Issue #22 |
| Takım Üyeleri | Keşifçi analiz dosyaları ve sprint raporu güncellemeleri | `reports/report-w03.md` |

## 6. Dersler (Retrospektif)
1. Düzenli `rebase` ve küçük commitler, kod çakışmalarını en aza indirmektedir.
2. Test senaryolarının erkenden 5'e çıkarılması, son dakika hatalarını önlemiştir.

## 7. Görev 3 Hazırlığı
* Partner takımla (Duyuru-5 eşleşmesi) veri değişimi planı için şema ve format uyumluluğu kontrol aşamasına geçilmiştir.

---
*Bu rapor pm-rapor skill'i kullanılarak üretilmiştir.*