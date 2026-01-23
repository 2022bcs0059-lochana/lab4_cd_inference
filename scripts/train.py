import json
import joblib
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
df = pd.read_csv("data/winequality-red.csv", sep=";")
X = df.drop("quality", axis=1)
y = df["quality"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#model
model = RandomForestRegressor(n_estimators=100, max_depth=15, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

os.makedirs("model", exist_ok=True)

joblib.dump(model, "model/model.pkl")

with open("metrics.json", "w") as f:
    json.dump({"mse": mse, "r2": r2}, f)

print("MSE:", mse)
print("R2:", r2)
