from typing import Dict, Any
from .base_scorer import BaseScorer

class ImageScoreScorer(BaseScorer):
    def __init__(self, weight: float = 0.03):
        super().__init__("image_score_scorer", weight)
    
    def calculate_score(self, data: Dict[str, Any]) -> float:
        try:
            image_quality = data.get('image_quality', 0.0)
            lighting_score = data.get('lighting_score', 0.0)
            composition_score = data.get('composition_score', 0.0)
            color_balance = data.get('color_balance', 0.0)
            
            quality = self.normalize_score(image_quality, 0.0, 1.0)
            lighting = self.normalize_score(lighting_score, 0.0, 1.0)
            composition = self.normalize_score(composition_score, 0.0, 1.0)
            color = self.normalize_score(color_balance, 0.0, 1.0)
            
            score = (
                quality * 0.4 +
                lighting * 0.3 +
                composition * 0.2 +
                color * 0.1
            )
            
            self.logger.debug(f"Image Score: {score:.3f}")
            return score
            
        except Exception as e:
            self.logger.error(f"Error calculating image score: {e}")
            return 0.0
    
    def get_components(self, data: Dict[str, Any]) -> Dict[str, float]:
        image_quality = data.get('image_quality', 0.0)
        lighting_score = data.get('lighting_score', 0.0)
        composition_score = data.get('composition_score', 0.0)
        color_balance = data.get('color_balance', 0.0)
        
        return {
            "quality": self.normalize_score(image_quality, 0.0, 1.0),
            "lighting": self.normalize_score(lighting_score, 0.0, 1.0),
            "composition": self.normalize_score(composition_score, 0.0, 1.0),
            "color": self.normalize_score(color_balance, 0.0, 1.0),
            "image_quality": image_quality,
            "lighting_score": lighting_score,
            "composition_score": composition_score,
            "color_balance": color_balance
        }