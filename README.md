🌾 Crop Yield Prediction System
A machine learning web application that predicts agricultural crop yield based on soil, weather, and farming inputs. Built with a Scikit-learn pipeline backend and a Flask REST API.

📌 Project Structure


crop-yield-prediction/
├── train_model.py                          # Model training script
├── app.py                                  # Flask prediction API
├── crop_yield.csv                          # Training dataset
└── crop_yield_prediction_model_pipeline.pkl  # Saved model pipeline

🧠 Model Overview

Detail                                   Value
Algorithm                            Linear Regression
Categorical Encoding                OneHotEncoder (handle_unknown="ignore")
Pipeline                            Scikit-learn Pipeline + ColumnTransformer
Train/Test Split                    80% / 20%
Saved Format                        .pkl via pickle


Input Features

Feature                           Type  
Crop                          Categorical
Season                        Categorical
State                         Categorical
Crop_Year                     Numeric
Area                          Numeric
Production                    Numeric
Annual_Rainfall               Numeric
Fertilizer                    Numeric
Pesticide                     Numeric




Target

Yield — predicted crop yield


🚀 Getting Started
1. Clone the repository
bashgit clone https://github.com/your-username/crop-yield-prediction.git
cd crop-yield-prediction
2. Install dependencies
bashpip install pandas scikit-learn flask flask-cors joblib
3. Train the model
bashpython train_model.py
This reads crop_yield.csv, trains the pipeline, and saves it as crop_yield_prediction_model_pipeline.pkl.
4. Start the Flask API
bashpython app.py
The server runs at http://localhost:5000.

🔌 API Reference
POST /predict
Accepts a JSON object with input features and returns the predicted yield.
Request
json{
  "Crop": "Rice",
  "Season": "Kharif",
  "State": "Odisha",
  "Crop_Year": 2023,
  "Area": 1500,
  "Production": 3200,
  "Annual_Rainfall": 1200.5,
  "Fertilizer": 450.0,
  "Pesticide": 12.5
}
Response
json{
  "input": { "Crop": "Rice", "Season": "Kharif", ... },
  "predicted_yield": [2.87]
}
Error Response
json{
  "error": "description of what went wrong"
}

⚙️ How It Works

train_model.py loads crop_yield.csv, builds a Scikit-learn Pipeline with a ColumnTransformer (OneHotEncoder for categoricals, passthrough for numerics), fits a LinearRegression model, and serializes the full pipeline to .pkl.
app.py loads the saved pipeline on startup and exposes a /predict POST endpoint. Incoming JSON is converted to a DataFrame, columns are aligned to the training feature order (missing columns default to 0), and the pipeline returns a yield prediction.


🏆 Achievement
This project was submitted to Smart India Hackathon 2025 and qualified Round 1, ranking among the top ~300 teams out of 100,000+ national entries.

📄 License
MIT License — free to use, modify, and distribute.
