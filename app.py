from fastapi import FastAPI, Body
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load("model/model.pkl")

FEATURES = [
    "fixed acidity","volatile acidity","citric acid",
    "residual sugar","chlorides","free sulfur dioxide",
    "total sulfur dioxide","density","pH","sulphates","alcohol"
]

@app.post("/predict")
def predict(features: list = Body(...)):
    data = pd.DataFrame([features], columns=FEATURES)
    pred = model.predict(data)
    return {
        "name": "Lochana Balivada",
        "roll_no": "2022BCS0059",
        "wine_quality": int(round(pred[0]))
    }
