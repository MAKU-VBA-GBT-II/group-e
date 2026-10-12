# Git Keşfi: XGBoost

## Repo Adı ve Bağlantısı
- **XGBoost (Extreme Gradient Boosting):** https://github.com/dmlc/xgboost

## Çözdüğü Problem
Büyük ölçekli ve yapılandırılmış tablosal veri setleri üzerinde yüksek doğruluklu tahminleme modelleri kurarken karşılaşılan işlem hızı ve bellek optimizasyonu sorunlarını çözer. Dağıtık ve paralel hesaplama altyapısı sayesinde karmaşık gradyan artırma (gradient boosting) algoritmalarını geleneksel makine öğrenmesi kütüphanelerine kıyasla çok daha hızlı eğitir.

## Güçlü Yanları
- **Yüksek Hız ve Donanım Optimizasyonu:** Paralel ağaç oluşturma mimarisi ve yerel GPU desteği sayesinde büyük veri kümelerinde minimum sürede sonuç üretir.
- **Dahili Aşırı Öğrenme Kontrolü:** Modelin ezberlemesini (overfitting) engelleyen L1 (Lasso) ve L2 (Ridge) regülarizasyon parametrelerini yerleşik olarak sunar.
- **Eksik Veri Toleransı:** Veri setinde yer alan boş veya eksik değerleri (missing values) fazladan bir ön işleme gerek kalmadan ağaç dallanma sürecinde kendiliğinden yönetir.

## Kendi Projemizde Kullanabileceğimiz Bir Fikir
- **RetailE Müşteri Kaybı (Churn) ve Talep Tahmini:** Perakende simülasyonumuzdaki geçmiş mağaza satış ve müşteri verilerini kullanarak, hangi müşterilerin alışverişi bırakabileceğini veya hangi ürün grubunda talep artışı olacağını XGBoost modeliyle yüksek doğrulukla tahmin edebiliriz.