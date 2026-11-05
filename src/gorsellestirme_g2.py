"""G2 grafik seti: zaman serisi + kategori kirilimi + dagilim (histogram).

Not: G2 veri semasi (issue #25) ve G2 veri uretimi (issue #26) henuz
ertelenmis durumdadir. Bu betik, mevcut G1 verisini (data/perakende-satislari.csv)
kullanarak 3 grafiklik G2 setini uretir; G2 verisi hazir oldugunda girdi dosyasi
ve sutun adlari bu betikte guncellenecektir.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT_DIR / "data" / "perakende-satislari.csv"
VISUALS_DIR = ROOT_DIR / "visuals"


def veriyi_yukle():
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Veri dosyasi bulunamadi: {DATA_PATH}")

    df = pd.read_csv(DATA_PATH)

    gerekli = {"tarih", "kategori", "toplam_tutar"}
    eksik = gerekli - set(df.columns)
    if eksik:
        raise ValueError(f"Eksik sutunlar: {sorted(eksik)}")

    df["tarih"] = pd.to_datetime(df["tarih"], errors="coerce")
    df["toplam_tutar"] = pd.to_numeric(df["toplam_tutar"], errors="coerce")
    df = df.dropna(subset=["tarih", "kategori", "toplam_tutar"])

    if df.empty:
        raise ValueError("Gecerli satis verisi bulunamadi.")

    return df


def zaman_serisi_grafigi(df):
    aylik = df.set_index("tarih")["toplam_tutar"].resample("MS").sum()

    fig, ax = plt.subplots(figsize=(11, 6))
    ax.plot(aylik.index, aylik.values, marker="o", linewidth=2, color="#1f77b4")
    ax.set_title("G2 — Aylara Gore Toplam Satis Tutari", fontsize=15, pad=14)
    ax.set_xlabel("Aylar")
    ax.set_ylabel("Satis tutari (TL)")
    ax.yaxis.set_major_formatter(
        ticker.FuncFormatter(lambda x, _: f"{x:,.0f} TL")
    )
    ax.grid(True, linestyle="--", alpha=0.35)
    fig.autofmt_xdate()
    fig.tight_layout()

    hedef = VISUALS_DIR / "g2-zaman-serisi.png"
    fig.savefig(hedef, dpi=160, bbox_inches="tight")
    plt.close(fig)
    print(f"Olusturuldu: {hedef}")


def kategori_kirilimi_grafigi(df):
    kategori = df.groupby("kategori")["toplam_tutar"].sum().sort_values()
    toplam = kategori.sum()

    fig, ax = plt.subplots(figsize=(11, 6))
    cubuklar = ax.barh(kategori.index, kategori.values, color="#ff7f0e")
    ax.set_title("G2 — Kategorilere Gore Satis Dagilimi", fontsize=15, pad=14)
    ax.set_xlabel("Satis tutari (TL)")
    ax.set_ylabel("Urun kategorisi")
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
            fontsize=9,
        )

    ax.grid(axis="x", linestyle="--", alpha=0.35)
    ax.set_axisbelow(True)
    fig.tight_layout()

    hedef = VISUALS_DIR / "g2-kategori-kirilimi.png"
    fig.savefig(hedef, dpi=160, bbox_inches="tight")
    plt.close(fig)
    print(f"Olusturuldu: {hedef}")


def dagilim_grafigi(df):
    fig, ax = plt.subplots(figsize=(11, 6))
    ax.hist(df["toplam_tutar"], bins=20, color="#2ca02c",
            edgecolor="white", alpha=0.85)
    ax.set_title("G2 — Satis Tutari Dagilimi (Histogram)", fontsize=15, pad=14)
    ax.set_xlabel("Satis tutari (TL)")
    ax.set_ylabel("Kayit sayisi")
    ax.xaxis.set_major_formatter(
        ticker.FuncFormatter(lambda x, _: f"{x:,.0f} TL")
    )
    ax.grid(axis="y", linestyle="--", alpha=0.35)
    fig.tight_layout()

    hedef = VISUALS_DIR / "g2-dagilim.png"
    fig.savefig(hedef, dpi=160, bbox_inches="tight")
    plt.close(fig)
    print(f"Olusturuldu: {hedef}")


def main():
    VISUALS_DIR.mkdir(parents=True, exist_ok=True)
    df = veriyi_yukle()
    print(f"{len(df)} gecerli satis kaydi kullaniliyor.")
    zaman_serisi_grafigi(df)
    kategori_kirilimi_grafigi(df)
    dagilim_grafigi(df)
    print("Uc grafik de olusturuldu.")


if __name__ == "__main__":
    main()
