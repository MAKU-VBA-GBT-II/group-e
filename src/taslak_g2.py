"""G2 grafik seti icin dijital taslak (mockup) uretir.

Bu dosya kodlama oncesi tasarim referansi olarak uretilen bir mockup'tir;
gercek veriyle cizilmemistir, yalnızca panel yerlesimini ve basliklari
gosterir. Uretilen dosya: docs/g2-taslak.png
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

ROOT_DIR = Path(__file__).resolve().parent.parent
OUT_PATH = ROOT_DIR / "docs" / "g2-taslak.png"


def main():
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis("off")

    ax.text(6, 6.6, "G2 Grafik Seti — Dijital Taslak (Mockup)",
            ha="center", va="center", fontsize=16, fontweight="bold")
    ax.text(6, 6.2, "Kodlama oncesi tasarim referansi | G2-gorsel (issue #28)",
            ha="center", va="center", fontsize=10, color="#555555")

    paneller = [
        (0.5, 3.3, 3.5, 2.5, "1) Zaman Serisi\nAylara gore toplam satis (TL)\n[x: Aylar, y: Satis tutari (TL)]"),
        (4.25, 3.3, 3.5, 2.5, "2) Kategori Kirilimi\nKategorilere gore satis (TL)\n[yatay bar + % pay etiketi]"),
        (8.0, 3.3, 3.5, 2.5, "3) Dagilim (Histogram)\nSatis tutari dagilimi\n[x: Satis tutari (TL), y: Kayit sayisi]"),
    ]
    for x, y, w, h, label in paneller:
        rect = Rectangle((x, y), w, h, linewidth=1.5,
                         edgecolor="#333333", facecolor="#f2f2f2")
        ax.add_patch(rect)
        ax.text(x + w / 2, y + h / 2, label, ha="center", va="center",
                fontsize=9)

    ax.text(6, 2.6, "Veri kaynagi: data/perakende-satislari.csv (G1 verisi, G2 verisi hazir olunca guncellenecek)",
            ha="center", va="center", fontsize=9, color="#777777")
    ax.text(6, 2.2, "Cikti dosyalari: visuals/g2-zaman-serisi.png, g2-kategori-kirilimi.png, g2-dagilim.png",
            ha="center", va="center", fontsize=9, color="#777777")
    ax.text(6, 1.8, "Betik: src/gorsellestirme_g2.py  |  dpi=160  |  bbox_inches=tight",
            ha="center", va="center", fontsize=9, color="#777777")

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT_PATH, dpi=160, bbox_inches="tight")
    plt.close(fig)
    print(f"Olusturuldu: {OUT_PATH}")


if __name__ == "__main__":
    main()
