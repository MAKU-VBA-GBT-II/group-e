import pandas as pd

def analiz_yap():
    # CSV dosyasını oku
    df = pd.read_csv('data/perakende-satislari.csv')
    
    # Tarihi datetime formatına çevir ve haftayı bul
    df['tarih'] = pd.to_datetime(df['tarih'])
    df['hafta'] = df['tarih'].dt.isocalendar().week
    
    toplam_satis = df['toplam_tutar'].sum()
    ortalama_sepet = df['toplam_tutar'].mean()
    
    kategori_satis = df.groupby('kategori')['toplam_tutar'].sum()
    kategori_yuzde = (kategori_satis / toplam_satis) * 100
    kategori_yuzde = kategori_yuzde.sort_values(ascending=False)
    
    haftalik_satis = df.groupby('hafta')['toplam_tutar'].sum()
    
    print(f"Toplam Satış: {toplam_satis:,.2f} TL")
    print(f"Ortalama Sepet: {ortalama_sepet:,.2f} TL\n")
    print("Kategori Kırılımı (%):")
    for kat, yuzde in kategori_yuzde.items():
        print(f"- {kat}: %{yuzde:.0f}")
        
    print("\nHaftalık Kırılım (Tutar):")
    for hafta, tutar in haftalik_satis.items():
        print(f"- {hafta}. Hafta: {tutar:,.2f} TL")

if __name__ == "__main__":
    analiz_yap()