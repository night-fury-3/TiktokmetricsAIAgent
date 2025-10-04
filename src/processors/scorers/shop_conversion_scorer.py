from typing import Dict, Any
from .base_scorer import BaseScorer

class ShopConversionScorer(BaseScorer):
    def __init__(self, weight: float = 0.15):
        super().__init__("shop_conversion_scorer", weight)
    
    def calculate_score(self, data: Dict[str, Any]) -> float:
        try:
            funnel_completion_rate = data.get('funnel_completion_rate', 0.0)
            cart_abandonment_rate = data.get('cart_abandonment_rate', 1.0)
            checkout_success_rate = data.get('checkout_success_rate', 0.0)
            
            funnel_score = self.normalize_score(funnel_completion_rate, 0.0, 1.0)
            abandonment_score = self.normalize_score(1.0 - cart_abandonment_rate, 0.0, 1.0)
            checkout_score = self.normalize_score(checkout_success_rate, 0.0, 1.0)
            
            score = (
                funnel_score * 0.5 +
                abandonment_score * 0.3 +
                checkout_score * 0.2
            )
            
            self.logger.debug(f"Shop Conversion Score: {score:.3f}")
            return score
            
        except Exception as e:
            self.logger.error(f"Error calculating shop conversion score: {e}")
            return 0.0
    
    def get_components(self, data: Dict[str, Any]) -> Dict[str, float]:
        funnel_completion_rate = data.get('funnel_completion_rate', 0.0)
        cart_abandonment_rate = data.get('cart_abandonment_rate', 1.0)
        checkout_success_rate = data.get('checkout_success_rate', 0.0)
        
        return {
            "funnel_score": self.normalize_score(funnel_completion_rate, 0.0, 1.0),
            "abandonment_score": self.normalize_score(1.0 - cart_abandonment_rate, 0.0, 1.0),
            "checkout_score": self.normalize_score(checkout_success_rate, 0.0, 1.0),
            "funnel_completion_rate": funnel_completion_rate,
            "cart_abandonment_rate": cart_abandonment_rate,
            "checkout_success_rate": checkout_success_rate
        }