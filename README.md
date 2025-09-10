# Drinks Dataset - Exploratory Data Analysis

## Overview
This repository contains exploratory data analysis of the `drinks.csv` dataset, which provides comprehensive information about alcohol consumption patterns across 193 countries worldwide.

## Dataset Description
The dataset contains the following columns:
- **country**: Name of the country
- **beer_servings**: Number of beer servings consumed on average per person per year
- **spirit_servings**: Number of spirit servings consumed on average per person per year  
- **wine_servings**: Number of wine servings consumed on average per person per year
- **total_litres_of_pure_alcohol**: Total liters of pure alcohol consumed per person per year
- **continent**: The continent each country belongs to

**Dataset Statistics:**
- 193 countries across 6 continents
- No missing values
- No duplicate records
- All numerical values are non-negative

## Key Findings

### 1. Global Consumption Patterns
- **Average beer consumption**: 106.16 servings per person per year
- **Average spirit consumption**: 80.99 servings per person per year
- **Average wine consumption**: 49.45 servings per person per year
- **Average total alcohol**: 4.72 litres of pure alcohol per person per year

### 2. Continental Analysis
**Distribution of countries by continent:**
- Africa: 53 countries
- Europe: 45 countries
- Asia: 44 countries
- North America: 23 countries
- Oceania: 16 countries
- South America: 12 countries

**Highest consuming continents:**
- **Beer**: Europe (193.78 servings/year)
- **Spirits**: North America (165.74 servings/year)
- **Wine**: Europe (142.22 servings/year)
- **Total Alcohol**: Europe (8.62 litres/year)

### 3. Top Consumers by Category

**Beer (servings/year):**
1. Namibia (376)
2. Czech Republic (361)
3. Gabon (347)
4. Germany (346)
5. Lithuania (343)

**Spirits (servings/year):**
1. Grenada (438)
2. Belarus (373)
3. Haiti (326)
4. Russian Federation (326)
5. St. Lucia (315)

**Wine (servings/year):**
1. France (370)
2. Portugal (339)
3. Andorra (312)
4. Switzerland (280)
5. Denmark (278)

**Total Alcohol (litres/year):**
1. Belarus (14.4)
2. Lithuania (12.9)
3. Andorra (12.4)
4. Grenada (11.9)
5. Czech Republic (11.8)

### 4. Countries with Zero Alcohol Consumption
13 countries report zero alcohol consumption:
Afghanistan, Bangladesh, North Korea, Iran, Kuwait, Libya, Maldives, Marshall Islands, Mauritania, Monaco, Pakistan, San Marino, Somalia

### 5. Correlation Analysis
Strong positive correlations found between alcohol types and total consumption:
- **Beer vs Total alcohol**: 0.836 (strongest correlation)
- **Wine vs Total alcohol**: 0.668
- **Spirits vs Total alcohol**: 0.655
- **Beer vs Wine**: 0.527
- **Beer vs Spirits**: 0.459
- **Spirits vs Wine**: 0.195 (weakest correlation)

### 6. Statistical Insights
- **Beer consumption** shows moderate right skewness (0.81)
- **Spirit consumption** is more heavily right-skewed (1.28)
- **Wine consumption** is the most right-skewed (1.89)
- **Total alcohol consumption** shows slight right skewness (0.43)

### 7. Outlier Analysis
- **Spirits**: 5 outlier countries (Belarus, Grenada, Haiti, Russian Federation, St. Lucia)
- **Wine**: 26 outlier countries, mostly European nations with high wine consumption
- **Beer and Total Alcohol**: No significant outliers detected

## Data Quality
✅ **Complete dataset** - No missing values  
✅ **Clean data** - No negative values or inconsistencies  
✅ **Unique records** - No duplicate countries  
✅ **Consistent format** - All data properly formatted  

## Files in this Analysis

### Scripts and Dependencies
- `exploratory_analysis.py` - Main analysis script with comprehensive EDA
- `requirements.txt` - Python package dependencies

### Data
- `drinks.csv` - Original dataset

### Output
- `drinks_analysis_plots.png` - Main visualization dashboard
- `continent_comparison.png` - Continent-wise comparison charts
- `README.md` - This documentation file

## Running the Analysis

### Prerequisites
```bash
pip install -r requirements.txt
```

### Execute Analysis
```bash
python exploratory_analysis.py
```

This will generate:
1. Comprehensive console output with detailed statistics
2. Visualization files (PNG format)
3. Complete exploratory data analysis results

## Methodology
The analysis follows standard EDA practices:
1. **Data Inspection** - Basic structure and quality assessment
2. **Descriptive Statistics** - Central tendency, spread, and distribution
3. **Categorical Analysis** - Continent-wise breakdown
4. **Correlation Analysis** - Relationships between variables
5. **Outlier Detection** - Using IQR method
6. **Visualization** - Multiple chart types for different insights

## Key Insights Summary
1. **Europe dominates** in beer, wine, and total alcohol consumption
2. **North America leads** in spirit consumption  
3. **Beer consumption** is the strongest predictor of total alcohol consumption
4. **Wide variation** exists both within and between continents
5. **Cultural/religious factors** likely influence zero-consumption countries
6. **Wine consumption** shows the highest variability and skewness

## Future Analysis Opportunities
- Economic correlation analysis (GDP vs consumption)
- Population-weighted regional analysis
- Time series analysis if historical data available
- Health outcome correlations
- Cultural and religious factor analysis

---

*Analysis generated using Python with pandas, matplotlib, seaborn, and scipy libraries.*