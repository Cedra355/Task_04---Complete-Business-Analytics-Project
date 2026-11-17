import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(
    "Dataset/Sample - Superstore.csv",
    encoding="cp1252"
)

# Display first five records
print("========== FIRST FIVE RECORDS ==========")
print(df.head())

# Display dataset information
print("\n========== DATASET INFORMATION ==========")
print(df.info())

# Display dataset dimensions
print("\n========== DATASET SHAPE ==========")
print(df.shape)

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

print("\n========== DUPLICATE ROWS ==========")
print(df.duplicated().sum())

# Remove duplicate records
df = df.drop_duplicates()

print("\n========== AFTER DUPLICATE REMOVAL ==========")
print("Dataset Shape:", df.shape)
print("Duplicate Rows:", df.duplicated().sum())

# Convert date columns
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

# Convert numerical columns
df["Sales"] = pd.to_numeric(df["Sales"])
df["Profit"] = pd.to_numeric(df["Profit"])
df["Quantity"] = pd.to_numeric(df["Quantity"])
df["Discount"] = pd.to_numeric(df["Discount"])

print("\n========== UPDATED DATA TYPES ==========")
print(df.dtypes)

# Check outliers using IQR method

columns = ["Sales", "Profit", "Quantity", "Discount"]

print("\n========== OUTLIER ANALYSIS ==========")

for column in columns:
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    outliers = df[
        (df[column] < lower_limit) |
        (df[column] > upper_limit)
    ]

    print(f"{column}: {len(outliers)} outliers")

    # Feature Engineering

df["Order Year"] = df["Order Date"].dt.year

df["Order Month"] = df["Order Date"].dt.month

df["Shipping Days"] = (
    df["Ship Date"] - df["Order Date"]
).dt.days

df["Profit Margin"] = (
    df["Profit"] / df["Sales"]
) * 100

print("\n========== FEATURE ENGINEERING ==========")
print(df[[
    "Order Year",
    "Order Month",
    "Shipping Days",
    "Profit Margin"
]].head())

print("\nUpdated Dataset Shape:", df.shape)

# Business KPI Analysis

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
total_customers = df["Customer ID"].nunique()

average_order_value = total_sales / total_orders
profit_margin = (total_profit / total_sales) * 100

print("\n========== BUSINESS KPIs ==========")

print("Total Sales:", round(total_sales, 2))
print("Total Profit:", round(total_profit, 2))
print("Total Orders:", total_orders)
print("Total Customers:", total_customers)
print("Average Order Value:", round(average_order_value, 2))
print("Profit Margin:", round(profit_margin, 2), "%")

# Monthly Sales Analysis

monthly_sales = df.groupby(
    ["Order Year", "Order Month"]
)["Sales"].sum().reset_index()

print("\n========== MONTHLY SALES ==========")
print(monthly_sales.head(15))

# Save monthly sales chart
plt.figure(figsize=(12, 6))

plt.plot(
    range(len(monthly_sales)),
    monthly_sales["Sales"],
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True)

plt.tight_layout()
plt.savefig("Dataset/Monthly_Sales_Trend.png")
plt.show()

# Sales by Category

category_sales = df.groupby("Category")["Sales"].sum().sort_values(
    ascending=False
)

print("\n========== SALES BY CATEGORY ==========")
print(category_sales)

plt.figure(figsize=(8, 5))

category_sales.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig(".DatasetSales_by_Category.png")
plt.show()

# Profit by Category

category_profit = df.groupby("Category")["Profit"].sum().sort_values(
    ascending=False
)

print("\n========== PROFIT BY CATEGORY ==========")
print(category_profit)

plt.figure(figsize=(8, 5))

category_profit.plot(kind="bar")

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Total Profit")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig(".DatasetProfit_by_Category.png")
plt.show()

# Sales by Region

region_sales = df.groupby("Region")["Sales"].sum().sort_values(
    ascending=False
)

print("\n========== SALES BY REGION ==========")
print(region_sales)

plt.figure(figsize=(8, 5))

region_sales.plot(kind="bar")

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig(".DatasetSales_by_Region.png")
plt.show()

# Profit by Region

region_profit = df.groupby("Region")["Profit"].sum().sort_values(
    ascending=False
)

print("\n========== PROFIT BY REGION ==========")
print(region_profit)

plt.figure(figsize=(8, 5))

region_profit.plot(kind="bar")

plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Total Profit")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig(".DatasetProfit_by_Region.png")
plt.show()

# Sales by Customer Segment

segment_sales = df.groupby("Segment")["Sales"].sum().sort_values(
    ascending=False
)

print("\n========== SALES BY SEGMENT ==========")
print(segment_sales)

plt.figure(figsize=(8, 5))

segment_sales.plot(kind="bar")

