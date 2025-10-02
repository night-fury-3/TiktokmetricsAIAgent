"""
Task 2 Testing: Revenue Optimization AI Pipeline
Tests the AI recommendation system and diagnostic capabilities
"""

import requests
import json
from datetime import datetime
import os
from src.config.config import settings

class Task2Tester:
    def __init__(self, base_url=None):
        self.base_url = base_url or settings.base_url
        self.test_results = []
    
    def test_bottleneck_identification(self):
        """Test 2.1: Bottleneck identification for different scenarios"""
        print("🧪 Test 2.1: Bottleneck Identification")
        print("=" * 50)
        
        # Test scenarios with different bottlenecks
        test_scenarios = [
            {
                "name": "Low Conversion Rate",
                "data": {
                    "creator_id": "low_conversion_test",
                    "conversion_rate": 0.01,  # Very low
                    "total_revenue": 500,
                    "avg_order_value": 30,
                    "funnel_completion_rate": 0.1,
                    "cart_abandonment_rate": 0.9,
                    "video_quality": 0.8,
                    "likes_ratio": 0.7,
                    "comments_ratio": 0.2,
                    "shares_ratio": 0.1,
                    "retention_rate": 0.7,
                    "engagement_growth_rate": 0.15,
                    "hashtag_performance": 0.6,
                    "content_freshness": 0.7,
                    "posting_consistency": 0.8,
                    "target_demographic_match": 0.6,
                    "audience_engagement_quality": 0.7,
                    "brand_alignment": 0.8,
                    "trust_score": 0.7,
                    "trend_alignment": 0.6,
                    "image_quality": 0.7,
                    "total_reach": 8000,
                    "cost_per_acquisition": 150,
                    "roi_score": 0.5
                },
                "expected_bottleneck": "sales_performance_scorer"
            },
            {
                "name": "High Cart Abandonment",
                "data": {
                    "creator_id": "high_abandonment_test",
                    "conversion_rate": 0.08,
                    "total_revenue": 2000,
                    "avg_order_value": 40,
                    "funnel_completion_rate": 0.2,  # Low
                    "cart_abandonment_rate": 0.9,   # Very high
                    "checkout_success_rate": 0.3,   # Low
                    "video_quality": 0.6,
                    "likes_ratio": 0.6,
                    "comments_ratio": 0.15,
                    "shares_ratio": 0.1,
                    "retention_rate": 0.5,
                    "engagement_growth_rate": 0.1,
                    "hashtag_performance": 0.5,
                    "content_freshness": 0.6,
                    "posting_consistency": 0.7,
                    "target_demographic_match": 0.5,
                    "audience_engagement_quality": 0.6,
                    "brand_alignment": 0.7,
                    "trust_score": 0.6,
                    "trend_alignment": 0.5,
                    "image_quality": 0.6,
                    "total_reach": 6000,
                    "cost_per_acquisition": 100,
                    "roi_score": 0.8
                },
                "expected_bottleneck": "shop_conversion_scorer"
            },
            {
                "name": "Poor Video Quality",
                "data": {
                    "creator_id": "poor_quality_test",
                    "conversion_rate": 0.06,
                    "total_revenue": 3000,
                    "avg_order_value": 50,
                    "funnel_completion_rate": 0.4,
                    "cart_abandonment_rate": 0.6,
                    "video_quality": 0.1,  # Very low
                    "content_freshness": 0.3,  # Low
                    "posting_consistency": 0.4,  # Low
                    "image_quality": 0.2,  # Very low
                    "lighting_score": 0.1,  # Very low
                    "likes_ratio": 0.5,
                    "comments_ratio": 0.1,
                    "shares_ratio": 0.05,
                    "retention_rate": 0.4,
                    "engagement_growth_rate": 0.05,
                    "hashtag_performance": 0.4,
                    "target_demographic_match": 0.5,
                    "audience_engagement_quality": 0.4,
                    "brand_alignment": 0.6,
                    "trust_score": 0.5,
                    "trend_alignment": 0.4,
                    "total_reach": 4000,
                    "cost_per_acquisition": 90,
                    "roi_score": 0.7
                },
                "expected_bottleneck": "content_strategy_scorer"
            }
        ]
        
        success_count = 0
        
        for scenario in test_scenarios:
            print(f"\n🔍 Testing: {scenario['name']}")
            
            try:
                response = requests.post(f"{self.base_url}/analyze", json=scenario['data'])
                if response.status_code == 200:
                    result = response.json()
                    recommendations = result['recommendations']
                    
                    if recommendations:
                        # Check if the expected bottleneck is identified
                        top_recommendation = recommendations[0]
                        affected_kpi = top_recommendation.get('kpi_affected', '')
                        
                        print(f"   Top KPI: {affected_kpi}")
                        print(f"   Expected: {scenario['expected_bottleneck']}")
                        print(f"   Priority Score: {top_recommendation.get('priority_score', 0):.1f}")
                        
                        if scenario['expected_bottleneck'] in affected_kpi:
                            print("   ✅ PASS: Correct bottleneck identified")
                            success_count += 1
                            self.test_results.append((f"Bottleneck: {scenario['name']}", True, affected_kpi))
                        else:
                            print("   ❌ FAIL: Wrong bottleneck identified")
                            self.test_results.append((f"Bottleneck: {scenario['name']}", False, f"Expected: {scenario['expected_bottleneck']}, Got: {affected_kpi}"))
                    else:
                        print("   ❌ FAIL: No recommendations generated")
                        self.test_results.append((f"Bottleneck: {scenario['name']}", False, "No recommendations"))
                else:
                    print(f"   ❌ FAIL: API error {response.status_code}")
                    self.test_results.append((f"Bottleneck: {scenario['name']}", False, f"API error {response.status_code}"))
                    
            except Exception as e:
                print(f"   ❌ FAIL: Error {e}")
                self.test_results.append((f"Bottleneck: {scenario['name']}", False, f"Error: {e}"))
        
        print(f"\n📊 Bottleneck Identification: {success_count}/{len(test_scenarios)} scenarios passed")
        return success_count == len(test_scenarios)
    
    def test_recommendation_quality(self):
        """Test 2.2: Recommendation quality and actionability"""
        print("\n🧪 Test 2.2: Recommendation Quality")
        print("=" * 50)
        
        # Test with mixed performance creator
        test_data = {
            "creator_id": "recommendation_quality_test",
            "conversion_rate": 0.03,
            "total_revenue": 1500,
            "avg_order_value": 35,
            "funnel_completion_rate": 0.25,
            "cart_abandonment_rate": 0.75,
            "video_quality": 0.2,
            "content_freshness": 0.4,
            "posting_consistency": 0.5,
            "likes_ratio": 0.6,
            "comments_ratio": 0.1,
            "shares_ratio": 0.05,
            "retention_rate": 0.4,
            "engagement_growth_rate": 0.08,
            "hashtag_performance": 0.3,
            "target_demographic_match": 0.4,
            "audience_engagement_quality": 0.3,
            "brand_alignment": 0.5,
            "trust_score": 0.4,
            "trend_alignment": 0.3,
            "image_quality": 0.2,
            "total_reach": 3000,
            "cost_per_acquisition": 120,
            "roi_score": 0.6
        }
        
        try:
            response = requests.post(f"{self.base_url}/analyze", json=test_data)
            if response.status_code == 200:
                result = response.json()
                recommendations = result['recommendations']
                
                print(f"✅ Generated {len(recommendations)} recommendations")
                
                # Test recommendation quality criteria
                quality_tests = []
                
                if len(recommendations) > 0:
                    quality_tests.append(("Has Recommendations", True, f"{len(recommendations)} recommendations"))
                else:
                    quality_tests.append(("Has Recommendations", False, "No recommendations"))
                
                # Check priority scoring
                if recommendations:
                    priorities = [rec.get('priority_score', 0) for rec in recommendations]
                    if all(p > 0 for p in priorities):
                        quality_tests.append(("Priority Scoring", True, f"All priorities > 0"))
                    else:
                        quality_tests.append(("Priority Scoring", False, f"Some priorities <= 0"))
                
                # Check expected improvement
                if recommendations:
                    improvements = [rec.get('expected_improvement', 0) for rec in recommendations]
                    if all(0 < imp < 1 for imp in improvements):
                        quality_tests.append(("Expected Improvement", True, f"All improvements 0-100%"))
                    else:
                        quality_tests.append(("Expected Improvement", False, f"Some improvements invalid"))
                
                # Check actions
                if recommendations:
                    actions = [rec.get('actions', []) for rec in recommendations]
                    if all(len(action_list) > 0 for action_list in actions):
                        quality_tests.append(("Actionable Steps", True, f"All recommendations have actions"))
                    else:
                        quality_tests.append(("Actionable Steps", False, f"Some recommendations lack actions"))
                
                # Check A/B test configs
                if recommendations:
                    experiments = [rec.get('experiment', {}) for rec in recommendations]
                    if all('type' in exp and 'duration_days' in exp for exp in experiments):
                        quality_tests.append(("A/B Test Configs", True, f"All have experiment configs"))
                    else:
                        quality_tests.append(("A/B Test Configs", False, f"Some lack experiment configs"))
                
                # Display results
                for test_name, success, result in quality_tests:
                    status = "✅ PASS" if success else "❌ FAIL"
                    print(f"   {status} {test_name}: {result}")
                    self.test_results.append((test_name, success, result))
                
                passed = sum(1 for _, success, _ in quality_tests if success)
                print(f"\n📊 Recommendation Quality: {passed}/{len(quality_tests)} criteria passed")
                
                return passed == len(quality_tests)
            else:
                print(f"❌ FAIL: API error {response.status_code}")
                return False
                
        except Exception as e:
            print(f"❌ FAIL: Error {e}")
            return False
    
    def test_revenue_optimization(self):
        """Test 2.3: Revenue-focused optimization validation"""
        print("\n🧪 Test 2.3: Revenue Optimization Focus")
        print("=" * 50)
        
        # Test with revenue-focused scenario
        test_data = {
            "creator_id": "revenue_optimization_test",
            "conversion_rate": 0.02,  # Low - should be prioritized
            "total_revenue": 1000,    # Low - should be prioritized
            "avg_order_value": 20,    # Low - should be prioritized
            "funnel_completion_rate": 0.15,  # Low - should be prioritized
            "cart_abandonment_rate": 0.85,   # High - should be prioritized
            "video_quality": 0.9,     # High - should not be prioritized
            "likes_ratio": 0.8,       # High - should not be prioritized
            "comments_ratio": 0.25,   # High - should not be prioritized
            "shares_ratio": 0.2,      # High - should not be prioritized
            "retention_rate": 0.9,    # High - should not be prioritized
            "engagement_growth_rate": 0.3,   # High - should not be prioritized
            "hashtag_performance": 0.8,      # High - should not be prioritized
            "content_freshness": 0.9,        # High - should not be prioritized
            "posting_consistency": 0.9,      # High - should not be prioritized
            "target_demographic_match": 0.8, # High - should not be prioritized
            "audience_engagement_quality": 0.9, # High - should not be prioritized
            "brand_alignment": 0.9,   # High - should not be prioritized
            "trust_score": 0.9,       # High - should not be prioritized
            "trend_alignment": 0.8,   # High - should not be prioritized
            "image_quality": 0.9,     # High - should not be prioritized
            "total_reach": 15000,     # High - should not be prioritized
            "cost_per_acquisition": 200,     # High - should not be prioritized
            "roi_score": 0.3          # Low - should be prioritized
        }
        
        try:
            response = requests.post(f"{self.base_url}/analyze", json=test_data)
            if response.status_code == 200:
                result = response.json()
                recommendations = result['recommendations']
                insights = result['insights']
                
                print(f"✅ Revenue Focus Score: {result['revenue_focus_score']:.3f}")
                print(f"✅ Overall Score: {result['overall_score']:.3f}")
                print(f"✅ Generated {len(recommendations)} recommendations")
                
                # Check if revenue KPIs are prioritized
                revenue_kpis = ['sales_performance_scorer', 'shop_conversion_scorer', 'tiktok_shop_scorer']
                revenue_recommendations = [rec for rec in recommendations if rec.get('kpi_affected') in revenue_kpis]
                
                if len(revenue_recommendations) > 0:
                    print(f"✅ Revenue KPIs prioritized: {len(revenue_recommendations)}/{len(recommendations)} recommendations")
                    self.test_results.append(("Revenue Prioritization", True, f"{len(revenue_recommendations)} revenue recommendations"))
                else:
                    print("❌ Revenue KPIs not prioritized")
                    self.test_results.append(("Revenue Prioritization", False, "No revenue recommendations"))
                
                # Check improvement potential
                if 'improvement_potential' in insights:
                    improvement = insights['improvement_potential']
                    print(f"✅ Improvement Potential: {improvement:.3f}")
                    if improvement > 0.1:  # Should be significant
                        print("✅ PASS: Significant improvement potential identified")
                        self.test_results.append(("Improvement Potential", True, f"{improvement:.3f}"))
                    else:
                        print("❌ FAIL: Low improvement potential")
                        self.test_results.append(("Improvement Potential", False, f"{improvement:.3f}"))
                
                # Check priority actions
                if 'priority_actions' in insights:
                    priority_actions = insights['priority_actions']
                    print(f"✅ Priority Actions: {len(priority_actions)} identified")
                    if len(priority_actions) > 0:
                        print("✅ PASS: Priority actions identified")
                        self.test_results.append(("Priority Actions", True, f"{len(priority_actions)} actions"))
                    else:
                        print("❌ FAIL: No priority actions")
                        self.test_results.append(("Priority Actions", False, "No actions"))
                
                return True
            else:
                print(f"❌ FAIL: API error {response.status_code}")
                return False
                
        except Exception as e:
            print(f"❌ FAIL: Error {e}")
            return False
    
    def run_all_tests(self):
        """Run all Task 2 tests"""
        print("🚀 Starting Task 2: Revenue Optimization AI Pipeline Tests")
        print("=" * 60)
        
        # Run all tests
        self.test_bottleneck_identification()
        self.test_recommendation_quality()
        self.test_revenue_optimization()
        
        # Summary
        print("\n📊 Task 2 Test Summary")
        print("=" * 30)
        passed = sum(1 for _, success, _ in self.test_results if success)
        total = len(self.test_results)
        
        for test_name, success, result in self.test_results:
            status = "✅ PASS" if success else "❌ FAIL"
            print(f"{status} {test_name}: {result}")
        
        print(f"\n🎯 Overall: {passed}/{total} tests passed")
        
        if passed == total:
            print("🎉 All Task 2 tests PASSED!")
        else:
            print("⚠️  Some Task 2 tests FAILED!")
        
        return passed == total

if __name__ == "__main__":
    tester = Task2Tester()
    tester.run_all_tests()
