from fastapi import APIRouter, HTTPException
from typing import List, Union
from app.api.schemas import (
    PredictionInput,
    PredictionOutput,
    PredictionResult,
    PredictionFeatures
)
from app.services.model import model_service
from app.core.config import settings

router = APIRouter()


@router.get("/health")
def health_check():
    return {"status": "success"}


@router.post("/predict", response_model=PredictionOutput)
def predict(input_data: PredictionInput):
    try:
        # Преобразуем входные данные в список, если это одиночный объект
        features = input_data.data
        if isinstance(features, PredictionFeatures):
            features = [features]

        predictions = model_service.predict(features)

        return PredictionOutput(
            predictions=[
                PredictionResult(
                    id=features[i].id,
                    prediction=float(pred),
                    model_version=settings.MODEL_VERSION
                )
                for i, pred in enumerate(predictions)
            ]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))