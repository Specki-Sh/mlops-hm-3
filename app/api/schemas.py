from pydantic import BaseModel
from typing import List, Union


class PredictionFeatures(BaseModel):
    id: int
    RESOURCE: int
    MGR_ID: int
    ROLE_ROLLUP_1: int
    ROLE_ROLLUP_2: int
    ROLE_DEPTNAME: int
    ROLE_TITLE: int
    ROLE_FAMILY_DESC: int
    ROLE_FAMILY: int
    ROLE_CODE: int


class PredictionInput(BaseModel):
    data: Union[PredictionFeatures, List[PredictionFeatures]]


class PredictionResult(BaseModel):
    id: int
    prediction: float
    model_version: str


class PredictionOutput(BaseModel):
    predictions: List[PredictionResult]
