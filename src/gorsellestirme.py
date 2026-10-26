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
        raise FileNotFoundError(f"Veri dosyası bulunamadı: {DATA_PATH}")

    df = pd.read_csv(DATA_PATH)

    gerekli = {"tarih", "kategori", "toplam_tutar"}
    eksik = gerekli - set(df.columns)
    if eksik:
        raise ValueError(f"Eksik sütunlar: {sorted(eksik)}")

    df["tarih"] = pd.to_datetime(df["tarih"], errors="coerce")
    df["toplam_tutar"] = pd.to_numeric(df["toplam_tutar"], errors="coerce")
    df = df.dropna(subset=["tarih", "kategori", "toplam_tutar"])

    if df.empty:
        raise ValueError("Geçerli satış verisi bulunamadı.")

    return df


def zaman_serisi_grafigi(df):
    aylik = df.set_index("tarih")["toplam_tutar"].resample("MS").sum()

    fig, ax = plt.subplots(figsize=(11, 6))
    ax.plot(aylik.index, aylik.values, marker="o", linewidth=2)
    ax.set_title("Aylara Göre Toplam Satış Tutarı", fontsize=15, pad=14)
    ax.set_xlabel("Aylar")
    ax.set_ylabel("Satış tutarı (TL)")
    ax.yaxis.set_major_formatter(
        ticker.FuncFormatter(lambda x, _: f"{x:,.0f} TL")
    )
    ax.grid(True, linestyle="--", alpha=0.35)
    fig.autofmt_xdate()
    fig.tight_layout()

    hedef = VISUALS_DIR / "zaman-serisi.png"
    fig.savefig(hedef, dpi=160, bbox_inches="tight")
    plt.close(fig)
    print(f"Oluşturuldu: {hedef}")


def kategori_kirilimi_grafigi(df):
    kategori = df.groupby("kategori")["toplam_tutar"].sum().sort_values()
    toplam = kategori.sum()

    fig, ax = plt.subplots(figsize=(11, 6))
    cubuklar = ax.barh(kategori.index, kategori.values)
    ax.set_title("Kategorilere Göre Satış Dağılımı", fontsize=15, pad=14)
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

    hedef = VISUALS_DIR / "kategori-kirilimi.png"
    fig.savefig(hedef, dpi=160, bbox_inches="tight")
    plt.close(fig)
    print(f"Oluşturuldu: {hedef}")


def main():
    VISUALS_DIR.mkdir(parents=True, exist_ok=True)
    df = veriyi_yukle()
    print(f"{len(df)} geçerli satış kaydı kullanılıyor.")
    zaman_serisi_grafigi(df)
    kategori_kirilimi_grafigi(df)
    print("İki grafik de oluşturuldu.")


if __name__ == "__main__":
    main()