plt.title("Sales by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig(".DatasetSales_by_Segment.png")
plt.show()

# Profit by Customer Segment

segment_profit = df.groupby("Segment")["Profit"].sum().sort_values(
    ascending=False
)

print("\n========== PROFIT BY SEGMENT ==========")
print(segment_profit)

plt.figure(figsize=(8, 5))

segment_profit.plot(kind="bar")

plt.title("Profit by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Total Profit")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig(".DatasetProfit_by_Segment.png")
plt.show()

# Top 10 Products by Sales

top_products = df.groupby("Product Name")["Sales"].sum().sort_values(
    ascending=False
).head(10)

print("\n========== TOP 10 PRODUCTS BY SALES ==========")
print(top_products)

plt.figure(figsize=(12, 6))

top_products.sort_values().plot(kind="barh")

plt.title("Top 10 Products by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Product Name")

plt.tight_layout()
plt.savefig(".DatasetTop_10_Products_by_Sales.png")
plt.show()

# Top 10 Customers by Sales

top_customers = df.groupby("Customer Name")["Sales"].sum().sort_values(
    ascending=False
).head(10)

print("\n========== TOP 10 CUSTOMERS BY SALES ==========")
print(top_customers)

plt.figure(figsize=(12, 6))

top_customers.sort_values().plot(kind="barh")

plt.title("Top 10 Customers by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Customer Name")

plt.tight_layout()
plt.savefig(".DatasetTop_10_Customers_by_Sales.png")
plt.show()

# Sales by Ship Mode

ship_sales = df.groupby("Ship Mode")["Sales"].sum().sort_values(
    ascending=False
)

print("\n========== SALES BY SHIP MODE ==========")
print(ship_sales)

plt.figure(figsize=(8, 5))

ship_sales.plot(kind="bar")

plt.title("Sales by Shipping Mode")
plt.xlabel("Ship Mode")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("Dataset/Sales_by_Ship_Mode.png")
plt.show()

# Sales by Sub-Category

subcategory_sales = df.groupby("Sub-Category")["Sales"].sum().sort_values(
    ascending=False
)

print("\n========== SALES BY SUB-CATEGORY ==========")
print(subcategory_sales)

plt.figure(figsize=(12, 6))

subcategory_sales.sort_values().plot(kind="barh")

plt.title("Sales by Sub-Category")
plt.xlabel("Total Sales")
plt.ylabel("Sub-Category")

plt.tight_layout()
plt.savefig("Dataset/Sales_by_Subcategory.png")
plt.show()

# Profit by Sub-Category

subcategory_profit = df.groupby("Sub-Category")["Profit"].sum().sort_values(
    ascending=False
)

print("\n========== PROFIT BY SUB-CATEGORY ==========")
print(subcategory_profit)

plt.figure(figsize=(12, 6))

subcategory_profit.sort_values().plot(kind="barh")

plt.title("Profit by Sub-Category")
plt.xlabel("Total Profit")
plt.ylabel("Sub-Category")

plt.tight_layout()
plt.savefig("Dataset/Profit_by_Subcategory.png")
plt.show()

# Monthly Profit Analysis

monthly_profit = df.groupby(
    ["Order Year", "Order Month"]
)["Profit"].sum().reset_index()

print("\n========== MONTHLY PROFIT ==========")
print(monthly_profit.head(15))

plt.figure(figsize=(12, 6))

plt.plot(
    range(len(monthly_profit)),
    monthly_profit["Profit"],
    marker="o"
)

plt.title("Monthly Profit Trend")
plt.xlabel("Month")
plt.ylabel("Total Profit")
plt.grid(True)

plt.tight_layout()
plt.savefig("Dataset/Monthly_Profit_Trend.png")
plt.show()

# Discount vs Profit Analysis

discount_profit = df.groupby("Discount")["Profit"].mean()

print("\n========== DISCOUNT VS PROFIT ==========")
print(discount_profit)

plt.figure(figsize=(10, 6))

plt.plot(
    discount_profit.index,
    discount_profit.values,
    marker="o"
)

plt.title("Impact of Discount on Average Profit")
plt.xlabel("Discount")
plt.ylabel("Average Profit")
plt.grid(True)

plt.tight_layout()
plt.savefig("Dataset/Discount_vs_Profit.png")
plt.show()

# Sales vs Profit Analysis

plt.figure(figsize=(10, 6))

plt.scatter(
    df["Sales"],
    df["Profit"],
    alpha=0.5
)

plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.grid(True)

plt.tight_layout()
plt.savefig("Dataset/Sales_vs_Profit.png")
plt.show()

correlation = df["Sales"].corr(df["Profit"])

print("\n========== SALES VS PROFIT ==========")
print("Correlation:", round(correlation, 3))

# Yearly Sales Analysis

yearly_sales = df.groupby("Order Year")["Sales"].sum()

print("\n========== YEARLY SALES ==========")
print(yearly_sales)

plt.figure(figsize=(9, 5))

yearly_sales.plot(kind="bar")

plt.title("Yearly Sales Performance")
plt.xlabel("Year")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("Dataset/Yearly_Sales.png")
plt.show()

# Sales by State

state_sales = df.groupby("State")["Sales"].sum().sort_values(
    ascending=False
)

print("\n========== TOP 10 STATES BY SALES ==========")
print(state_sales.head(10))

plt.figure(figsize=(12, 6))

state_sales.head(10).sort_values().plot(kind="barh")

plt.title("Top 10 States by Sales")
plt.xlabel("Total Sales")
plt.ylabel("State")

plt.tight_layout()
plt.savefig("Dataset/Top_10_States_by_Sales.png")
plt.show()

# Customer Analysis

customer_analysis = df.groupby("Customer Name").agg(
    Total_Sales=("Sales", "sum"),
    Total_Orders=("Order ID", "nunique")
).sort_values("Total_Sales", ascending=False)

print("\n========== TOP 10 CUSTOMER ANALYSIS ==========")
print(customer_analysis.head(10))

plt.figure(figsize=(12, 6))

customer_analysis.head(10)["Total_Sales"].sort_values().plot(kind="barh")

plt.title("Top 10 Customers by Revenue")
plt.xlabel("Total Sales")
plt.ylabel("Customer Name")

plt.tight_layout()
plt.savefig("Dataset/Customer_Analysis.png")
plt.show()

# Shipping Performance Analysis

shipping_analysis = df.groupby("Ship Mode")["Shipping Days"].mean().sort_values()

print("\n========== SHIPPING PERFORMANCE ==========")
print(shipping_analysis.round(2))

plt.figure(figsize=(9, 5))

shipping_analysis.plot(kind="bar")

plt.title("Average Shipping Days by Ship Mode")
plt.xlabel("Shipping Mode")
plt.ylabel("Average Shipping Days")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("Dataset/Shipping_Performance.png")
plt.show()

# Profit Margin by Category

category_margin = df.groupby("Category").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
)

