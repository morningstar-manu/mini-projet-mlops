from __future__ import annotations

from pathlib import Path

import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

MODEL_PATH = Path("model.pkl")
TARGET_NAMES = ["setosa", "versicolor", "virginica"]

app = FastAPI(title="Mini Projet MLOps API", version="1.0.0")


class PredictRequest(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            "Model file not found. Run `python train.py` before starting the API."
        )
    return joblib.load(MODEL_PATH)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/predict")
def predict(payload: PredictRequest) -> dict[str, str | int]:
    try:
        model = load_model()
    except FileNotFoundError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    features = [
        [
            payload.sepal_length,
            payload.sepal_width,
            payload.petal_length,
            payload.petal_width,
        ]
    ]
    prediction = int(model.predict(features)[0])
    return {"prediction": prediction, "class_name": TARGET_NAMES[prediction]}
