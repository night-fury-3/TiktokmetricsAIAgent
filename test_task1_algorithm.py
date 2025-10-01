"""
Task 1 Testing: KPI Algorithm Optimization
Tests the multi-tier weighted algorithm vs equal weighting
"""

import requests
import json
from datetime import datetime

class Task1Tester:
    def __init__(self, base_url="http://localhost:8000"):
        self.base_url = base_url
        self.test_results = []
    
    def test_algorithm_comparison(self):
        """Test 1.1: Compare new algorithm vs equal weighting"""
        print("🧪 Test 1.1: Algorithm Comparison")
        print("=" * 50)
        
        # Test data with mixed performance
        test_data = {
            "creator_id": "algorithm_test_creator",
            "conversion_rate": 0.05,
            "total_revenue": 5000,
            "avg_order_value": 45,
            "funnel_completion_rate": 0.3,
            "cart_abandonment_rate": 0.7,
            "video_quality": 0.3,
            "likes_ratio": 0.7,
            "comments_ratio": 0.15,
            "shares_ratio": 0.15,
            "retention_rate": 0.6,
            "engagement_growth_rate": 0.1,
            "hashtag_performance": 0.4,
            "content_freshness": 0.6,
            "posting_consistency": 0.7,
            "target_demographic_match": 0.6,
            "audience_engagement_quality": 0.5,
            "brand_alignment": 0.7,
            "trust_score": 0.6,
            "trend_alignment": 0.4,
            "image_quality": 0.3,
            "total_reach": 5000,
            "cost_per_acquisition": 80,
            "roi_score": 1.2
        }
        
        try:
            # Test new algorithm
            response = requests.post(f"{self.base_url}/analyze", json=test_data)
            if response.status_code == 200:
                new_result = response.json()
                new_score = new_result['overall_score']
                revenue_score = new_result['revenue_focus_score']
                print(f"✅ New Algorithm Score: {new_score:.3f}")
                print(f"✅ Revenue Focus Score: {revenue_score:.3f}")
            else:
                print(f"❌ New algorithm test failed: {response.status_code}")
                return False
            
            # Test algorithm comparison
            response = requests.post(f"{self.base_url}/compare-algorithms", json=test_data)
            if response.status_code == 200:
                comparison = response.json()['comparison']
                old_score = comparison['equal_weighted_score']
                improvement = comparison['percentage_change']
                
                print(f"✅ Equal Weighted Score: {old_score:.3f}")
                print(f"✅ Improvement: {improvement:+.1f}%")
                
                # Validate success criteria
                if improvement > 5.0:  # Should be around 8.6%
                    print("✅ PASS: Algorithm shows significant improvement")
                    self.test_results.append(("Algorithm Improvement", True, f"{improvement:+.1f}%"))
                else:
                    print("❌ FAIL: Improvement too low")
                    self.test_results.append(("Algorithm Improvement", False, f"{improvement:+.1f}%"))
                
                return True
            else:
                print(f"❌ Comparison test failed: {response.status_code}")
                return False
                
        except Exception as e:
            print(f"❌ Test failed with error: {e}")
            return False
    
    def test_tier_weights(self):
        """Test 1.2: Validate tier weight distribution"""
        print("\n🧪 Test 1.2: Tier Weight Validation")
        print("=" * 50)
        
        try:
            response = requests.get(f"{self.base_url}/weights")
            if response.status_code == 200:
                weights_data = response.json()
                tier_breakdown = weights_data['tier_breakdown']
                
                # Check Tier 1 (Revenue Drivers)
                tier1_weight = tier_breakdown['tier_1']['total_weight']
                print(f"✅ Tier 1 (Revenue Drivers): {tier1_weight:.1%}")
                
                # Check Tier 2 (Revenue Enablers)
                tier2_weight = tier_breakdown['tier_2']['total_weight']
                print(f"✅ Tier 2 (Revenue Enablers): {tier2_weight:.1%}")
                
                # Check Tier 3 (General Health)
                tier3_weight = tier_breakdown['tier_3']['total_weight']
                print(f"✅ Tier 3 (General Health): {tier3_weight:.1%}")
                
                # Validate weights
                total_weight = tier1_weight + tier2_weight + tier3_weight
                if abs(total_weight - 1.0) < 0.01:  # Allow small floating point errors
                    print("✅ PASS: Total weights sum to 100%")
                    self.test_results.append(("Weight Sum", True, f"{total_weight:.1%}"))
                else:
                    print(f"❌ FAIL: Total weights = {total_weight:.1%}")
                    self.test_results.append(("Weight Sum", False, f"{total_weight:.1%}"))
                
                # Check specific weights
                weights = weights_data['weights']
                sales_weight = weights['sales_performance_scorer']
                if abs(sales_weight - 0.30) < 0.01:
                    print("✅ PASS: Sales Performance = 30%")
                    self.test_results.append(("Sales Weight", True, f"{sales_weight:.1%}"))
                else:
                    print(f"❌ FAIL: Sales Performance = {sales_weight:.1%}")
                    self.test_results.append(("Sales Weight", False, f"{sales_weight:.1%}"))
                
                return True
            else:
                print(f"❌ Weights test failed: {response.status_code}")
                return False
                
        except Exception as e:
            print(f"❌ Test failed with error: {e}")
            return False
    
    def test_revenue_focus(self):
        """Test 1.3: Validate revenue focus prioritization"""
        print("\n🧪 Test 1.3: Revenue Focus Validation")
        print("=" * 50)
        
        # High revenue, low engagement creator
        high_revenue_data = {
            "creator_id": "high_revenue_test",
            "conversion_rate": 0.12,
            "total_revenue": 25000,
            "avg_order_value": 85,
            "funnel_completion_rate": 0.8,
            "cart_abandonment_rate": 0.2,
            "video_quality": 0.3,  # Low quality
            "likes_ratio": 0.5,    # Low engagement
            "comments_ratio": 0.1,
            "shares_ratio": 0.05,
            "retention_rate": 0.4,
            "engagement_growth_rate": 0.02,
            "hashtag_performance": 0.3,
            "content_freshness": 0.4,
            "posting_consistency": 0.5,
            "target_demographic_match": 0.4,
            "audience_engagement_quality": 0.3,
            "brand_alignment": 0.5,
            "trust_score": 0.4,
            "trend_alignment": 0.3,
            "image_quality": 0.2,
            "total_reach": 3000,
            "cost_per_acquisition": 120,
            "roi_score": 0.8
        }
        
        # Low revenue, high engagement creator
        high_engagement_data = {
            "creator_id": "high_engagement_test",
            "conversion_rate": 0.02,
            "total_revenue": 2000,
            "avg_order_value": 25,
            "funnel_completion_rate": 0.2,
            "cart_abandonment_rate": 0.8,
            "video_quality": 0.9,  # High quality
            "likes_ratio": 0.8,    # High engagement
            "comments_ratio": 0.25,
            "shares_ratio": 0.2,
            "retention_rate": 0.9,
            "engagement_growth_rate": 0.3,
            "hashtag_performance": 0.8,
            "content_freshness": 0.9,
            "posting_consistency": 0.9,
            "target_demographic_match": 0.8,
            "audience_engagement_quality": 0.9,
            "brand_alignment": 0.9,
            "trust_score": 0.8,
            "trend_alignment": 0.8,
            "image_quality": 0.9,
            "total_reach": 15000,
            "cost_per_acquisition": 30,
            "roi_score": 2.5
        }
        
        try:
            # Test high revenue creator
            response = requests.post(f"{self.base_url}/analyze", json=high_revenue_data)
            if response.status_code == 200:
                high_revenue_result = response.json()
                high_revenue_score = high_revenue_result['overall_score']
                high_revenue_revenue = high_revenue_result['revenue_focus_score']
                print(f"✅ High Revenue Creator Score: {high_revenue_score:.3f}")
                print(f"✅ High Revenue Revenue Focus: {high_revenue_revenue:.3f}")
            else:
                print(f"❌ High revenue test failed: {response.status_code}")
                return False
            
            # Test high engagement creator
            response = requests.post(f"{self.base_url}/analyze", json=high_engagement_data)
            if response.status_code == 200:
                high_engagement_result = response.json()
                high_engagement_score = high_engagement_result['overall_score']
                high_engagement_revenue = high_engagement_result['revenue_focus_score']
                print(f"✅ High Engagement Creator Score: {high_engagement_score:.3f}")
                print(f"✅ High Engagement Revenue Focus: {high_engagement_revenue:.3f}")
            else:
                print(f"❌ High engagement test failed: {response.status_code}")
                return False
            
            # Validate revenue focus
            if high_revenue_score > high_engagement_score:
                print("✅ PASS: Revenue-focused creator scores higher")
                self.test_results.append(("Revenue Focus", True, f"High revenue: {high_revenue_score:.3f} > High engagement: {high_engagement_score:.3f}"))
            else:
                print("❌ FAIL: Revenue focus not properly prioritized")
                self.test_results.append(("Revenue Focus", False, f"High revenue: {high_revenue_score:.3f} <= High engagement: {high_engagement_score:.3f}"))
            
            return True
            
        except Exception as e:
            print(f"❌ Test failed with error: {e}")
            return False
    
    def run_all_tests(self):
        """Run all Task 1 tests"""
        print("�� Starting Task 1: KPI Algorithm Optimization Tests")
        print("=" * 60)
        
        # Run all tests
        self.test_algorithm_comparison()
        self.test_tier_weights()
        self.test_revenue_focus()
        
        # Summary
        print("\n📊 Task 1 Test Summary")
        print("=" * 30)
        passed = sum(1 for _, success, _ in self.test_results if success)
        total = len(self.test_results)
        
        for test_name, success, result in self.test_results:
            status = "✅ PASS" if success else "❌ FAIL"
            print(f"{status} {test_name}: {result}")
        
        print(f"\n🎯 Overall: {passed}/{total} tests passed")
        
        if passed == total:
            print("🎉 All Task 1 tests PASSED!")
        else:
            print("⚠️  Some Task 1 tests FAILED!")
        
        return passed == total

if __name__ == "__main__":
    tester = Task1Tester()
    tester.run_all_tests()
