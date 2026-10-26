"""G1 perakende satış verisi için temel analizleri üretir.

Bu betik `data/perakende-satislari.csv` dosyasını okur; toplam satış,
ortalama sepet, kategori kırılımı ve haftalık satış tutarlarını hesaplayıp
terminal çıktısı olarak gösterir.
"""

import pandas as pd


def analiz_yap():
    """Perakende satış CSV dosyasını okuyup özet analiz sonuçlarını yazdırır.

    İşlem adımları:
    1. Satış verisini CSV dosyasından okur.
    2. Tarih alanını datetime tipine çevirip ISO hafta numarasını üretir.
    3. Toplam satış ve ortalama sepet tutarını hesaplar.
    4. Kategorilerin toplam satış içindeki yüzdesini hesaplar.
    5. Haftalara göre toplam satış tutarını hesaplar.
    6. Sonuçları okunabilir biçimde terminale yazdırır.
    """
    # Projenin ana satış veri dosyasını pandas DataFrame olarak oku.
    df = pd.read_csv("data/perakende-satislari.csv")

    # Tarih sütununu tarih tipine çevir ve haftalık analiz için ISO hafta numarası oluştur.
    df["tarih"] = pd.to_datetime(df["tarih"])
    df["hafta"] = df["tarih"].dt.isocalendar().week

    # Genel performans metrikleri: toplam satış tutarı ve işlem başına ortalama tutar.
    toplam_satis = df["toplam_tutar"].sum()
    ortalama_sepet = df["toplam_tutar"].mean()

    # Her kategorinin toplam satışını ve genel toplam içindeki yüzde payını hesapla.
    kategori_satis = df.groupby("kategori")["toplam_tutar"].sum()
    kategori_yuzde = (kategori_satis / toplam_satis) * 100
    kategori_yuzde = kategori_yuzde.sort_values(ascending=False)

    # Satış tutarlarını ISO hafta numarasına göre gruplayarak haftalık toplamları oluştur.
    haftalik_satis = df.groupby("hafta")["toplam_tutar"].sum()

    # Hesaplanan genel metrikleri terminalde iki ondalık basamakla göster.
    print(f"Toplam Satış: {toplam_satis:,.2f} TL")
    print(f"Ortalama Sepet: {ortalama_sepet:,.2f} TL\n")

    # Kategori paylarını büyükten küçüğe yüzde olarak yazdır.
    print("Kategori Kırılımı (%):")
    for kat, yuzde in kategori_yuzde.items():
        print(f"- {kat}: %{yuzde:.0f}")

    # Haftalık satış toplamlarını TL cinsinden yazdır.
    print("\nHaftalık Kırılım (Tutar):")
    for hafta, tutar in haftalik_satis.items():
        print(f"- {hafta}. Hafta: {tutar:,.2f} TL")


if __name__ == "__main__":
    # Dosya doğrudan çalıştırıldığında analiz fonksiyonunu başlat.
    analiz_yap()
