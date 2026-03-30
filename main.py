import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# ---------------------------
# CONFIG
# ---------------------------
IMG_SIZE = (224, 224)

# Load model
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("model.keras", compile=False)
    return model

model = load_model()

class_names = [
    "angry", "disgust", "fear",
    "happy", "neutral", "sad", "surprise"
]

# ---------------------------
# CUSTOM CSS (HTML Styling)
# ---------------------------
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: #4A90E2;
    }
    .sub-text {
        text-align: center;
        color: gray;
        margin-bottom: 20px;
    }
    .prediction-box {
        padding: 20px;
        border-radius: 15px;
        background-color: #f0f2f6;
        text-align: center;
        margin-top: 20px;
    }
    .emotion {
        font-size: 28px;
        font-weight: bold;
        color: #333;
    }
    .confidence {
        font-size: 20px;
        color: #666;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------
# UI
# ---------------------------
st.markdown('<div class="main-title">🧠 Emotion Classifier</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Upload an image and click predict</div>', unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

# ---------------------------
# PREPROCESS
# ---------------------------
def preprocess_image(image):
    image = image.resize(IMG_SIZE)
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

# ---------------------------
# DISPLAY IMAGE
# ---------------------------
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Predict Button
    if st.button("🔍 Predict"):
        img_array = preprocess_image(image)

        prediction = model.predict(img_array)
        predicted_class = class_names[np.argmax(prediction)]
        confidence = np.max(prediction)

        # ---------------------------
        # OUTPUT (Styled)
        # ---------------------------
        st.markdown(f"""
            <div class="prediction-box">
                <div class="emotion">Emotion: {predicted_class}</div>
                <div class="confidence">Confidence: {confidence*100:.2f}%</div>
            </div>
        """, unsafe_allow_html=True)

        # Progress bar
        st.progress(float(confidence))

        # ---------------------------
        # All probabilities
        # ---------------------------
        st.subheader("Class Probabilities")

        for i, prob in enumerate(prediction[0]):
            st.write(f"{class_names[i]}: {prob*100:.2f}%")

# ---------------------------
# DISCLAIMER
# ---------------------------
st.markdown("---")

st.markdown("""
<div style="
    text-align:center; 
    font-size:14px; 
    color:#888; 
    padding:10px;
">
⚠️ <b>Note:</b> This model has limited accuracy (~50%) and is intended for educational and demonstration purposes only. 
Results may not be reliable for real-world applications.
</div>
""", unsafe_allow_html=True)
