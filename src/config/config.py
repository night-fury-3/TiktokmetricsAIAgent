"""
Configuration settings for TikTok Metrics AI Agent
"""

from typing import Dict, List
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings"""
    
    # API Settings
    app_name: str = "TikTok Metrics AI Agent"
    version: str = "1.0.0"
    debug: bool = False
    
    # KPI Weights Configuration (Task 1 - Optimized Weights)
    KPI_WEIGHTS: Dict[str, float] = {
        # Tier 1: Direct Revenue Drivers (55% total)
        "sales_performance_scorer": 0.30,
        "shop_conversion_scorer": 0.15,
        "tiktok_shop_scorer": 0.10,
        
        # Tier 2: Revenue Enablers (32% total)
        "engagement_scorer": 0.10,
        "engagement_growth_scorer": 0.05,
        "discovery_scorer": 0.04,
        "content_strategy_scorer": 0.06,
        "audience_fit_scorer": 0.04,
        "brand_fit_scorer": 0.03,
        
        # Tier 3: General Health/Cost/Reach (13% total)
        "trend_fit_scorer": 0.04,
        "image_score_scorer": 0.03,
        "reach_visibility_scorer": 0.03,
        "cost_efficiency_scorer": 0.03,
    }
    
    # KPI Categories for analysis
    TIER_1_KPIS: List[str] = [
        "sales_performance_scorer",
        "shop_conversion_scorer", 
        "tiktok_shop_scorer"
    ]
    
    TIER_2_KPIS: List[str] = [
        "engagement_scorer",
        "engagement_growth_scorer",
        "discovery_scorer",
        "content_strategy_scorer",
        "audience_fit_scorer",
        "brand_fit_scorer"
    ]
    
    TIER_3_KPIS: List[str] = [
        "trend_fit_scorer",
        "image_score_scorer",
        "reach_visibility_scorer",
        "cost_efficiency_scorer"
    ]
    
    # Revenue-focused KPIs for diagnostic model
    REVENUE_KPIS: List[str] = [
        "sales_performance_scorer",
        "tiktok_shop_scorer",
        "shop_conversion_scorer"
    ]
    
    # Model Configuration
    MODEL_RETRAIN_FREQUENCY_DAYS: int = 30
    MIN_SAMPLES_FOR_TRAINING: int = 100
    
    # Recommendation Engine Configuration
    MAX_RECOMMENDATIONS: int = 3
    MIN_CONFIDENCE_THRESHOLD: float = 0.7
    
    class Config:
        env_file = ".env"


# Global settings instance
settings = Settings()
