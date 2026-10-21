# ✨ FreshMart Cleaned Data & Models

This folder holds the transformed, normalized, and verified Excel datasets for the FreshMart project.

---

## 📄 File Inventory

| File Name | Size | Purpose |
| :--- | :--- | :--- |
| **`freshmart.dashboard.xlsx`** | ~1.2 MB | Cleaned reporting workbook with integrated KPI cards, pivot charts, and slicers |
| **`FreshMart_Sales_Transactions (1).xlsx`** | ~1.2 MB | Cleaned and validated transactional sales records with formatted datatypes and verified keys |

---

## 🧹 Data Cleaning Procedures Applied

1. **Date Standardization**: Standardized order and delivery timestamps into unified `YYYY-MM-DD` date formats.
2. **Missing & Duplicate Values**: Audited and resolved missing entries in transaction logs and eliminated redundant rows.
3. **Data Type Casting**: Ensured numeric fields (`Quantity`, `Unit_Price`, `Discount`, `Total_Amount`) are stored as numbers rather than text strings.
4. **Referential Consistency**: Verified foreign keys (`Customer_ID`, `Store_ID`, `Product_ID`, `Employee_ID`) to prevent unmapped records during pivot aggregation.
