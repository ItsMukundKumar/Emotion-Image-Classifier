import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras import layers, models

# -----------------------------
# Load Model (Rebuilt)
# -----------------------------
@st.cache_resource
def load_model():
    
    base_model = MobileNetV2(
        input_shape=(224, 224, 3),
        include_top=False,
        weights=None  # IMPORTANT: no downloading
    )

    x = base_model.output
    x = layers.GlobalAveragePooling2D()(x)
    x = layers.BatchNormalization()(x)
    x = layers.Dense(128, activation='relu')(x)
    x = layers.Dropout(0.5)(x)
    outputs = layers.Dense(7, activation='softmax')(x)

    model = models.Model(inputs=base_model.input, outputs=outputs)

    return model

model = load_model()

class_names = [
    "angry", "disgust", "fear",
    "happy", "neutral", "sad", "surprise"
]

# -----------------------------
# Image Preprocessing
# -----------------------------
def preprocess_image(image):
    image = image.resize((224, 224))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

# -----------------------------
# UI
# -----------------------------
st.title("Emotion Image Classifier")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    img = preprocess_image(image)

    preds = model.predict(img)
    pred_class = class_names[np.argmax(preds)]
    confidence = np.max(preds)

    st.write(f"Prediction: {pred_class}")
    st.write(f"Confidence: {confidence:.2f}")
