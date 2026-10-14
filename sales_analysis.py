
import pandas as pd
import matplotlib.pyplot as plt

# Sample sales data for practice
data = {
    "Product": ["Laptop", "Mobile", "Laptop", "Tablet", "Mobile",
                "Tablet", "Laptop", "Mobile", "Tablet", "Laptop"],
    "Category": ["Electronics", "Electronics", "Electronics",
                 "Electronics", "Electronics", "Electronics",
                 "Electronics", "Electronics", "Electronics",
                 "Electronics"],
    "Region": ["North", "South", "East", "West", "North",
               "South", "West", "East", "North", "South"],
    "Quantity": [2, 5, 3, 4, 6, 2, 1, 3, 5, 2],
    "Price": [50000, 15000, 50000, 20000, 15000,
              20000, 50000, 15000, 20000, 50000]
}

df = pd.DataFrame(data)

# Calculate revenue for each sale
df["Revenue"] = df["Quantity"] * df["Price"]
print("SALES DATA")
print(df.to_string(index=False))

print("\nTotal Revenue:", df["Revenue"].sum())

print("\nRevenue by Product:")
print(df.groupby("Product")["Revenue"].sum().sort_values(ascending=False))

print("\nRevenue by Region:")
print(df.groupby("Region")["Revenue"].sum().sort_values(ascending=False))

# 1. Revenue by Product
product_revenue = df.groupby("Product")["Revenue"].sum()

product_revenue.plot(kind="bar", title="Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (Rs.)")
plt.tight_layout()
plt.savefig("revenue_by_product.png")
plt.show()

# 2. Revenue by Region
region_revenue = df.groupby("Region")["Revenue"].sum()

region_revenue.plot(kind="bar", title="Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue (Rs.)")
plt.tight_layout()
plt.savefig("revenue_by_region.png")
plt.show()

# 3. Quantity Sold by Product
quantity_sold = df.groupby("Product")["Quantity"].sum()

quantity_sold.plot(kind="pie", autopct="%1.1f%%",
                   title="Quantity Sold by Product")
plt.ylabel("")
plt.tight_layout()
plt.savefig("quantity_by_product.png")
plt.show()

print("\nAll 3 charts saved successfully!")

# Business Insights and Report

total_revenue = df["Revenue"].sum()
total_quantity = df["Quantity"].sum()

product_revenue = df.groupby("Product")["Revenue"].sum()
region_revenue = df.groupby("Region")["Revenue"].sum()

top_product = product_revenue.idxmax()
top_region = region_revenue.idxmax()

report = f"""
BUSINESS SALES PERFORMANCE ANALYTICS
====================================

1. OVERVIEW
Total Revenue: Rs. {total_revenue:,.0f}
Total Units Sold: {total_quantity}
Total Sales Records: {len(df)}

2. PRODUCT PERFORMANCE
{product_revenue.sort_values(ascending=False).to_string()}

Top Revenue-Generating Product: {top_product}

3. REGIONAL PERFORMANCE
{region_revenue.sort_values(ascending=False).to_string()}

Best Performing Region: {top_region}

4. BUSINESS INSIGHTS
- {top_product} generates the highest revenue.
- {top_region} has the highest total revenue.
- Product and regional performance can guide business decisions.

5. RECOMMENDATIONS
- Study why the top product generates more revenue.
- Investigate opportunities to improve lower-performing regions.
- Monitor sales and revenue regularly.

NOTE:
This report uses a sample dataset for practice.
Results do not represent a real business.
"""

with open("business_report.txt", "w", encoding="utf-8") as file:
    file.write(report)

print("\nBusiness report created: business_report.txt")
print(report)
