"""
Discovery Scorer - Tier 2 (Revenue Enabler)
Weight: 0.04 (4%)
"""

from typing import Dict, Any
from .base_scorer import BaseScorer


class DiscoveryScorer(BaseScorer):
    """
    Calculates discovery score based on content visibility metrics
    """
    
    def __init__(self, weight: float = 0.04):
        super().__init__("discovery_scorer", weight)
    
    def calculate_score(self, data: Dict[str, Any]) -> float:
        """
        Calculate discovery score
        """
        try:
            # Extract discovery metrics
            hashtag_performance = data.get('hashtag_performance', 0.0)
            search_visibility = data.get('search_visibility', 0.0)
            recommendation_rate = data.get('recommendation_rate', 0.0)
            viral_potential = data.get('viral_potential', 0.0)
            
            # Calculate component scores
            hashtag_score = self.normalize_score(hashtag_performance, 0.0, 1.0)
            search_score = self.normalize_score(search_visibility, 0.0, 1.0)
            recommendation_score = self.normalize_score(recommendation_rate, 0.0, 0.1)  # 0-10%
            viral_score = self.normalize_score(viral_potential, 0.0, 1.0)
            
            # Weighted combination
            score = (
                hashtag_score * 0.3 +
                search_score * 0.3 +
                recommendation_score * 0.2 +
                viral_score * 0.2
            )
            
            self.logger.debug(f"Discovery Score: {score:.3f}")
            return score
            
        except Exception as e:
            self.logger.error(f"Error calculating discovery score: {e}")
            return 0.0
    
    def get_components(self, data: Dict[str, Any]) -> Dict[str, float]:
        """
        Get detailed component scores
        """
        hashtag_performance = data.get('hashtag_performance', 0.0)
        search_visibility = data.get('search_visibility', 0.0)
        recommendation_rate = data.get('recommendation_rate', 0.0)
        viral_potential = data.get('viral_potential', 0.0)
        
        return {
            "hashtag_score": self.normalize_score(hashtag_performance, 0.0, 1.0),
            "search_score": self.normalize_score(search_visibility, 0.0, 1.0),
            "recommendation_score": self.normalize_score(recommendation_rate, 0.0, 0.1),
            "viral_score": self.normalize_score(viral_potential, 0.0, 1.0),
            "hashtag_performance": hashtag_performance,
            "search_visibility": search_visibility,
            "recommendation_rate": recommendation_rate,
            "viral_potential": viral_potential
        }
