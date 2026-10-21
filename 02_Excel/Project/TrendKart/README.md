# 👗 TrendKart Fashion E-Commerce Analytics Project

End-to-end data cleansing, quality auditing, relational data modeling, and interactive executive reporting for **TrendKart**, an online multi-channel fashion and apparel retailer.

---

## 📌 Project Overview

TrendKart is a digital apparel brand managing direct-to-consumer sales across multiple channels and regional fulfillment centers. This project demonstrates how messy, uncurated transactional data is systematically cleansed, audited using a formal **Data Quality Log**, and synthesized into an interactive executive KPI dashboard.

---

## 🏗️ Folder Structure & File Inventory

```text
TrendKart/
├── README.md                           # This comprehensive project documentation
├── TrendKart_FinalDashboard.xlsx       # Executive KPI dashboard and presentation workbook
├── 📁 Cleaned/                         # Cleaned models, audit logs & calculations
│   └── TrendKart_Data_Cleaning.xlsx    # Full data transformation & audit workbook
└── 📁 Raw/                             # Source fashion enterprise dataset
    └── TrendMart_Fashion_Enterprise_Dataset (1).xlsx # Master raw multi-sheet dataset
```

---

## 🔍 Comprehensive Data Quality Audit (`Data_Quality_Log`)

The hallmark of the TrendKart project is rigorous data hygiene. A dedicated audit identified, quantified, and resolved data anomalies:

| Table / Entity | Anomaly Type Identified | Rows Affected | Remediation Applied |
| :--- | :--- | :---: | :--- |
| **Sales_Transactions** | Duplicate Invoice Numbers | 5 | Deduplicated based on timestamp and order sequence |
| **Sales_Transactions** | Blank `Customer_ID` | 6 | Cross-referenced against delivery address / mapped to Guest profile |
| **Sales_Transactions** | Blank `Product_ID` | 5 | Inferred from item description and unit price catalog lookup |
| **Sales_Transactions** | Blank `Employee_ID` | 5 | Assigned default online self-service fulfillment code |
| **Sales_Transactions** | Mixed Date Formats | 6 | Converted non-standard string formats into serial `YYYY-MM-DD` |
| **Sales_Transactions** | Text stored as Numbers (`Quantity`) | 5 | Cast strings to numeric values using `VALUE()` / `INT()` |
| **Sales_Transactions** | Extra Spaces in `Payment Mode` | 4 | Applied `TRIM()` and `CLEAN()` to sanitize trailing spaces |
| **Sales_Transactions** | Negative Profit values | 4 | Corrected reversed Cost Price vs. Selling Price inputs |
| **Sales_Transactions** | `Quantity = 0` | 5 | Filtered zero-quantity non-events from active revenue counts |
| **Sales_Transactions** | Mixed Payment Mode casing | 5 | Standardized text using `PROPER()` / `UPPER()` |
| **Sales_Transactions** | Status Typos (`Return Status`) | 4 | Corrected spelling variations (e.g., 'Returnd' -> 'Returned') |
| **Customers** | Duplicate Phone Numbers | 5 | Merged secondary customer profiles to preserve history |
| **Customers** | Invalid Email Formats | 5 | Regex-like string validation for `@` and domain extensions |
| **Customers** | Mixed Gender Values | 5 | Standardized gender codes into unified categories (`M`, `F`, `Other`) |

---

## 📑 Analytical Sheets & Data Cross-Tabulations

Inside `TrendKart_FinalDashboard.xlsx`, dedicated pivot models analyze relationships between fashion dimensions:

* **`proandsal` (Products & Sales)**: Aggregates revenue, unit volume, and discounts across apparel categories (Men's Wear, Women's Ethnic, Western Wear, Footwear, Accessories).
* **`payandsal` (Payment & Sales)**: Compares order volumes and total transaction amounts across payment gateways (UPI, Credit Card, Debit Card, Net Banking, Cash on Delivery).
* **`modendsal` (Mode & Sales)**: Evaluates fulfillment channels (Standard Ground, Express 1-Day, Click & Collect).
* **`prdandpro` (Product Profitability)**: Evaluates gross margin contribution and discount sensitivity across SKUs.
* **`salandsto` (Sales by Store/Hub)**: Benchmarks regional fulfillment hubs and retail pickup centers.
* **`KPI Dashboard` & `Dashboard`**: Executive reporting interfaces equipped with interactive slicers and KPI summary cards.

---

## 📊 Key Performance Indicators (KPIs)

* **Gross Merchandise Value (GMV)**: Total gross sales value recorded across 2,991 order lines.
* **Net Revenue**: Gross sales minus discounts and validated product returns.
* **Return Rate %**: Proportion of fulfilled orders resulting in a return:
  $$\text{Return Rate \%} = \frac{\text{Returned Orders}}{\text{Total Orders}} \times 100$$
* **Average Order Value (AOV)**: Average spend per customer order.
* **Payment Preference Ratio**: Share of digital prepaid transactions (UPI/Cards) vs. COD.

---

## 🛠️ Usage Instructions

1. Open `TrendKart_FinalDashboard.xlsx` in **Microsoft Excel**.
2. Navigate to the **`Dashboard`** or **`KPI Dashboard`** tab to view executive visuals.
3. Use the slicers to filter data by **Payment Mode**, **Product Category**, and **Store Location**.
4. To inspect the cleaning pipeline, open `Cleaned/TrendKart_Data_Cleaning.xlsx` and review the **`Data_Quality_Log`** tab.
