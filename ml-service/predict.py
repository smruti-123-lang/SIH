import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)

MODEL_PATH = "crop_yield_prediction_model_pipeline.pkl"

try:
    model = joblib.load(MODEL_PATH)
    print(f"✅ Model loaded successfully: {MODEL_PATH}")

    # Required columns from pipeline
    expected_features = []
    if hasattr(model, "feature_names_in_"):
        expected_features = list(model.feature_names_in_)
    elif hasattr(model, "named_steps") and "preprocessor" in model.named_steps:
        preprocessor = model.named_steps["preprocessor"]
        expected_features = []
        for name, trans, cols in preprocessor.transformers:
            expected_features.extend(cols)
    print("📌 Expected features:", expected_features)

except Exception as e:
    print("❌ Error loading model:", e)
    model = None
    expected_features = []

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        print("📥 Incoming data:", data)

        # Convert JSON → DataFrame
        df = pd.DataFrame([data])

        # 🔥 Align columns with training order
        for col in expected_features:
            if col not in df.columns:
                df[col] = 0   # missing columns fill with 0
        df = df[expected_features]

        print("✅ Final DataFrame:")
        print(df)

        # Prediction
        prediction = model.predict(df)

        return jsonify({
            "input": data,
            "predicted_yield": prediction.tolist()
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
