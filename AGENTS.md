# RetailE — Yapay Zekâ Ajan Skill Envanteri (AGENTS.md)

Bu dosya, projede yer alan tüm rollerin yapay zekâ ajanları (Codex, Claude Code vb.) ile icra edeceği skill'lerin merkezi envanteridir.

---

## 1. Skill Listesi ve Yol Haritası

| Rol | Görev Kodu | Skill Yolu | İşlevi | Durum |
| :--- | :--- | :--- | :--- | :--- |
| **BE** | G1-veri | `skills/be-veri/SKILL.md` | Sabit tohumlu sentetik perakende satış verisi ve veri sözlüğü üretir. | Hazırlanıyor |
| **DQ** | G1-analiz | `skills/dq-analiz/SKILL.md` | BE verisini okur; 5 temel metrik, 3 gözlem ve 1 eylem önerisi çıkarır. | Hazırlanıyor |
| **FE** | G1-gorsel | `skills/fe-gorsel/SKILL.md` | BE verisi ve DQ metrikleriyle zaman serisi ve kırılım grafikleri çizer. | Hazırlanıyor |
| **DQ** | G1-test | `skills/dq-test/SKILL.md` | Veri şeması ve kalite denetimi için 5 test senaryosu çalıştırır/doğrular. | Hazırlanıyor |
| **PM** | Raporlama | `skills/pm-rapor/SKILL.md` | Sprint gidişatını, devir zincirini ve haftalık ilerleme raporunu derler. | Aktif |

---

## 2. Skill Kullanım Rehberi

Ajan araçları ilgili görevi yürütürken yukarıdaki dizinlerde yer alan `SKILL.md` talimatlarını doğrudan okuyup uygular.