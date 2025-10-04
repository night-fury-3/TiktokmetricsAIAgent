from typing import Dict, Any
from .base_scorer import BaseScorer

class EngagementGrowthScorer(BaseScorer):
    def __init__(self, weight: float = 0.05):
        super().__init__("engagement_growth_scorer", weight)
    
    def calculate_score(self, data: Dict[str, Any]) -> float:
        try:
            engagement_growth_rate = data.get('engagement_growth_rate', 0.0)
            follower_growth_rate = data.get('follower_growth_rate', 0.0)
            views_growth_rate = data.get('views_growth_rate', 0.0)
            
            engagement_growth = self.normalize_score(engagement_growth_rate, -0.5, 2.0)
            follower_growth = self.normalize_score(follower_growth_rate, -0.3, 1.0)
            views_growth = self.normalize_score(views_growth_rate, -0.5, 2.0)
            
            score = (
                engagement_growth * 0.5 +
                follower_growth * 0.3 +
                views_growth * 0.2
            )
            
            self.logger.debug(f"Engagement Growth Score: {score:.3f}")
            return score
            
        except Exception as e:
            self.logger.error(f"Error calculating engagement growth score: {e}")
            return 0.0
    
    def get_components(self, data: Dict[str, Any]) -> Dict[str, float]:
        engagement_growth_rate = data.get('engagement_growth_rate', 0.0)
        follower_growth_rate = data.get('follower_growth_rate', 0.0)
        views_growth_rate = data.get('views_growth_rate', 0.0)
        
        return {
            "engagement_growth": self.normalize_score(engagement_growth_rate, -0.5, 2.0),
            "follower_growth": self.normalize_score(follower_growth_rate, -0.3, 1.0),
            "views_growth": self.normalize_score(views_growth_rate, -0.5, 2.0),
            "engagement_growth_rate": engagement_growth_rate,
            "follower_growth_rate": follower_growth_rate,
            "views_growth_rate": views_growth_rate
        }