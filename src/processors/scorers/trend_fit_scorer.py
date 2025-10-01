"""
Trend Fit Scorer - Tier 3 (General Health/Cost/Reach)
Weight: 0.04 (4%)
"""

from typing import Dict, Any
from .base_scorer import BaseScorer


class TrendFitScorer(BaseScorer):
    """
    Calculates trend fit score based on trend alignment and timing
    """
    
    def __init__(self, weight: float = 0.04):
        super().__init__("trend_fit_scorer", weight)
    
    def calculate_score(self, data: Dict[str, Any]) -> float:
        """
        Calculate trend fit score
        """
        try:
            # Extract trend metrics
            trend_alignment = data.get('trend_alignment', 0.0)
            timing_score = data.get('timing_score', 0.0)
            viral_potential = data.get('viral_potential', 0.0)
            trend_relevance = data.get('trend_relevance', 0.0)
            
            # Calculate component scores
            alignment_score = self.normalize_score(trend_alignment, 0.0, 1.0)
            timing = self.normalize_score(timing_score, 0.0, 1.0)
            viral = self.normalize_score(viral_potential, 0.0, 1.0)
            relevance = self.normalize_score(trend_relevance, 0.0, 1.0)
            
            # Weighted combination
            score = (
                alignment_score * 0.3 +
                timing * 0.3 +
                viral * 0.2 +
                relevance * 0.2
            )
            
            self.logger.debug(f"Trend Fit Score: {score:.3f}")
            return score
            
        except Exception as e:
            self.logger.error(f"Error calculating trend fit score: {e}")
            return 0.0
    
    def get_components(self, data: Dict[str, Any]) -> Dict[str, float]:
        """
        Get detailed component scores
        """
        trend_alignment = data.get('trend_alignment', 0.0)
        timing_score = data.get('timing_score', 0.0)
        viral_potential = data.get('viral_potential', 0.0)
        trend_relevance = data.get('trend_relevance', 0.0)
        
        return {
            "alignment_score": self.normalize_score(trend_alignment, 0.0, 1.0),
            "timing": self.normalize_score(timing_score, 0.0, 1.0),
            "viral": self.normalize_score(viral_potential, 0.0, 1.0),
            "relevance": self.normalize_score(trend_relevance, 0.0, 1.0),
            "trend_alignment": trend_alignment,
            "timing_score": timing_score,
            "viral_potential": viral_potential,
            "trend_relevance": trend_relevance
        }
