# 📦 FreshMart Source & Dashboard Workbooks

This directory contains the central assets for the FreshMart project, including the master dashboard workbook, the cleaned data files, and the raw source tables.

---

## 📄 Contents

* **`freshmart.dashboard.xlsx`**:
  * The primary analytical workbook containing the interactive executive dashboard.
  * Includes sheets: `Dashboard`, `Dashboard KPI'S`, `KPI VALUES`, `Sales_Transactions`, `Customer`, `Employee`, `Products`, `Store`, and `Supplier`.
  * Features interactive pivot charts, slicers, and summary metrics.
* **`CLEANED/`**:
  * Contains cleaned copies of the dataset and validated transaction spreadsheets ready for visualization.
* **`RAW/`**:
  * Contains the original source spreadsheets for each business entity before cleaning and modeling.

---

## 🛠️ Usage Instructions

1. Open `freshmart.dashboard.xlsx` in Microsoft Excel (version 2016 or newer recommended for optimal slicer and dynamic array support).
2. Use the slicers on the **Dashboard** sheet to filter the views by Store, Product Category, or Time Period.
3. Review the supporting entity tabs (`Supplier`, `Store`, `Products`, etc.) to inspect underlying lookup formulas and pivot tables.
