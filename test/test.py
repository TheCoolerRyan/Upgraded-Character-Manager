import pandas as pd
import matplotlib.pyplot as plt

# 1. Create a synthetic dataset representing monthly sales
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Electronics': [15000, 18000, 12000, 22000, 19000, 25000],
    'Apparel': [8000, 7500, 9000, 11000, 15000, 14000],
    'Home_Decor': [5000, 6000, 5500, 8000, 7000, 9500]
}

# Convert dictionary to a Pandas DataFrame
df = pd.DataFrame(data)

# 2. BASIC BAR CHART
# Comparing 'Electronics' sales across different months
df.plot(kind='bar', x='Month', y='Electronics', color='skyblue', figsize=(8, 5))
plt.title('Monthly Electronics Sales')
plt.ylabel('Sales ($)')
plt.xticks(rotation=0) # Keeps month labels horizontal
plt.show()

# 3. GROUPED BAR CHART
# Comparing all categories side-by-side
df.plot(kind='bar', x='Month', figsize=(10, 6))
plt.title('Sales Comparison by Category')
plt.ylabel('Sales ($)')
plt.legend(title='Category')
plt.show()

# 4. PIE CHART
# Showing the distribution of sales for the most recent month (June)
# .iloc[-1, 1:] selects the last row and excludes the 'Month' label
june_sales = df.iloc[-1, 1:] 
june_sales.plot(kind='pie', autopct='%1.1f%%', startangle=140, figsize=(7, 7))
plt.title(f"Sales Distribution for {df.iloc[-1, 0]}")
plt.ylabel('') # Hides the redundant y-label
plt.show()

# 5. LINE CHART
# Visualizing trends over time for all categories
df.plot(kind='line', x='Month', marker='o', figsize=(10, 6))
plt.title('Sales Trends Over Time')
plt.ylabel('Sales ($)')
plt.grid(True, linestyle='--', alpha=0.6) # Adds a subtle background grid
plt.show()
