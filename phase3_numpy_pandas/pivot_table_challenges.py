import pandas as pd

df = pd.read_csv("phase3_numpy_pandas/data/sales_data.csv")

print(df.head(), "\n\n")


# 1. Region-wise Total Sales
print("====  Challenge 1: Region-wise Total Sales  ====")
region_sales = df.pivot_table(values="Sales", index="Region", aggfunc="sum")
print(region_sales)
print("\n===============================\n")

# 2. Category-wise Profit Analysis
print("====  Challenge 2: Category-wise Profit Analysis  ====")
category_profit = df.pivot_table(values="Profit", index="Category", aggfunc="sum")
print(category_profit)
print("\n===============================\n")

# 3. Monthly Sales Trend
print("====  Challenge 3: Monthly Sales Trend  ====")
df["Month"] = pd.to_datetime(df["Date"]).dt.to_period("M")
monthly_sales = df.pivot_table(values="Sales", index="Month", aggfunc="sum")
print(monthly_sales)
print("\n===============================\n")

# 4. City vs Category Sales Matrix

print("====  Challenge 4: City vs Category Sales Matrix  ====")
city_category_sales = df.pivot_table(values="Sales", index="City", columns="Category", aggfunc="sum", fill_value=0)
print(city_category_sales)
print("\n===============================\n")

# 5. Top Performing Product
print("====  Challenge 5: Top Performing Product  ====")
top_product = df.pivot_table(values="Sales", index="Product", aggfunc="sum").sort_values(by="Sales", ascending=False).head(1)
print(top_product)
print("\n===============================\n")