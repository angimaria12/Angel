# 📊 HealthPlus Care Relational CSV Tables

This directory contains 17 normalized CSV files corresponding to the tables defined in `Healthplus.sql`. These datasets can be imported into MySQL, PostgreSQL, or SQL Server.

---

## 📋 Table Index & Primary Keys

| CSV File Name | Table Name | Primary Key | Description |
| :--- | :--- | :--- | :--- |
| **`Clinics.csv`** | `clinics` | `clinic_id` | Branch clinic locations, clinic types, cities, states, and established years |
| **`Specialists.csv`** | `specialists` | `specialist_id` | Doctors, credentials, specializations, clinic affiliations, and fees |
| **`Staff.csv`** | `staff` | `staff_id` | Clinic administrative and support staff, roles, and clinic assignments |
| **`Members.csv`** | `members` | `member_id` | Registered patients, demographics, contact details, and registration dates |
| **`Corporates.csv`** | `corporates` | `corporate_id` | Corporate partner companies holding health coverage agreements |
| **`Corporate_Members.csv`** | `corporate_members` | Composite / FK | Association between registered members and their sponsoring corporate entity |
| **`Consultations.csv`** | `consultations` | `consultation_id` | In-person clinic doctor consultations, diagnoses, and fees |
| **`Telemedicine_Sessions.csv`**| `telemedicine_sessions` | `session_id` | Virtual telemedicine consultations, call durations, and outcomes |
| **`Lab_Tests.csv`** | `lab_tests` | `test_id` | Diagnostic laboratory orders, test types, test results, and costs |
| **`Prescriptions.csv`** | `prescriptions` | `prescription_id` | Medication prescriptions issued during consultations |
| **`Health_Packages.csv`** | `health_packages` | `package_id` | Preventive health checkup bundles, prices, and test inclusions |
| **`Package_Subscriptions.csv`**| `package_subscriptions`| `subscription_id` | Patient purchases of preventive healthcare packages |
| **`Chronic_Care_Programs.csv`**| `chronic_care_programs`| `program_id` | Specialized long-term disease management enrollments |
| **`Billing.csv`** | `billing` | `bill_id` | Invoices generated across clinical services, taxes, and total amounts |
| **`Payments.csv`** | `payments` | `payment_id` | Payment transaction records, payment methods, and timestamps |
| **`Claims.csv`** | `claims` | `claim_id` | Insurance claims submitted, approved amounts, and claim status |
| **`Feedback.csv`** | `feedback` | `feedback_id` | Patient ratings, clinic reviews, and doctor satisfaction feedback |

---

## 💡 Import Command Example (MySQL)

```sql
LOAD DATA LOCAL INFILE 'C:/Angel/03_SQL/Projects/HealthPlus/CSV files/Clinics.csv'
INTO TABLE clinics
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
```
