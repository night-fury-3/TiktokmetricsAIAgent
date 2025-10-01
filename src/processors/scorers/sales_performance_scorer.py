"""
Sales Performance Scorer - Tier 1 (Direct Revenue Driver)
Weight: 0.30 (30%)
"""

from typing import Dict, Any
from .base_scorer import BaseScorer


class SalesPerformanceScorer(BaseScorer):
    """
    Calculates sales performance score based on revenue metrics
    """
    
    def __init__(self, weight: float = 0.30):
        super().__init__("sales_performance_scorer", weight)
    
    def calculate_score(self, data: Dict[str, Any]) -> float:
        """
        Calculate sales performance score
        
        Components:
        - Conversion Score (40%)
        - Revenue Score (40%) 
        - AOV Score (20%)
        """
        try:
            # Extract metrics with defaults
            conversion_rate = data.get('conversion_rate', 0.0)
            total_revenue = data.get('total_revenue', 0.0)
            avg_order_value = data.get('avg_order_value', 0.0)
            target_revenue = data.get('target_revenue', 10000.0)
            target_aov = data.get('target_aov', 50.0)
            
            # Calculate component scores
            conversion_score = self.normalize_score(conversion_rate, 0.0, 0.1)  # 0-10% range
            revenue_score = self.normalize_score(total_revenue, 0.0, target_revenue)
            aov_score = self.normalize_score(avg_order_value, 0.0, target_aov)
            
            # Weighted combination
            score = (
                conversion_score * 0.4 +
                revenue_score * 0.4 +
                aov_score * 0.2
            )
            
            self.logger.debug(f"Sales Performance Score: {score:.3f}")
            return score
            
        except Exception as e:
            self.logger.error(f"Error calculating sales performance score: {e}")
            return 0.0
    
    def get_components(self, data: Dict[str, Any]) -> Dict[str, float]:
        """
        Get detailed component scores
        """
        conversion_rate = data.get('conversion_rate', 0.0)
        total_revenue = data.get('total_revenue', 0.0)
        avg_order_value = data.get('avg_order_value', 0.0)
        target_revenue = data.get('target_revenue', 10000.0)
        target_aov = data.get('target_aov', 50.0)
        
        return {
            "conversion_score": self.normalize_score(conversion_rate, 0.0, 0.1),
            "revenue_score": self.normalize_score(total_revenue, 0.0, target_revenue),
            "aov_score": self.normalize_score(avg_order_value, 0.0, target_aov),
            "conversion_rate": conversion_rate,
            "total_revenue": total_revenue,
            "avg_order_value": avg_order_value
        }
