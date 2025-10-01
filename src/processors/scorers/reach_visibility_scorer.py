"""
Reach Visibility Scorer - Tier 3 (General Health/Cost/Reach)
Weight: 0.03 (3%)
"""

from typing import Dict, Any
from .base_scorer import BaseScorer


class ReachVisibilityScorer(BaseScorer):
    """
    Calculates reach and visibility score based on audience reach metrics
    """
    
    def __init__(self, weight: float = 0.03):
        super().__init__("reach_visibility_scorer", weight)
    
    def calculate_score(self, data: Dict[str, Any]) -> float:
        """
        Calculate reach and visibility score
        """
        try:
            # Extract reach metrics
            total_reach = data.get('total_reach', 0.0)
            unique_viewers = data.get('unique_viewers', 0.0)
            impression_rate = data.get('impression_rate', 0.0)
            visibility_score = data.get('visibility_score', 0.0)
            target_reach = data.get('target_reach', 10000.0)
            
            # Calculate component scores
            reach_score = self.normalize_score(total_reach, 0.0, target_reach)
            unique_score = self.normalize_score(unique_viewers, 0.0, target_reach)
            impression = self.normalize_score(impression_rate, 0.0, 0.1)  # 0-10%
            visibility = self.normalize_score(visibility_score, 0.0, 1.0)
            
            # Weighted combination
            score = (
                reach_score * 0.3 +
                unique_score * 0.3 +
                impression * 0.2 +
                visibility * 0.2
            )
            
            self.logger.debug(f"Reach Visibility Score: {score:.3f}")
            return score
            
        except Exception as e:
            self.logger.error(f"Error calculating reach visibility score: {e}")
            return 0.0
    
    def get_components(self, data: Dict[str, Any]) -> Dict[str, float]:
        """
        Get detailed component scores
        """
        total_reach = data.get('total_reach', 0.0)
        unique_viewers = data.get('unique_viewers', 0.0)
        impression_rate = data.get('impression_rate', 0.0)
        visibility_score = data.get('visibility_score', 0.0)
        target_reach = data.get('target_reach', 10000.0)
        
        return {
            "reach_score": self.normalize_score(total_reach, 0.0, target_reach),
            "unique_score": self.normalize_score(unique_viewers, 0.0, target_reach),
            "impression": self.normalize_score(impression_rate, 0.0, 0.1),
            "visibility": self.normalize_score(visibility_score, 0.0, 1.0),
            "total_reach": total_reach,
            "unique_viewers": unique_viewers,
            "impression_rate": impression_rate,
            "visibility_score": visibility_score
        }
