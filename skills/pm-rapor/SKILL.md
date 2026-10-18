# PM Sprint Raporlama Skill'i (pm-rapor)

## Ne İşe Yarar?
RetailE projesinde haftalık sprint ilerlemesini, ekip rollerinin (BE, DQ, FE) devir teslim zincirini ve GitHub üzerindeki durumları denetleyerek haftalık ilerleme raporunu (`reports/report-wXX.md`) standart formatta üretir.

## Adım Adım Talimatlar
1. **GitHub Durum Denetimi:** `RetailE-Grup E Panosu` üzerindeki kartların sütunlarını (Todo, In Progress, Done) ve Issue numaralarını kontrol et.
2. **Devir Teslim Zinciri Kontrolü:** 
   - BE'nin veri teslim yorumunu (`G1-analiz` ve `G1-gorsel` issue'larında),
   - FE'nin taslak çizim yorumunu (`G1-gorsel` issue'sında),
   - DQ'nun analiz devir yorumunu denetle.
3. **Metrik ve Çıktı Doğrulama:** `data/`, `docs/`, `visuals/`, `tests/` ve `skills/` dizinlerindeki zorunlu dosyaların varlığını doğrula.
4. **Rapor Derleme:** `reports/report-w03.md` şablonuna; planlanan işleri, tamamlanan adımları, devir teslim kanıtlarını (yorum/commit linkleri) ve olası blokajları/tıkanıklıkları yaz.

## Kullandığı Dosyalar
- Girdi: `AGENTS.md`, GitHub Issues & Projects, ilgili hafta klasörleri (`data/`, `docs/`, `visuals/`, `tests/`)
- Çıktı: `reports/report-w03.md`

## Nasıl Çalıştırılır?
Ajan aracına (Claude Code / Codex / Gemini CLI) şu komut/istem verilir:
> "pm-rapor skill'ini kullanarak mevcut GitHub panosu ve repo commit durumuna göre reports/report-w03.md sprint raporunu güncelle."