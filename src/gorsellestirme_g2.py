"""G2 grafik seti: Zaman Serisi, Kategori Kırılımı ve Mağaza Dağılımı.
Liderin (PM) talimatına uygun olarak mevcut dosya güncellenmiştir.
"""
from pathlib import Path
import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd

ROOT_DIR = Path(__file__).resolve().parent.parent
# Hata veren dosya yolu, klasöründeki mevcut dosya adına göre düzeltildi
DATA_PATH = ROOT_DIR / "data" / "perakende-satislari.csv"
VISUALS_DIR = ROOT_DIR / "visuals"


def veriyi_yukle():
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Veri dosyası bulunamadı: {DATA_PATH}")

    df = pd.read_csv(DATA_PATH)

    # G2 için 'magaza' sütunu zorunlu alanlara eklendi
    gerekli = {"tarih", "kategori", "magaza", "toplam_tutar"}
    eksik = gerekli - set(df.columns)
    if eksik:
        raise ValueError(f"Eksik sütunlar var: {sorted(eksik)}")

    df["tarih"] = pd.to_datetime(df["tarih"], errors="coerce")
    df["toplam_tutar"] = pd.to_numeric(df["toplam_tutar"], errors="coerce")
    df = df.dropna(subset=["tarih", "kategori", "magaza", "toplam_tutar"])

    if df.empty:
        raise ValueError("Geçerli G2 satış verisi bulunamadı.")

    return df


def zaman_serisi_grafigi(df):
    aylik = df.set_index("tarih")["toplam_tutar"].resample("MS").sum()

    fig, ax = plt.subplots(figsize=(11, 6))
    ax.plot(aylik.index, aylik.values, marker="o", linewidth=2, color="#1f77b4")
    ax.set_title("G2 — Aylara Göre Toplam Satış Tutarı", fontsize=15, pad=14, fontweight="bold")
    ax.set_xlabel("Aylar")
    ax.set_ylabel("Satış tutarı (TL)")
    ax.yaxis.set_major_formatter(
        ticker.FuncFormatter(lambda x, _: f"{x:,.0f} TL")
    )
    ax.grid(True, linestyle="--", alpha=0.35)
    fig.autofmt_xdate()
    fig.tight_layout()

    hedef = VISUALS_DIR / "g2-zaman-serisi.png"
    fig.savefig(hedef, dpi=160, bbox_inches="tight")
    plt.close(fig)
    print(f"Oluşturuldu: {hedef}")


def kategori_kirilimi_grafigi(df):
    kategori = df.groupby("kategori")["toplam_tutar"].sum().sort_values()
    toplam = kategori.sum()

    fig, ax = plt.subplots(figsize=(11, 6))
    cubuklar = ax.barh(kategori.index, kategori.values, color="#ff7f0e")
    ax.set_title("G2 — Kategorilere Göre Satış Dağılımı", fontsize=15, pad=14, fontweight="bold")
    ax.set_xlabel("Satış tutarı (TL)")
    ax.set_ylabel("Ürün kategorisi")
    ax.xaxis.set_major_formatter(
        ticker.FuncFormatter(lambda x, _: f"{x:,.0f} TL")
    )

    for cubuk, tutar in zip(cubuklar, kategori.values):
        pay = tutar / toplam * 100 if toplam else 0
        ax.annotate(
            f"{tutar:,.0f} TL (%{pay:.1f})",
            (cubuk.get_width(), cubuk.get_y() + cubuk.get_height() / 2),
            xytext=(5, 0),
            textcoords="offset points",
            va="center",
            fontsize=9
        )

    ax.grid(axis="x", linestyle="--", alpha=0.35)
    ax.set_axisbelow(True)
    fig.tight_layout()

    hedef = VISUALS_DIR / "g2-kategori-kirilimi.png"
    fig.savefig(hedef, dpi=160, bbox_inches="tight")
    plt.close(fig)
    print(f"Oluşturuldu: {hedef}")


def magaza_dagilimi_grafigi(df):
    magaza = df.groupby("magaza")["toplam_tutar"].sum().sort_values()
    toplam = magaza.sum()

    fig, ax = plt.subplots(figsize=(11, 6))
    cubuklar = ax.barh(magaza.index, magaza.values, color="#2ca02c")
    ax.set_title("G2 — Mağazalara Göre Satış Performansı", fontsize=15, pad=14, fontweight="bold")
    ax.set_xlabel("Satış tutarı (TL)")
    ax.set_ylabel("Mağazalar")
    ax.xaxis.set_major_formatter(
        ticker.FuncFormatter(lambda x, _: f"{x:,.0f} TL")
    )

    for cubuk, tutar in zip(cubuklar, magaza.values):
        pay = tutar / toplam * 100 if toplam else 0
        ax.annotate(
            f"{tutar:,.0f} TL (%{pay:.1f})",
            (cubuk.get_width(), cubuk.get_y() + cubuk.get_height() / 2),
            xytext=(5, 0),
            textcoords="offset points",
            va="center",
            fontsize=9
        )

    ax.grid(axis="x", linestyle="--", alpha=0.35)
    ax.set_axisbelow(True)
    fig.tight_layout()

    hedef = VISUALS_DIR / "g2-magaza-dagilimi.png"
    fig.savefig(hedef, dpi=160, bbox_inches="tight")
    plt.close(fig)
    print(f"Oluşturuldu: {hedef}")


def main():
    VISUALS_DIR.mkdir(parents=True, exist_ok=True)
    try:
        df = veriyi_yukle()
        print(f"{len(df)} geçerli satış kaydı kullanılıyor.")
        zaman_serisi_grafigi(df)
        kategori_kirilimi_grafigi(df)
        magaza_dagilimi_grafigi(df)
        print("Üç Görev 2 grafiği de başarıyla oluşturuldu.")
    except Exception as e:
        print(f"Hata: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()