# 🌱 Crop Disease Identification on Mobile

A lightweight deep learning system that helps farmers identify crop leaf diseases using a smartphone camera. The model analyzes leaf images and predicts diseases such as leaf spots, blight, and discoloration patterns. It is optimized to run on mobile devices and works even with limited internet connectivity.

---

## 📌 Features

- Detect crop diseases from leaf images
- Lightweight CNN model for mobile devices
- Fast predictions without cloud processing
- Works in rural areas with limited internet
- Displays prediction confidence

---

## 🧠 Model Approach

The system uses a **Convolutional Neural Network (CNN)** to classify leaf diseases.

Main components:
- **Convolution Layers** – extract features like spots and discoloration  
- **ReLU Activation** – adds non-linearity  
- **Pooling Layers** – reduce image dimensions and computation  
- **Fully Connected Layer** – predicts the disease class

---

## ⚙️ Mobile Optimization

To run efficiently on smartphones, the model uses:

- Lightweight architectures (MobileNet / EfficientNet-Lite)
- Model quantization
- Parameter reduction
- Pruning

These techniques reduce memory usage and improve prediction speed.

---

## 🛠 Technologies Used

- Python  
- TensorFlow / Keras  
- NumPy  
- Matplotlib  
- CNN (Deep Learning)

---

## ▶️ Usage

Clone the repository:

```bash
git clone https://github.com/prem-sah
```

Install dependencies:

pip install tensorflow numpy matplotlib


Run prediction:

python predict.py

Prem Kumar Sah
