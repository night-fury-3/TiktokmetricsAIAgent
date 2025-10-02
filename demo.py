"""
TikTok Metrics AI Agent - Demo Script
Comprehensive demonstration of Task 1 and Task 2 functionality
"""

import requests
import json
import time
from datetime import datetime
import os
from src.config.config import settings

def check_api_health(base_url=None):
    """Check if the API is running and healthy"""
    base_url = base_url or settings.base_url
    try:
        response = requests.get(f"{base_url}/health", timeout=5)
        if response.status_code == 200:
            data = response.json()
            return True, data
        else:
            return False, f"API returned status {response.status_code}"
    except requests.exceptions.RequestException as e:
        return False, f"Connection error: {e}"

def get_demo_data(base_url=None):
    """Get demo data from the API"""
    base_url = base_url or settings.base_url
    try:
        response = requests.get(f"{base_url}/demo-data", timeout=10)
        if response.status_code == 200:
            return True, response.json()
        else:
            return False, f"API returned status {response.status_code}"
    except requests.exceptions.RequestException as e:
        return False, f"Connection error: {e}"

def test_creator_analysis(base_url=None):
    """Test creator analysis with recommendations"""
    base_url = base_url or settings.base_url
    
    # Demo creator data
    demo_data = {
        "creator_id": "demo_creator_001",
        "conversion_rate": 0.05,
        "total_revenue": 5000.0,
        "avg_order_value": 45.0,
        "funnel_completion_rate": 0.3,
        "cart_abandonment_rate": 0.7,
        "video_quality": 0.3,
        "likes_ratio": 0.7,
        "comments_ratio": 0.15,
        "shares_ratio": 0.15,
        "retention_rate": 0.6,
        "engagement_growth_rate": 0.1,
        "hashtag_performance": 0.5,
        "content_freshness": 0.4,
        "posting_consistency": 0.6,
        "target_demographic_match": 0.5,
        "audience_engagement_quality": 0.6,
        "brand_alignment": 0.7,
        "trust_score": 0.6,
        "trend_alignment": 0.4,
        "image_quality": 0.3,
        "total_reach": 8000,
        "cost_per_acquisition": 100,
        "roi_score": 0.7
    }
    
    try:
        response = requests.post(f"{base_url}/analyze", json=demo_data, timeout=15)
        if response.status_code == 200:
            return True, response.json()
        else:
            return False, f"API returned status {response.status_code}"
    except requests.exceptions.RequestException as e:
        return False, f"Connection error: {e}"

def test_algorithm_comparison(base_url=None):
    """Test algorithm comparison functionality"""
    base_url = base_url or settings.base_url
    
    comparison_data = {
        "creator_id": "comparison_test",
        "conversion_rate": 0.05,
        "total_revenue": 5000.0,
        "avg_order_value": 45.0,
        "funnel_completion_rate": 0.3,
        "cart_abandonment_rate": 0.7,
        "video_quality": 0.3,
        "likes_ratio": 0.7,
        "comments_ratio": 0.15,
        "shares_ratio": 0.15,
        "retention_rate": 0.6,
        "engagement_growth_rate": 0.1,
        "hashtag_performance": 0.5,
        "content_freshness": 0.4,
        "posting_consistency": 0.6,
        "target_demographic_match": 0.5,
        "audience_engagement_quality": 0.6,
        "brand_alignment": 0.7,
        "trust_score": 0.6,
        "trend_alignment": 0.4,
        "image_quality": 0.3,
        "total_reach": 8000,
        "cost_per_acquisition": 100,
        "roi_score": 0.7
    }
    
    try:
        response = requests.post(f"{base_url}/compare-algorithms", json=comparison_data, timeout=15)
        if response.status_code == 200:
            return True, response.json()
        else:
            return False, f"API returned status {response.status_code}"
    except requests.exceptions.RequestException as e:
        return False, f"Connection error: {e}"

