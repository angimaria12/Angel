# 📊 Medicare Relational CSV Datasets

This directory contains 15 clean, structured CSV files ready for database ingestion into `HospitalAnalyticsDB`.

---

## 📋 Table Index & Primary Keys

| CSV File Name | Table Name | Primary Key | Description |
| :--- | :--- | :--- | :--- |
| **`Hospitals.csv`** | `hospitals` | `hospital_id` | Hospital facilities, hospital types, locations, and bed capacities |
| **`Departments.csv`** | `departments` | `department_id`| Clinical departments (Cardiology, Orthopedics, Oncology, etc.) |
| **`Doctors.csv`** | `doctors` | `doctor_id` | Physicians, specializations, qualifications, and department affiliations |
| **`Employees.csv`** | `employees` | `employee_id` | Nursing, technician, and administrative healthcare staff |
| **`Rooms.csv`** | `rooms` | `room_id` | Inpatient hospital rooms, room types (ICU, General, Private), and daily rates |
| **`Patients.csv`** | `patients` | `patient_id` | Patient demographic records, blood groups, and emergency contacts |
| **`Appointments.csv`** | `appointments`| `appointment_id`| Scheduled doctor consultations and appointment statuses |
| **`Admissions.csv`** | `admissions` | `admission_id` | Inpatient admission records, admission dates, discharge dates, and room IDs |
| **`Treatments.csv`** | `treatments` | `treatment_id` | Medical procedures, treatment costs, and attending doctor IDs |
| **`Laboratory.csv`** | `laboratory` | `lab_test_id` | Diagnostic lab test orders, patient samples, test costs, and results |
| **`Pharmacy.csv`** | `pharmacy` | `pharmacy_id` | Pharmacy dispensed order records linked to patients and doctors |
| **`Medicines.csv`** | `medicines` | `medicine_id` | Medication inventory catalog, dosage types, and unit prices |
| **`Insurance.csv`** | `insurance` | `policy_id` | Patient insurance policies, providers, coverage limits, and validities |
| **`Billing.csv`** | `billing` | `bill_id` | Inpatient/outpatient invoices, room charges, procedure charges, and totals |
| **`Payments.csv`** | `payments` | `payment_id` | Patient payments, payment methods, transaction references, and dates |

---

## 💡 Quick Ingestion Guide (MySQL)

```sql
LOAD DATA LOCAL INFILE 'C:/Angel/03_SQL/Projects/Medicare/CSV files/Hospitals.csv'
INTO TABLE hospitals
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
```
