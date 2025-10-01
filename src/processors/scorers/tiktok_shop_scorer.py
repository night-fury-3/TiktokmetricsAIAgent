"""
TikTok Shop Scorer - Tier 1 (Direct Revenue Driver)
Weight: 0.10 (10%)
"""

from typing import Dict, Any
from .base_scorer import BaseScorer


class TikTokShopScorer(BaseScorer):
    """
    Calculates TikTok Shop integration score
    """
    
    def __init__(self, weight: float = 0.10):
        super().__init__("tiktok_shop_scorer", weight)
    
    def calculate_score(self, data: Dict[str, Any]) -> float:
        """
        Calculate TikTok Shop score
        
        Components:
        - Listing Score (40%)
        - Velocity Score (35%)
        - Integration Score (25%)
        """
        try:
            # Extract metrics with defaults
            listing_quality = data.get('listing_quality', 0.0)
            product_velocity = data.get('product_velocity', 0.0)
            integration_seamlessness = data.get('integration_seamlessness', 0.0)
            
            # Calculate component scores
            listing_score = self.normalize_score(listing_quality, 0.0, 1.0)
            velocity_score = self.normalize_score(product_velocity, 0.0, 1.0)
            integration_score = self.normalize_score(integration_seamlessness, 0.0, 1.0)
            
            # Weighted combination
            score = (
                listing_score * 0.4 +
                velocity_score * 0.35 +
                integration_score * 0.25
            )
            
            self.logger.debug(f"TikTok Shop Score: {score:.3f}")
            return score
            
        except Exception as e:
            self.logger.error(f"Error calculating TikTok Shop score: {e}")
            return 0.0
    
    def get_components(self, data: Dict[str, Any]) -> Dict[str, float]:
        """
        Get detailed component scores
        """
        listing_quality = data.get('listing_quality', 0.0)
        product_velocity = data.get('product_velocity', 0.0)
        integration_seamlessness = data.get('integration_seamlessness', 0.0)
        
        return {
            "listing_score": self.normalize_score(listing_quality, 0.0, 1.0),
            "velocity_score": self.normalize_score(product_velocity, 0.0, 1.0),
            "integration_score": self.normalize_score(integration_seamlessness, 0.0, 1.0),
            "listing_quality": listing_quality,
            "product_velocity": product_velocity,
            "integration_seamlessness": integration_seamlessness
        }
