import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression

# 1. Load dataset
data = pd.read_csv("crop_yield.csv")

print("✅ Columns in dataset:", data.columns.tolist())

# 2. Features & target
X = data.drop(columns=["Yield"])   # independent vars
y = data["Yield"]                  # target

# 3. Identify categorical and numeric columns
categorical_features = ["Crop", "Season", "State"]
numeric_features = ["Crop_Year", "Area", "Production", "Annual_Rainfall", "Fertilizer", "Pesticide"]

# 4. Preprocessor
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
        ("num", "passthrough", numeric_features)
    ]
)

# 5. Build pipeline
pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("model", LinearRegression())
])

# 6. Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 7. Fit pipeline
pipeline.fit(X_train, y_train)

print("✅ Model trained successfully")

# 8. Save pipeline as .pkl
with open("crop_yield_prediction_model_pipeline.pkl", "wb") as f:
    pickle.dump(pipeline, f)

print("✅ Pipeline model saved as crop_yield_prediction_model_pipeline.pkl")
