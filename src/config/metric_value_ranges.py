from typing import Dict, Tuple

SCORE_RANGES: Dict[str, Tuple[float, float]] = {
    "sales_performance": (0.0, 1.0),
    "shop_conversion": (0.0, 1.0),
    "tiktok_shop": (0.0, 1.0),
    "engagement": (0.0, 1.0),
    "engagement_growth": (0.0, 1.0),
    "discovery": (0.0, 1.0),
    "content_strategy": (0.0, 1.0),
    "audience_fit": (0.0, 1.0),
    "brand_fit": (0.0, 1.0),
    "trend_fit": (0.0, 1.0),
    "image_score": (0.0, 1.0),
    "reach_visibility": (0.0, 1.0),
    "cost_efficiency": (0.0, 1.0),
}

COMPONENT_RANGES: Dict[str, Tuple[float, float]] = {
    "conversion_score": (0.0, 1.0),
    "revenue_score": (0.0, 1.0),
    "aov_score": (0.0, 1.0),
    "funnel_score": (0.0, 1.0),
    "abandonment_score": (0.0, 1.0),
    "checkout_score": (0.0, 1.0),
    "listing_score": (0.0, 1.0),
    "velocity_score": (0.0, 1.0),
    "integration_score": (0.0, 1.0),
    "interaction_balance": (0.0, 1.0),
    "retention_score": (0.0, 1.0),
    "sharing_score": (0.0, 1.0),
    "video_quality": (0.0, 1.0),
    "content_freshness": (0.0, 1.0),
    "posting_consistency": (0.0, 1.0),
}

PERFORMANCE_THRESHOLDS = {
    "low": 0.3,
    "medium": 0.6,
    "high": 0.8
}

ACTION_COSTS = {
    "low_cost": 1.0,
    "medium_cost": 3.0,
    "high_cost": 5.0
}