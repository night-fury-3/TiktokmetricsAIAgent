"""
Engagement Scorer - Tier 2 (Revenue Enabler)
Weight: 0.10 (10%)
"""

from typing import Dict, Any
from .base_scorer import BaseScorer


class EngagementScorer(BaseScorer):
    """
    Calculates engagement score based on user interaction metrics
    """
    
    def __init__(self, weight: float = 0.10):
        super().__init__("engagement_scorer", weight)
    
    def calculate_score(self, data: Dict[str, Any]) -> float:
        """
        Calculate engagement score
        
        Components:
        - Interaction Balance (40%)
        - Retention Score (35%)
        - Sharing Score (25%)
        """
        try:
            # Extract metrics with defaults
            likes_ratio = data.get('likes_ratio', 0.0)
            comments_ratio = data.get('comments_ratio', 0.0)
            shares_ratio = data.get('shares_ratio', 0.0)
            retention_rate = data.get('retention_rate', 0.0)
            avg_watch_time = data.get('avg_watch_time', 0.0)
            video_duration = data.get('video_duration', 30.0)
            
            # Calculate component scores
            interaction_balance = self._calculate_interaction_balance(likes_ratio, comments_ratio, shares_ratio)
            retention_score = self.normalize_score(retention_rate, 0.0, 1.0)
            sharing_score = self.normalize_score(shares_ratio, 0.0, 0.1)  # 0-10% range
            watch_completion = min(avg_watch_time / video_duration, 1.0) if video_duration > 0 else 0.0
            
            # Weighted combination
            score = (
                interaction_balance * 0.4 +
                retention_score * 0.25 +
                sharing_score * 0.25 +
                watch_completion * 0.1
            )
            
            self.logger.debug(f"Engagement Score: {score:.3f}")
            return score
            
        except Exception as e:
            self.logger.error(f"Error calculating engagement score: {e}")
            return 0.0
    
    def _calculate_interaction_balance(self, likes: float, comments: float, shares: float) -> float:
        """
        Calculate interaction balance score
        """
        total_interactions = likes + comments + shares
        if total_interactions == 0:
            return 0.0
        
        # Ideal balance: 70% likes, 20% comments, 10% shares
        ideal_likes = 0.7
        ideal_comments = 0.2
        ideal_shares = 0.1
        
        likes_ratio = likes / total_interactions
        comments_ratio = comments / total_interactions
        shares_ratio = shares / total_interactions
        
        # Calculate balance score (closer to ideal = higher score)
        balance_score = 1.0 - (
            abs(likes_ratio - ideal_likes) +
            abs(comments_ratio - ideal_comments) +
            abs(shares_ratio - ideal_shares)
        ) / 2.0  # Normalize to 0-1 range
        
        return max(0.0, balance_score)
    
    def get_components(self, data: Dict[str, Any]) -> Dict[str, float]:
        """
        Get detailed component scores
        """
        likes_ratio = data.get('likes_ratio', 0.0)
        comments_ratio = data.get('comments_ratio', 0.0)
        shares_ratio = data.get('shares_ratio', 0.0)
        retention_rate = data.get('retention_rate', 0.0)
        avg_watch_time = data.get('avg_watch_time', 0.0)
        video_duration = data.get('video_duration', 30.0)
        
        return {
            "interaction_balance": self._calculate_interaction_balance(likes_ratio, comments_ratio, shares_ratio),
            "retention_score": self.normalize_score(retention_rate, 0.0, 1.0),
            "sharing_score": self.normalize_score(shares_ratio, 0.0, 0.1),
            "watch_completion": min(avg_watch_time / video_duration, 1.0) if video_duration > 0 else 0.0,
            "likes_ratio": likes_ratio,
            "comments_ratio": comments_ratio,
            "shares_ratio": shares_ratio,
            "retention_rate": retention_rate
        }
