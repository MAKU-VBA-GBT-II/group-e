\# BE Veri Üretici Skill



\## Amaç



Bu skill, RetailE projesi için tekrarlanabilir sentetik perakende satış verisi üretmek amacıyla hazırlanmıştır.



\## Görev



Veri üretim ajanı aşağıdaki işlemleri gerçekleştirir:



1\. `src/veri\_uretici.py` betiğini çalıştırır.

2\. Sentetik perakende satış verilerini üretir.

3\. Üretilen verileri `data/perakende-satislari.csv` dosyasına kaydeder.

4\. Veri setinin gerekli koşulları sağladığını kontrol eder.

5\. Veri yapısının `docs/veri-sozlugu-g1.md` dosyasında açıklanan şema ile uyumlu olmasını sağlar.



\## Veri Üretim Kuralları



Üretilen veri seti:



\- En az 100 kayıt içermelidir.

\- En az 6 alan içermelidir.

\- Ana kategori alanında en az 4 farklı değer bulunmalıdır.

\- Sentetik veriler gerçek kişi veya gerçek satış bilgileri içermemelidir.

\- Veri üretimi tekrarlanabilir olmalıdır.

\- Sabit seed değeri kullanılmalıdır.



Bu projede sabit seed değeri `42` olarak belirlenmiştir.



\## Çıktı



Veri üretim betiğinin oluşturduğu dosya:



`data/perakende-satislari.csv`



Mevcut veri seti 150 satış kaydı, 8 alan ve 5 farklı ana kategori içermektedir.



\## Veri Sözlüğü



Veri setindeki alanların açıklamaları ve veri tipleri aşağıdaki dosyada bulunmaktadır:



`docs/veri-sozlugu-g1.md`



\## Çalıştırma



Veri üretim betiği proje ana klasöründen aşağıdaki komutla çalıştırılır:



`python src/veri\_uretici.py`



Betik başarılı şekilde çalıştığında `data/perakende-satislari.csv` dosyası yeniden oluşturulur.



`random.seed(42)` kullanıldığı için betik her çalıştırıldığında aynı sentetik veri seti üretilebilir.