category_margin["Profit_Margin"] = (
    category_margin["Total_Profit"] /
    category_margin["Total_Sales"]
) * 100

print("\n========== PROFIT MARGIN BY CATEGORY ==========")
print(category_margin.round(2))

plt.figure(figsize=(8, 5))

category_margin["Profit_Margin"].plot(kind="bar")

plt.title("Profit Margin by Category")
plt.xlabel("Category")
plt.ylabel("Profit Margin (%)")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("Dataset/Profit_Margin_by_Category.png")
plt.show()


# Correlation Analysis

correlation_data = df[
    ["Sales", "Profit", "Quantity", "Discount", "Shipping Days"]
]

correlation_matrix = correlation_data.corr()

print("\n========== CORRELATION MATRIX ==========")
print(correlation_matrix.round(2))

plt.figure(figsize=(9, 7))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Business Data Correlation Analysis")

plt.tight_layout()
plt.savefig("Dataset/Correlation_Analysis.png")
plt.show()

# Export Cleaned Dataset

df.to_csv(
    "Dataset/Cleaned_Superstore.csv",
    index=False
)

print("\n========== DATA EXPORT ==========")
print("Cleaned dataset saved successfully!")
print("Total Rows:", df.shape[0])
print("Total Columns:", df.shape[1])


# Export Business Analysis Results to Excel

with pd.ExcelWriter(
    "Dataset/Business_Analysis_Results.xlsx",
    engine="openpyxl"
) as writer:

    category_sales.to_frame("Total Sales").to_excel(
        writer, sheet_name="Category Sales"
    )

    category_profit.to_frame("Total Profit").to_excel(
        writer, sheet_name="Category Profit"
    )

    region_sales.to_frame("Total Sales").to_excel(
        writer, sheet_name="Region Sales"
    )

    region_profit.to_frame("Total Profit").to_excel(
        writer, sheet_name="Region Profit"
    )

    segment_sales.to_frame("Total Sales").to_excel(
        writer, sheet_name="Segment Sales"
    )

    subcategory_sales.to_frame("Total Sales").to_excel(
        writer, sheet_name="Subcategory Sales"
    )

    yearly_sales.to_frame("Total Sales").to_excel(
        writer, sheet_name="Yearly Sales"
    )

    customer_analysis.head(20).to_excel(
        writer, sheet_name="Customer Analysis"
    )

    shipping_analysis.to_frame("Average Shipping Days").to_excel(
        writer, sheet_name="Shipping Analysis"
    )

    category_margin.to_excel(
        writer, sheet_name="Profit Margins"
    )

    correlation_matrix.to_excel(
        writer, sheet_name="Correlation"
    )

print("\nBusiness analysis Excel file created successfully!")