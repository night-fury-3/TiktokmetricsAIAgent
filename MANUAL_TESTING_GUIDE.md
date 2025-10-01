# 🧪 Manual Testing Guide - TikTok Metrics AI Agent

## Quick Start Testing

### Prerequisites
1. Ensure the application is running: `python3 app.py`
2. Open browser to: http://localhost:8000/
3. Have the API documentation ready: http://localhost:8000/docs

## 🎯 Task 1: KPI Algorithm Optimization Testing

### Test 1.1: Algorithm Comparison
**Objective**: Verify the new algorithm shows improvement over equal weighting

**Steps**:
1. Open the dashboard at http://localhost:8000/
2. Click "Load Demo Data" to populate the form
3. Click "Compare Algorithms" button
4. Observe the comparison results

**Expected Results**:
- New Weighted Score should be higher than Equal Weighted Score
- Improvement percentage should be around +8.6%
- Clear indication of algorithm benefits

### Test 1.2: Weight Distribution Validation
**Objective**: Verify correct tier weight distribution

**Steps**:
1. Navigate to http://localhost:8000/weights
2. Check the tier breakdown
3. Verify individual KPI weights

**Expected Results**:
- Tier 1 (Revenue Drivers): 55% total weight
- Tier 2 (Revenue Enablers): 32% total weight
- Tier 3 (General Health): 13% total weight
- Sales Performance: 30% weight
- All weights sum to 100%

### Test 1.3: Revenue Focus Validation
**Objective**: Verify revenue-focused creators score higher

**Steps**:
1. Create two test scenarios in the dashboard:

**High Revenue Creator**:
- Conversion Rate: 0.12
- Total Revenue: 25000
- Video Quality: 0.3 (low)
- Engagement: Low values

**High Engagement Creator**:
- Conversion Rate: 0.02
- Total Revenue: 2000
- Video Quality: 0.9 (high)
- Engagement: High values

2. Analyze both creators
3. Compare overall scores

**Expected Results**:
- High Revenue Creator should score higher
- Revenue focus should override engagement metrics
- Clear business alignment with e-commerce goals

## 🎯 Task 2: Revenue Optimization AI Pipeline Testing

### Test 2.1: Bottleneck Identification
**Objective**: Verify correct bottleneck identification for different scenarios

**Test Scenario 1: Low Conversion Rate**
1. Set these values in the dashboard:
   - Conversion Rate: 0.01
   - Total Revenue: 500
   - Video Quality: 0.8 (high)
   - Engagement: High values
2. Click "Analyze Creator"
3. Check recommendations

**Expected Results**:
- Top recommendation should focus on Sales Performance
- Priority should be high for conversion-related issues

**Test Scenario 2: High Cart Abandonment**
1. Set these values:
   - Conversion Rate: 0.08
   - Cart Abandonment Rate: 0.9
   - Funnel Completion Rate: 0.2
   - Other metrics: Moderate values
2. Click "Analyze Creator"
3. Check recommendations

**Expected Results**:
- Top recommendation should focus on Shop Conversion
- Should suggest funnel optimization actions

**Test Scenario 3: Poor Video Quality**
1. Set these values:
   - Video Quality: 0.1
   - Content Freshness: 0.3
   - Image Quality: 0.2
   - Other metrics: Moderate values
2. Click "Analyze Creator"
3. Check recommendations

**Expected Results**:
- Top recommendation should focus on Content Strategy
- Should suggest video quality improvements

### Test 2.2: Recommendation Quality
**Objective**: Verify recommendations are actionable and well-structured

**Steps**:
1. Use the demo data (click "Load Demo Data")
2. Click "Analyze Creator"
3. Review the generated recommendations

**Expected Results**:
- Recommendations should have clear titles
- Priority scores should be calculated
- Expected improvement percentages should be realistic (0-100%)
- Actions should be specific and actionable
- A/B test configurations should be complete
- Confidence scores should be provided

### Test 2.3: Revenue Optimization Focus
**Objective**: Verify revenue-focused optimization

