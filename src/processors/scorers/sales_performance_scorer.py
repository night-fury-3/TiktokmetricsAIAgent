from typing import Dict, Any
from .base_scorer import BaseScorer

class SalesPerformanceScorer(BaseScorer):
    def __init__(self, weight: float = 0.30):
        super().__init__("sales_performance_scorer", weight)
    
    def calculate_score(self, data: Dict[str, Any]) -> float:
        try:
            conversion_rate = data.get('conversion_rate', 0.0)
            total_revenue = data.get('total_revenue', 0.0)
            avg_order_value = data.get('avg_order_value', 0.0)
            target_revenue = data.get('target_revenue', 10000.0)
            target_aov = data.get('target_aov', 50.0)
            
            conversion_score = self.normalize_score(conversion_rate, 0.0, 0.1)
            revenue_score = self.normalize_score(total_revenue, 0.0, target_revenue)
            aov_score = self.normalize_score(avg_order_value, 0.0, target_aov)
            
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