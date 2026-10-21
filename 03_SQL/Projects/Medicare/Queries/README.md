# 📝 Medicare SQL Scripts & Analytical Queries

This folder contains the complete SQL query suite for the `HospitalAnalyticsDB` database.

---

## 📜 Scripts Overview

### 1. `medicare.sql` (DDL - Schema Definition)
* Creates the `HospitalAnalyticsDB` database.
* Defines 15 relational tables (`hospitals`, `departments`, `doctors`, `employees`, `rooms`, `patients`, `admissions`, `treatments`, `billing`, etc.) with defined data types and primary key constraints.

### 2. `Data Validation.sql` (Quality & Integrity Checks)
* Primary key uniqueness audits on all core entities.
* Checks for NULL values in essential operational columns.
* Referential integrity checks between treatments, admissions, rooms, and patients.
* Validates bed occupancy logic and admission date ranges vs. discharge dates.

### 3. `Data Cleaning.sql` (DML - Data Cleansing)
* Standardizes dates, telephone numbers, and email representations.
* Resolves typos and inconsistencies in department and specialization naming.
* Updates missing financial records and cleans payment status fields.

### 4. `Business Questions.sql` (Healthcare Business Intelligence)
Answers critical hospital administration and operational questions:
* Which hospitals have the highest patient admission and consultation volumes?
* What is the average length of stay (ALOS) across departments and room categories?
* What are the most revenue-generating clinical departments and treatment types?
* Doctor workload distribution and appointment completion rates.
* Insurance claim coverage versus out-of-pocket patient payments.

---

## 🏃 Execution Sequence

```text
1. medicare.sql            --> (Define database schema)
   [Import CSV Data]       --> (Load 15 CSV datasets)
2. Data Validation.sql     --> (Verify data health)
3. Data Cleaning.sql       --> (Clean & standardize records)
4. Business Questions.sql  --> (Extract clinical & operational insights)
```
