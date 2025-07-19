

# 🩺 Breast Cancer Prediction Web App

>A full-stack web application for predicting breast cancer using a machine learning model.

---

## 🚀 Live Demo

- **Frontend:** [https://breast-cancer-diagnosis-one.vercel.app/](https://breast-cancer-diagnosis-one.vercel.app/)
- **Backend API:** [https://cancer-backend-wlc9.onrender.com/predict](https://cancer-backend-wlc9.onrender.com/predict)

---

## 🛠️ Tech Stack

<p align-text="left">
  <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" alt="React"/>
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="scikit-learn"/>
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5"/>
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3"/>
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript"/>
</p>

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
