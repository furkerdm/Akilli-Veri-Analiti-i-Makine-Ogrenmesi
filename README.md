# Proje 3: Akıllı Veri Analitiği ve Makine Öğrenmesi Uygulaması

Bu proje, bulut bilişim altyapıları kullanılarak geliştirilmiş tam kapsamlı (end-to-end) bir makine öğrenmesi uygulamasıdır. Proje kapsamında trafik verileri uzak bir MongoDB veritabanından çekilmiş, makine öğrenmesi algoritmalarıyla modellenmiş ve **AWS Lambda** kullanılarak serverless (sunucusuz) bir mimari ile dağıtımı gerçekleştirilmiştir.

## 🚀 Mimari ve Teknolojiler

* **Veri Kaynağı:** MongoDB Atlas (NoSQL)
* **Makine Öğrenmesi:** Python, Scikit-learn (Random Forest Regressor)
* **Model Serileştirme:** Joblib
* **Bulut Depolama:** Amazon S3
* **Sunucusuz İşlem (Serverless):** AWS Lambda
* **Kütüphane Optimizasyonu:** AWS Lambda boyut sınırlarına uygun `manylinux` uyumlu özel katman (layer) mimarisi.

## 🧠 Çalışma Mantığı

1. `train_model.py` betiği, MongoDB'deki kaza verilerini çeker ve veriyi Pandas ile ön işlemeye sokar (tarih ayrıştırması vb.).
2. Ön işlenen verilerle bir **Random Forest** modeli eğitilir ve model `model.joblib` adıyla diske kaydedilir.
3. Eğitilen model Amazon S3 kovasına yüklenir.
4. AWS Lambda üzerinde çalışan `lambda_function.py`, gelen API istekleri doğrultusunda modeli S3'ten anlık olarak indirir, hafızaya alır ve istemciye milisaniyeler içinde trafik yoğunluğu tahmini döndürür.

## 🛠️ Kurulum ve Kullanım (Yerel Ortam)

Projeyi yerel ortamınızda test etmek için:

1. Depoyu klonlayın:
   ```bash
   git clone [https://github.com/KULLANICI_ADINIZ/proje3-veri-analitigi.git](https://github.com/KULLANICI_ADINIZ/proje3-veri-analitigi.git)
