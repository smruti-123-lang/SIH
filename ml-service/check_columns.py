import pandas as pd

# apna dataset load karo
df = pd.read_csv("crop_yield.csv")

print("✅ Columns in training data:")
print(list(df.columns))
