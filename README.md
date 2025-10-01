# TikTok Metrics AI Agent

Professional demo implementation of KPI algorithm optimization and revenue optimization AI pipeline for TikTok creator content evaluation.

## Overview

This project implements two key solutions:

1. **Task 1: KPI Algorithm Optimization** - A multi-tier weighted algorithm that prioritizes e-commerce revenue drivers
2. **Task 2: Revenue Optimization AI Pipeline** - An end-to-end AI system for automated diagnosis and actionable recommendations

## Key Features

### Optimized KPI Algorithm
- **Multi-tier weighting system** prioritizing revenue drivers
- **Tier 1 (55% weight)**: Direct revenue drivers (Sales, Shop Conversion, TikTok Shop)
- **Tier 2 (32% weight)**: Revenue enablers (Engagement, Content Strategy, etc.)
- **Tier 3 (13% weight)**: General health metrics (Image, Reach, Cost Efficiency)

### AI Recommendation Pipeline
- **Automated diagnosis** of performance bottlenecks
- **Actionable recommendations** with A/B test configurations
- **Priority scoring** based on impact and feasibility
- **Revenue-focused insights** for creator optimization

## Project Structure

```
TikTokMetricsAIAgent/
├── app.py                          # FastAPI application
├── requirements.txt                # Dependencies
├── requirements-dev.txt           # Development dependencies
├── README.md                      # This file
├── src/
│   ├── config/
│   │   ├── config.py              # Configuration settings
│   │   └── metric_value_ranges.py # Metric ranges and thresholds
│   ├── logger/
│   │   └── logger.py              # Logging configuration
│   └── processors/
│       ├── kpi_orchestrator.py    # KPI calculation orchestrator
│       ├── recommendation_generator.py # AI recommendation engine
│       └── scorers/               # 13 KPI scoring modules
│           ├── base_scorer.py
│           ├── sales_performance_scorer.py
│           ├── shop_conversion_scorer.py
│           ├── tiktok_shop_scorer.py
│           ├── engagement_scorer.py
│           ├── engagement_growth_scorer.py
│                   ├── discovery_scorer.py
│                   ├── content_strategy_scorer.py
│                   ├── audience_fit_scorer.py
│                   ├── brand_fit_scorer.py
│                   ├── trend_fit_scorer.py
│                   ├── image_score_scorer.py
│                   ├── reach_visibility_scorer.py
│                   └── cost_efficiency_scorer.py
├── logs/                          # Application logs
├── models/                        # Model artifacts (if any)
└── processed/                     # Processed data storage
```

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd TikTokMetricsAIAgent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the API**
   - API Documentation: http://localhost:8000/docs
   - Main Interface: http://localhost:8000/
   - Health Check: http://localhost:8000/health

## API Usage

### Analyze Creator Metrics

```bash
curl -X POST "http://localhost:8000/analyze" \
     -H "Content-Type: application/json" \
     -d '{
       "creator_id": "creator_001",
       "conversion_rate": 0.05,
       "total_revenue": 5000.0,
       "avg_order_value": 45.0,
       "funnel_completion_rate": 0.3,
       "cart_abandonment_rate": 0.7,
       "video_quality": 0.3,
       "likes_ratio": 0.7,
       "comments_ratio": 0.15,
       "shares_ratio": 0.15
     }'
```

### Get Demo Data

```bash
curl -X GET "http://localhost:8000/demo-data"
```

### Compare Algorithms

```bash
curl -X POST "http://localhost:8000/compare-algorithms" \
     -H "Content-Type: application/json" \
     -d '{
       "creator_id": "creator_001",
       "conversion_rate": 0.05,
       "total_revenue": 5000.0
     }'
```

## Algorithm Details

### Weight Distribution

| Tier | KPI | Weight | Rationale |
|------|-----|--------|-----------|
| **Tier 1** | Sales Performance | 30% | Direct revenue measurement |
| | Shop Conversion | 15% | Funnel optimization |
| | TikTok Shop | 10% | Platform integration |
| **Tier 2** | Engagement | 10% | Revenue precursor |
| | Content Strategy | 6% | Content quality |
| | Engagement Growth | 5% | Growth potential |
| | Discovery | 4% | Audience reach |
| | Audience Fit | 4% | Target alignment |
| | Brand Fit | 3% | Trust and authenticity |
| **Tier 3** | Trend Fit | 4% | General health |
| | Image Score | 3% | Visual quality |
| | Reach Visibility | 3% | Broad reach |
| | Cost Efficiency | 3% | ROI optimization |

### Recommendation Types

1. **Funnel Optimization** - Improve conversion rates
2. **Engagement Balance** - Enhance user interaction
3. **Video Quality** - Upgrade content production
4. **Sales Conversion** - Boost revenue generation
5. **Cart Abandonment** - Reduce drop-off rates

## Business Impact

### Revenue Alignment
- **55% weight** on direct revenue drivers vs. 23% in equal weighting
- **2.4x higher** priority for sales performance metrics
- **Clear intervention guidance** for revenue optimization

### Actionable Insights
- **Automated bottleneck identification** using diagnostic model
- **Prioritized recommendations** with expected impact
- **A/B test configurations** for validation
- **ROI-focused** improvement strategies

## Development

### Running Tests
```bash
pip install -r requirements-dev.txt
pytest
```

### Code Quality
```bash
black src/
flake8 src/
mypy src/
```

## Architecture Decisions

### Lightweight Implementation
- **No heavy ML frameworks** - Uses scikit-learn for basic operations
- **FastAPI** for high-performance API
- **Modular design** for easy extension
- **Configuration-driven** weights and thresholds

### Scalability Considerations
- **Stateless design** for horizontal scaling
- **Caching-ready** architecture
- **Database-agnostic** data models
- **Microservice-ready** component separation

## License

This is a demo project for algorithmic optimization and AI pipeline implementation.

## Contact

For questions about the implementation or algorithm design, please refer to the code documentation and API endpoints.
