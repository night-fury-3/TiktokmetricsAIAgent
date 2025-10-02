"""
TikTok Metrics AI Agent - Production App
FastAPI application for TikTok content analysis and revenue optimization
"""

import os
import uvicorn
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from src.config.config import settings

# Initialize FastAPI app
app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    description="AI-powered TikTok content analysis and revenue optimization platform"
)

# Setup templates and static files
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Import processors
from src.processors.kpi_orchestrator import KPIOrchestrator
from src.processors.recommendation_generator import RecommendationGenerator

# Initialize processors
kpi_orchestrator = KPIOrchestrator()
recommendation_generator = RecommendationGenerator()

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    """Main dashboard interface"""
    return templates.TemplateResponse("dashboard.html", {"request": request, "base_url": settings.base_url})

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard_alt(request: Request):
    """Alternative dashboard route"""
    return templates.TemplateResponse("dashboard.html", {"request": request, "base_url": settings.base_url})

@app.get("/weights", response_class=HTMLResponse)
async def weights_page(request: Request):
    """Weights visualization page"""
    return templates.TemplateResponse("weights_visualization.html", {"request": request, "base_url": settings.base_url})

@app.get("/weights/api", response_class=HTMLResponse)
async def weights_api():
    """API endpoint for weights data"""
    try:
        weights_data = kpi_orchestrator.get_weights_data()
        return weights_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving weights: {str(e)}")

@app.get("/test-weights", response_class=HTMLResponse)
async def test_weights(request: Request):
    """Test page for weights API"""
    return templates.TemplateResponse("test_weights.html", {"request": request, "base_url": settings.base_url})

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": settings.app_name,
        "version": settings.version
    }

@app.post("/analyze")
async def analyze_creator(data: dict):
    """Analyze creator performance and generate recommendations"""
    try:
        # Extract creator data
        creator_id = data.get("creator_id", "unknown")
        kpi_scores = data.get("kpi_scores", {})
        
        # Generate analysis
        analysis_result = kpi_orchestrator.analyze_creator(creator_id, kpi_scores)
        
        # Generate recommendations
        recommendations = recommendation_generator.generate_recommendations(analysis_result)
        
        return {
            "creator_id": creator_id,
            "analysis": analysis_result,
            "recommendations": recommendations,
            "status": "success"
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

@app.post("/compare-algorithms")
async def compare_algorithms(data: dict):
    """Compare new weighted algorithm vs equal weighting"""
    try:
        creator_id = data.get("creator_id", "unknown")
        kpi_scores = data.get("kpi_scores", {})
        
        comparison_result = kpi_orchestrator.compare_algorithms(creator_id, kpi_scores)
        
        return {
            "creator_id": creator_id,
            "comparison": comparison_result,
            "status": "success"
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Algorithm comparison failed: {str(e)}")

@app.get("/demo-data")
async def get_demo_data():
    """Get demo data for testing"""
    return {
        "creator_id": "demo_creator_001",
        "kpi_scores": {
            "sales_performance_scorer": 0.75,
            "shop_conversion_scorer": 0.60,
            "tiktok_shop_scorer": 0.80,
            "engagement_scorer": 0.70,
            "engagement_growth_scorer": 0.65,
            "discovery_scorer": 0.55,
            "content_strategy_scorer": 0.72,
            "audience_fit_scorer": 0.68,
            "brand_fit_scorer": 0.63,
            "trend_fit_scorer": 0.58,
            "image_score_scorer": 0.77,
            "reach_visibility_scorer": 0.62,
            "cost_efficiency_scorer": 0.69
        },
        "metadata": {
            "total_videos": 150,
            "total_revenue": 2500.00,
            "conversion_rate": 0.035,
            "avg_engagement_rate": 0.082
        }
    }

if __name__ == "__main__":
    # Production configuration
    port = int(os.environ.get("PORT", settings.api_port))
    uvicorn.run(
        "app:app",
        host=settings.api_host,
        port=port,
        reload=False,  # Disable reload in production
        log_level="info"
    )
