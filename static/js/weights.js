// TikTok Metrics AI Agent - Weights Visualization JavaScript

class WeightsVisualization {
    constructor() {
        this.apiBaseUrl = window.location.origin; // Use relative URLs
        console.log('WeightsVisualization initialized with API URL:', this.apiBaseUrl);
        this.init();
    }
    
    async init() {
        console.log('Starting weights loading...');
        await this.loadWeights();
    }
    
    async loadWeights() {
        try {
            console.log('Fetching weights from:', `${this.apiBaseUrl}/weights/api`);
            const response = await fetch(`${this.apiBaseUrl}/weights/api`, {
                method: 'GET',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                }
            });
            
            console.log('Response status:', response.status);
            console.log('Response ok:', response.ok);
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status} - ${response.statusText}`);
            }
            
            const data = await response.json();
            console.log('Weights data loaded successfully:', data);
            this.displayWeights(data);
        } catch (error) {
            console.error('Error loading weights:', error);
            this.showError(error.message);
        }
    }
    
    displayWeights(data) {
        console.log('Displaying weights data...');
        
        // Hide loading, show content
        const loadingEl = document.getElementById('loading');
        const contentEl = document.getElementById('content');
        
        if (loadingEl) loadingEl.style.display = 'none';
        if (contentEl) contentEl.style.display = 'block';
        
        // Update summary stats
        this.updateSummaryStats(data);
        
        // Create tier visualization
        this.createTierVisualization(data);
        
        // Create weights table
        this.createWeightsTable(data);
        
        console.log('Weights visualization completed successfully');
    }
    
    updateSummaryStats(data) {
        const tierBreakdown = data.tier_breakdown;
        
        const tier1El = document.getElementById('tier1Weight');
        const tier2El = document.getElementById('tier2Weight');
        const tier3El = document.getElementById('tier3Weight');
        
        if (tier1El) tier1El.textContent = `${(tierBreakdown.tier_1.total_weight * 100).toFixed(0)}%`;
        if (tier2El) tier2El.textContent = `${(tierBreakdown.tier_2.total_weight * 100).toFixed(0)}%`;
        if (tier3El) tier3El.textContent = `${(tierBreakdown.tier_3.total_weight * 100).toFixed(0)}%`;
    }
    
    createTierVisualization(data) {
        const container = document.getElementById('tierVisualization');
        if (!container) {
            console.error('Tier visualization container not found');
            return;
        }
        
        const tierBreakdown = data.tier_breakdown;
        const weights = data.weights;
        
        const tiers = [
            {
                id: 'tier_1',
                title: 'Tier 1: Revenue Drivers',
                description: 'Direct revenue and conversion metrics that directly impact e-commerce success',
                weight: tierBreakdown.tier_1.total_weight,
                kpis: tierBreakdown.tier_1.kpis,
                class: 'tier-1'
            },
            {
                id: 'tier_2',
                title: 'Tier 2: Revenue Enablers',
                description: 'Metrics that enable and support revenue generation through engagement and content quality',
                weight: tierBreakdown.tier_2.total_weight,
                kpis: tierBreakdown.tier_2.kpis,
                class: 'tier-2'
            },
            {
                id: 'tier_3',
                title: 'Tier 3: General Health',
                description: 'General content health, reach, and efficiency metrics for long-term sustainability',
                weight: tierBreakdown.tier_3.total_weight,
                kpis: tierBreakdown.tier_3.kpis,
                class: 'tier-3'
            }
        ];
        
        container.innerHTML = tiers.map(tier => `
            <div class="tier-card ${tier.class}">
                <div class="tier-header">
                    <div class="tier-title">${tier.title}</div>
                    <div class="tier-weight">${(tier.weight * 100).toFixed(0)}%</div>
                </div>
                <div class="tier-description">${tier.description}</div>
                <ul class="kpi-list">
                    ${tier.kpis.map(kpi => `
                        <li class="kpi-item">
                            <span class="kpi-name">${this.formatKPIName(kpi)}</span>
                            <span class="kpi-weight">${(weights[kpi] * 100).toFixed(0)}%</span>
                        </li>
                    `).join('')}
                </ul>
            </div>
        `).join('');
    }
    
    createWeightsTable(data) {
        const tbody = document.getElementById('weightsTableBody');
        if (!tbody) {
            console.error('Weights table body not found');
            return;
        }
        
        const weights = data.weights;
        const tierBreakdown = data.tier_breakdown;
        
        // Create mapping of KPI to tier
        const kpiToTier = {};
        Object.keys(tierBreakdown).forEach(tier => {
            tierBreakdown[tier].kpis.forEach(kpi => {
                kpiToTier[kpi] = tier;
            });
        });
        
        // Sort KPIs by weight (descending)
        const sortedKPIs = Object.entries(weights).sort((a, b) => b[1] - a[1]);
        
        tbody.innerHTML = sortedKPIs.map(([kpi, weight]) => {
            const tier = kpiToTier[kpi];
            const tierClass = tier.replace('_', '-');
            const tierName = tier.replace('_', ' ').replace(/\b\w/g, l => l.toUpperCase());
            
            return `
                <tr>
                    <td><strong>${this.formatKPIName(kpi)}</strong></td>
                    <td><span class="tier-badge ${tierClass}">${tierName}</span></td>
                    <td><strong>${(weight * 100).toFixed(1)}%</strong></td>
                    <td>
                        <div class="weight-bar">
                            <div class="weight-fill ${tierClass}" style="width: ${weight * 100}%"></div>
                        </div>
                    </td>
                </tr>
            `;
        }).join('');
    }
    
    formatKPIName(kpi) {
        return kpi.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
    }
    
    showError(message) {
        console.error('Showing error:', message);
        
        const loadingEl = document.getElementById('loading');
        const errorEl = document.getElementById('error');
        
        if (loadingEl) loadingEl.style.display = 'none';
        if (errorEl) {
            errorEl.style.display = 'block';
            const errorText = errorEl.querySelector('p');
            if (errorText) {
                errorText.textContent = `Failed to load algorithm weights: ${message}`;
            }
        }
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    console.log('DOM loaded, initializing Weights Visualization...');
    try {
        new WeightsVisualization();
    } catch (error) {
        console.error('Error initializing Weights Visualization:', error);
    }
});
