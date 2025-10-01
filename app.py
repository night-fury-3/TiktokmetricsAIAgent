"""
FastAPI Application for TikTok Metrics AI Agent
"""

from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Dict, Any, List, Optional
import uvicorn
from datetime import datetime
import json
import os

from src.config.config import settings
from src.logger.logger import logger
from src.processors.kpi_orchestrator import KPIOrchestrator
from src.processors.recommendation_generator import RecommendationGenerator


# Initialize FastAPI app
app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    description="Professional demo implementation of KPI algorithm optimization and revenue optimization AI pipeline"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize components
kpi_orchestrator = KPIOrchestrator()
recommendation_generator = RecommendationGenerator()


# Pydantic models
class CreatorMetrics(BaseModel):
    """Creator metrics input model"""
    creator_id: str
    timestamp: Optional[str] = None
    
    # Sales Performance Metrics
    conversion_rate: Optional[float] = 0.0
    total_revenue: Optional[float] = 0.0
    avg_order_value: Optional[float] = 0.0
    target_revenue: Optional[float] = 10000.0
    target_aov: Optional[float] = 50.0
    
    # Shop Conversion Metrics
    funnel_completion_rate: Optional[float] = 0.0
    cart_abandonment_rate: Optional[float] = 1.0
    checkout_success_rate: Optional[float] = 0.0
    
    # TikTok Shop Metrics
    listing_quality: Optional[float] = 0.0
    product_velocity: Optional[float] = 0.0
    integration_seamlessness: Optional[float] = 0.0
    
    # Engagement Metrics
    likes_ratio: Optional[float] = 0.0
    comments_ratio: Optional[float] = 0.0
    shares_ratio: Optional[float] = 0.0
    retention_rate: Optional[float] = 0.0
    avg_watch_time: Optional[float] = 0.0
    video_duration: Optional[float] = 30.0
    
    # Growth Metrics
    engagement_growth_rate: Optional[float] = 0.0
    follower_growth_rate: Optional[float] = 0.0
    views_growth_rate: Optional[float] = 0.0
    
    # Discovery Metrics
    hashtag_performance: Optional[float] = 0.0
    search_visibility: Optional[float] = 0.0
    recommendation_rate: Optional[float] = 0.0
    viral_potential: Optional[float] = 0.0
    
    # Content Strategy Metrics
    video_quality: Optional[float] = 0.0
    content_freshness: Optional[float] = 0.0
    posting_consistency: Optional[float] = 0.0
    content_diversity: Optional[float] = 0.0
    
    # Audience Fit Metrics
    target_demographic_match: Optional[float] = 0.0
    audience_engagement_quality: Optional[float] = 0.0
    follower_quality_score: Optional[float] = 0.0
    audience_retention: Optional[float] = 0.0
    
    # Brand Fit Metrics
    brand_alignment: Optional[float] = 0.0
    trust_score: Optional[float] = 0.0
    authenticity_score: Optional[float] = 0.0
    brand_consistency: Optional[float] = 0.0
    
    # Trend Fit Metrics
    trend_alignment: Optional[float] = 0.0
    timing_score: Optional[float] = 0.0
    trend_relevance: Optional[float] = 0.0
    
    # Image Quality Metrics
    image_quality: Optional[float] = 0.0
    lighting_score: Optional[float] = 0.0
    composition_score: Optional[float] = 0.0
    color_balance: Optional[float] = 0.0
    
    # Reach Metrics
    total_reach: Optional[float] = 0.0
    unique_viewers: Optional[float] = 0.0
    impression_rate: Optional[float] = 0.0
    visibility_score: Optional[float] = 0.0
    target_reach: Optional[float] = 10000.0
    
    # Cost Efficiency Metrics
    cost_per_acquisition: Optional[float] = 100.0
    cost_per_engagement: Optional[float] = 1.0
    cost_per_view: Optional[float] = 0.1
    roi_score: Optional[float] = 0.0
    target_cpa: Optional[float] = 50.0
    target_cpe: Optional[float] = 0.5
    target_cpv: Optional[float] = 0.05


class AnalysisResponse(BaseModel):
    """Analysis response model"""
    success: bool
    creator_id: str
    overall_score: float
    revenue_focus_score: float
    tier_breakdown: Dict[str, Any]
    individual_scores: Dict[str, float]
    performance_levels: Dict[str, str]
    recommendations: List[Dict[str, Any]]
    insights: Dict[str, Any]
    timestamp: str


