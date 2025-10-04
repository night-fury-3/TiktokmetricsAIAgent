from typing import Dict, Any
from .base_scorer import BaseScorer

class CostEfficiencyScorer(BaseScorer):
    def __init__(self, weight: float = 0.03):
        super().__init__("cost_efficiency_scorer", weight)
    
    def calculate_score(self, data: Dict[str, Any]) -> float:
        try:
            cost_per_acquisition = data.get('cost_per_acquisition', 100.0)
            cost_per_engagement = data.get('cost_per_engagement', 1.0)
            cost_per_view = data.get('cost_per_view', 0.1)
            roi_score = data.get('roi_score', 0.0)
            target_cpa = data.get('target_cpa', 50.0)
            target_cpe = data.get('target_cpe', 0.5)
            target_cpv = data.get('target_cpv', 0.05)
            
            cpa_score = self.normalize_score(target_cpa / max(cost_per_acquisition, 0.01), 0.0, 2.0)
            cpe_score = self.normalize_score(target_cpe / max(cost_per_engagement, 0.01), 0.0, 2.0)
            cpv_score = self.normalize_score(target_cpv / max(cost_per_view, 0.001), 0.0, 2.0)
            roi = self.normalize_score(roi_score, 0.0, 5.0)
            
            score = (
                cpa_score * 0.4 +
                cpe_score * 0.3 +
                cpv_score * 0.2 +
                roi * 0.1
            )
            
            self.logger.debug(f"Cost Efficiency Score: {score:.3f}")
            return score
            
        except Exception as e:
            self.logger.error(f"Error calculating cost efficiency score: {e}")
            return 0.0
    
    def get_components(self, data: Dict[str, Any]) -> Dict[str, float]:
        cost_per_acquisition = data.get('cost_per_acquisition', 100.0)
        cost_per_engagement = data.get('cost_per_engagement', 1.0)
        cost_per_view = data.get('cost_per_view', 0.1)
        roi_score = data.get('roi_score', 0.0)
        target_cpa = data.get('target_cpa', 50.0)
        target_cpe = data.get('target_cpe', 0.5)
        target_cpv = data.get('target_cpv', 0.05)
        
        return {
            "cpa_score": self.normalize_score(target_cpa / max(cost_per_acquisition, 0.01), 0.0, 2.0),
            "cpe_score": self.normalize_score(target_cpe / max(cost_per_engagement, 0.01), 0.0, 2.0),
            "cpv_score": self.normalize_score(target_cpv / max(cost_per_view, 0.001), 0.0, 2.0),
            "roi": self.normalize_score(roi_score, 0.0, 5.0),
            "cost_per_acquisition": cost_per_acquisition,
            "cost_per_engagement": cost_per_engagement,
            "cost_per_view": cost_per_view,
            "roi_score": roi_score
        }