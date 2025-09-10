# Flight Data Exploratory Analysis

This repository contains a comprehensive exploratory data analysis (EDA) of airline route and fare data. The analysis examines 638 flight routes across the United States, providing insights into pricing patterns, market competition, and route characteristics.

## 📊 Dataset Overview

The `Airfares.csv` dataset contains information about:
- **638 flight routes** between 51 starting cities and 68 destination cities
- **18 variables** including fares, distances, passenger counts, and market characteristics
- **Route information**: Starting/ending cities and airport codes
- **Pricing data**: Ticket fares and fare types
- **Market data**: Southwest Airlines presence, vacation routes, airport restrictions
- **Demographics**: City income levels and populations
- **Competition metrics**: Market concentration indices and slot restrictions

### Data Dictionary

| Column | Description |
|--------|-------------|
| S_CODE, S_CITY | Starting airport code and city |
| E_CODE, E_CITY | Ending airport code and city |
| COUPON | Coupon fare type |
| NEW | New route indicator |
| VACATION | Vacation route (Yes/No) |
| SW | Southwest Airlines presence (Yes/No) |
| HI | Market concentration index |
| S_INCOME, E_INCOME | Starting and ending city income levels |
| S_POP, E_POP | Starting and ending city populations |
| SLOT, GATE | Airport slot and gate restrictions |
| DISTANCE | Route distance in miles |
| PAX | Number of passengers |
| FARE | Ticket fare in dollars |

## 🔍 Key Findings

### Fare Analysis
- **Average fare**: $160.88 (range: $42.47 - $402.02)
- **Strong distance correlation**: 0.670 correlation between fare and distance
- **Southwest Airlines impact**: 47.7% lower fares on routes with Southwest presence
- **Premium routes**: Transcontinental routes (Boston-San Jose, NYC-San Francisco) command highest fares

### Route Patterns
- **Top hubs**: Chicago (90 routes), New York/Newark (88 routes), Atlanta (41 routes)
- **Popular destinations**: New York/Newark (75 inbound), Washington DC (54 inbound)
- **Average distance**: 976 miles
- **Route range**: 114 miles (shortest) to 2,764 miles (longest)

### Market Competition
- **Southwest presence**: 30.4% of routes (194 routes)
- **Vacation routes**: 26.6% of routes (170 routes)
- **Airport restrictions**: 28.5% controlled slots, 19.4% constrained gates
- **Market concentration**: Average HI index of 4,442

### Demographics & Economics
- **Average city income**: ~$27,700 (both starting and destination cities)
- **Population impact**: Larger cities tend to have higher passenger volumes
- **Income correlation**: Higher-income cities show moderately higher fares

## 📁 Repository Structure

```
├── Airfares.csv                    # Raw flight data
├── flight_data_analysis.py         # Complete EDA script
├── flight_data_exploration.ipynb   # Interactive Jupyter notebook
├── README.md                       # This documentation
├── fare_analysis.png              # Fare analysis visualizations
├── route_analysis.png             # Route pattern visualizations
├── market_analysis.png            # Market characteristics charts
└── correlation_matrix.png         # Variable correlation heatmap
```

## 🚀 Getting Started

### Prerequisites
```bash
pip install pandas matplotlib seaborn numpy jupyter
```

### Running the Analysis

#### Option 1: Complete Script
```bash
python flight_data_analysis.py
```
This generates:
- Comprehensive console output with all findings
- Four visualization files (PNG format)
- Statistical summaries and business insights

#### Option 2: Interactive Jupyter Notebook
```bash
jupyter notebook flight_data_exploration.ipynb
```
This provides:
- Cell-by-cell interactive exploration
- Detailed explanations and methodology
- Customizable analysis parameters
- Rich visualizations and insights

## 📈 Analysis Components

### 1. Data Quality Assessment
- ✅ No missing values
- ✅ Minimal duplicates (4 rows)
- ✅ Consistent categorical values
- ✅ Appropriate data types

### 2. Descriptive Statistics
- Central tendencies and distributions
- Outlier identification
- Variable ranges and patterns

