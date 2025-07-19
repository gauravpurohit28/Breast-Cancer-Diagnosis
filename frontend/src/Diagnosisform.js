import React, { useState } from "react";
import axios from "axios";
import './index.css'; 

const DiagnosisForm = () => {
      const [formData, setFormData] = useState({
      radius_mean: "",
      texture_mean: "",
      smoothness_mean: "",
      compactness_mean: "",
      symmetry_mean: "",
      radius_se: "",
      smoothness_se: "",
      compactness_se: "",
      radius_worst: "",
      texture_worst: ""
    });

  const [prediction, setPrediction] = useState(null);
  const [error, setError] = useState(null);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const features = Object.values(formData).map(parseFloat);

    try {
      const res = await axios.post("https://cancer-backend-wlc9.onrender.com/predict", { features });
      setPrediction(res.data.prediction === 1 ? "Malignant" : "Benign");
      setError(null);
    } catch (err) {
      console.error(err);
      setError("Prediction failed. Please try again.");
      setPrediction(null);
    }
  };

  return (
    <div className="page-wrapper">
      <div className="container">
        <h2>Breast Cancer Diagnosis</h2>
        <form onSubmit={handleSubmit}>
          {Object.keys(formData).map((key) => (
            <div key={key}>
              <label>{key.replaceAll("_", " ")}</label>
              <input
                type="number"
                step="any"
                name={key}
                value={formData[key]}
                onChange={handleChange}
                required
              />
            </div>
          ))}
          <button type="submit">Predict</button>
        </form>

        {prediction && (
          <p className="result success">
            <strong>Prediction:</strong> {prediction}
          </p>
        )}
        {error && (
          <p className="result error">
            <strong>Error:</strong> {error}
          </p>
        )}
      </div>
    </div>
  );
};

export default DiagnosisForm;
