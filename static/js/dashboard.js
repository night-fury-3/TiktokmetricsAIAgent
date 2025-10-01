// TikTok Metrics AI Agent - Dashboard JavaScript

class TikTokMetricsDashboard {
    constructor() {
        this.apiBaseUrl = 'http://localhost:8000';
        this.currentAnalysis = null;
        this.init();
    }

    init() {
        this.setupEventListeners();
        this.loadDemoData();
        this.checkAPIHealth();
    }

    setupEventListeners() {
        // Analyze button
        document.getElementById('analyzeBtn').addEventListener('click', () => {
            this.analyzeCreator();
        });

        // Demo data button
        document.getElementById('demoBtn').addEventListener('click', () => {
            this.loadDemoData();
        });

        // Compare algorithms button
        document.getElementById('compareBtn').addEventListener('click', () => {
            this.compareAlgorithms();
        });

        // Reset form button
        document.getElementById('resetBtn').addEventListener('click', () => {
            this.resetForm();
        });
    }

    async checkAPIHealth() {
        try {
            const response = await fetch(`${this.apiBaseUrl}/health`);
            const data = await response.json();
            
            const statusIndicator = document.querySelector('.status-indicator');
            if (data.status === 'healthy') {
                statusIndicator.textContent = '🟢 API Online';
                statusIndicator.style.background = 'linear-gradient(135deg, #27ae60, #2ecc71)';
            } else {
                statusIndicator.textContent = '🔴 API Offline';
                statusIndicator.style.background = 'linear-gradient(135deg, #e74c3c, #c0392b)';
            }
        } catch (error) {
            console.error('API Health Check Failed:', error);
            const statusIndicator = document.querySelector('.status-indicator');
            statusIndicator.textContent = '🔴 API Offline';
            statusIndicator.style.background = 'linear-gradient(135deg, #e74c3c, #c0392b)';
        }
    }

    async loadDemoData() {
        try {
            this.showLoading('Loading demo data...');
            
            const response = await fetch(`${this.apiBaseUrl}/demo-data`);
            const data = await response.json();
            
            if (data.success) {
                this.populateForm(data.demo_data);
                this.hideLoading();
                this.showNotification('Demo data loaded successfully!', 'success');
            } else {
                throw new Error('Failed to load demo data');
            }
        } catch (error) {
            console.error('Error loading demo data:', error);
            this.hideLoading();
            this.showNotification('Failed to load demo data', 'error');
        }
    }

    populateForm(data) {
        // Populate form fields with demo data
        const fields = [
            'creator_id', 'conversion_rate', 'total_revenue', 'avg_order_value',
            'funnel_completion_rate', 'cart_abandonment_rate', 'checkout_success_rate',
            'listing_quality', 'product_velocity', 'integration_seamlessness',
            'likes_ratio', 'comments_ratio', 'shares_ratio', 'retention_rate',
            'video_quality', 'content_freshness', 'posting_consistency',
            'target_demographic_match', 'audience_engagement_quality',
            'brand_alignment', 'trust_score', 'trend_alignment',
            'image_quality', 'lighting_score', 'total_reach', 'cost_per_acquisition'
        ];

        fields.forEach(field => {
            const input = document.getElementById(field);
            if (input && data[field] !== undefined) {
                input.value = data[field];
            }
        });
    }

    async analyzeCreator() {
        try {
            this.showLoading('Analyzing creator metrics...');
            
            const formData = this.getFormData();
            const response = await fetch(`${this.apiBaseUrl}/analyze`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData)
            });

            const data = await response.json();
            
