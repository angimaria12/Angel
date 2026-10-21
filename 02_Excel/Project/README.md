# 🛒 Excel Projects Portfolio

This directory houses full-scale enterprise case study projects built using Microsoft Excel. Each project models a complete data pipeline: from raw entity tables to cleaned and validated records, ending in an interactive executive dashboard.

---

## 📁 Projects Summary

| Project | Domain | Key Files | Core Focus |
| :--- | :--- | :--- | :--- |
| **[FreshMart](./FreshMart/)** | Supermarket Retail Chain | `freshmart.dashboard.xlsx`, Raw & Cleaned entity tables | Retail transactions, store performance, supplier analytics, customer demographics |
| **[TrendKart](./TrendKart/)** | Fashion E-Commerce | `TrendKart_FinalDashboard.xlsx`, `TrendKart_Data_Cleaning.xlsx` | Order volume, payment method preferences, product categories, data quality logging |

---

## 🌟 Common Architecture in Each Project

1. **Raw Layer**: Unmodified transactional and dimension worksheets extracted directly from operational systems.
2. **Cleaned Layer**: Data transformed with standardized data types, removed nulls/duplicates, validated dates, and calculated helper columns.
3. **Analytical & Reporting Layer**: Star-schema joins in Excel feeding dynamic Pivot Tables, Slicers, KPI Cards, and executive visualizations.
