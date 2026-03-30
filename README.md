<h1 align="center">🧠 Emotion Image Classifier</h1>

<p align="center">
A Deep Learning powered web app that predicts human emotions from images using Transfer Learning.
</p>

---

<h2>🚀 Live Demo</h2>
<p>
🔗 <i>Add your deployed Streamlit link here</i>
</p>

---

<h2>📌 Project Overview</h2>

<p>
This project leverages a pretrained <b>MobileNetV2</b> model and applies <b>fine-tuning</b> to classify images into 7 emotion categories.
It is deployed using <b>Streamlit</b>, allowing real-time predictions through a clean UI.
</p>

---

<h2>🎯 Emotion Classes</h2>

<ul>
  <li>😠 Angry</li>
  <li>🤢 Disgust</li>
  <li>😨 Fear</li>
  <li>😄 Happy</li>
  <li>😐 Neutral</li>
  <li>😢 Sad</li>
  <li>😲 Surprise</li>
</ul>

---

<h2>🧠 Model Details</h2>

<table>
<tr><td><b>Base Model</b></td><td>MobileNetV2 (ImageNet)</td></tr>
<tr><td><b>Technique</b></td><td>Transfer Learning + Fine-Tuning</td></tr>
<tr><td><b>Input Size</b></td><td>224 × 224</td></tr>
<tr><td><b>Classes</b></td><td>7</td></tr>
<tr><td><b>Test Accuracy</b></td><td>~50%</td></tr>
</table>

---

<h2>⚙️ Tech Stack</h2>

<p>
Python • TensorFlow • Keras • Streamlit • NumPy • Pillow
</p>

---

<h2>📂 Project Structure</h2>

<pre>
project/
│── app.py
│── model.keras
│── requirements.txt
│── README.md
</pre>

---

<h2>▶️ Run Locally</h2>

<ol>
<li><b>Clone repository</b></li>

<pre>git clone https://github.com/ItsMukundKumar/Emotion-Image-Classifier.git
cd emotion-classifier</pre>

<li><b>Install dependencies</b></li>

<pre>pip install -r requirements.txt</pre>

<li><b>Run app</b></li>

<pre>streamlit run app.py</pre>
</ol>

---

<h2>✨ Features</h2>

<ul>
  <li>📤 Upload image for prediction</li>
  <li>⚡ Real-time emotion classification</li>
  <li>📊 Confidence score display</li>
  <li>🎨 Clean and modern UI</li>
  <li>🚀 Lightweight and fast inference</li>
</ul>

---

<h2>⚠️ Disclaimer</h2>

<p style="color:gray;">
This model has limited accuracy (~50%) and is intended for <b>educational and demonstration purposes only</b>.
Predictions may not be reliable for real-world applications.
</p>

---

<h2>📈 Future Improvements</h2>

<ul>
  <li>Improve dataset quality and size</li>
  <li>Increase accuracy (target: 70%+)</li>
  <li>Add real-time camera input</li>
  <li>Face detection before prediction</li>
  <li>Cloud deployment (Streamlit / AWS / GCP)</li>
</ul>

---

<h2>🤝 Contributing</h2>

<p>
Feel free to fork this repository and enhance the model or UI.
</p>

---

<h2>📬 Contact</h2>

<p>
🔗 https://www.linkedin.com/in/mukund-kumar-shah/<br>
💻 https://github.com/ItsMukundKumar
</p>

---

<p align="center">
⭐ If you like this project, consider giving it a star!
</p>
