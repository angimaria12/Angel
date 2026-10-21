# 📝 HealthPlus Care SQL Scripts & Analysis

This directory contains the complete SQL script suite for creating, validating, cleaning, and querying the `Healthplus_care` database.

---

## 📜 Scripts Overview

### 1. `Healthplus.sql` (DDL - Data Definition Language)
* Creates the `Healthplus_care` database.
* Creates all 17 normalized tables (`clinics`, `specialists`, `members`, `corporates`, `consultations`, `telemedicine_sessions`, `billing`, etc.) with defined primary keys, foreign key references, and appropriate column datatypes.

### 2. `Data Validation.sql` (Diagnostic Integrity Checks)
* Primary key uniqueness tests (e.g., `SELECT clinic_id, COUNT(*) FROM clinics GROUP BY clinic_id HAVING COUNT(*) > 1;`).
* NULL checks on mandatory attributes across tables.
* Referential integrity audits checking for orphan consultation, prescription, and billing records.
* Outlier and sanity checks on dates and amounts.

### 3. `Data Cleaning.sql` (DML - Data Manipulation Language)
* Standardizes dates stored as text strings into standard `DATE` or `DATETIME` formats using `STR_TO_DATE`.
* Replaces blanks or inconsistently formatted phone numbers and email strings.
* Standardizes categorical status fields (e.g., Payment status, Claim status, Membership types).

### 4. `Business Questions.sql` (Analytical & BI Queries)
Answers key managerial and clinical operational questions, including:
* Which clinics have the highest consultation volume?
* Which specialists carry the highest consultation workload?
* Which medical specializations experience the highest patient demand?
* What is the revenue distribution across clinics, packages, and telemedicine?
* What are the member retention rates and corporate contract values?

---

## 🏃 Execution Sequence

```text
1. Healthplus.sql          --> (Create schema)
   [Import CSV Data]       --> (Load data into tables)
2. Data Validation.sql     --> (Verify data consistency)
3. Data Cleaning.sql       --> (Apply cleanups & standardizations)
4. Business Questions.sql  --> (Generate business intelligence insights)
```
