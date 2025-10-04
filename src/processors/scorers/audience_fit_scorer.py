from typing import Dict, Any
from .base_scorer import BaseScorer

class AudienceFitScorer(BaseScorer):
    def __init__(self, weight: float = 0.04):
        super().__init__("audience_fit_scorer", weight)
    
    def calculate_score(self, data: Dict[str, Any]) -> float:
        try:
            target_demographic_match = data.get('target_demographic_match', 0.0)
            audience_engagement_quality = data.get('audience_engagement_quality', 0.0)
            follower_quality_score = data.get('follower_quality_score', 0.0)
            audience_retention = data.get('audience_retention', 0.0)
            
            demographic_score = self.normalize_score(target_demographic_match, 0.0, 1.0)
            engagement_quality_score = self.normalize_score(audience_engagement_quality, 0.0, 1.0)
            follower_quality = self.normalize_score(follower_quality_score, 0.0, 1.0)
            retention_score = self.normalize_score(audience_retention, 0.0, 1.0)
            
            score = (
                demographic_score * 0.3 +
                engagement_quality_score * 0.3 +
                follower_quality * 0.2 +
                retention_score * 0.2
            )
            
            self.logger.debug(f"Audience Fit Score: {score:.3f}")
            return score
            
        except Exception as e:
            self.logger.error(f"Error calculating audience fit score: {e}")
            return 0.0
    
    def get_components(self, data: Dict[str, Any]) -> Dict[str, float]:
        target_demographic_match = data.get('target_demographic_match', 0.0)
        audience_engagement_quality = data.get('audience_engagement_quality', 0.0)
        follower_quality_score = data.get('follower_quality_score', 0.0)
        audience_retention = data.get('audience_retention', 0.0)
        
        return {
            "demographic_score": self.normalize_score(target_demographic_match, 0.0, 1.0),
            "engagement_quality_score": self.normalize_score(audience_engagement_quality, 0.0, 1.0),
            "follower_quality": self.normalize_score(follower_quality_score, 0.0, 1.0),
            "retention_score": self.normalize_score(audience_retention, 0.0, 1.0),
            "target_demographic_match": target_demographic_match,
            "audience_engagement_quality": audience_engagement_quality,
            "follower_quality_score": follower_quality_score,
            "audience_retention": audience_retention
        }