"""
Comprehensive Testing Suite for TikTok Metrics AI Agent
Tests both Task 1 (Algorithm Optimization) and Task 2 (AI Pipeline)
"""

import requests
import time
import sys
from datetime import datetime

def check_api_health(base_url="http://localhost:8000"):
    """Check if the API is running and healthy"""
    try:
        response = requests.get(f"{base_url}/health", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ API Health: {data['status']}")
            print(f"   Service: {data['service']}")
            print(f"   Version: {data['version']}")
            return True
        else:
            print(f"❌ API Health Check Failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ API Health Check Failed: {e}")
        return False

def run_task1_tests():
    """Run Task 1: KPI Algorithm Optimization Tests"""
    print("\n" + "="*60)
    print("🎯 TASK 1: KPI ALGORITHM OPTIMIZATION TESTING")
    print("="*60)
    
    try:
        from test_task1_algorithm import Task1Tester
        tester = Task1Tester()
        return tester.run_all_tests()
    except ImportError as e:
        print(f"❌ Failed to import Task 1 tester: {e}")
        return False
    except Exception as e:
        print(f"❌ Task 1 tests failed: {e}")
        return False

def run_task2_tests():
    """Run Task 2: Revenue Optimization AI Pipeline Tests"""
    print("\n" + "="*60)
    print("🎯 TASK 2: REVENUE OPTIMIZATION AI PIPELINE TESTING")
    print("="*60)
    
    try:
        from test_task2_pipeline import Task2Tester
        tester = Task2Tester()
        return tester.run_all_tests()
    except ImportError as e:
        print(f"❌ Failed to import Task 2 tester: {e}")
        return False
    except Exception as e:
        print(f"❌ Task 2 tests failed: {e}")
        return False

def run_frontend_tests():
    """Run Frontend Integration Tests"""
    print("\n" + "="*60)
    print("🎨 FRONTEND INTEGRATION TESTING")
    print("="*60)
    
    base_url = "http://localhost:8000"
    tests_passed = 0
    total_tests = 0
    
    # Test 1: Dashboard accessibility
    total_tests += 1
    try:
        response = requests.get(f"{base_url}/", timeout=10)
        if response.status_code == 200 and "TikTok Metrics AI Agent" in response.text:
            print("✅ Dashboard accessible")
            tests_passed += 1
        else:
            print("❌ Dashboard not accessible")
    except Exception as e:
        print(f"❌ Dashboard test failed: {e}")
    
    # Test 2: Static files serving
    total_tests += 1
    try:
        response = requests.get(f"{base_url}/static/css/dashboard.css", timeout=5)
        if response.status_code == 200:
            print("✅ CSS files serving correctly")
            tests_passed += 1
        else:
            print("❌ CSS files not serving")
    except Exception as e:
        print(f"❌ CSS test failed: {e}")
    
    # Test 3: JavaScript files
    total_tests += 1
    try:
        response = requests.get(f"{base_url}/static/js/dashboard.js", timeout=5)
        if response.status_code == 200:
            print("✅ JavaScript files serving correctly")
            tests_passed += 1
        else:
            print("❌ JavaScript files not serving")
    except Exception as e:
        print(f"❌ JavaScript test failed: {e}")
    
    # Test 4: API endpoints accessible from frontend
    total_tests += 1
    try:
        response = requests.get(f"{base_url}/demo-data", timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data.get('success') and 'demo_data' in data:
                print("✅ Demo data endpoint working")
                tests_passed += 1
            else:
                print("❌ Demo data endpoint not working correctly")
        else:
            print("❌ Demo data endpoint not accessible")
    except Exception as e:
        print(f"❌ Demo data test failed: {e}")
    
    print(f"\n📊 Frontend Tests: {tests_passed}/{total_tests} passed")
    return tests_passed == total_tests

def run_performance_tests():
    """Run Performance and Load Tests"""
    print("\n" + "="*60)
    print("⚡ PERFORMANCE TESTING")
    print("="*60)
    
    base_url = "http://localhost:8000"
    tests_passed = 0
    total_tests = 0
    
    # Test 1: Response time for health check
    total_tests += 1
    try:
        start_time = time.time()
        response = requests.get(f"{base_url}/health", timeout=5)
        end_time = time.time()
        response_time = (end_time - start_time) * 1000  # Convert to milliseconds
        
        if response.status_code == 200 and response_time < 1000:  # Less than 1 second
            print(f"✅ Health check response time: {response_time:.0f}ms")
            tests_passed += 1
        else:
            print(f"❌ Health check too slow: {response_time:.0f}ms")
    except Exception as e:
        print(f"❌ Health check performance test failed: {e}")
    
    # Test 2: Response time for analysis
    total_tests += 1
    try:
        test_data = {
            "creator_id": "performance_test",
            "conversion_rate": 0.05,
            "total_revenue": 5000,
            "video_quality": 0.3
        }
        
        start_time = time.time()
        response = requests.post(f"{base_url}/analyze", json=test_data, timeout=10)
        end_time = time.time()
        response_time = (end_time - start_time) * 1000
        
        if response.status_code == 200 and response_time < 5000:  # Less than 5 seconds
            print(f"✅ Analysis response time: {response_time:.0f}ms")
            tests_passed += 1
        else:
            print(f"❌ Analysis too slow: {response_time:.0f}ms")
    except Exception as e:
        print(f"❌ Analysis performance test failed: {e}")
    
    # Test 3: Concurrent requests
    total_tests += 1
    try:
        import threading
        import queue
        
        results = queue.Queue()
        
        def make_request():
            try:
                response = requests.get(f"{base_url}/health", timeout=5)
                results.put(response.status_code == 200)
            except:
                results.put(False)
        
        # Make 5 concurrent requests
        threads = []
        for _ in range(5):
            thread = threading.Thread(target=make_request)
            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join()
        
        concurrent_success = sum(1 for _ in range(5) if results.get())
        if concurrent_success >= 4:  # At least 4 out of 5 should succeed
            print(f"✅ Concurrent requests: {concurrent_success}/5 successful")
            tests_passed += 1
        else:
            print(f"❌ Concurrent requests failed: {concurrent_success}/5 successful")
    except Exception as e:
        print(f"❌ Concurrent request test failed: {e}")
    
    print(f"\n📊 Performance Tests: {tests_passed}/{total_tests} passed")
    return tests_passed == total_tests

def generate_test_report(task1_passed, task2_passed, frontend_passed, performance_passed):
    """Generate comprehensive test report"""
    print("\n" + "="*80)
    print("📋 COMPREHENSIVE TEST REPORT")
    print("="*80)
    
    total_tests = 4
    passed_tests = sum([task1_passed, task2_passed, frontend_passed, performance_passed])
    
    print(f"📅 Test Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"�� Overall Result: {passed_tests}/{total_tests} test suites passed")
    print()
    
    print("📊 Test Suite Results:")
    print(f"   Task 1 (Algorithm Optimization): {'✅ PASSED' if task1_passed else '❌ FAILED'}")
    print(f"   Task 2 (AI Pipeline): {'✅ PASSED' if task2_passed else '❌ FAILED'}")
    print(f"   Frontend Integration: {'✅ PASSED' if frontend_passed else '❌ FAILED'}")
    print(f"   Performance Testing: {'✅ PASSED' if performance_passed else '❌ FAILED'}")
    print()
    
    if passed_tests == total_tests:
        print("🎉 ALL TESTS PASSED! The TikTok Metrics AI Agent is fully functional.")
        print("✅ Ready for production use!")
    else:
        print("⚠️  SOME TESTS FAILED! Please review the results above.")
        print("🔧 Check the specific test failures and fix any issues.")
    
    print("\n🚀 Next Steps:")
    print("   1. Review any failed tests")
    print("   2. Fix identified issues")
    print("   3. Re-run tests to verify fixes")
    print("   4. Deploy to production environment")
    
    return passed_tests == total_tests

def main():
    """Main test runner"""
    print("🚀 TikTok Metrics AI Agent - Comprehensive Testing Suite")
    print("="*80)
    print(f"⏰ Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Check API health first
    if not check_api_health():
        print("\n❌ API is not running or not healthy. Please start the application first.")
        print("   Run: python3 app.py")
        sys.exit(1)
    
    print("\n✅ API is healthy. Starting comprehensive tests...")
    
    # Run all test suites
    task1_passed = run_task1_tests()
    task2_passed = run_task2_tests()
    frontend_passed = run_frontend_tests()
    performance_passed = run_performance_tests()
    
    # Generate final report
    all_passed = generate_test_report(task1_passed, task2_passed, frontend_passed, performance_passed)
    
    print(f"\n⏰ Completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    if all_passed:
        sys.exit(0)  # Success
    else:
        sys.exit(1)  # Failure

if __name__ == "__main__":
    main()
