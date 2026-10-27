# RetailE – Yapay Zekâ Ajan Skill Envanteri (AGENTS.md)

Bu dosya, projede yer alan tüm rollerin yapay zekâ ajanları ile icra edeceği skill'lerin merkezi envanteridir.

---

## 1. Skill Listesi ve Envanter

| Rol | Görev Kodu | Sorumlu | Skill Yolu | İşlevi | Durum |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **BE** | G1-veri | Yaşar Coşkun | `skills/be-veri/SKILL.md` | Sabit tohumlu sentetik perakende satış verisi ve veri sözlüğü üretir. | Hazır |
| **DQ** | G1-analiz | Sena Çiftçi | `skills/dq-analiz/SKILL.md` | BE verisini okur; 5 temel metrik, 3 gözlem ve 1 eylem önerisi çıkarır. | Hazır |
| **FE** | G1-gorsel | Burak T. Demir | `skills/fe-gorsel/SKILL.md` | BE verisi ve DQ metrikleriyle zaman serisi ve kategori kırılım grafikleri çizer. | Hazır |
| **DQ** | G1-test | Sena Çiftçi | `skills/dq-test/SKILL.md` | Veri şeması ve kalite denetimi için 5 test senaryosu çalıştırır/doğrular. | Hazır |
| **PM** | Raporlama | Umut Kılıç | `skills/pm-rapor/SKILL.md` | Sprint gidişatını, devir zincirini ve haftalık ilerleme raporunu derler. | Aktif |

---

## 2. Skill Kullanım Rehberi
Ajan araçları ilgili görevi yürütürken yukarıdaki dizinlerde yer alan `SKILL.md` talimatlarını doğrudan okuyup uygular.