
import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

# Modeli yükle
model = tf.keras.models.load_model("transfer_model.keras")

# İngilizce sınıf isimleri
class_names = ['butterfly', 'cat', 'chicken', 'cow', 'dog', 'elephant', 'horse', 'sheep', 'spider', 'squirrel']

# Türkçeye çeviri
translate = {
    "butterfly": "Farfalla",
    "cat": "Gatto",
    "chicken": "Gallina",
    "cow": "Mucca",
    "dog": "Cane",
    "elephant": "Elefante",
    "horse": "Cavallo",
    "sheep": "Pecora",
    "spider": "Ragno",
    "squirrel": "Scoiattolo"
}

# Sayfa yapılandırması
st.set_page_config(
    page_title="Hayvan Görseli Sınıflandırıcı",
    page_icon="🦋",
    layout="centered",
)

# Başlık
st.markdown(
    "<h1 style='text-align: center; color: #4CAF50;'>🧠 Hayvan Görseli Sınıflandırıcı</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center;'>Bir hayvan görseli yükleyin ve hangi tür olduğunu tahmin edelim!</p>",
    unsafe_allow_html=True
)

# Dosya yükleyici
uploaded_file = st.file_uploader("📁 Görsel Yükleyin", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="Yüklenen Görsel", use_column_width=True)

    # Görseli işleme
    img = img.convert("RGB")
    img = img.resize((128, 128))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Tahmin
    if st.button("🔍 Tahmin Et"):
        with st.spinner("Model tahmin yapıyor..."):
            prediction = model.predict(img_array)
            predicted_class = np.argmax(prediction)
            predicted_class_name = class_names[predicted_class]
            translated_class = translate[predicted_class_name]

        st.success("✅ Tahmin Başarılı!")
        st.markdown(
            f"<h3 style='text-align: center;'>🔎 Tahmin Edilen Sınıf:</h3><h2 style='text-align: center; color: #2196F3;'>{translated_class} ({predicted_class_name})</h2>",
            unsafe_allow_html=True
        )

