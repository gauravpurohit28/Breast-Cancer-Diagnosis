

# 🩺 Breast Cancer Prediction Web App

>A full-stack web application for predicting breast cancer using a machine learning model.

---

## 🚀 Live Demo

- **Frontend:** [https://breast-cancer-diagnosis-one.vercel.app/](https://breast-cancer-diagnosis-one.vercel.app/)
- **Backend API:** [https://cancer-backend-wlc9.onrender.com/predict](https://cancer-backend-wlc9.onrender.com/predict)

---

## 🛠️ Tech Stack

<p align="left">
  <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" alt="React"/>
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white" alt="TensorFlow"/>
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="scikit-learn"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"/>
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy"/>
  <img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white" alt="Matplotlib"/>
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5"/>
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3"/>
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript"/>
</p>
---

## 🧑‍💻 Model Training & Colab Code

The model training process is performed in a Jupyter/Colab notebook using Python. Here’s what happens:

- **Data Preprocessing:**
  - The breast cancer dataset is loaded using Pandas and NumPy for data manipulation and analysis.
  - Data cleaning, normalization, and feature selection are performed.
- **Model Training:**
  - A Logistic Regression model is trained using scikit-learn to classify tumors as malignant or benign.
  - Model performance is evaluated using metrics like accuracy, precision, recall, and confusion matrix.
  - Visualizations are created using Matplotlib to better understand the data and results.
- **TensorFlow (optional):**
  - TensorFlow can be used for experimenting with deep learning models for comparison.
- **Model Export:**
  - The trained model is saved as a `.pkl` file and used by the Flask backend for real-time predictions.

**Logistic Regression** is chosen for its effectiveness in binary classification tasks like cancer detection, providing interpretable results and strong baseline performance.

---

---

## ✨ Features

- User-friendly web interface for submitting diagnostic data
- Machine learning model (scikit-learn) for breast cancer prediction
- REST API for communication between frontend and backend
- Easy-to-use form for entering patient data

---

## 📁 Project Structure

```text
Breast-Cancer/
├── backend/
│   ├── app.py              # Flask API server
│   ├── model.pkl           # Trained ML model
│   ├── requirements.txt    # Python dependencies
│   └── train_model.py      # Model training script
├── frontend/
│   ├── package.json        # React project config
│   ├── public/             # Static assets
│   └── src/                # React source code
│       ├── App.js
│       ├── Diagnosisform.js
│       ├── index.css
│       └── index.js
```

---

## 🏁 Getting Started

### Backend Setup
```sh
cd backend
pip install -r requirements.txt
python app.py
```

### Frontend Setup
```sh
cd frontend
npm install
npm start
```

---

## 🌐 Usage

1. Open the [frontend app](https://breast-cancer-diagnosis-one.vercel.app/) in your browser.
2. Fill in the diagnostic form and submit to get a prediction.

---

## 📡 API Endpoint

Send a POST request to:

```
https://cancer-backend-wlc9.onrender.com/predict
```

---

## 📜 License

This project is for educational purposes.