def test_weights_configuration(base_url=None):
    """Test weights configuration endpoint"""
    base_url = base_url or settings.base_url
    try:
        response = requests.get(f"{base_url}/weights/api", timeout=10)
        if response.status_code == 200:
            return True, response.json()
        else:
            return False, f"API returned status {response.status_code}"
    except requests.exceptions.RequestException as e:
        return False, f"Connection error: {e}"

def main():
    """Main demo function"""
    print("�� TikTok Metrics AI Agent - Demo")
    print("=" * 50)
    print()
    
    base_url = settings.base_url
    print(f"Using base URL: {base_url}")
    print()
    
    # Test 1: Health Check
    print("1. Testing Health Check...")
    success, result = check_api_health(base_url)
    if success:
        print("✅ Health check passed")
        print(f"   Service: {result.get('service', 'Unknown')}")
        print(f"   Version: {result.get('version', 'Unknown')}")
    else:
        print(f"❌ Health check failed: {result}")
        print("   Please ensure the API is running with: python app.py")
        return
    print()
    
    # Test 2: Demo Data
    print("2. Getting Demo Data...")
    success, result = get_demo_data(base_url)
    if success:
        print("✅ Demo data retrieved")
        print(f"   Creator ID: {result.get('creator_id', 'Unknown')}")
        print(f"   Conversion Rate: {result.get('conversion_rate', 0):.1%}")
        print(f"   Total Revenue: ${result.get('total_revenue', 0):,}")
    else:
        print(f"❌ Demo data failed: {result}")
    print()
    
    # Test 3: Creator Analysis
    print("3. Testing Creator Analysis...")
    success, result = test_creator_analysis(base_url)
    if success:
        print("✅ Analysis completed")
        print(f"   Overall Score: {result.get('overall_score', 0):.3f}")
        print(f"   Revenue Focus Score: {result.get('revenue_focus_score', 0):.3f}")
        print(f"   Recommendations: {len(result.get('recommendations', []))}")
        
        # Display top recommendations
        recommendations = result.get('recommendations', [])
        if recommendations:
            print("\n   Top Recommendations:")
            for i, rec in enumerate(recommendations[:3], 1):
                print(f"   {i}. {rec.get('title', 'Unknown')} (Priority: {rec.get('priority_score', 0):.1f})")
                print(f"      Expected Improvement: {rec.get('expected_improvement', 0):.1%}")
                actions = rec.get('actions', [])
                if actions:
                    print(f"      Actions: {', '.join(actions[:2])}...")
    else:
        print(f"❌ Analysis failed: {result}")
    print()
    
    # Test 4: Algorithm Comparison
    print("4. Testing Algorithm Comparison...")
    success, result = test_algorithm_comparison(base_url)
    if success:
        print("✅ Algorithm comparison completed")
        print(f"   New Weighted Score: {result.get('new_weighted_score', 0):.3f}")
        print(f"   Equal Weighted Score: {result.get('equal_weighted_score', 0):.3f}")
        print(f"   Improvement: {result.get('percentage_change', 0):+.1f}%")
    else:
        print(f"❌ Algorithm comparison failed: {result}")
    print()
    
    # Test 5: Weights Configuration
    print("5. Testing Weights Configuration...")
    success, result = test_weights_configuration(base_url)
    if success:
        print("✅ Weights configuration retrieved")
        total_weight = sum(result["weights"].values())
        print(f"   Total Weight: {total_weight:.3f}")
        print("   Number of KPIs: {}".format(len(result["weights"])))
    else:
        print(f"❌ Weights configuration failed: {result}")
    print()
    
    print("🎉 Demo completed successfully!")
    print()
    print("Next steps:")
    print("- Visit {}/docs for interactive API documentation".format(base_url))
    print("- Use the /analyze endpoint with your own creator data")
    print("- Explore the recommendation engine for actionable insights")

if __name__ == "__main__":
    main()
