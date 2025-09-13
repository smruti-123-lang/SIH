import pickle

# apna model ka exact path do
model_path = "crop_yield_prediction_model_pipeline.pkl"

with open(model_path, "rb") as f:
    model = pickle.load(f)

# try to print feature names
try:
    print("✅ Model Feature Names:")
    print(model.feature_names_in_)
except AttributeError:
    print("⚠️ feature_names_in_ attribute not found. Maybe pipeline ke andar transformer h.")
    print("Type of model:", type(model))
    print("Steps in pipeline:", getattr(model, "steps", "No steps found"))