# API Endpoints
@app.get("/", response_class=HTMLResponse)
async def dashboard():
    """Serve the interactive dashboard"""
    return FileResponse("templates/dashboard.html")


@app.get("/api", response_class=HTMLResponse)
async def api_docs():
    """API documentation page"""
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>TikTok Metrics AI Agent - API Documentation</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            .header { color: #2c3e50; }
            .section { margin: 20px 0; }
            .endpoint { background: #f8f9fa; padding: 10px; margin: 10px 0; border-radius: 5px; }
            .method { color: #27ae60; font-weight: bold; }
        </style>
    </head>
    <body>
        <h1 class="header">TikTok Metrics AI Agent - API Documentation</h1>
        <p>Professional demo implementation of KPI algorithm optimization and revenue optimization AI pipeline</p>
        
        <div class="section">
            <h2>API Endpoints</h2>
            
            <div class="endpoint">
                <span class="method">POST</span> /analyze - Analyze creator metrics and generate recommendations
            </div>
            
            <div class="endpoint">
                <span class="method">GET</span> /health - Health check endpoint
            </div>
            
            <div class="endpoint">
                <span class="method">GET</span> /weights - Get current KPI weights configuration
            </div>
            
            <div class="endpoint">
                <span class="method">GET</span> /docs - Interactive API documentation
            </div>
        </div>
        
        <div class="section">
            <h2>Key Features</h2>
            <ul>
                <li><strong>Optimized KPI Algorithm:</strong> Multi-tier weighting system prioritizing revenue drivers</li>
                <li><strong>AI Recommendation Pipeline:</strong> Automated diagnosis and actionable recommendations</li>
                <li><strong>Revenue Focus:</strong> 55% weight on direct revenue drivers (Tier 1)</li>
                <li><strong>Performance Analysis:</strong> Detailed breakdown by tiers and components</li>
            </ul>
        </div>
        
        <div class="section">
            <h2>Algorithm Weights</h2>
            <p><strong>Tier 1 (Direct Revenue Drivers - 55%):</strong></p>
            <ul>
                <li>Sales Performance: 30%</li>
                <li>Shop Conversion: 15%</li>
                <li>TikTok Shop: 10%</li>
            </ul>
            
            <p><strong>Tier 2 (Revenue Enablers - 32%):</strong></p>
            <ul>
                <li>Engagement: 10%</li>
                <li>Content Strategy: 6%</li>
                <li>Engagement Growth: 5%</li>
                <li>Discovery: 4%</li>
                <li>Audience Fit: 4%</li>
                <li>Brand Fit: 3%</li>
            </ul>
            
            <p><strong>Tier 3 (General Health - 13%):</strong></p>
            <ul>
                <li>Trend Fit: 4%</li>
                <li>Image Score: 3%</li>
                <li>Reach Visibility: 3%</li>
                <li>Cost Efficiency: 3%</li>
            </ul>
        </div>
        
        <div class="section">
            <h2>Quick Links</h2>
            <p>
                <a href="/">📊 Interactive Dashboard</a> | 
                <a href="/docs">📚 Swagger UI</a> | 
                <a href="/health">❤️ Health Check</a>
            </p>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": settings.app_name,
        "version": settings.version,
        "timestamp": datetime.now().isoformat()
    }


@app.get("/weights")
async def get_weights():
    """Get current KPI weights configuration"""
    return {
        "weights": settings.KPI_WEIGHTS,
        "tier_breakdown": {
            "tier_1": {
                "kpis": settings.TIER_1_KPIS,
                "total_weight": sum(settings.KPI_WEIGHTS[kpi] for kpi in settings.TIER_1_KPIS)
            },
            "tier_2": {
                "kpis": settings.TIER_2_KPIS,
                "total_weight": sum(settings.KPI_WEIGHTS[kpi] for kpi in settings.TIER_2_KPIS)
            },
            "tier_3": {
                "kpis": settings.TIER_3_KPIS,
                "total_weight": sum(settings.KPI_WEIGHTS[kpi] for kpi in settings.TIER_3_KPIS)
            }
        },
        "algorithm_description": "Multi-tier weighted algorithm prioritizing e-commerce revenue"
    }


@app.post("/analyze", response_model=AnalysisResponse)
async def analyze_creator_metrics(metrics: CreatorMetrics):
    """
    Analyze creator metrics and generate recommendations
    
    This endpoint implements the optimized KPI algorithm and AI recommendation pipeline
    """
    try:
        # Convert Pydantic model to dictionary
        data = metrics.dict()
        
        # Add timestamp if not provided
        if not data.get("timestamp"):
            data["timestamp"] = datetime.now().isoformat()
        
        # Calculate overall score using optimized algorithm
        kpi_analysis = kpi_orchestrator.calculate_overall_score(data)
        
        # Generate recommendations using AI pipeline
        recommendations = recommendation_generator.generate_recommendations(data)
        
        # Prepare response
        response = AnalysisResponse(
            success=True,
            creator_id=metrics.creator_id,
            overall_score=kpi_analysis["overall_score"],
            revenue_focus_score=kpi_analysis["revenue_focus_score"],
            tier_breakdown=kpi_analysis["tier_breakdown"],
            individual_scores=kpi_analysis["individual_scores"],
            performance_levels=kpi_analysis["performance_levels"],
            recommendations=recommendations.get("recommendations", []),
            insights=recommendations.get("insights", {}),
            timestamp=data["timestamp"]
        )
        
        logger.info(f"Analysis completed for creator {metrics.creator_id}")
        return response
        
    except Exception as e:
        logger.error(f"Error analyzing creator metrics: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/compare-algorithms")
async def compare_algorithms(metrics: CreatorMetrics):
    """
    Compare the new optimized algorithm with the old equal weighting approach
    """
    try:
        data = metrics.dict()
        comparison = kpi_orchestrator.compare_with_equal_weighting(data)
        
        return {
            "success": True,
            "creator_id": metrics.creator_id,
            "comparison": comparison,
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        logger.error(f"Error comparing algorithms: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/demo-data")
async def get_demo_data():
    """
    Get sample data for testing the API
    """
    demo_data = {
        "creator_id": "demo_creator_001",
        "timestamp": datetime.now().isoformat(),
        
        # Sales Performance (Tier 1)
        "conversion_rate": 0.05,  # 5%
        "total_revenue": 5000.0,
        "avg_order_value": 45.0,
        
        # Shop Conversion (Tier 1)
        "funnel_completion_rate": 0.3,
        "cart_abandonment_rate": 0.7,  # High abandonment
        "checkout_success_rate": 0.8,
        
        # TikTok Shop (Tier 1)
        "listing_quality": 0.6,
        "product_velocity": 0.4,
        "integration_seamlessness": 0.7,
        
        # Engagement (Tier 2)
        "likes_ratio": 0.7,
        "comments_ratio": 0.15,
        "shares_ratio": 0.15,
        "retention_rate": 0.6,
        "avg_watch_time": 20.0,
        "video_duration": 30.0,
        
        # Growth (Tier 2)
        "engagement_growth_rate": 0.1,
        "follower_growth_rate": 0.05,
        "views_growth_rate": 0.15,
        
        # Discovery (Tier 2)
        "hashtag_performance": 0.4,
        "search_visibility": 0.3,
        "recommendation_rate": 0.02,
        "viral_potential": 0.5,
        
        # Content Strategy (Tier 2)
        "video_quality": 0.3,  # Low quality
        "content_freshness": 0.6,
        "posting_consistency": 0.7,
        "content_diversity": 0.5,
        
        # Audience Fit (Tier 2)
        "target_demographic_match": 0.6,
        "audience_engagement_quality": 0.5,
        "follower_quality_score": 0.4,
        "audience_retention": 0.6,
        
        # Brand Fit (Tier 2)
        "brand_alignment": 0.7,
        "trust_score": 0.6,
        "authenticity_score": 0.8,
        "brand_consistency": 0.5,
        
        # Trend Fit (Tier 3)
        "trend_alignment": 0.4,
        "timing_score": 0.5,
        "trend_relevance": 0.6,
        
        # Image Quality (Tier 3)
        "image_quality": 0.3,  # Low quality
        "lighting_score": 0.4,
        "composition_score": 0.5,
        "color_balance": 0.6,
        
        # Reach (Tier 3)
        "total_reach": 5000.0,
        "unique_viewers": 4000.0,
        "impression_rate": 0.03,
        "visibility_score": 0.5,
        
        # Cost Efficiency (Tier 3)
        "cost_per_acquisition": 80.0,
        "cost_per_engagement": 0.8,
        "cost_per_view": 0.08,
        "roi_score": 1.2
    }
    
    return {
        "success": True,
        "demo_data": demo_data,
        "description": "Sample creator data with various performance levels for testing"
    }


if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
