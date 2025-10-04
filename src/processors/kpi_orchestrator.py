from typing import Dict, Any, List, Tuple
import numpy as np
from src.config.config import settings
from src.logger.logger import logger
from src.processors.scorers import (
    SalesPerformanceScorer, ShopConversionScorer, TikTokShopScorer,
    EngagementScorer, EngagementGrowthScorer, DiscoveryScorer,
    ContentStrategyScorer, AudienceFitScorer, BrandFitScorer,
    TrendFitScorer, ImageScoreScorer, ReachVisibilityScorer, CostEfficiencyScorer
)

class KPIOrchestrator:
    def __init__(self):
        self.logger = logger
        
        self.scorers = {
            "sales_performance_scorer": SalesPerformanceScorer(settings.KPI_WEIGHTS["sales_performance_scorer"]),
            "shop_conversion_scorer": ShopConversionScorer(settings.KPI_WEIGHTS["shop_conversion_scorer"]),
            "tiktok_shop_scorer": TikTokShopScorer(settings.KPI_WEIGHTS["tiktok_shop_scorer"]),
            "engagement_scorer": EngagementScorer(settings.KPI_WEIGHTS["engagement_scorer"]),
            "engagement_growth_scorer": EngagementGrowthScorer(settings.KPI_WEIGHTS["engagement_growth_scorer"]),
            "discovery_scorer": DiscoveryScorer(settings.KPI_WEIGHTS["discovery_scorer"]),
            "content_strategy_scorer": ContentStrategyScorer(settings.KPI_WEIGHTS["content_strategy_scorer"]),
            "audience_fit_scorer": AudienceFitScorer(settings.KPI_WEIGHTS["audience_fit_scorer"]),
            "brand_fit_scorer": BrandFitScorer(settings.KPI_WEIGHTS["brand_fit_scorer"]),
            "trend_fit_scorer": TrendFitScorer(settings.KPI_WEIGHTS["trend_fit_scorer"]),
            "image_score_scorer": ImageScoreScorer(settings.KPI_WEIGHTS["image_score_scorer"]),
            "reach_visibility_scorer": ReachVisibilityScorer(settings.KPI_WEIGHTS["reach_visibility_scorer"]),
            "cost_efficiency_scorer": CostEfficiencyScorer(settings.KPI_WEIGHTS["cost_efficiency_scorer"]),
        }
        
        self.logger.info("KPI Orchestrator initialized with optimized weights")
    
    def calculate_overall_score(self, data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            scores = {}
            weighted_scores = {}
            components = {}
            tier_scores = {"tier_1": 0.0, "tier_2": 0.0, "tier_3": 0.0}
            tier_weights = {"tier_1": 0.0, "tier_2": 0.0, "tier_3": 0.0}
            
            for scorer_name, scorer in self.scorers.items():
                score = scorer.calculate_score(data)
                weighted_score = scorer.calculate_weighted_score(data)
                component_scores = scorer.get_components(data)
                
                scores[scorer_name] = score
                weighted_scores[scorer_name] = weighted_score
                components[scorer_name] = component_scores
                
                if scorer_name in settings.TIER_1_KPIS:
                    tier_scores["tier_1"] += weighted_score
                    tier_weights["tier_1"] += scorer.weight
                elif scorer_name in settings.TIER_2_KPIS:
                    tier_scores["tier_2"] += weighted_score
                    tier_weights["tier_2"] += scorer.weight
                elif scorer_name in settings.TIER_3_KPIS:
                    tier_scores["tier_3"] += weighted_score
                    tier_weights["tier_3"] += scorer.weight
            
            overall_score = sum(weighted_scores.values())
            
            tier_averages = {}
            for tier in ["tier_1", "tier_2", "tier_3"]:
                if tier_weights[tier] > 0:
                    tier_averages[tier] = tier_scores[tier] / tier_weights[tier]
                else:
                    tier_averages[tier] = 0.0
            
            performance_levels = {
                scorer_name: scorer.get_performance_level(score)
                for scorer_name, score in scores.items()
            }
            
            revenue_focus_score = tier_averages["tier_1"]
            
            result = {
                "overall_score": overall_score,
                "revenue_focus_score": revenue_focus_score,
                "tier_scores": tier_averages,
                "individual_scores": scores,
                "weighted_scores": weighted_scores,
                "components": components,
                "performance_levels": performance_levels,
                "weights": settings.KPI_WEIGHTS,
                "tier_breakdown": {
                    "tier_1": {
                        "kpis": settings.TIER_1_KPIS,
                        "total_weight": tier_weights["tier_1"],
                        "average_score": tier_averages["tier_1"]
                    },
                    "tier_2": {
                        "kpis": settings.TIER_2_KPIS,
                        "total_weight": tier_weights["tier_2"],
                        "average_score": tier_averages["tier_2"]
                    },
                    "tier_3": {
                        "kpis": settings.TIER_3_KPIS,
                        "total_weight": tier_weights["tier_3"],
                        "average_score": tier_averages["tier_3"]
                    }
                }
            }
            
            self.logger.info(f"Overall Score calculated: {overall_score:.3f}")
            self.logger.info(f"Revenue Focus Score: {revenue_focus_score:.3f}")
            
            return result
            
        except Exception as e:
            self.logger.error(f"Error calculating overall score: {e}")
            return {
                "overall_score": 0.0,
                "error": str(e),
                "individual_scores": {},
                "components": {}
            }
    
    def get_revenue_optimization_insights(self, data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            result = self.calculate_overall_score(data)
            
            revenue_kpis = settings.REVENUE_KPIS
            low_performance_kpis = []
            
            for kpi in revenue_kpis:
                if kpi in result["individual_scores"]:
                    score = result["individual_scores"][kpi]
                    if score < 0.3:
                        low_performance_kpis.append({
                            "kpi": kpi,
                            "score": score,
                            "weight": settings.KPI_WEIGHTS[kpi],
                            "impact": score * settings.KPI_WEIGHTS[kpi]
                        })
            
            low_performance_kpis.sort(key=lambda x: x["impact"], reverse=True)
            
            current_revenue_score = result["revenue_focus_score"]
            max_possible_revenue_score = sum(settings.KPI_WEIGHTS[kpi] for kpi in revenue_kpis)
            improvement_potential = max_possible_revenue_score - current_revenue_score
            
            insights = {
                "current_revenue_score": current_revenue_score,
                "max_possible_revenue_score": max_possible_revenue_score,
                "improvement_potential": improvement_potential,
                "low_performance_kpis": low_performance_kpis,
                "priority_actions": low_performance_kpis[:3],
                "tier_performance": result["tier_scores"],
                "overall_performance": result["overall_score"]
            }
            
            return insights
            
        except Exception as e:
            self.logger.error(f"Error generating revenue optimization insights: {e}")
            return {"error": str(e)}
    
    def compare_with_equal_weighting(self, data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            new_result = self.calculate_overall_score(data)
            
            equal_weight = 1.0 / len(self.scorers)
            equal_weighted_scores = []
            
            for scorer_name, scorer in self.scorers.items():
                score = scorer.calculate_score(data)
                equal_weighted_scores.append(score * equal_weight)
            
            equal_weighted_score = sum(equal_weighted_scores)
            
            score_difference = new_result["overall_score"] - equal_weighted_score
            percentage_change = (score_difference / equal_weighted_score * 100) if equal_weighted_score > 0 else 0
            
            comparison = {
                "new_weighted_score": new_result["overall_score"],
                "equal_weighted_score": equal_weighted_score,
                "score_difference": score_difference,
                "percentage_change": percentage_change,
                "revenue_focus_improvement": new_result["revenue_focus_score"] - (sum(new_result["individual_scores"][kpi] for kpi in settings.REVENUE_KPIS) / len(settings.REVENUE_KPIS)),
                "algorithm_benefits": {
                    "revenue_alignment": "Prioritizes direct revenue drivers (55% weight)",
                    "intervention_guidance": "Identifies highest-impact improvement areas",
                    "business_focus": "Aligns with e-commerce revenue maximization goal"
                }
            }
            
            return comparison
            
        except Exception as e:
            self.logger.error(f"Error comparing algorithms: {e}")
            return {"error": str(e)}