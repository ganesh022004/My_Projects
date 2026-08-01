import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load model
model = tf.keras.models.load_model("mask_model.h5")

st.set_page_config(page_title="Face Mask Detector", page_icon="😷")
st.title("😷 Face Mask Detection using CNN")
st.write("Upload a face image to check if person is wearing a mask or not")

# Upload
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Preprocess
    img = image.resize((224, 224))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    # Predict
    with st.spinner("Analyzing..."):
        prediction = model.predict(img)
    
    score = prediction[0][0]

    if score < 0.5:
        st.success("✅ With Mask — Stay Safe!")
    else:
        st.error("❌ Without Mask — Please wear a mask!")

    st.write(f"Confidence Score: `{score:.4f}`")