#!/usr/bin/env python3
"""
Exploratory Data Analysis of drinks.csv
========================================

This script performs comprehensive exploratory data analysis on the drinks dataset,
which contains information about alcohol consumption by country.

Author: Data Analysis Script
Date: Generated for exploratory analysis
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Set up plotting style
plt.style.use('default')
sns.set_palette("husl")

def load_and_inspect_data():
    """Load the drinks dataset and perform basic inspection."""
    print("="*60)
    print("DRINKS DATASET - EXPLORATORY DATA ANALYSIS")
    print("="*60)
    
    # Load the data
    df = pd.read_csv('drinks.csv')
    
    print("\n1. BASIC DATASET INFORMATION")
    print("-" * 40)
    print(f"Dataset shape: {df.shape}")
    print(f"Number of countries: {df.shape[0]}")
    print(f"Number of features: {df.shape[1]}")
    
    print("\nColumn names and data types:")
    print(df.dtypes)
    
    print("\nFirst 5 rows:")
    print(df.head())
    
    print("\nLast 5 rows:")
    print(df.tail())
    
    return df

def check_data_quality(df):
    """Check for missing values, duplicates, and data quality issues."""
    print("\n2. DATA QUALITY ASSESSMENT")
    print("-" * 40)
    
    # Missing values
    missing_values = df.isnull().sum()
    print("Missing values per column:")
    print(missing_values)
    
    # Duplicates
    duplicates = df.duplicated().sum()
    print(f"\nNumber of duplicate rows: {duplicates}")
    
    # Check for negative values in numerical columns
    numerical_cols = ['beer_servings', 'spirit_servings', 'wine_servings', 'total_litres_of_pure_alcohol']
    print("\nChecking for negative values:")
    for col in numerical_cols:
        negative_count = (df[col] < 0).sum()
        print(f"{col}: {negative_count} negative values")
    
    # Unique values in categorical columns
    print(f"\nUnique countries: {df['country'].nunique()}")
    print(f"Unique continents: {df['continent'].nunique()}")
    print("\nContinents in dataset:")
    print(df['continent'].value_counts())
    
    return df

def descriptive_statistics(df):
    """Generate comprehensive descriptive statistics."""
    print("\n3. DESCRIPTIVE STATISTICS")
    print("-" * 40)
    
    numerical_cols = ['beer_servings', 'spirit_servings', 'wine_servings', 'total_litres_of_pure_alcohol']
    
    print("Summary statistics for numerical variables:")
    print(df[numerical_cols].describe())
    
    print("\nAdditional statistics:")
    for col in numerical_cols:
        data = df[col]
        print(f"\n{col}:")
        print(f"  Variance: {data.var():.2f}")
        print(f"  Standard Deviation: {data.std():.2f}")
        print(f"  Skewness: {stats.skew(data):.2f}")
        print(f"  Kurtosis: {stats.kurtosis(data):.2f}")
        print(f"  Range: {data.max() - data.min():.2f}")

def continent_analysis(df):
    """Analyze alcohol consumption patterns by continent."""
    print("\n4. ANALYSIS BY CONTINENT")
    print("-" * 40)
    
    numerical_cols = ['beer_servings', 'spirit_servings', 'wine_servings', 'total_litres_of_pure_alcohol']
    
    # Group by continent and calculate statistics
    continent_stats = df.groupby('continent')[numerical_cols].agg(['mean', 'median', 'std', 'min', 'max'])
    
    print("Average consumption by continent:")
    print(continent_stats.round(2))
    
    # Countries per continent
    print("\nNumber of countries per continent:")
    continent_counts = df['continent'].value_counts()
    print(continent_counts)
    
    # Highest consuming continent for each alcohol type
    print("\nHighest average consumption by continent:")
    avg_by_continent = df.groupby('continent')[numerical_cols].mean()
    for col in numerical_cols:
        highest_continent = avg_by_continent[col].idxmax()
        highest_value = avg_by_continent[col].max()
        print(f"{col}: {highest_continent} ({highest_value:.2f})")

def correlation_analysis(df):
    """Analyze correlations between different types of alcohol consumption."""
    print("\n5. CORRELATION ANALYSIS")
    print("-" * 40)
    
    numerical_cols = ['beer_servings', 'spirit_servings', 'wine_servings', 'total_litres_of_pure_alcohol']
    correlation_matrix = df[numerical_cols].corr()
    
    print("Correlation matrix:")
    print(correlation_matrix.round(3))
    
    # Find strongest correlations
    print("\nStrongest positive correlations (excluding self-correlations):")
    corr_pairs = []
    for i in range(len(numerical_cols)):
        for j in range(i+1, len(numerical_cols)):
            corr_val = correlation_matrix.iloc[i, j]
            corr_pairs.append((numerical_cols[i], numerical_cols[j], corr_val))
    
    corr_pairs.sort(key=lambda x: abs(x[2]), reverse=True)
    for var1, var2, corr in corr_pairs:
        print(f"{var1} vs {var2}: {corr:.3f}")

def top_consumers_analysis(df):
    """Identify top and bottom consumers for each type of alcohol."""
    print("\n6. TOP AND BOTTOM CONSUMERS")
    print("-" * 40)
    
    alcohol_types = ['beer_servings', 'spirit_servings', 'wine_servings', 'total_litres_of_pure_alcohol']
    
    for alcohol_type in alcohol_types:
        print(f"\n{alcohol_type.upper().replace('_', ' ')}:")
        
        # Top 5 consumers
        top_5 = df.nlargest(5, alcohol_type)[['country', alcohol_type]]
        print("Top 5 consumers:")
        for idx, row in top_5.iterrows():
            print(f"  {row['country']}: {row[alcohol_type]}")
        
        # Bottom 5 consumers (excluding zeros for better insight)
        non_zero = df[df[alcohol_type] > 0]
        if len(non_zero) >= 5:
            bottom_5 = non_zero.nsmallest(5, alcohol_type)[['country', alcohol_type]]
            print("Bottom 5 consumers (excluding zeros):")
            for idx, row in bottom_5.iterrows():
                print(f"  {row['country']}: {row[alcohol_type]}")
        
        # Count of zero consumers
        zero_count = (df[alcohol_type] == 0).sum()
        print(f"Countries with zero consumption: {zero_count}")

def outlier_analysis(df):
    """Identify outliers in the dataset."""
    print("\n7. OUTLIER ANALYSIS")
    print("-" * 40)
    
    numerical_cols = ['beer_servings', 'spirit_servings', 'wine_servings', 'total_litres_of_pure_alcohol']
    
    for col in numerical_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
        
        print(f"\n{col}:")
        print(f"  IQR range: {Q1:.2f} - {Q3:.2f}")
        print(f"  Outlier bounds: {lower_bound:.2f} - {upper_bound:.2f}")
        print(f"  Number of outliers: {len(outliers)}")
        
        if len(outliers) > 0:
            print("  Outlier countries:")
            for idx, row in outliers.iterrows():
                print(f"    {row['country']}: {row[col]}")

def create_visualizations(df):
    """Create comprehensive visualizations of the data."""
    print("\n8. CREATING VISUALIZATIONS")
    print("-" * 40)
    
    # Set up the plotting area
    plt.figure(figsize=(20, 15))
    
    numerical_cols = ['beer_servings', 'spirit_servings', 'wine_servings', 'total_litres_of_pure_alcohol']
    
    # 1. Distribution plots
    plt.subplot(3, 4, 1)
    for i, col in enumerate(numerical_cols):
        plt.subplot(3, 4, i+1)
        plt.hist(df[col], bins=20, alpha=0.7, edgecolor='black')
        plt.title(f'Distribution of {col.replace("_", " ").title()}')
        plt.xlabel(col.replace('_', ' ').title())
        plt.ylabel('Frequency')
    
    # 2. Box plots by continent
    plt.subplot(3, 4, 5)
    df_melted = df.melt(id_vars=['country', 'continent'], 
                        value_vars=numerical_cols,
                        var_name='alcohol_type', 
                        value_name='servings')
    
    for i, col in enumerate(numerical_cols):
        plt.subplot(3, 4, i+5)
        col_data = df_melted[df_melted['alcohol_type'] == col]
        sns.boxplot(data=col_data, x='continent', y='servings')
        plt.title(f'{col.replace("_", " ").title()} by Continent')
        plt.xticks(rotation=45)
    
    # 3. Correlation heatmap
    plt.subplot(3, 4, 9)
    correlation_matrix = df[numerical_cols].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
    plt.title('Correlation Matrix')
    
    # 4. Scatter plot: Total alcohol vs individual types
    plt.subplot(3, 4, 10)
    plt.scatter(df['beer_servings'], df['total_litres_of_pure_alcohol'], alpha=0.6)
    plt.xlabel('Beer Servings')
    plt.ylabel('Total Litres of Pure Alcohol')
    plt.title('Beer vs Total Alcohol Consumption')
    
    plt.subplot(3, 4, 11)
    plt.scatter(df['wine_servings'], df['total_litres_of_pure_alcohol'], alpha=0.6)
    plt.xlabel('Wine Servings')
    plt.ylabel('Total Litres of Pure Alcohol')
    plt.title('Wine vs Total Alcohol Consumption')
    
    plt.subplot(3, 4, 12)
    plt.scatter(df['spirit_servings'], df['total_litres_of_pure_alcohol'], alpha=0.6)
    plt.xlabel('Spirit Servings')
    plt.ylabel('Total Litres of Pure Alcohol')
    plt.title('Spirits vs Total Alcohol Consumption')
    
    plt.tight_layout()
    plt.savefig('drinks_analysis_plots.png', dpi=300, bbox_inches='tight')
    print("Visualizations saved as 'drinks_analysis_plots.png'")
    
    # Additional plot: Average consumption by continent
    plt.figure(figsize=(12, 8))
    avg_by_continent = df.groupby('continent')[numerical_cols].mean()
    
    plt.subplot(2, 2, 1)
    avg_by_continent['beer_servings'].plot(kind='bar')
    plt.title('Average Beer Consumption by Continent')
    plt.ylabel('Servings')
    plt.xticks(rotation=45)
    
    plt.subplot(2, 2, 2)
    avg_by_continent['spirit_servings'].plot(kind='bar')
    plt.title('Average Spirit Consumption by Continent')
    plt.ylabel('Servings')
    plt.xticks(rotation=45)
    
    plt.subplot(2, 2, 3)
    avg_by_continent['wine_servings'].plot(kind='bar')
    plt.title('Average Wine Consumption by Continent')
    plt.ylabel('Servings')
    plt.xticks(rotation=45)
    
    plt.subplot(2, 2, 4)
    avg_by_continent['total_litres_of_pure_alcohol'].plot(kind='bar')
    plt.title('Average Total Alcohol Consumption by Continent')
    plt.ylabel('Litres')
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.savefig('continent_comparison.png', dpi=300, bbox_inches='tight')
    print("Continent comparison saved as 'continent_comparison.png'")

def generate_insights(df):
    """Generate key insights and conclusions from the analysis."""
    print("\n9. KEY INSIGHTS AND CONCLUSIONS")
    print("-" * 40)
    
    numerical_cols = ['beer_servings', 'spirit_servings', 'wine_servings', 'total_litres_of_pure_alcohol']
    
    # Global averages
    global_avg = df[numerical_cols].mean()
    print("Global average consumption:")
    for col in numerical_cols:
        print(f"  {col.replace('_', ' ').title()}: {global_avg[col]:.2f}")
    
    # Continent with highest consumption
    continent_avg = df.groupby('continent')[numerical_cols].mean()
    print("\nHighest consuming continents:")
    for col in numerical_cols:
        highest = continent_avg[col].idxmax()
        value = continent_avg[col].max()
        print(f"  {col.replace('_', ' ').title()}: {highest} ({value:.2f})")
    
    # Most alcohol-consuming country overall
    top_country = df.loc[df['total_litres_of_pure_alcohol'].idxmax()]
    print(f"\nHighest overall alcohol consumption: {top_country['country']} ({top_country['total_litres_of_pure_alcohol']:.2f} litres)")
    
    # Countries with no alcohol consumption
    no_alcohol = df[df['total_litres_of_pure_alcohol'] == 0]
    print(f"\nCountries with no recorded alcohol consumption: {len(no_alcohol)}")
    if len(no_alcohol) > 0:
        print("Countries:", ", ".join(no_alcohol['country'].tolist()))
    
    # Correlation insights
    correlation_matrix = df[numerical_cols].corr()
    highest_corr = correlation_matrix.loc['beer_servings', 'total_litres_of_pure_alcohol']
    print(f"\nBeer consumption has the strongest correlation with total alcohol consumption: {highest_corr:.3f}")

def main():
    """Main function to run the complete exploratory data analysis."""
    try:
        # Load and inspect data
        df = load_and_inspect_data()
        
        # Perform various analyses
        check_data_quality(df)
        descriptive_statistics(df)
        continent_analysis(df)
        correlation_analysis(df)
        top_consumers_analysis(df)
        outlier_analysis(df)
        create_visualizations(df)
        generate_insights(df)
        
        print("\n" + "="*60)
        print("EXPLORATORY DATA ANALYSIS COMPLETED SUCCESSFULLY")
        print("="*60)
        print("\nOutput files generated:")
        print("- drinks_analysis_plots.png: Main analysis visualizations")
        print("- continent_comparison.png: Continent-wise comparison charts")
        
    except FileNotFoundError:
        print("Error: drinks.csv file not found in current directory.")
        print("Please ensure the file exists and try again.")
    except Exception as e:
        print(f"An error occurred during analysis: {str(e)}")

if __name__ == "__main__":
    main()