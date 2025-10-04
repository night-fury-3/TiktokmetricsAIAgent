from typing import Dict, Any
from .base_scorer import BaseScorer

class EngagementScorer(BaseScorer):
    def __init__(self, weight: float = 0.10):
        super().__init__("engagement_scorer", weight)
    
    def calculate_score(self, data: Dict[str, Any]) -> float:
        try:
            likes_ratio = data.get('likes_ratio', 0.0)
            comments_ratio = data.get('comments_ratio', 0.0)
            shares_ratio = data.get('shares_ratio', 0.0)
            retention_rate = data.get('retention_rate', 0.0)
            avg_watch_time = data.get('avg_watch_time', 0.0)
            video_duration = data.get('video_duration', 30.0)
            
            interaction_balance = self._calculate_interaction_balance(likes_ratio, comments_ratio, shares_ratio)
            retention_score = self.normalize_score(retention_rate, 0.0, 1.0)
            sharing_score = self.normalize_score(shares_ratio, 0.0, 0.1)
            watch_completion = min(avg_watch_time / video_duration, 1.0) if video_duration > 0 else 0.0
            
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
        total_interactions = likes + comments + shares
        if total_interactions == 0:
            return 0.0
        
        ideal_likes = 0.7
        ideal_comments = 0.2
        ideal_shares = 0.1
        
        likes_ratio = likes / total_interactions
        comments_ratio = comments / total_interactions
        shares_ratio = shares / total_interactions
        
        balance_score = 1.0 - (
            abs(likes_ratio - ideal_likes) +
            abs(comments_ratio - ideal_comments) +
            abs(shares_ratio - ideal_shares)
        ) / 2.0
        
        return max(0.0, balance_score)
    
    def get_components(self, data: Dict[str, Any]) -> Dict[str, float]:
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