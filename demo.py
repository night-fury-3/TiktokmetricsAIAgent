"""
Demo script for TikTok Metrics AI Agent
"""

import requests
import json
from datetime import datetime


def test_api():
    """Test the API endpoints"""
    base_url = "http://localhost:8000"
    
    print("🚀 TikTok Metrics AI Agent - Demo")
    print("=" * 50)
    
    # Test health check
    print("\n1. Testing Health Check...")
    try:
        response = requests.get(f"{base_url}/health")
        if response.status_code == 200:
            print("✅ Health check passed")
            print(f"   Service: {response.json()['service']}")
            print(f"   Version: {response.json()['version']}")
        else:
            print("❌ Health check failed")
            return
    except Exception as e:
        print(f"❌ Health check failed: {e}")
        return
    
    # Get demo data
    print("\n2. Getting Demo Data...")
    try:
        response = requests.get(f"{base_url}/demo-data")
        if response.status_code == 200:
            demo_data = response.json()["demo_data"]
            print("✅ Demo data retrieved")
            print(f"   Creator ID: {demo_data['creator_id']}")
            print(f"   Conversion Rate: {demo_data['conversion_rate']:.1%}")
            print(f"   Total Revenue: ${demo_data['total_revenue']:,.0f}")
        else:
            print("❌ Failed to get demo data")
            return
    except Exception as e:
        print(f"❌ Failed to get demo data: {e}")
        return
    
    # Test analysis
    print("\n3. Testing Creator Analysis...")
    try:
        response = requests.post(f"{base_url}/analyze", json=demo_data)
        if response.status_code == 200:
            result = response.json()
            print("✅ Analysis completed")
            print(f"   Overall Score: {result['overall_score']:.3f}")
            print(f"   Revenue Focus Score: {result['revenue_focus_score']:.3f}")
            print(f"   Recommendations: {len(result['recommendations'])}")
            
            # Show top recommendations
            if result['recommendations']:
                print("\n   Top Recommendations:")
                for i, rec in enumerate(result['recommendations'][:3], 1):
                    print(f"   {i}. {rec['title']} (Priority: {rec['priority_score']:.1f})")
                    print(f"      Expected Improvement: {rec['expected_improvement']:.1%}")
                    print(f"      Actions: {', '.join(rec['actions'][:2])}...")
        else:
            print("❌ Analysis failed")
            print(f"   Error: {response.text}")
            return
    except Exception as e:
        print(f"❌ Analysis failed: {e}")
        return
    
    # Test algorithm comparison
    print("\n4. Testing Algorithm Comparison...")
    try:
        response = requests.post(f"{base_url}/compare-algorithms", json=demo_data)
        if response.status_code == 200:
            comparison = response.json()["comparison"]
            print("✅ Algorithm comparison completed")
            print(f"   New Weighted Score: {comparison['new_weighted_score']:.3f}")
            print(f"   Equal Weighted Score: {comparison['equal_weighted_score']:.3f}")
            print(f"   Improvement: {comparison['percentage_change']:+.1f}%")
        else:
            print("❌ Algorithm comparison failed")
    except Exception as e:
        print(f"❌ Algorithm comparison failed: {e}")
    
    # Test weights endpoint
    print("\n5. Testing Weights Configuration...")
    try:
        response = requests.get(f"{base_url}/weights")
        if response.status_code == 200:
            weights = response.json()
            print("✅ Weights configuration retrieved")
            print("   Tier 1 (Revenue Drivers):")
            for kpi in weights["tier_breakdown"]["tier_1"]["kpis"]:
                weight = weights["weights"][kpi]
                print(f"     {kpi}: {weight:.1%}")
        else:
            print("❌ Failed to get weights")
    except Exception as e:
        print(f"❌ Failed to get weights: {e}")
    
    print("\n🎉 Demo completed successfully!")
    print("\nNext steps:")
    print("- Visit http://localhost:8000/docs for interactive API documentation")
    print("- Use the /analyze endpoint with your own creator data")
    print("- Explore the recommendation engine for actionable insights")


if __name__ == "__main__":
    test_api()
