"""
Content Strategy Scorer - Tier 2 (Revenue Enabler)
Weight: 0.06 (6%)
"""

from typing import Dict, Any
from .base_scorer import BaseScorer


class ContentStrategyScorer(BaseScorer):
    """
    Calculates content strategy score based on content quality and consistency
    """
    
    def __init__(self, weight: float = 0.06):
        super().__init__("content_strategy_scorer", weight)
    
    def calculate_score(self, data: Dict[str, Any]) -> float:
        """
        Calculate content strategy score
        """
        try:
            # Extract content metrics
            video_quality = data.get('video_quality', 0.0)
            content_freshness = data.get('content_freshness', 0.0)
            posting_consistency = data.get('posting_consistency', 0.0)
            content_diversity = data.get('content_diversity', 0.0)
            
            # Calculate component scores
            quality_score = self.normalize_score(video_quality, 0.0, 1.0)
            freshness_score = self.normalize_score(content_freshness, 0.0, 1.0)
            consistency_score = self.normalize_score(posting_consistency, 0.0, 1.0)
            diversity_score = self.normalize_score(content_diversity, 0.0, 1.0)
            
            # Weighted combination
            score = (
                quality_score * 0.4 +
                freshness_score * 0.25 +
                consistency_score * 0.2 +
                diversity_score * 0.15
            )
            
            self.logger.debug(f"Content Strategy Score: {score:.3f}")
            return score
            
        except Exception as e:
            self.logger.error(f"Error calculating content strategy score: {e}")
            return 0.0
    
    def get_components(self, data: Dict[str, Any]) -> Dict[str, float]:
        """
        Get detailed component scores
        """
        video_quality = data.get('video_quality', 0.0)
        content_freshness = data.get('content_freshness', 0.0)
        posting_consistency = data.get('posting_consistency', 0.0)
        content_diversity = data.get('content_diversity', 0.0)
        
        return {
            "video_quality": self.normalize_score(video_quality, 0.0, 1.0),
            "content_freshness": self.normalize_score(content_freshness, 0.0, 1.0),
            "posting_consistency": self.normalize_score(posting_consistency, 0.0, 1.0),
            "content_diversity": self.normalize_score(content_diversity, 0.0, 1.0),
            "raw_video_quality": video_quality,
            "raw_content_freshness": content_freshness,
            "raw_posting_consistency": posting_consistency,
            "raw_content_diversity": content_diversity
        }
