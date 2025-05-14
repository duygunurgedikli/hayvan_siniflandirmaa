# 🐾 Hayvan Görüntüleri Sınıflandırma (Transfer Learning)

Bu proje, **MobileNetV2** mimarisi kullanarak farklı hayvan türlerini sınıflandırmak için transfer learning yöntemini uygulamaktadır. Proje sonunda, eğitilmiş model ile görsel sınıflandırma yapılabilir ve kullanıcı dostu bir arayüz üzerinden test edilebilir.

## 📁 Proje Yapısı

proje_klasoru/
│
├── raw-img/ # Tüm ham görsellerin bulunduğu ana klasör 
├── transfer_model.keras # Eğitilmiş model 
├── app.py # Streamlit ile hazırlanmış görsel arayüz
├── README.md 
└── CNN.py # Model eğitimi ve analizleri 


---

## 🧠 Kullanılan Yöntemler

- 📦 **Veri Artırma (Image Augmentation)**
- 🔄 **Transfer Learning (MobileNetV2)**
- 📊 **Model Analizi: Confusion Matrix, Classification Report**
- 🖼️ **Streamlit ile Web Arayüzü**

---

## 🔧 Gereksinimler

Aşağıdaki Python kütüphanelerine ihtiyaç vardır:

```bash
pip install tensorflow matplotlib seaborn scikit-learn streamlit

## 🔧 Gereksinimler
Modeli eğittikten sonra, kullanıcı arayüzünü çalıştırmak için terminalde şu komutu yaz:

bash
Kopyala
Düzenle
streamlit run app.py
Not: transfer_model.keras ve app.py aynı klasörde olmalıdır. Komutu bu klasör içinde çalıştırmalısınız.