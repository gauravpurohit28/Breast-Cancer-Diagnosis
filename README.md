
# Breast Cancer Prediction Web App

This project is a full-stack web application for predicting breast cancer using a machine learning model. It consists of a Python Flask backend for model inference and training, and a React frontend for user interaction.

## Features
- User-friendly web interface for submitting diagnostic data
- Machine learning model (scikit-learn) for breast cancer prediction
- REST API for communication between frontend and backend
- Easy-to-use form for entering patient data

## Project Structure

```
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

## Getting Started

### Backend Setup
1. Navigate to the `backend` directory:
   ```sh
   cd backend
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the Flask server:
   ```sh
   python app.py
   ```

### Frontend Setup
1. Navigate to the `frontend` directory:
   ```sh
   cd frontend
   ```
2. Install dependencies:
   ```sh
   npm install
   ```
3. Start the React development server:
   ```sh
   npm start
   ```

The frontend will typically run on [http://localhost:3000](http://localhost:3000) and the backend on [http://localhost:5000](http://localhost:5000).

## Usage
- Open the frontend in your browser.
- Fill in the diagnostic form and submit to get a prediction.

## License
This project is for educational purposes.
