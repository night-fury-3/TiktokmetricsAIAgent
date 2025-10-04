from typing import Dict, List
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "TikTok Metrics AI Agent"
    version: str = "1.0.0"
    debug: bool = False
    base_url: str
    api_host: str
    api_port: int
    
    KPI_WEIGHTS: Dict[str, float] = {
        "sales_performance_scorer": 0.30,
        "shop_conversion_scorer": 0.15,
        "tiktok_shop_scorer": 0.10,
        "engagement_scorer": 0.10,
        "engagement_growth_scorer": 0.05,
        "discovery_scorer": 0.04,
        "content_strategy_scorer": 0.06,
        "audience_fit_scorer": 0.04,
        "brand_fit_scorer": 0.03,
        "trend_fit_scorer": 0.04,
        "image_score_scorer": 0.03,
        "reach_visibility_scorer": 0.03,
        "cost_efficiency_scorer": 0.03,
    }
    
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
    
    REVENUE_KPIS: List[str] = [
        "sales_performance_scorer",
        "tiktok_shop_scorer",
        "shop_conversion_scorer"
    ]
    
    MODEL_RETRAIN_FREQUENCY_DAYS: int = 30
    MIN_SAMPLES_FOR_TRAINING: int = 100
    
    MAX_RECOMMENDATIONS: int = 3
    MIN_CONFIDENCE_THRESHOLD: float = 0.7
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()