"""
Recommendation Generator - AI Pipeline for Revenue Optimization
"""

from typing import Dict, Any, List, Tuple
import numpy as np
from src.config.config import settings
from src.logger.logger import logger
from src.processors.kpi_orchestrator import KPIOrchestrator


class RecommendationGenerator:
    """
    Generates actionable recommendations for revenue optimization
    """
    
    def __init__(self):
        """Initialize the recommendation generator"""
        self.logger = logger
        self.kpi_orchestrator = KPIOrchestrator()
        
        # Recommendation templates for different component issues
        self.recommendation_templates = {
            "funnel_score": {
                "title": "Improve Conversion Funnel",
                "priority": "high",
                "cost": "medium",
                "expected_improvement": 0.15,
                "actions": [
                    "Add 3-step CTA in video description",
                    "Implement pinned comment with discount code",
                    "Optimize checkout process (reduce steps)",
                    "Add trust signals (reviews, guarantees)",
                    "Test different CTA placements"
                ],
                "experiment": {
                    "type": "A/B Test",
                    "variants": ["baseline", "optimized_funnel"],
                    "duration_days": 14,
                    "primary_metric": "shop_conversion_score",
                    "success_threshold": 0.1
                }
            },
            "interaction_balance": {
                "title": "Improve Engagement Balance",
                "priority": "medium",
                "cost": "low",
                "expected_improvement": 0.12,
                "actions": [
                    "Add interactive prompts (questions, polls)",
                    "Create micro-challenges or contests",
                    "Respond to comments within 2 hours",
                    "Use call-to-action for comments",
                    "Share behind-the-scenes content"
                ],
                "experiment": {
                    "type": "A/B Test",
                    "variants": ["baseline", "interactive_content"],
                    "duration_days": 7,
                    "primary_metric": "engagement_score",
                    "success_threshold": 0.08
                }
            },
            "video_quality": {
                "title": "Enhance Video Quality",
                "priority": "medium",
                "cost": "low",
                "expected_improvement": 0.10,
                "actions": [
                    "Follow lighting checklist (natural light, avoid backlight)",
                    "Use stable camera (tripod or gimbal)",
                    "Follow 15-second product demo template",
                    "Add clear product close-ups",
                    "Use trending audio with product focus"
                ],
                "experiment": {
                    "type": "A/B Test",
                    "variants": ["baseline", "enhanced_quality"],
                    "duration_days": 10,
                    "primary_metric": "content_strategy_score",
                    "success_threshold": 0.06
                }
            },
            "conversion_score": {
                "title": "Boost Sales Conversion",
                "priority": "high",
                "cost": "high",
                "expected_improvement": 0.20,
                "actions": [
                    "Implement urgency tactics (limited time offers)",
                    "Add social proof (customer testimonials)",
                    "Create product comparison videos",
                    "Use influencer partnerships",
                    "Optimize product descriptions and pricing"
                ],
                "experiment": {
                    "type": "A/B Test",
                    "variants": ["baseline", "conversion_optimized"],
                    "duration_days": 21,
                    "primary_metric": "sales_performance_score",
                    "success_threshold": 0.15
                }
            },
            "abandonment_score": {
                "title": "Reduce Cart Abandonment",
                "priority": "high",
                "cost": "medium",
                "expected_improvement": 0.18,
                "actions": [
                    "Add exit-intent popup with discount",
                    "Implement cart recovery email sequence",
                    "Simplify checkout process",
                    "Add multiple payment options",
                    "Show security badges and guarantees"
                ],
                "experiment": {
                    "type": "A/B Test",
                    "variants": ["baseline", "abandonment_reduction"],
                    "duration_days": 14,
                    "primary_metric": "shop_conversion_score",
                    "success_threshold": 0.12
                }
            }
        }
    
    def generate_recommendations(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate actionable recommendations for revenue optimization
        
        Args:
            data: Input data dictionary containing all metrics
            
        Returns:
            Dictionary containing prioritized recommendations
        """
        try:
            # Get KPI analysis
            kpi_analysis = self.kpi_orchestrator.calculate_overall_score(data)
            insights = self.kpi_orchestrator.get_revenue_optimization_insights(data)
            
            # Identify bottlenecks using diagnostic model
            bottlenecks = self._identify_bottlenecks(kpi_analysis)
            
            # Generate recommendations for each bottleneck
            recommendations = []
            for bottleneck in bottlenecks:
                recommendation = self._create_recommendation(bottleneck, kpi_analysis)
                if recommendation:
                    recommendations.append(recommendation)
            
            # Sort by priority and expected impact
            recommendations.sort(key=lambda x: (x["priority_score"], x["expected_improvement"]), reverse=True)
            
            # Limit to top recommendations
            top_recommendations = recommendations[:settings.MAX_RECOMMENDATIONS]
            
            result = {
                "creator_id": data.get("creator_id", "unknown"),
                "analysis_timestamp": data.get("timestamp", "unknown"),
                "overall_score": kpi_analysis["overall_score"],
                "revenue_focus_score": kpi_analysis["revenue_focus_score"],
                "bottlenecks_identified": len(bottlenecks),
                "recommendations": top_recommendations,
                "insights": insights,
                "next_steps": self._generate_next_steps(top_recommendations)
            }
            
            self.logger.info(f"Generated {len(top_recommendations)} recommendations for creator {data.get('creator_id', 'unknown')}")
            return result
            
        except Exception as e:
            self.logger.error(f"Error generating recommendations: {e}")
            return {"error": str(e), "recommendations": []}
    
    def _identify_bottlenecks(self, kpi_analysis: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Identify performance bottlenecks using diagnostic model
        
        Args:
            kpi_analysis: KPI analysis results
            
        Returns:
            List of identified bottlenecks
        """
        bottlenecks = []
        
        # Check individual KPI scores
        for kpi_name, score in kpi_analysis["individual_scores"].items():
            if score < 0.3:  # Low performance threshold
                weight = settings.KPI_WEIGHTS.get(kpi_name, 0.0)
                impact = score * weight
                
                bottlenecks.append({
                    "kpi": kpi_name,
                    "score": score,
                    "weight": weight,
                    "impact": impact,
                    "severity": "high" if score < 0.2 else "medium"
                })
        
        # Check component-level bottlenecks
        for kpi_name, components in kpi_analysis["components"].items():
            for component_name, component_score in components.items():
                if isinstance(component_score, (int, float)) and component_score < 0.3:
                    bottlenecks.append({
                        "kpi": kpi_name,
                        "component": component_name,
                        "score": component_score,
                        "weight": settings.KPI_WEIGHTS.get(kpi_name, 0.0),
                        "impact": component_score * settings.KPI_WEIGHTS.get(kpi_name, 0.0),
                        "severity": "high" if component_score < 0.2 else "medium"
                    })
        
        # Sort by impact (score * weight)
        bottlenecks.sort(key=lambda x: x["impact"], reverse=True)
        
        return bottlenecks
    
    def _create_recommendation(self, bottleneck: Dict[str, Any], kpi_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a specific recommendation for a bottleneck
        
        Args:
            bottleneck: Bottleneck information
            kpi_analysis: KPI analysis results
            
        Returns:
            Recommendation dictionary
        """
        try:
            # Map bottleneck to recommendation template
            component = bottleneck.get("component", bottleneck["kpi"])
            template_key = self._map_component_to_template(component)
            
            if template_key not in self.recommendation_templates:
                return None
            
            template = self.recommendation_templates[template_key]
            
            # Calculate priority score
            priority_score = self._calculate_priority_score(bottleneck, template)
            
            # Calculate expected improvement
            expected_improvement = template["expected_improvement"] * (1 - bottleneck["score"])
            
            # Calculate confidence
            confidence = self._calculate_confidence(bottleneck, kpi_analysis)
            
            recommendation = {
                "id": f"rec_{bottleneck['kpi']}_{component}",
                "title": template["title"],
                "description": f"Improve {component} in {bottleneck['kpi']}",
                "priority_score": priority_score,
                "expected_improvement": expected_improvement,
                "confidence": confidence,
                "cost_level": template["cost"],
                "severity": bottleneck["severity"],
                "current_score": bottleneck["score"],
                "target_score": min(1.0, bottleneck["score"] + expected_improvement),
                "actions": template["actions"],
                "experiment": template["experiment"],
                "kpi_affected": bottleneck["kpi"],
                "component": component,
                "estimated_effort_hours": self._estimate_effort(template["cost"]),
                "success_metrics": self._get_success_metrics(bottleneck["kpi"])
            }
            
            return recommendation
            
        except Exception as e:
            self.logger.error(f"Error creating recommendation: {e}")
            return None
    
    def _map_component_to_template(self, component: str) -> str:
        """
        Map component name to recommendation template key
        """
        mapping = {
            "funnel_score": "funnel_score",
            "abandonment_score": "abandonment_score",
            "conversion_score": "conversion_score",
            "interaction_balance": "interaction_balance",
            "video_quality": "video_quality",
            "sales_performance_scorer": "conversion_score",
            "shop_conversion_scorer": "funnel_score",
            "engagement_scorer": "interaction_balance",
            "content_strategy_scorer": "video_quality"
        }
        
        return mapping.get(component, "video_quality")  # Default fallback
    
    def _calculate_priority_score(self, bottleneck: Dict[str, Any], template: Dict[str, Any]) -> float:
        """
        Calculate priority score for recommendation
        """
        # Base priority from template
        priority_map = {"high": 3.0, "medium": 2.0, "low": 1.0}
        base_priority = priority_map.get(template["priority"], 1.0)
        
        # Weight by KPI importance
        weight_factor = bottleneck["weight"] * 2.0
        
        # Weight by current performance (lower = higher priority)
        performance_factor = (1.0 - bottleneck["score"]) * 2.0
        
        # Weight by severity
        severity_factor = 2.0 if bottleneck["severity"] == "high" else 1.0
        
        return base_priority * weight_factor * performance_factor * severity_factor
    
    def _calculate_confidence(self, bottleneck: Dict[str, Any], kpi_analysis: Dict[str, Any]) -> float:
        """
        Calculate confidence in recommendation
        """
        # Base confidence from data quality
        base_confidence = 0.7
        
        # Adjust based on sample size (if available)
        sample_size = kpi_analysis.get("sample_size", 100)
        sample_factor = min(1.0, sample_size / 1000.0)
        
        # Adjust based on consistency
        consistency = kpi_analysis.get("consistency_score", 0.5)
        
        return min(0.95, base_confidence * sample_factor * (0.5 + consistency))
    
    def _estimate_effort(self, cost_level: str) -> int:
        """
        Estimate effort in hours
        """
        effort_map = {"low": 4, "medium": 12, "high": 24}
        return effort_map.get(cost_level, 8)
    
    def _get_success_metrics(self, kpi: str) -> List[str]:
        """
        Get success metrics for a KPI
        """
        metrics_map = {
            "sales_performance_scorer": ["conversion_rate", "total_revenue", "avg_order_value"],
            "shop_conversion_scorer": ["funnel_completion_rate", "cart_abandonment_rate"],
            "engagement_scorer": ["likes_ratio", "comments_ratio", "shares_ratio"],
            "content_strategy_scorer": ["video_quality", "content_freshness"]
        }
        
        return metrics_map.get(kpi, ["overall_score"])
    
    def _generate_next_steps(self, recommendations: List[Dict[str, Any]]) -> List[str]:
        """
        Generate next steps based on recommendations
        """
        if not recommendations:
            return ["No immediate actions required"]
        
        steps = [
            f"1. Implement '{recommendations[0]['title']}' (Priority: {recommendations[0]['priority_score']:.1f})",
            f"2. Set up A/B test: {recommendations[0]['experiment']['type']}",
            f"3. Monitor {recommendations[0]['success_metrics'][0]} for {recommendations[0]['experiment']['duration_days']} days"
        ]
        
        if len(recommendations) > 1:
            steps.append(f"4. Plan implementation of '{recommendations[1]['title']}'")
        
        return steps
