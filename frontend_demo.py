"""
Frontend Demo Script for TikTok Metrics AI Agent
"""

import requests
import webbrowser
import time
from datetime import datetime


def test_frontend_integration():
    """Test the frontend integration and open dashboard"""
    print("🚀 TikTok Metrics AI Agent - Frontend Integration Demo")
    print("=" * 60)
    
    base_url = "http://localhost:8000"
    
    # Test API health
    print("\n1. Testing API Health...")
    try:
        response = requests.get(f"{base_url}/health")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ API Status: {data['status']}")
            print(f"   Service: {data['service']}")
            print(f"   Version: {data['data']['version']}")
        else:
            print("❌ API Health check failed")
            return
    except Exception as e:
        print(f"❌ API Health check failed: {e}")
        return
    
    # Test dashboard endpoint
    print("\n2. Testing Dashboard Endpoint...")
    try:
        response = requests.get(f"{base_url}/")
        if response.status_code == 200:
            print("✅ Dashboard endpoint accessible")
            print(f"   Content-Type: {response.headers.get('content-type', 'unknown')}")
            print(f"   Content Length: {len(response.content)} bytes")
        else:
            print("❌ Dashboard endpoint failed")
            return
    except Exception as e:
        print(f"❌ Dashboard endpoint failed: {e}")
        return
    
    # Test static files
    print("\n3. Testing Static Files...")
    static_files = [
        "/static/css/dashboard.css",
        "/static/js/dashboard.js"
    ]
    
    for file_path in static_files:
        try:
            response = requests.get(f"{base_url}{file_path}")
            if response.status_code == 200:
                print(f"✅ {file_path} - {len(response.content)} bytes")
            else:
                print(f"❌ {file_path} - Status: {response.status_code}")
        except Exception as e:
            print(f"❌ {file_path} - Error: {e}")
    
    # Test API endpoints
    print("\n4. Testing API Endpoints...")
    
    # Test demo data endpoint
    try:
        response = requests.get(f"{base_url}/demo-data")
        if response.status_code == 200:
            data = response.json()
            print("✅ Demo data endpoint working")
            print(f"   Creator ID: {data['demo_data']['creator_id']}")
        else:
            print("❌ Demo data endpoint failed")
    except Exception as e:
        print(f"❌ Demo data endpoint failed: {e}")
    
    # Test analysis endpoint
    try:
        demo_data = {
            "creator_id": "frontend_test",
            "conversion_rate": 0.08,
            "total_revenue": 8000,
            "video_quality": 0.2,
            "cart_abandonment_rate": 0.5
        }
        
        response = requests.post(f"{base_url}/analyze", json=demo_data)
        if response.status_code == 200:
            data = response.json()
            print("✅ Analysis endpoint working")
            print(f"   Overall Score: {data['overall_score']:.3f}")
            print(f"   Recommendations: {len(data['recommendations'])}")
        else:
            print("❌ Analysis endpoint failed")
    except Exception as e:
        print(f"❌ Analysis endpoint failed: {e}")
    
    # Test weights endpoint
    try:
        response = requests.get(f"{base_url}/weights")
        if response.status_code == 200:
            data = response.json()
            print("✅ Weights endpoint working")
            print(f"   Tier 1 Weight: {data['tier_breakdown']['tier_1']['total_weight']:.1%}")
        else:
            print("❌ Weights endpoint failed")
    except Exception as e:
        print(f"❌ Weights endpoint failed: {e}")
    
    # Open dashboard in browser
    print("\n5. Opening Dashboard in Browser...")
    try:
        dashboard_url = f"{base_url}/"
        print(f"🌐 Dashboard URL: {dashboard_url}")
        print("   Opening in default browser...")
        
        # Try to open in browser
        webbrowser.open(dashboard_url)
        print("✅ Dashboard opened in browser")
        
        print("\n📋 Frontend Features Available:")
        print("   • Interactive form for creator metrics input")
        print("   • Real-time API health indicator")
        print("   • Algorithm overview with tier breakdown")
        print("   • Live analysis results with visualizations")
        print("   • AI recommendations with priority scoring")
        print("   • Algorithm comparison functionality")
        print("   • Responsive design for all devices")
        
    except Exception as e:
        print(f"❌ Could not open browser: {e}")
        print(f"   Please manually open: {dashboard_url}")
    
    print("\n🎉 Frontend Integration Demo Completed!")
    print("\nNext Steps:")
    print("1. Open the dashboard in your browser")
    print("2. Click 'Load Demo Data' to populate the form")
    print("3. Click 'Analyze Creator' to see the results")
    print("4. Try 'Compare Algorithms' to see the improvement")
    print("5. Explore the interactive visualizations")


def show_frontend_features():
    """Display frontend features and capabilities"""
    print("\n🎨 Frontend Features Overview")
    print("=" * 40)
    
    features = [
        {
            "name": "Interactive Dashboard",
            "description": "Modern, responsive web interface with real-time updates",
            "url": "http://localhost:8000/"
        },
        {
            "name": "Creator Metrics Form",
            "description": "Comprehensive input form for all 13 KPI metrics",
            "features": ["Tiered organization", "Real-time validation", "Demo data loading"]
        },
        {
            "name": "Algorithm Visualization",
            "description": "Visual representation of the 3-tier weighting system",
            "features": ["Tier 1: Revenue Drivers (55%)", "Tier 2: Revenue Enablers (32%)", "Tier 3: General Health (13%)"]
        },
        {
            "name": "Real-time Analysis",
            "description": "Live KPI scoring and performance analysis",
            "features": ["Overall score visualization", "Individual KPI breakdown", "Performance level indicators"]
        },
        {
            "name": "AI Recommendations",
            "description": "Actionable insights with priority scoring",
            "features": ["Priority-based ranking", "Expected improvement metrics", "A/B test configurations"]
        },
        {
            "name": "Algorithm Comparison",
            "description": "Side-by-side comparison of old vs new algorithms",
            "features": ["Performance improvement metrics", "Business impact analysis"]
        },
        {
            "name": "API Documentation",
            "description": "Interactive Swagger UI for API exploration",
            "url": "http://localhost:8000/docs"
        }
    ]
    
    for i, feature in enumerate(features, 1):
        print(f"\n{i}. {feature['name']}")
        print(f"   {feature['description']}")
        
        if 'features' in feature:
            for sub_feature in feature['features']:
                print(f"   • {sub_feature}")
        
        if 'url' in feature:
            print(f"   🔗 {feature['url']}")


if __name__ == "__main__":
    test_frontend_integration()
    show_frontend_features()
