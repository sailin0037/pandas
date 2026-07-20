import pandas as pd
import matplotlib.pyplot as plt

#Dataset
data = {
    'Price': [50, 60, 70, 80, 90, 100],
    'Bottles Sold': [120, 100, 85, 70, 50, 30]
}
df = pd.DataFrame(data)

#Cal Revenue
df['Revenue'] = df['Price'] * df['Bottles Sold']

#  Highest Revenue & Optimal Price
max_rev = df['Revenue'].max()
opt_price = df.loc[df['Revenue'].idxmax(), 'Price']

print("Price and sales preview:")
print(df)
print(f"\nHighest Revenue: ₹{max_rev}")
print(f"Optimal Price: ₹{opt_price}")

#Bar Chart: Price vs Revenue
plt.figure(figsize=(8, 5))
plt.bar(df['Price'], df['Revenue'], color='steelblue', edgecolor='black')
plt.xlabel('Price (₹)')
plt.ylabel('Revenue (₹)')
plt.title('Price vs Revenue Analysis')
plt.xticks(df['Price'])
plt.tight_layout()
plt.savefig("price_revenue_analysis.png")
print("\nSaved chart preview to: price_revenue_analysis.png")
