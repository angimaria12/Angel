# 🗄️ 03. Relational Databases & SQL Engineering

This directory contains enterprise-grade relational database implementations, SQL schema architecture (DDL), ETL data cleansing scripts (DML), data validation suites, and advanced analytical business intelligence queries.

---

## 📑 Module Overview

Structured Query Language (SQL) is the core standard for extracting, manipulating, and modeling relational data. This module demonstrates end-to-end database engineering across multiple real-world healthcare domains:

1. **Database & Schema Design (DDL)**:
   * Creation of relational schemas with explicit primary keys, foreign key constraints, column datatypes, and indices.
2. **Data Validation & Diagnostics**:
   * Automated verification queries checking for primary key collisions, duplicate records, null violations, format discrepancies, and orphan records across child tables.
3. **Data Cleansing & Transformation (DML)**:
   * In-place SQL transformations utilizing string parsing, date standardization (`STR_TO_DATE`), conditional case statements, and updates.
4. **Business Intelligence & Analytical Querying**:
   * Multi-table inner/left joins, window functions (`RANK()`, `DENSE_RANK()`, `ROW_NUMBER()`), grouping & aggregations (`GROUP BY`, `HAVING`), subqueries, and CTEs (Common Table Expressions).

---

## 🗂️ Folder Structure

```text
03_SQL/
└── 📁 Projects/                      # Production-scale relational database projects
    ├── 📁 HealthPlus/                # HealthPlus Care outpatient clinic & chronic care DB
    └── 📁 Medicare/                  # Medicare hospital analytics & inpatient operations DB
```

---

## 🚀 Projects Overview

* **[HealthPlus Care Database](./Projects/HealthPlus/) (`Healthplus_care`)**:
  * Outpatient network analytics tracking 17 relational tables: clinics, specialist doctors, member registrations, corporate partnerships, consultations, telemedicine sessions, diagnostic lab tests, prescriptions, health packages, and billing.
* **[Medicare Hospital Operations](./Projects/Medicare/) (`HospitalAnalyticsDB`)**:
  * Multi-facility hospital intelligence database across 15 relational tables: inpatient admissions, appointments, clinical departments, doctors, hospital rooms, treatments, laboratory tests, pharmacy, and insurance claims.