### 3. Fare Analysis
- Distribution patterns and pricing models
- Southwest Airlines competitive impact
- Distance-based pricing validation
- Premium route identification

### 4. Route Geography
- Hub and spoke network analysis
- Distance distributions
- Passenger volume patterns
- City-pair relationships

### 5. Market Competition
- Airport restriction impacts
- Market concentration effects
- Demographic correlations
- Competition intensity measures

### 6. Statistical Relationships
- Correlation matrix analysis
- Predictive variable identification
- Market driver quantification

## 💡 Business Insights & Recommendations

### Strategic Opportunities
1. **Competitive Pricing**: Southwest Airlines demonstrates significant fare reduction capability
2. **Premium Markets**: Transcontinental routes support premium pricing strategies
3. **Hub Strategy**: Focus on high-traffic metropolitan areas (Chicago, NYC, Atlanta)
4. **Market Entry**: Identify underserved high-income city pairs

### Operational Insights
1. **Distance-Based Pricing**: Strong correlation suggests distance is a primary fare driver
2. **Vacation Premium**: Leisure routes may support higher margins
3. **Slot Management**: Controlled airports show different pricing dynamics
4. **Capacity Planning**: Population correlates with passenger demand

### Market Dynamics
1. **Competition Impact**: Southwest presence significantly affects market pricing
2. **Market Concentration**: HI index indicates competitive intensity levels
3. **Geographic Patterns**: East-West routes command premium pricing
4. **Seasonal Opportunities**: Vacation routes suggest seasonal pricing potential

## 🔧 Technical Details

### Analysis Methodology
- **Exploratory Data Analysis (EDA)**: Comprehensive statistical exploration
- **Visualization**: Multiple chart types for pattern identification
- **Correlation Analysis**: Quantitative relationship measurement
- **Segmentation**: Market-based route categorization
- **Benchmarking**: Competitive positioning analysis

### Tools & Libraries
- **pandas**: Data manipulation and analysis
- **matplotlib**: Statistical visualizations
- **seaborn**: Advanced plotting and aesthetics
- **numpy**: Numerical computations
- **jupyter**: Interactive analysis environment

### Data Processing
- Automated data quality checks
- Statistical summary generation
- Correlation matrix computation
- Categorical variable analysis
- Outlier identification and handling

## 📊 Visualizations Generated

1. **Fare Analysis Charts**
   - Fare distribution histogram
   - Fare vs. distance scatter plot
   - Southwest Airlines impact comparison
   - Vacation route fare analysis

2. **Route Pattern Charts**
   - Top cities by route count
   - Distance distribution analysis
   - Passenger volume relationships

3. **Market Analysis Charts**
   - Airport restriction breakdowns
   - Income vs. fare correlations
   - Market concentration distributions

4. **Correlation Matrix**
   - Complete variable relationship heatmap
   - Statistical significance indicators

## 🎯 Use Cases

This analysis supports:
- **Airline Strategy**: Route planning and pricing optimization
- **Market Research**: Competitive landscape understanding
- **Investment Analysis**: Market opportunity assessment
- **Academic Research**: Transportation economics studies
- **Policy Analysis**: Aviation market regulation insights

## 📝 Future Enhancements

Potential extensions to this analysis:
- **Time Series Analysis**: Seasonal pricing patterns
- **Predictive Modeling**: Fare forecasting algorithms
- **Geographic Mapping**: Route visualization on maps
- **Economic Modeling**: Price elasticity analysis
- **Competitive Intelligence**: Dynamic pricing strategies

## 🤝 Contributing

Feel free to extend this analysis by:
1. Adding temporal analysis components
2. Implementing predictive models
3. Creating interactive dashboards
4. Expanding visualization capabilities
5. Including additional market variables

## 📄 License

This analysis is provided for educational and research purposes. Please ensure appropriate data usage compliance for commercial applications.

---

*Generated through comprehensive exploratory data analysis of airline route and fare data. For questions or suggestions, please open an issue or submit a pull request.*