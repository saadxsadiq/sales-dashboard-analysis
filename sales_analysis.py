
import pandas as pd

print("📊 SALES DASHBOARD ANALYSIS")
print("=" * 30)

# Load the data
df = pd.read_csv('simple_sales_analysis.csv')

print(f"✅ Loaded {len(df)} sales records")

# Basic statistics
total_revenue = df['total_revenue'].sum()
avg_sale = df['total_revenue'].mean()
total_orders = len(df)

print(f"\n💰 KEY METRICS:")
print(f"   • Total Revenue: ${total_revenue:,.2f}")
print(f"   • Average Sale: ${avg_sale:.2f}")
print(f"   • Total Orders: {total_orders:,}")

# Top performers
top_product = df.groupby('product')['total_revenue'].sum().sort_values(ascending=False)
top_region = df.groupby('region')['total_revenue'].sum().sort_values(ascending=False)

print(f"\n🏆 TOP PERFORMERS:")
print(f"   • Best Product: {top_product.index[0]} (${top_product.iloc[0]:,.2f})")
print(f"   • Best Region: {top_region.index[0]} (${top_region.iloc[0]:,.2f})")

# Monthly trends
df['date'] = pd.to_datetime(df['date'])
monthly_sales = df.groupby(df['date'].dt.month)['total_revenue'].sum()
best_month = monthly_sales.idxmax()

print(f"\n📈 TRENDS:")
print(f"   • Best Month: Month {best_month} (${monthly_sales[best_month]:,.2f})")
print(f"   • Growth Opportunity: Focus on {top_product.index[-1]} (lowest performer)")

print(f"\n✅ Analysis Complete! Ready for presentation.")
