#!/usr/bin/env python3
"""
Exploratory Data Analysis for Flight Data (Airfares.csv)
This script performs comprehensive analysis of airline route and fare data.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# Set up plotting style
plt.style.use('default')
sns.set_palette("husl")

class FlightDataAnalyzer:
    """Class to perform exploratory data analysis on flight data."""
    
    def __init__(self, data_file='Airfares.csv'):
        """Initialize the analyzer with the data file."""
        self.data_file = data_file
        self.df = None
        self.load_data()
    
    def load_data(self):
        """Load and prepare the flight data."""
        print(f"Loading data from {self.data_file}...")
        try:
            self.df = pd.read_csv(self.data_file)
            print(f"✅ Data loaded successfully: {self.df.shape[0]} rows, {self.df.shape[1]} columns")
        except FileNotFoundError:
            print(f"❌ Error: {self.data_file} not found!")
            return
        except Exception as e:
            print(f"❌ Error loading data: {e}")
            return
    
    def basic_info(self):
        """Display basic information about the dataset."""
        print("\n" + "="*60)
        print("BASIC DATASET INFORMATION")
        print("="*60)
        
        print(f"Dataset shape: {self.df.shape}")
        print(f"Memory usage: {self.df.memory_usage(deep=True).sum() / 1024:.2f} KB")
        
        print("\nColumn Information:")
        print("-" * 40)
        for i, col in enumerate(self.df.columns, 1):
            dtype = self.df[col].dtype
            null_count = self.df[col].isnull().sum()
            print(f"{i:2d}. {col:<15} | {str(dtype):<10} | {null_count} nulls")
        
        print("\nFirst 5 rows:")
        print("-" * 40)
        print(self.df.head())
        
        print("\nData types:")
        print("-" * 40)
        print(self.df.dtypes)
    
    def data_quality_check(self):
        """Check data quality and missing values."""
        print("\n" + "="*60)
        print("DATA QUALITY ANALYSIS")
        print("="*60)
        
        # Missing values
        missing_data = self.df.isnull().sum()
        missing_percent = (missing_data / len(self.df)) * 100
        
        print("Missing Values Summary:")
        print("-" * 30)
        missing_df = pd.DataFrame({
            'Missing Count': missing_data,
            'Percentage': missing_percent
        })
        print(missing_df[missing_df['Missing Count'] > 0])
        
        if missing_df['Missing Count'].sum() == 0:
            print("✅ No missing values found!")
        
        # Duplicate rows
        duplicates = self.df.duplicated().sum()
        print(f"\nDuplicate rows: {duplicates}")
        
        # Unique values in categorical columns
        print("\nUnique values in key columns:")
        print("-" * 30)
        categorical_cols = ['VACATION', 'SW', 'SLOT', 'GATE']
        for col in categorical_cols:
            if col in self.df.columns:
                unique_vals = self.df[col].unique()
                print(f"{col}: {unique_vals}")
    
    def descriptive_statistics(self):
        """Generate descriptive statistics for numerical variables."""
        print("\n" + "="*60)
        print("DESCRIPTIVE STATISTICS")
        print("="*60)
        
        # Numerical columns
        numerical_cols = self.df.select_dtypes(include=[np.number]).columns
        
        print("Numerical Variables Summary:")
        print("-" * 40)
        print(self.df[numerical_cols].describe().round(2))
        
        # Key insights
        print("\nKey Insights:")
        print("-" * 20)
        print(f"• Average fare: ${self.df['FARE'].mean():.2f}")
        print(f"• Fare range: ${self.df['FARE'].min():.2f} - ${self.df['FARE'].max():.2f}")
        print(f"• Average distance: {self.df['DISTANCE'].mean():.0f} miles")
        print(f"• Average passengers: {self.df['PAX'].mean():.0f}")
        print(f"• Total routes analyzed: {len(self.df)}")
        print(f"• Unique starting cities: {self.df['S_CITY'].nunique()}")
        print(f"• Unique ending cities: {self.df['E_CITY'].nunique()}")
    
    def fare_analysis(self):
        """Analyze fare patterns and distributions."""
        print("\n" + "="*60)
        print("FARE ANALYSIS")
        print("="*60)
        
        # Create subplots for fare analysis
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        fig.suptitle('Flight Fare Analysis', fontsize=16, fontweight='bold')
        
        # 1. Fare distribution
        axes[0, 0].hist(self.df['FARE'], bins=30, alpha=0.7, color='skyblue', edgecolor='black')
        axes[0, 0].set_title('Distribution of Fares')
        axes[0, 0].set_xlabel('Fare ($)')
        axes[0, 0].set_ylabel('Frequency')
        axes[0, 0].axvline(self.df['FARE'].mean(), color='red', linestyle='--', 
                          label=f'Mean: ${self.df["FARE"].mean():.2f}')
        axes[0, 0].legend()
        
        # 2. Fare vs Distance
        axes[0, 1].scatter(self.df['DISTANCE'], self.df['FARE'], alpha=0.6, color='green')
        axes[0, 1].set_title('Fare vs Distance')
        axes[0, 1].set_xlabel('Distance (miles)')
        axes[0, 1].set_ylabel('Fare ($)')
        
        # Add trend line
        z = np.polyfit(self.df['DISTANCE'], self.df['FARE'], 1)
        p = np.poly1d(z)
        axes[0, 1].plot(self.df['DISTANCE'], p(self.df['DISTANCE']), "r--", alpha=0.8)
        
        # 3. Fare by Southwest presence
        sw_fare = self.df.groupby('SW')['FARE'].mean()
        axes[1, 0].bar(sw_fare.index, sw_fare.values, color=['orange', 'purple'])
        axes[1, 0].set_title('Average Fare by Southwest Presence')
        axes[1, 0].set_xlabel('Southwest Airlines Present')
        axes[1, 0].set_ylabel('Average Fare ($)')
        
        # 4. Fare by vacation routes
        vacation_fare = self.df.groupby('VACATION')['FARE'].mean()
        axes[1, 1].bar(vacation_fare.index, vacation_fare.values, color=['coral', 'lightblue'])
        axes[1, 1].set_title('Average Fare by Route Type')
        axes[1, 1].set_xlabel('Vacation Route')
        axes[1, 1].set_ylabel('Average Fare ($)')
        
        plt.tight_layout()
        plt.savefig('fare_analysis.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        # Print fare insights
        print("\nFare Insights:")
        print("-" * 20)
        correlation = self.df['FARE'].corr(self.df['DISTANCE'])
        print(f"• Fare-Distance correlation: {correlation:.3f}")
        print(f"• Routes with Southwest Airlines: {(self.df['SW'] == 'Yes').sum()}")
        print(f"• Vacation routes: {(self.df['VACATION'] == 'Yes').sum()}")
        
        if 'Yes' in sw_fare.index and 'No' in sw_fare.index:
            sw_impact = ((sw_fare['No'] - sw_fare['Yes']) / sw_fare['No'] * 100)
            print(f"• Southwest Airlines fare reduction: {sw_impact:.1f}%")
    
    def route_analysis(self):
        """Analyze route patterns and geography."""
        print("\n" + "="*60)
        print("ROUTE ANALYSIS")
        print("="*60)
        
        # Top cities analysis
        print("Top 10 Starting Cities by Number of Routes:")
        print("-" * 45)
        top_start_cities = self.df['S_CITY'].value_counts().head(10)
        for i, (city, count) in enumerate(top_start_cities.items(), 1):
            print(f"{i:2d}. {city:<25} {count} routes")
        
        print("\nTop 10 Destination Cities by Number of Routes:")
        print("-" * 47)
        top_end_cities = self.df['E_CITY'].value_counts().head(10)
        for i, (city, count) in enumerate(top_end_cities.items(), 1):
            print(f"{i:2d}. {city:<25} {count} routes")
        
        # Distance analysis
        print(f"\nDistance Statistics:")
        print("-" * 20)
        print(f"• Shortest route: {self.df['DISTANCE'].min()} miles")
        print(f"• Longest route: {self.df['DISTANCE'].max()} miles")
        print(f"• Average distance: {self.df['DISTANCE'].mean():.0f} miles")
        
        # Create route visualizations
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        fig.suptitle('Route Analysis', fontsize=16, fontweight='bold')
        
        # 1. Top starting cities
        top_start_cities.head(8).plot(kind='barh', ax=axes[0, 0], color='lightgreen')
        axes[0, 0].set_title('Top Starting Cities')
        axes[0, 0].set_xlabel('Number of Routes')
        
        # 2. Top destination cities
        top_end_cities.head(8).plot(kind='barh', ax=axes[0, 1], color='lightcoral')
        axes[0, 1].set_title('Top Destination Cities')
        axes[0, 1].set_xlabel('Number of Routes')
        
        # 3. Distance distribution
        axes[1, 0].hist(self.df['DISTANCE'], bins=25, alpha=0.7, color='gold', edgecolor='black')
        axes[1, 0].set_title('Distribution of Route Distances')
        axes[1, 0].set_xlabel('Distance (miles)')
        axes[1, 0].set_ylabel('Frequency')
        
        # 4. Passengers vs Distance
        axes[1, 1].scatter(self.df['DISTANCE'], self.df['PAX'], alpha=0.6, color='purple')
        axes[1, 1].set_title('Passengers vs Distance')
        axes[1, 1].set_xlabel('Distance (miles)')
        axes[1, 1].set_ylabel('Passengers')
        
        plt.tight_layout()
        plt.savefig('route_analysis.png', dpi=300, bbox_inches='tight')
        plt.show()
    
    def market_analysis(self):
        """Analyze market characteristics and competition."""
        print("\n" + "="*60)
        print("MARKET ANALYSIS")
        print("="*60)
        
        # Airport slot and gate analysis
        print("Airport Restrictions Analysis:")
        print("-" * 30)
        slot_counts = self.df['SLOT'].value_counts()
        gate_counts = self.df['GATE'].value_counts()
        
        print("Slot Restrictions:")
        for slot_type, count in slot_counts.items():
            percentage = (count / len(self.df)) * 100
            print(f"  {slot_type}: {count} routes ({percentage:.1f}%)")
        
        print("Gate Restrictions:")
        for gate_type, count in gate_counts.items():
            percentage = (count / len(self.df)) * 100
            print(f"  {gate_type}: {count} routes ({percentage:.1f}%)")
        
        # Income analysis
        print(f"\nIncome Level Analysis:")
        print("-" * 25)
        print(f"• Average starting city income: ${self.df['S_INCOME'].mean():.0f}")
        print(f"• Average destination city income: ${self.df['E_INCOME'].mean():.0f}")
        
        # Population analysis
        print(f"\nPopulation Analysis:")
        print("-" * 20)
        print(f"• Average starting city population: {self.df['S_POP'].mean():,.0f}")
        print(f"• Average destination city population: {self.df['E_POP'].mean():,.0f}")
        
        # Create market analysis visualizations
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        fig.suptitle('Market Analysis', fontsize=16, fontweight='bold')
        
        # 1. Slot restrictions
        slot_counts.plot(kind='pie', ax=axes[0, 0], autopct='%1.1f%%', colors=['lightblue', 'orange'])
        axes[0, 0].set_title('Airport Slot Restrictions')
        axes[0, 0].set_ylabel('')
        
        # 2. Income correlation with fare
        axes[0, 1].scatter(self.df['S_INCOME'], self.df['FARE'], alpha=0.6, color='green', label='Starting City')
        axes[0, 1].scatter(self.df['E_INCOME'], self.df['FARE'], alpha=0.6, color='red', label='Destination City')
        axes[0, 1].set_title('City Income vs Fare')
        axes[0, 1].set_xlabel('City Income ($)')
        axes[0, 1].set_ylabel('Fare ($)')
        axes[0, 1].legend()
        
        # 3. Population vs Passengers
        axes[1, 0].scatter(self.df['S_POP'], self.df['PAX'], alpha=0.6, color='blue')
        axes[1, 0].set_title('Starting City Population vs Passengers')
        axes[1, 0].set_xlabel('Starting City Population')
        axes[1, 0].set_ylabel('Passengers')
        
        # 4. HI (Market concentration) distribution
        axes[1, 1].hist(self.df['HI'], bins=20, alpha=0.7, color='purple', edgecolor='black')
        axes[1, 1].set_title('Market Concentration Index (HI) Distribution')
        axes[1, 1].set_xlabel('HI Index')
        axes[1, 1].set_ylabel('Frequency')
        
        plt.tight_layout()
        plt.savefig('market_analysis.png', dpi=300, bbox_inches='tight')
        plt.show()
    
    def correlation_analysis(self):
        """Analyze correlations between variables."""
        print("\n" + "="*60)
        print("CORRELATION ANALYSIS")
        print("="*60)
        
        # Select numerical columns for correlation
        numerical_cols = self.df.select_dtypes(include=[np.number]).columns
        correlation_matrix = self.df[numerical_cols].corr()
        
        # Create correlation heatmap
        plt.figure(figsize=(12, 10))
        mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
        sns.heatmap(correlation_matrix, mask=mask, annot=True, cmap='coolwarm', center=0,
                   square=True, fmt='.2f', cbar_kws={"shrink": .8})
        plt.title('Correlation Matrix of Numerical Variables', fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.savefig('correlation_matrix.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        # Print strongest correlations with FARE
        print("Strongest correlations with FARE:")
        print("-" * 35)
        fare_corr = correlation_matrix['FARE'].abs().sort_values(ascending=False)
        for var, corr in fare_corr.items():
            if var != 'FARE' and abs(corr) > 0.1:  # Show correlations > 0.1
                direction = "positive" if correlation_matrix['FARE'][var] > 0 else "negative"
                print(f"• {var:<12}: {corr:.3f} ({direction})")
    
    def generate_summary_report(self):
        """Generate a comprehensive summary report."""
        print("\n" + "="*60)
        print("EXECUTIVE SUMMARY")
        print("="*60)
        
        print("Dataset Overview:")
        print("-" * 20)
        print(f"• Total routes analyzed: {len(self.df):,}")
        print(f"• Unique starting cities: {self.df['S_CITY'].nunique()}")
        print(f"• Unique destination cities: {self.df['E_CITY'].nunique()}")
        print(f"• Date range: Based on airfare data analysis")
        
        print("\nKey Findings:")
        print("-" * 15)
        
        # Fare insights
        avg_fare = self.df['FARE'].mean()
        print(f"• Average airfare: ${avg_fare:.2f}")
        
        # Distance insights
        avg_distance = self.df['DISTANCE'].mean()
        print(f"• Average route distance: {avg_distance:.0f} miles")
        
        # Southwest Airlines impact
        if 'Yes' in self.df['SW'].values and 'No' in self.df['SW'].values:
            sw_routes = (self.df['SW'] == 'Yes').sum()
            sw_percentage = (sw_routes / len(self.df)) * 100
            print(f"• Routes with Southwest Airlines: {sw_routes} ({sw_percentage:.1f}%)")
            
            sw_avg_fare = self.df[self.df['SW'] == 'Yes']['FARE'].mean()
            non_sw_avg_fare = self.df[self.df['SW'] == 'No']['FARE'].mean()
            if non_sw_avg_fare > sw_avg_fare:
                fare_reduction = ((non_sw_avg_fare - sw_avg_fare) / non_sw_avg_fare) * 100
                print(f"• Southwest Airlines provides {fare_reduction:.1f}% lower fares on average")
        
        # Vacation routes
        vacation_routes = (self.df['VACATION'] == 'Yes').sum()
        vacation_percentage = (vacation_routes / len(self.df)) * 100
        print(f"• Vacation routes: {vacation_routes} ({vacation_percentage:.1f}%)")
        
        # Market concentration
        high_concentration = (self.df['HI'] > self.df['HI'].median()).sum()
        print(f"• Routes with high market concentration: {high_concentration}")
        
        print("\nRecommendations:")
        print("-" * 18)
        
        # Find most profitable routes
        profitable_routes = self.df.nlargest(5, 'FARE')[['S_CITY', 'E_CITY', 'FARE', 'DISTANCE']]
        print("• Highest fare routes for premium pricing strategy:")
        for _, route in profitable_routes.iterrows():
            fare_per_mile = route['FARE'] / route['DISTANCE']
            print(f"  {route['S_CITY']} → {route['E_CITY']}: ${route['FARE']:.2f} (${fare_per_mile:.2f}/mile)")
        
        print("\n• Consider Southwest Airlines' competitive pricing strategy")
        print("• Focus on high-traffic routes between major metropolitan areas")
        print("• Vacation routes may command premium pricing")
    
    def run_complete_analysis(self):
        """Run the complete exploratory data analysis."""
        print("🛫 FLIGHT DATA EXPLORATORY ANALYSIS 🛬")
        print("=" * 60)
        
        if self.df is None:
            print("❌ No data available for analysis!")
            return
        
        # Run all analysis components
        self.basic_info()
        self.data_quality_check()
        self.descriptive_statistics()
        self.fare_analysis()
        self.route_analysis()
        self.market_analysis()
        self.correlation_analysis()
        self.generate_summary_report()
        
        print("\n" + "="*60)
        print("✅ ANALYSIS COMPLETE!")
        print("📊 Visualizations saved as PNG files")
        print("📈 Check the generated charts for detailed insights")
        print("="*60)

def main():
    """Main function to run the flight data analysis."""
    analyzer = FlightDataAnalyzer()
    analyzer.run_complete_analysis()

if __name__ == "__main__":
    main()