            if (data.success) {
                this.currentAnalysis = data;
                this.displayAnalysis(data);
                this.hideLoading();
                this.showNotification('Analysis completed successfully!', 'success');
            } else {
                throw new Error(data.error || 'Analysis failed');
            }
        } catch (error) {
            console.error('Error analyzing creator:', error);
            this.hideLoading();
            this.showNotification('Analysis failed: ' + error.message, 'error');
        }
    }

    async compareAlgorithms() {
        try {
            this.showLoading('Comparing algorithms...');
            
            const formData = this.getFormData();
            const response = await fetch(`${this.apiBaseUrl}/compare-algorithms`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData)
            });

            const data = await response.json();
            
            if (data.success) {
                this.displayComparison(data.comparison);
                this.hideLoading();
                this.showNotification('Algorithm comparison completed!', 'success');
            } else {
                throw new Error('Comparison failed');
            }
        } catch (error) {
            console.error('Error comparing algorithms:', error);
            this.hideLoading();
            this.showNotification('Comparison failed: ' + error.message, 'error');
        }
    }

    getFormData() {
        const formData = {};
        const inputs = document.querySelectorAll('input[type="number"], input[type="text"]');
        
        inputs.forEach(input => {
            if (input.value !== '') {
                formData[input.id] = input.type === 'number' ? parseFloat(input.value) : input.value;
            }
        });

        return formData;
    }

    displayAnalysis(data) {
        // Update overall score
        this.updateOverallScore(data.overall_score, data.revenue_focus_score);
        
        // Update tier breakdown
        this.updateTierBreakdown(data.tier_breakdown);
        
        // Update individual scores
        this.updateIndividualScores(data.individual_scores, data.performance_levels);
        
        // Update recommendations
        this.updateRecommendations(data.recommendations);
        
        // Show analysis section
        document.getElementById('analysisSection').style.display = 'block';
        document.getElementById('analysisSection').scrollIntoView({ behavior: 'smooth' });
    }

    updateOverallScore(overallScore, revenueScore) {
        const scoreElement = document.querySelector('.overall-score');
        const scoreFill = document.querySelector('.score-fill');
        
        scoreElement.textContent = overallScore.toFixed(3);
        scoreFill.style.width = `${overallScore * 100}%`;
        
        // Update revenue focus score
        const revenueElement = document.getElementById('revenueScore');
        if (revenueElement) {
            revenueElement.textContent = revenueScore.toFixed(3);
        }
    }

    updateTierBreakdown(tierBreakdown) {
        const tiers = ['tier_1', 'tier_2', 'tier_3'];
        
        tiers.forEach(tier => {
            const tierData = tierBreakdown[tier];
            const tierElement = document.getElementById(tier);
            
            if (tierElement) {
                const weightElement = tierElement.querySelector('.tier-weight');
                const averageElement = tierElement.querySelector('.tier-average');
                
                if (weightElement) {
                    weightElement.textContent = `${(tierData.total_weight * 100).toFixed(0)}%`;
                }
                
                if (averageElement) {
                    averageElement.textContent = tierData.average_score.toFixed(3);
                }
            }
        });
    }

    updateIndividualScores(scores, performanceLevels) {
        const scoresContainer = document.getElementById('individualScores');
        scoresContainer.innerHTML = '';

        Object.entries(scores).forEach(([kpi, score]) => {
            const level = performanceLevels[kpi];
            const scoreItem = document.createElement('div');
            scoreItem.className = `score-item ${level}`;
            
            scoreItem.innerHTML = `
                <div class="score-item-name">${this.formatKPIName(kpi)}</div>
                <div class="score-item-value">${score.toFixed(3)}</div>
            `;
            
            scoresContainer.appendChild(scoreItem);
        });
    }

    updateRecommendations(recommendations) {
        const recommendationsContainer = document.getElementById('recommendations');
        recommendationsContainer.innerHTML = '';

        if (recommendations.length === 0) {
            recommendationsContainer.innerHTML = '<p>No specific recommendations at this time.</p>';
            return;
        }

        recommendations.forEach((rec, index) => {
            const recElement = document.createElement('div');
            recElement.className = 'recommendation-item fade-in';
            recElement.style.animationDelay = `${index * 0.1}s`;
            
            recElement.innerHTML = `
                <div class="recommendation-header">
                    <div class="recommendation-title">${rec.title}</div>
                    <div class="priority-badge">Priority: ${rec.priority_score.toFixed(1)}</div>
                </div>
                <div class="recommendation-meta">
                    <div class="meta-item">
                        <div class="meta-label">Expected Improvement</div>
                        <div class="meta-value">${(rec.expected_improvement * 100).toFixed(1)}%</div>
                    </div>
                    <div class="meta-item">
                        <div class="meta-label">Confidence</div>
                        <div class="meta-value">${(rec.confidence * 100).toFixed(1)}%</div>
                    </div>
                    <div class="meta-item">
                        <div class="meta-label">Effort</div>
                        <div class="meta-value">${rec.estimated_effort_hours}h</div>
                    </div>
                    <div class="meta-item">
                        <div class="meta-label">Cost Level</div>
                        <div class="meta-value">${rec.cost_level}</div>
                    </div>
                </div>
                <div class="actions-list">
                    <strong>Actions:</strong>
                    ${rec.actions.slice(0, 3).map(action => `<div class="action-item">${action}</div>`).join('')}
                </div>
            `;
            
            recommendationsContainer.appendChild(recElement);
        });
    }

    displayComparison(comparison) {
        const comparisonContainer = document.getElementById('comparisonResults');
        comparisonContainer.innerHTML = `
            <div class="card">
                <h3>📊 Algorithm Comparison Results</h3>
                <div class="comparison-grid">
                    <div class="comparison-item">
                        <div class="comparison-label">New Weighted Score</div>
                        <div class="comparison-value new">${comparison.new_weighted_score.toFixed(3)}</div>
                    </div>
                    <div class="comparison-item">
                        <div class="comparison-label">Equal Weighted Score</div>
                        <div class="comparison-value old">${comparison.equal_weighted_score.toFixed(3)}</div>
                    </div>
                    <div class="comparison-item">
                        <div class="comparison-label">Improvement</div>
                        <div class="comparison-value improvement">+${comparison.percentage_change.toFixed(1)}%</div>
                    </div>
                </div>
                <div class="comparison-benefits">
                    <h4>Algorithm Benefits:</h4>
                    <ul>
                        <li>✅ Revenue Alignment: Prioritizes direct revenue drivers (55% weight)</li>
                        <li>✅ Intervention Guidance: Identifies highest-impact improvement areas</li>
                        <li>✅ Business Focus: Aligns with e-commerce revenue maximization goal</li>
                    </ul>
                </div>
            </div>
        `;
        
        document.getElementById('comparisonSection').style.display = 'block';
        document.getElementById('comparisonSection').scrollIntoView({ behavior: 'smooth' });
    }

    formatKPIName(kpi) {
        return kpi.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
    }

    showLoading(message) {
        const loadingElement = document.getElementById('loading');
        loadingElement.innerHTML = `
            <div class="loading">
                <div class="spinner"></div>
                <p>${message}</p>
            </div>
        `;
        loadingElement.style.display = 'block';
    }

    hideLoading() {
        document.getElementById('loading').style.display = 'none';
    }

    showNotification(message, type) {
        const notification = document.createElement('div');
        notification.className = `notification ${type}`;
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            padding: 15px 20px;
            border-radius: 10px;
            color: white;
            font-weight: 600;
            z-index: 1000;
            animation: slideIn 0.3s ease;
            background: ${type === 'success' ? 'linear-gradient(135deg, #27ae60, #2ecc71)' : 'linear-gradient(135deg, #e74c3c, #c0392b)'};
        `;
        notification.textContent = message;
        
        document.body.appendChild(notification);
        
        setTimeout(() => {
            notification.remove();
        }, 3000);
    }

    resetForm() {
        document.querySelectorAll('input').forEach(input => {
            input.value = '';
        });
        document.getElementById('analysisSection').style.display = 'none';
        document.getElementById('comparisonSection').style.display = 'none';
        this.showNotification('Form reset successfully!', 'success');
    }
}

// Initialize dashboard when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new TikTokMetricsDashboard();
});
