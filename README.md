# Task_04---Complete-Business-Analytics-Project | Superstore Data Analysis

## Project Overview

This project focuses on **Business Analytics and Exploratory Data Analysis (EDA)** using the Superstore dataset and Python.

The goal is to transform raw sales data into meaningful business insights by analyzing sales, profit, customer behavior, product performance, regional performance, discounts, and shipping operations.

The project uses Python libraries to perform data cleaning, feature engineering, statistical analysis, and data visualization. It also exports the cleaned dataset and business analysis results into CSV and Excel files.

## Project Objectives

- Understand the structure and quality of business data.
- Identify and handle duplicate records.
- Detect potential outliers using the IQR method.
- Perform feature engineering to create useful business variables.
- Calculate important business KPIs.
- Analyze sales and profit trends.
- Evaluate product and category performance.
- Compare regional and customer segment performance.
- Understand the relationship between discounts and profitability.
- Analyze shipping performance.
- Perform correlation analysis.
- Generate visualizations and export analysis results.

## Technologies & Libraries

| Technology | Purpose |
|---|---|
| Python | Programming and analysis |
| Pandas | Data cleaning and manipulation |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| OpenPyXL | Excel file generation |

## Project Structure

```text
Business-Analytics/
│
├── Dataset/
│   ├── Sample - Superstore.csv
│   ├── Cleaned_Superstore.csv
│   ├── Business_Analysis_Results.xlsx
│   │
│   └── Visualizations/
│       ├── Monthly_Sales_Trend.png
│       ├── Monthly_Profit_Trend.png
│       ├── Sales_by_Category.png
│       ├── Profit_by_Category.png
│       ├── Sales_by_Region.png
│       ├── Profit_by_Region.png
│       ├── Sales_by_Segment.png
│       ├── Profit_by_Segment.png
│       ├── Discount_vs_Profit.png
│       ├── Sales_vs_Profit.png
│       ├── Yearly_Sales.png
│       ├── Shipping_Performance.png
│       └── Correlation_Analysis.png
│
├── business_analytics.py
│
└── README.md
```

## Project Workflow

### 1. Data Loading and Exploration

- Load the Superstore dataset using Pandas.
- Display the first five records.
- Examine dataset information and dimensions.
- Identify missing values.
- Check duplicate records.

### 2. Data Cleaning

- Remove duplicate records.
- Convert Order Date and Ship Date into datetime format.
- Convert Sales, Profit, Quantity, and Discount into numerical data types.
- Verify updated data types.

### 3. Outlier Detection

Use the **Interquartile Range (IQR)** method to identify potential outliers in:

- Sales
- Profit
- Quantity
- Discount

The project identifies and counts outliers without automatically removing them.

### 4. Feature Engineering

Create additional columns to improve business analysis:

| Feature | Description |
|---|---|
| Order Year | Extracted year from Order Date |
| Order Month | Extracted month from Order Date |
| Shipping Days | Difference between Ship Date and Order Date |
| Profit Margin | Profit divided by Sales × 100 |

### 5. Business KPI Analysis

Calculate essential business performance indicators:

- Total Sales
- Total Profit
- Total Orders
- Total Customers
- Average Order Value (AOV)
- Overall Profit Margin

### 6. Exploratory Data Analysis (EDA)

Perform detailed business analysis across multiple dimensions.

**Sales Analysis**
- Monthly Sales Trends
- Yearly Sales Performance
- Sales by Category
- Sales by Region
- Sales by Customer Segment
- Sales by Sub-Category
- Sales by Shipping Mode
- Top 10 Products by Sales
- Top 10 Customers by Sales
- Top 10 States by Sales

**Profit Analysis**
- Monthly Profit Trends
- Profit by Category
- Profit by Region
- Profit by Customer Segment
- Profit by Sub-Category
- Profit Margin by Category

**Customer Analysis**
- Customer-wise Total Sales
- Customer-wise Order Count
- Top 10 Customers by Revenue

**Discount Analysis**
- Discount vs Average Profit
- Impact of Discounts on Profitability

**Shipping Analysis**
- Average Shipping Days by Shipping Mode

### 7. Data Visualization

Use Matplotlib and Seaborn to generate:

- Line Charts
- Bar Charts
- Horizontal Bar Charts
- Scatter Plots
- Correlation Heatmaps

Visualizations are saved as PNG files in the Dataset folder.

### 8. Correlation Analysis

Analyze relationships between:

- Sales
- Profit
- Quantity
- Discount
- Shipping Days

A correlation matrix and heatmap are generated to understand relationships between numerical business variables.

### 9. Export Results

The project generates two major output files:

**Cleaned_Superstore.csv**
- Contains cleaned business data.
- Includes newly engineered features.

**Business_Analysis_Results.xlsx**

Contains multiple worksheets:

- Category Sales
- Category Profit
- Region Sales
- Region Profit
- Segment Sales
- Subcategory Sales
- Yearly Sales
- Customer Analysis
- Shipping Analysis
- Profit Margins
- Correlation

## 📈 Key Business Metrics

| KPI | Formula |
|---|---|
| Total Sales | Sum of Sales |
| Total Profit | Sum of Profit |
| Total Orders | Unique Order IDs |
| Total Customers | Unique Customer IDs |
| Average Order Value | Total Sales / Total Orders |
| Profit Margin | (Total Profit / Total Sales) × 100 |

## Installation & Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/Business-Analytics.git
```

### Step 2: Navigate to the Project Folder

```bash
cd Business-Analytics
```

### Step 3: Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn openpyxl
```

### Step 4: Add the Dataset

Place the original CSV file inside the Dataset folder:

```text
Dataset/Sample - Superstore.csv
```

### Step 5: Run the Python Script

```bash
python business_analytics.py
```

The script will perform data cleaning, analysis, generate visualizations, and export the results.

## Key Learning Outcomes

Through this project, I practiced:

- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Feature engineering
- Outlier detection using IQR
- Business KPI calculation
- Sales and profit analysis
- Customer and regional analysis
- Data visualization
- Correlation analysis
- Exporting business reports to Excel

## Conclusion

This project demonstrates how Python can be used to analyze business data and generate actionable insights.

By combining data cleaning, exploratory analysis, KPI calculations, and visualization, the project provides a comprehensive understanding of business performance and supports data-driven decision-making.

## Author

**Sidra Maqsood**

Aspiring Data Analyst | Python | SQL | Excel | Power BI | Business Analytics
