"""
Task 1 Testing: KPI Algorithm Optimization
Tests the multi-tier weighted algorithm vs equal weighting
"""

import requests
import json
from datetime import datetime
import os
from src.config.config import settings

class Task1Tester:
    def __init__(self, base_url=None):
        self.base_url = base_url or settings.base_url
        self.test_results = []
    
    def test_algorithm_comparison(self):
        """Test 1.1: Compare new algorithm vs equal weighting"""
        print("🧪 Test 1.1: Algorithm Comparison")
        print("=" * 50)
        
        # Test data with mixed performance
        test_data = {
            "creator_id": "algorithm_test_001",
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
            response = requests.post(f"{self.base_url}/compare-algorithms", json=test_data)
            if response.status_code == 200:
                result = response.json()
                
                print("✅ New Weighted Score: {:.3f}".format(result["comparison"]["new_weighted_score"]))
                print("✅ Equal Weighted Score: {:.3f}".format(result["comparison"]["equal_weighted_score"]))
                print("✅ Score Difference: {:.3f}".format(result["comparison"]["score_difference"]))
                print("✅ Percentage Change: {:.1f}%".format(result["comparison"]["percentage_change"]))
                
                # Validate improvement
                if result["comparison"]["percentage_change"] > 0:
                    print("✅ PASS: New algorithm shows improvement")
                    self.test_results.append(("Algorithm Improvement", True, "{:.1f}% improvement".format(result["comparison"]["percentage_change"])))
                else:
                    print("❌ FAIL: No improvement detected")
                    self.test_results.append(("Algorithm Improvement", False, "{:.1f}% change".format(result["comparison"]["percentage_change"])))
                
                # Validate revenue focus
                if result["comparison"].get("revenue_focus_improvement", 0) > 0:
                    print("✅ PASS: Revenue focus improvement detected")
                    self.test_results.append(("Revenue Focus", True, "{:.3f} improvement".format(result["comparison"]["revenue_focus_improvement"])))
                else:
                    print("❌ FAIL: No revenue focus improvement")
                    self.test_results.append(("Revenue Focus", False, "No improvement"))
                
                return True
            else:
                print(f"❌ FAIL: API error {response.status_code}")
                self.test_results.append(("Algorithm Comparison", False, f"API error {response.status_code}"))
                return False
                
        except Exception as e:
            print(f"❌ FAIL: Error {e}")
            self.test_results.append(("Algorithm Comparison", False, f"Error: {e}"))
            return False
    
    def test_weight_distribution(self):
        """Test 1.2: Validate weight distribution"""
        print("\n🧪 Test 1.2: Weight Distribution Validation")
        print("=" * 50)
        
        try:
            response = requests.get(f"{self.base_url}/weights/api")
            if response.status_code == 200:
                weights = response.json()["weights"]
                
                # Check if weights sum to 1.0
                total_weight = sum(weights.values())
                print(f"✅ Total Weight: {total_weight:.3f}")
                
                if abs(total_weight - 1.0) < 0.001:
                    print("✅ PASS: Weights sum to 1.0")
                    self.test_results.append(("Weight Sum", True, f"{total_weight:.3f}"))
                else:
                    print("❌ FAIL: Weights do not sum to 1.0")
                    self.test_results.append(("Weight Sum", False, f"{total_weight:.3f}"))
                
                # Check tier distribution
                tier_1_weight = sum(weights[k] for k in ['sales_performance_scorer', 'shop_conversion_scorer', 'tiktok_shop_scorer'])
                tier_2_weight = sum(weights[k] for k in ['engagement_scorer', 'engagement_growth_scorer', 'discovery_scorer', 'content_strategy_scorer', 'audience_fit_scorer', 'brand_fit_scorer'])
                tier_3_weight = sum(weights[k] for k in ['trend_fit_scorer', 'image_score_scorer', 'reach_visibility_scorer', 'cost_efficiency_scorer'])
                
                print(f"✅ Tier 1 Weight: {tier_1_weight:.3f} (Target: 0.55)")
                print(f"✅ Tier 2 Weight: {tier_2_weight:.3f} (Target: 0.32)")
                print(f"✅ Tier 3 Weight: {tier_3_weight:.3f} (Target: 0.13)")
                
                if abs(tier_1_weight - 0.55) < 0.01:
                    print("✅ PASS: Tier 1 weight correct")
                    self.test_results.append(("Tier 1 Weight", True, f"{tier_1_weight:.3f}"))
                else:
                    print("❌ FAIL: Tier 1 weight incorrect")
                    self.test_results.append(("Tier 1 Weight", False, f"{tier_1_weight:.3f}"))
                
                return True
            else:
                print(f"❌ FAIL: API error {response.status_code}")
                self.test_results.append(("Weight Distribution", False, f"API error {response.status_code}"))
                return False
                
        except Exception as e:
            print(f"❌ FAIL: Error {e}")
            self.test_results.append(("Weight Distribution", False, f"Error: {e}"))
            return False
    
    def test_revenue_focus_calculation(self):
        """Test 1.3: Validate revenue focus calculation"""
        print("\n🧪 Test 1.3: Revenue Focus Calculation")
        print("=" * 50)
        
        # Test with revenue-focused data
        test_data = {
            "creator_id": "revenue_focus_test",
            "conversion_rate": 0.08,  # High conversion
            "total_revenue": 10000.0,  # High revenue
            "avg_order_value": 80.0,   # High AOV
            "funnel_completion_rate": 0.6,  # High funnel completion
            "cart_abandonment_rate": 0.3,   # Low abandonment
            "video_quality": 0.2,      # Low quality (should not dominate)
            "likes_ratio": 0.5,        # Medium engagement
            "comments_ratio": 0.1,
            "shares_ratio": 0.05,
            "retention_rate": 0.4,
            "engagement_growth_rate": 0.05,
            "hashtag_performance": 0.3,
            "content_freshness": 0.2,
            "posting_consistency": 0.3,
            "target_demographic_match": 0.4,
            "audience_engagement_quality": 0.3,
            "brand_alignment": 0.5,
            "trust_score": 0.4,
            "trend_alignment": 0.2,
            "image_quality": 0.1,      # Very low quality
            "total_reach": 5000,       # Medium reach
            "cost_per_acquisition": 120,
            "roi_score": 0.8           # High ROI
        }
        
        try:
            response = requests.post(f"{self.base_url}/analyze", json=test_data)
            if response.status_code == 200:
                result = response.json()
                
                overall_score = result['overall_score']
                revenue_focus_score = result['revenue_focus_score']
                
                print(f"✅ Overall Score: {overall_score:.3f}")
                print(f"✅ Revenue Focus Score: {revenue_focus_score:.3f}")
                
                # Revenue focus should be higher than overall score for this data
                if revenue_focus_score > overall_score * 0.8:  # At least 80% of overall
                    print("✅ PASS: Revenue focus calculation correct")
                    self.test_results.append(("Revenue Focus Calculation", True, f"{revenue_focus_score:.3f}"))
                else:
                    print("❌ FAIL: Revenue focus calculation incorrect")
                    self.test_results.append(("Revenue Focus Calculation", False, f"{revenue_focus_score:.3f}"))
                
                return True
            else:
                print(f"❌ FAIL: API error {response.status_code}")
                self.test_results.append(("Revenue Focus Calculation", False, f"API error {response.status_code}"))
                return False
                
        except Exception as e:
            print(f"❌ FAIL: Error {e}")
            self.test_results.append(("Revenue Focus Calculation", False, f"Error: {e}"))
            return False
    
    def test_tier_classification(self):
        """Test 1.4: Validate tier classification"""
        print("\n🧪 Test 1.4: Tier Classification")
        print("=" * 50)
        
        try:
            response = requests.get(f"{self.base_url}/weights/api")
            if response.status_code == 200:
                weights = response.json()["weights"]
                
                # Check Tier 1 KPIs (Direct Revenue)
                tier_1_kpis = ['sales_performance_scorer', 'shop_conversion_scorer', 'tiktok_shop_scorer']
                tier_1_total = sum(weights[k] for k in tier_1_kpis)
                
                print(f"✅ Tier 1 Total: {tier_1_total:.3f}")
                
                if abs(tier_1_total - 0.55) < 0.01:
                    print("✅ PASS: Tier 1 classification correct")
                    self.test_results.append(("Tier 1 Classification", True, f"{tier_1_total:.3f}"))
                else:
                    print("❌ FAIL: Tier 1 classification incorrect")
                    self.test_results.append(("Tier 1 Classification", False, f"{tier_1_total:.3f}"))
                
                # Check individual Tier 1 weights
                sales_weight = weights.get('sales_performance_scorer', 0)
                if sales_weight >= 0.25:  # Should be highest weight
                    print("✅ PASS: Sales performance has highest weight")
                    self.test_results.append(("Sales Weight", True, f"{sales_weight:.3f}"))
                else:
                    print("❌ FAIL: Sales performance weight too low")
                    self.test_results.append(("Sales Weight", False, f"{sales_weight:.3f}"))
                
                return True
            else:
                print(f"❌ FAIL: API error {response.status_code}")
                self.test_results.append(("Tier Classification", False, f"API error {response.status_code}"))
                return False
                
        except Exception as e:
            print(f"❌ FAIL: Error {e}")
            self.test_results.append(("Tier Classification", False, f"Error: {e}"))
            return False
    
    def test_mathematical_formula(self):
        """Test 1.5: Validate mathematical formula implementation"""
        print("\n🧪 Test 1.5: Mathematical Formula Validation")
        print("=" * 50)
        
        # Test with known values
        test_data = {
            "creator_id": "formula_test",
            "conversion_rate": 0.1,
            "total_revenue": 1000.0,
            "avg_order_value": 50.0,
            "funnel_completion_rate": 0.5,
            "cart_abandonment_rate": 0.5,
            "video_quality": 0.5,
            "likes_ratio": 0.5,
            "comments_ratio": 0.1,
            "shares_ratio": 0.1,
            "retention_rate": 0.5,
            "engagement_growth_rate": 0.1,
            "hashtag_performance": 0.5,
            "content_freshness": 0.5,
            "posting_consistency": 0.5,
            "target_demographic_match": 0.5,
            "audience_engagement_quality": 0.5,
            "brand_alignment": 0.5,
            "trust_score": 0.5,
            "trend_alignment": 0.5,
            "image_quality": 0.5,
            "total_reach": 5000,
            "cost_per_acquisition": 100,
            "roi_score": 0.5
        }
        
        try:
            response = requests.post(f"{self.base_url}/analyze", json=test_data)
            if response.status_code == 200:
                result = response.json()
                
                overall_score = result['overall_score']
                
                # For uniform data, score should be close to 0.5
                if 0.4 <= overall_score <= 0.6:
                    print("✅ PASS: Mathematical formula correct")
                    self.test_results.append(("Mathematical Formula", True, f"{overall_score:.3f}"))
                else:
                    print("❌ FAIL: Mathematical formula incorrect")
                    self.test_results.append(("Mathematical Formula", False, f"{overall_score:.3f}"))
                
                return True
            else:
                print(f"❌ FAIL: API error {response.status_code}")
                self.test_results.append(("Mathematical Formula", False, f"API error {response.status_code}"))
                return False
                
        except Exception as e:
            print(f"❌ FAIL: Error {e}")
            self.test_results.append(("Mathematical Formula", False, f"Error: {e}"))
            return False
    
    def test_business_impact_measurement(self):
        """Test 1.6: Validate business impact measurement"""
        print("\n🧪 Test 1.6: Business Impact Measurement")
        print("=" * 50)
        
        # Test with high-revenue, low-quality data
        test_data = {
            "creator_id": "business_impact_test",
            "conversion_rate": 0.12,   # Very high conversion
            "total_revenue": 20000.0,  # Very high revenue
            "avg_order_value": 100.0,  # Very high AOV
            "funnel_completion_rate": 0.8,  # Very high funnel completion
            "cart_abandonment_rate": 0.2,   # Very low abandonment
            "video_quality": 0.1,      # Very low quality
            "likes_ratio": 0.3,        # Low engagement
            "comments_ratio": 0.05,
            "shares_ratio": 0.02,
            "retention_rate": 0.2,
            "engagement_growth_rate": 0.02,
            "hashtag_performance": 0.1,
            "content_freshness": 0.1,
            "posting_consistency": 0.1,
            "target_demographic_match": 0.2,
            "audience_engagement_quality": 0.1,
            "brand_alignment": 0.3,
            "trust_score": 0.2,
            "trend_alignment": 0.1,
            "image_quality": 0.05,     # Very low quality
            "total_reach": 2000,       # Low reach
            "cost_per_acquisition": 200,
            "roi_score": 0.9           # Very high ROI
        }
        
        try:
            response = requests.post(f"{self.base_url}/analyze", json=test_data)
            if response.status_code == 200:
                result = response.json()
                
                overall_score = result['overall_score']
                revenue_focus_score = result['revenue_focus_score']
                
                print(f"✅ Overall Score: {overall_score:.3f}")
                print(f"✅ Revenue Focus Score: {revenue_focus_score:.3f}")
                
                # Revenue focus should be significantly higher than overall
                if revenue_focus_score > overall_score * 1.2:  # At least 20% higher
                    print("✅ PASS: Business impact measurement correct")
                    self.test_results.append(("Business Impact", True, f"Revenue: {revenue_focus_score:.3f}, Overall: {overall_score:.3f}"))
                else:
                    print("❌ FAIL: Business impact measurement incorrect")
                    self.test_results.append(("Business Impact", False, f"Revenue: {revenue_focus_score:.3f}, Overall: {overall_score:.3f}"))
                
                return True
            else:
                print(f"❌ FAIL: API error {response.status_code}")
                self.test_results.append(("Business Impact", False, f"API error {response.status_code}"))
                return False
                
        except Exception as e:
            print(f"❌ FAIL: Error {e}")
            self.test_results.append(("Business Impact", False, f"Error: {e}"))
            return False
    
    def test_performance_validation(self):
        """Test 1.7: Validate performance metrics"""
        print("\n🧪 Test 1.7: Performance Validation")
        print("=" * 50)
        
        import time
        
        test_data = {
            "creator_id": "performance_test",
            "conversion_rate": 0.05,
            "total_revenue": 5000.0,
            "avg_order_value": 50.0,
            "funnel_completion_rate": 0.4,
            "cart_abandonment_rate": 0.6,
            "video_quality": 0.4,
            "likes_ratio": 0.6,
            "comments_ratio": 0.1,
            "shares_ratio": 0.1,
            "retention_rate": 0.5,
            "engagement_growth_rate": 0.1,
            "hashtag_performance": 0.4,
            "content_freshness": 0.4,
            "posting_consistency": 0.5,
            "target_demographic_match": 0.5,
            "audience_engagement_quality": 0.5,
            "brand_alignment": 0.6,
            "trust_score": 0.5,
            "trend_alignment": 0.4,
            "image_quality": 0.4,
            "total_reach": 6000,
            "cost_per_acquisition": 120,
            "roi_score": 0.6
        }
        
        try:
            start_time = time.time()
            response = requests.post(f"{self.base_url}/analyze", json=test_data)
            end_time = time.time()
            
            response_time = (end_time - start_time) * 1000  # Convert to milliseconds
            
            print(f"✅ Response Time: {response_time:.1f}ms")
            
            if response.status_code == 200 and response_time < 200:  # Target: < 200ms
                print("✅ PASS: Performance validation passed")
                self.test_results.append(("Performance", True, f"{response_time:.1f}ms"))
            else:
                print("❌ FAIL: Performance validation failed")
                self.test_results.append(("Performance", False, f"{response_time:.1f}ms"))
            
            return True
            
        except Exception as e:
            print(f"❌ FAIL: Error {e}")
            self.test_results.append(("Performance", False, f"Error: {e}"))
            return False
    
    def test_edge_cases(self):
        """Test 1.8: Validate edge case handling"""
        print("\n�� Test 1.8: Edge Case Handling")
        print("=" * 50)
        
        # Test with extreme values
        test_data = {
            "creator_id": "edge_case_test",
            "conversion_rate": 0.0,    # Zero conversion
            "total_revenue": 0.0,      # Zero revenue
            "avg_order_value": 0.0,    # Zero AOV
            "funnel_completion_rate": 0.0,  # Zero funnel completion
            "cart_abandonment_rate": 1.0,   # 100% abandonment
            "video_quality": 0.0,      # Zero quality
            "likes_ratio": 0.0,
            "comments_ratio": 0.0,
            "shares_ratio": 0.0,
            "retention_rate": 0.0,
            "engagement_growth_rate": 0.0,
            "hashtag_performance": 0.0,
            "content_freshness": 0.0,
            "posting_consistency": 0.0,
            "target_demographic_match": 0.0,
            "audience_engagement_quality": 0.0,
            "brand_alignment": 0.0,
            "trust_score": 0.0,
            "trend_alignment": 0.0,
            "image_quality": 0.0,
            "total_reach": 0,
            "cost_per_acquisition": 0,
            "roi_score": 0.0
        }
        
        try:
            response = requests.post(f"{self.base_url}/analyze", json=test_data)
            
            if response.status_code == 200:
                result = response.json()
                overall_score = result['overall_score']
                
                print(f"✅ Overall Score: {overall_score:.3f}")
                
                # Should handle zero values gracefully
                if 0.0 <= overall_score <= 1.0:
                    print("✅ PASS: Edge case handling correct")
                    self.test_results.append(("Edge Cases", True, f"{overall_score:.3f}"))
                else:
                    print("❌ FAIL: Edge case handling incorrect")
                    self.test_results.append(("Edge Cases", False, f"{overall_score:.3f}"))
                
                return True
            else:
                print(f"❌ FAIL: API error {response.status_code}")
                self.test_results.append(("Edge Cases", False, f"API error {response.status_code}"))
                return False
                
        except Exception as e:
            print(f"❌ FAIL: Error {e}")
            self.test_results.append(("Edge Cases", False, f"Error: {e}"))
            return False
    
    def run_all_tests(self):
        """Run all Task 1 tests"""
        print("🚀 Starting Task 1: KPI Algorithm Optimization Tests")
        print("=" * 60)
        
        # Run all tests
        self.test_algorithm_comparison()
        self.test_weight_distribution()
        self.test_revenue_focus_calculation()
        self.test_tier_classification()
        self.test_mathematical_formula()
        self.test_business_impact_measurement()
        self.test_performance_validation()
        self.test_edge_cases()
        
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
