import catboost
import numpy as np
from typing import List, Union, Optional
from app.core.config import settings
from app.api.schemas import PredictionFeatures


class ModelService:
    _model: Optional[catboost.CatBoost]

    @property
    def model(self) -> catboost.CatBoost:
        if self._model is None:
            raise ValueError("Model is not loaded")
        return self._model

    def load_model(self):
        try:
            self._model = catboost.CatBoost()
            self._model.load_model(settings.MODEL_PATH)
        except Exception as e:
            self._model = None
            raise Exception(f"Error loading model: {str(e)}")

    @staticmethod
    def _prepare_features(features: PredictionFeatures) -> np.ndarray:
        return np.array(
            [
                features.RESOURCE,
                features.MGR_ID,
                features.ROLE_ROLLUP_1,
                features.ROLE_ROLLUP_2,
                features.ROLE_DEPTNAME,
                features.ROLE_TITLE,
                features.ROLE_FAMILY_DESC,
                features.ROLE_FAMILY,
                features.ROLE_CODE,
            ]
        ).reshape(1, -1)

    def predict(
        self, features: Union[PredictionFeatures, List[PredictionFeatures]]
    ) -> List[float]:
        try:
            if isinstance(features, PredictionFeatures):
                features = [features]

            features_array = np.vstack(
                [self._prepare_features(feature) for feature in features]
            )

            predictions = self.model.predict(
                features_array, prediction_type="Probability"
            )
            if len(predictions.shape) > 1:
                predictions = predictions[:, 1]

            return predictions.tolist()
        except Exception as e:
            raise Exception(f"Error making prediction: {str(e)}")


model_service = ModelService()
