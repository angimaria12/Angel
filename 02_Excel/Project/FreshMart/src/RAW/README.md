# 📥 FreshMart Raw Datasets

This directory archives the unprocessed, raw source spreadsheets for the FreshMart enterprise retail system.

---

## 📄 File Inventory

| File Name | Description | Key Attributes / Fields |
| :--- | :--- | :--- |
| **`FreshMart_Customers.xlsx`** | Customer master records | `Customer_ID`, `Customer_Name`, `Gender`, `City`, `Contact_Number`, `Registration_Date` |
| **`FreshMart_Employess.xlsx`** | Store employee roster | `Employee_ID`, `Employee_Name`, `Role`, `Department`, `Store_ID`, `Salary`, `Join_Date` |
| **`FreshMart_Enterprise_Dataset.xlsx`** | Consolidated multi-table dataset | Master multi-tab workbook containing raw tables across the organization |
| **`FreshMart_Products.xlsx`** | Product catalog & pricing | `Product_ID`, `Product_Name`, `Category`, `Unit_Price`, `Cost_Price`, `Supplier_ID` |
| **`FreshMart_Sales_Transactions.xlsx`** | Operational sales log | `Transaction_ID`, `Date`, `Customer_ID`, `Product_ID`, `Store_ID`, `Quantity`, `Payment_Mode` |
| **`FreshMart_Stores.xlsx`** | Store branch directory | `Store_ID`, `Store_Name`, `City`, `State`, `Region`, `Square_Footage`, `Manager_ID` |
| **`FreshMart_Suppliers.xlsx`** | Vendor directory | `Supplier_ID`, `Supplier_Name`, `Contact_Person`, `City`, `Payment_Terms` |

---

## ⚠️ Data Integrity Note

These files reflect raw data directly extracted from source systems. They contain raw datatypes, potential formatting quirks, and unmerged records that were subsequently transformed in the `CLEANED/` stage.
