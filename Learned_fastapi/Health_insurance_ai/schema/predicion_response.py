
from pydantic import BaseModel, Field
from typing import Dict


class PredictionResponse(BaseModel):
    predicted_category: str = Field(..., description="Predicted category of insurance", example="High")
    confidence: float = Field(..., description="Confidence score of the prediction", example=0.85)
    class_probabilities: Dict[str, float] = Field(..., description="Probabilities for each class", example={"Low": 0.1, "Medium": 0.3, "High": 0.6})
    