**Steps**:
1. Create a creator with:
   - Low revenue metrics (conversion, revenue, AOV)
   - High engagement metrics (likes, comments, shares)
   - High content quality metrics
2. Analyze the creator
3. Review recommendations and insights

**Expected Results**:
- Revenue KPIs should be prioritized in recommendations
- Improvement potential should be calculated
- Priority actions should focus on revenue drivers
- Clear revenue focus in the analysis

## 🎨 Frontend Testing

### Test 3.1: Dashboard Functionality
**Objective**: Verify all frontend features work correctly

**Steps**:
1. Open http://localhost:8000/
2. Test form interactions:
   - Fill in various metric values
   - Use "Load Demo Data" button
   - Use "Reset Form" button
3. Test analysis features:
   - Click "Analyze Creator"
   - Click "Compare Algorithms"
4. Verify results display:
   - Overall score visualization
   - Individual KPI scores
   - Recommendations list
   - Tier breakdown

**Expected Results**:
- Form should accept all input values
- Demo data should populate correctly
- Analysis should complete successfully
- Results should display with proper formatting
- All buttons should be responsive

### Test 3.2: Responsive Design
**Objective**: Verify mobile and tablet compatibility

**Steps**:
1. Open dashboard on different screen sizes
2. Test on mobile device or browser dev tools
3. Verify all elements are accessible
4. Test form interactions on small screens

**Expected Results**:
- Layout should adapt to screen size
- All elements should be accessible
- Form should be usable on mobile
- Text should be readable

## ⚡ Performance Testing

### Test 4.1: Response Times
**Objective**: Verify acceptable performance

**Steps**:
1. Time the following operations:
   - Page load time
   - Demo data loading
   - Creator analysis
   - Algorithm comparison
2. Test with different data sets
3. Monitor for any timeouts

**Expected Results**:
- Page load: < 2 seconds
- Demo data: < 1 second
- Analysis: < 5 seconds
- Comparison: < 3 seconds

### Test 4.2: Concurrent Users
**Objective**: Verify system handles multiple requests

**Steps**:
1. Open multiple browser tabs
2. Run analysis in each tab simultaneously
3. Monitor system performance
4. Check for any errors

**Expected Results**:
- All requests should complete successfully
- No timeout errors
- Consistent response times

## 🐛 Common Issues & Solutions

### Issue: "ModuleNotFoundError: pydantic_settings"
**Solution**: Run with PYTHONPATH set:
```bash
PYTHONPATH=/home/ubuntu/Documents/Dev/AlgoTest/TikTokMetricsAIAgent python3 app.py
```

### Issue: "Address already in use"
**Solution**: Stop existing process:
```bash
pkill -f "python3 app.py"
```

### Issue: Frontend not loading
**Solution**: Check if static files are being served:
```bash
curl http://localhost:8000/static/css/dashboard.css
```

### Issue: API timeout
**Solution**: Check application logs:
```bash
tail -f app.log
```

## 📊 Success Criteria

### Task 1 Success Criteria
- [ ] Algorithm shows 8.6% improvement over equal weighting
- [ ] Revenue drivers have 55% total weight
- [ ] Revenue-focused creators score higher than engagement-focused
- [ ] Clear business alignment with e-commerce goals

### Task 2 Success Criteria
- [ ] Correct bottleneck identification for different scenarios
- [ ] Actionable recommendations with priority scoring
- [ ] Expected improvement calculations are realistic
- [ ] A/B test configurations are complete and valid
- [ ] Revenue-focused optimization is evident

### Frontend Success Criteria
- [ ] All form interactions work correctly
- [ ] Analysis results display properly
- [ ] Responsive design works on all devices
- [ ] Performance is acceptable (< 5s for analysis)

## 🚀 Automated Testing

For comprehensive automated testing, run:
```bash
python3 run_comprehensive_tests.py
```

This will execute all test suites and generate a detailed report.

## 📝 Test Documentation

After completing tests, document:
1. Test results and any issues found
2. Performance metrics observed
3. Recommendations for improvements
4. Overall system readiness assessment
