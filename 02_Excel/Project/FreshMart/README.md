# 🛍️ FreshMart Enterprise Analytics Project

Comprehensive retail sales analytics, relational data modeling, and executive KPI dashboard developed for **FreshMart**, a multi-branch supermarket retail enterprise.

---

## 📌 Project Overview

FreshMart operates multiple supermarket branches offering diverse product categories (Groceries, Fresh Produce, Dairy, Beverages, Personal Care, Household). This project models the complete business intelligence pipeline: from raw operational exports to cleaned and validated records, ending in an interactive, dynamic Excel executive dashboard.

---

## 🖥️ Executive Sales Performance Dashboard

![FreshMart Sales Performance Dashboard](./assets/freshmart_dashboard.png)

### Key Metrics Displayed on Dashboard:
* **Total Sales**: **₹ 28,68,433**
* **Total Profit**: **₹ 7,37,359**
* **Profit Margin**: **25.7%**
* **Units Sold**: **9,823**
* **Return Rate**: **4.6%**

### Visual Reports & Analytical Breakdowns:
1. **Interactive Multi-Level Slicers**:
   * **Membership**: Segment views by `Gold`, `Bronze`, and unassigned profiles.
   * **Region**: Filter by `East`, `North`, `South`, `West`, and unmapped zones.
   * **Return Status**: Filter between `Not Returned` vs. `Returned`.
   * **Payment Mode**: Multi-select across `Cash`, `Credit Card`, `Debit Card`, `Net Banking`, `UPI`, and `Wallet`.
   * **Sales Channel**: Analyze performance across `In-Store`, `Mobile App`, and `Online`.
2. **How Does Sales Performance Change Throughout the Year? (Seasonality Trend)**:
   * Dual-axis time series tracking monthly Sales Amount vs. Profit from January through December.
   * Highlights a major festive peak in **October** (Sales surpassing ₹4,50,000 with > ₹1,20,000 in gross profit).
3. **How Does Each Region Contribute to Business Performance?**:
   * Clustered column chart comparing Sales Amount, Profit, and Quantity across geographic zones.
   * The **South Region** serves as the primary revenue engine, contributing over ₹18,00,000 in sales.
4. **Where Do Customers Prefer to Shop? (Channel Distribution)**:
   * **In-Store**: **70%** (Dominant point-of-sale volume).
   * **Online**: **21%** (Digital website delivery).
   * **Mobile App**: **9%** (Direct app orders).
5. **Customer Profitability & Transaction Frequency**:
   * Pivot audit tracking top patrons (e.g., *Lalitha Nathan* ₹9,206 profit / 16 transactions, *Elango Nair* ₹8,434 profit / 15 transactions).
6. **How Do Product Categories Perform?**:
   * Category contribution benchmark showing high-velocity sales in **Beverages**, **Snacks**, **Bakery**, and **Dairy**.
7. **Which Products Drive Overall Performance?**:
   * Item-level volume and revenue ranking featuring top SKUs: *Coca-Cola Coffee*, *Harvest Gold Rusk*, *Nescafe Coffee 1kg*, *Lays Namkeen*, *Pepsi Tea*, and *Local Farm Fresh Vegetables*.

---

## 🏗️ Relational Schema & Data Architecture

The project connects 6 relational business entities into a star/snowflake schema inside Excel:

```mermaid
erDiagram
    CUSTOMERS ||--o{ SALES_TRANSACTIONS : places
    STORES ||--o{ SALES_TRANSACTIONS : processes
    EMPLOYEES ||--o{ SALES_TRANSACTIONS : assists
    PRODUCTS ||--o{ SALES_TRANSACTIONS : sold_in
    SUPPLIERS ||--o{ PRODUCTS : supplies

    CUSTOMERS {
        string Customer_ID PK
        string Customer_Name
        string Gender
        string City
        string Contact_Number
        date Registration_Date
    }
    STORES {
        string Store_ID PK
        string Store_Name
        string City
        string State
        string Region
        int Square_Footage
        string Manager_ID
    }
    EMPLOYEES {
        string Employee_ID PK
        string Employee_Name
        string Role
        string Department
        string Store_ID FK
        decimal Salary
        date Join_Date
    }
    PRODUCTS {
        string Product_ID PK
        string Product_Name
        string Category
        decimal Unit_Price
        decimal Cost_Price
        string Supplier_ID FK
    }
    SUPPLIERS {
        string Supplier_ID PK
        string Supplier_Name
        string Contact_Person
        string City
        string Payment_Terms
    }
    SALES_TRANSACTIONS {
        string Invoice_Number PK
        date Transaction_Date
        string Customer_ID FK
        string Product_ID FK
        string Store_ID FK
        string Employee_ID FK
        int Quantity
        decimal Unit_Price
        decimal Discount_Pct
        decimal Discount_Amount
        decimal Sales_Amount
        decimal Cost_Amount
        decimal Profit
        string Payment_Mode
        string Return_Status
        string Sales_Channel
        time Order_Time
        string Day_Type
    }
```

---

## 📂 Folder Structure & File Inventory

```text
FreshMart/
├── README.md                           # This comprehensive project documentation
├── 📁 assets/                          # Dashboard visuals and screenshot media
│   └── freshmart_dashboard.png         # Executive Sales Performance Dashboard preview
└── 📁 src/                             # Source files, dashboard models & datasets
    ├── freshmart.dashboard.xlsx        # Master interactive Excel workbook with dashboards & KPI models
    ├── 📁 CLEANED/                     # Transformed, audited & analysis-ready data
    │   ├── freshmart.dashboard.xlsx    # Cleaned production dashboard copy
    │   └── FreshMart_Sales_Transactions (1).xlsx # Validated transaction records
    └── 📁 RAW/                         # Original source spreadsheets
        ├── FreshMart_Customers.xlsx    # Customer demographics & loyalty records
        ├── FreshMart_Employess.xlsx    # Store employee staff roster
        ├── FreshMart_Enterprise_Dataset.xlsx # Consolidated multi-sheet master file
        ├── FreshMart_Products.xlsx     # Catalog of SKUs, pricing & supplier links
        ├── FreshMart_Sales_Transactions.xlsx # Raw POS sales logs
        ├── FreshMart_Stores.xlsx       # Store branches & retail square footage
        └── FreshMart_Suppliers.xlsx    # Supplier directory & lead terms
```

---

## 📊 Core Business KPIs & Formulas

Inside `freshmart.dashboard.xlsx`, dynamic formulas and Pivot Tables calculate the key operational and financial indicators:

1. **Total Gross Revenue**:  
   $$\text{Total Sales} = \sum (\text{Quantity} \times \text{Unit Price} \times (1 - \text{Discount Pct}))$$
2. **Total Cost of Goods Sold (COGS)**:  
   $$\text{Total COGS} = \sum (\text{Quantity} \times \text{Cost Price})$$
3. **Gross Profit & Profit Margin %**:  
   $$\text{Profit} = \text{Sales Amount} - \text{Cost Amount}$$  
   $$\text{Margin \%} = \frac{\text{Profit}}{\text{Sales Amount}} \times 100$$
4. **Average Order Value (AOV)**:  
   $$\text{AOV} = \frac{\text{Total Sales Amount}}{\text{Total Unique Invoices}}$$
5. **Discount Impact**: Total revenue waived through promotional campaigns.
6. **Sales Channel Mix**: Revenue share of **In-Store** vs. **Online Delivery**.
7. **Temporal Trends**: Revenue volume analyzed by **Day Type** (*Weekday* vs. *Weekend*) and hourly peak trading intervals (*Order Time*).

---

## 🛠️ Usage Instructions

1. Open `src/freshmart.dashboard.xlsx` in **Microsoft Excel (2016 or newer)**.
2. Ensure macros/data connections are enabled if prompted.
3. Navigate to the `Dashboard` tab to interact with visual filters and examine real-time KPI card updates.
4. Review the `KPI VALUES` and supporting entity sheets (`Supplier`, `Store`, `Products`, `Employee`, `Customer`) to inspect the underlying `XLOOKUP` and Pivot logic.
