# 🧼 TrendKart Cleaned & Transformed Datasets

This directory holds the audited and cleaned datasets for the TrendKart project, documenting the data wrangling workflow from raw spreadsheets to analysis-ready data structures.

---

## 📄 File Inventory

* **`TrendKart_Data_Cleaning.xlsx`**:
  * Multi-worksheet workbook containing:
    * `Data_Quality_Log`: Log tracking anomalies, missing fields, format fixes, and deduplication actions.
    * `Pivot_Table`: Analytical pivot summaries pre-configured for reporting.
    * `Calculations`: Helper calculation columns and dynamic formula references.
    * Normalized tables: `Sales_Transactions`, `Customers`, `Products`, `Stores`, `Employees`, and `Suppliers`.
    * `Dashboard` & `Detail1`: Preliminary visual summaries and detailed report breakdowns.

---

## 🔍 Data Transformation Checklist

* **Null Value Imputation**: Imputed missing customer demographic values and confirmed transaction records.
* **Date Parsing**: Converted text dates into standardized serial dates.
* **Price & Currency Normalization**: Removed stray symbols and cast sales numbers to decimal currencies.
* **Audit Trail**: Every anomaly identified during exploration is explicitly cataloged in the `Data_Quality_Log` tab.
