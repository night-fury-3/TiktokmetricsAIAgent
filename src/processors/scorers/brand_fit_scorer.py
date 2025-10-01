"""
Brand Fit Scorer - Tier 2 (Revenue Enabler)
Weight: 0.03 (3%)
"""

from typing import Dict, Any
from .base_scorer import BaseScorer


class BrandFitScorer(BaseScorer):
    """
    Calculates brand fit score based on brand alignment and trust
    """
    
    def __init__(self, weight: float = 0.03):
        super().__init__("brand_fit_scorer", weight)
    
    def calculate_score(self, data: Dict[str, Any]) -> float:
        """
        Calculate brand fit score
        """
        try:
            # Extract brand metrics
            brand_alignment = data.get('brand_alignment', 0.0)
            trust_score = data.get('trust_score', 0.0)
            authenticity_score = data.get('authenticity_score', 0.0)
            brand_consistency = data.get('brand_consistency', 0.0)
            
            # Calculate component scores
            alignment_score = self.normalize_score(brand_alignment, 0.0, 1.0)
            trust = self.normalize_score(trust_score, 0.0, 1.0)
            authenticity = self.normalize_score(authenticity_score, 0.0, 1.0)
            consistency = self.normalize_score(brand_consistency, 0.0, 1.0)
            
            # Weighted combination
            score = (
                alignment_score * 0.3 +
                trust * 0.3 +
                authenticity * 0.2 +
                consistency * 0.2
            )
            
            self.logger.debug(f"Brand Fit Score: {score:.3f}")
            return score
            
        except Exception as e:
            self.logger.error(f"Error calculating brand fit score: {e}")
            return 0.0
    
    def get_components(self, data: Dict[str, Any]) -> Dict[str, float]:
        """
        Get detailed component scores
        """
        brand_alignment = data.get('brand_alignment', 0.0)
        trust_score = data.get('trust_score', 0.0)
        authenticity_score = data.get('authenticity_score', 0.0)
        brand_consistency = data.get('brand_consistency', 0.0)
        
        return {
            "alignment_score": self.normalize_score(brand_alignment, 0.0, 1.0),
            "trust": self.normalize_score(trust_score, 0.0, 1.0),
            "authenticity": self.normalize_score(authenticity_score, 0.0, 1.0),
            "consistency": self.normalize_score(brand_consistency, 0.0, 1.0),
            "brand_alignment": brand_alignment,
            "trust_score": trust_score,
            "authenticity_score": authenticity_score,
            "brand_consistency": brand_consistency
        }
