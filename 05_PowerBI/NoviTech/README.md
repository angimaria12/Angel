# ⚙️ NoviTech Manufacturing Power BI Analytics

Production-grade manufacturing intelligence dashboard, plant productivity monitoring, and equipment utilization system developed for **NoviTech Manufacturing**, an industrial machinery production enterprise.

---

## 📌 Project Overview

NoviTech Manufacturing operates heavy machinery fabrication plants where maintaining continuous throughput, optimizing batch runs, minimizing scrap, and maximizing first-pass yield are critical operational drivers. This Power BI project consolidates plant operational runs, defect rates, good unit outputs, and machine downtime into an executive management dashboard.

---

## 🏗️ Data Model & Dimensions

The analytical model leverages dimensional tables and operational metrics:

* **`dim_plants`**: Manufacturing facilities, plant names (e.g., Detroit Plant, Chicago Plant, Austin Facility), regional codes, and operating managers.
* **`bridge_bill_of_materials`**: Centralized calculation hub housing enterprise business logic and DAX measure definitions.
* **Operational Production Telemetry**: Tracks batch runs, shift cycles, good output units, defective units, and machine stoppage logs.

---

## 📐 Core DAX Measures & Formulations

The business logic in `bridge_bill_of_materials` computes the following KPIs:

1. **Total Production**:
   ```dax
   Total_Production = SUM(fact_production[produced_units])
   ```
2. **Total Production Runs**:
   ```dax
   Total Production Runs = COUNTROWS(fact_production)
   ```
3. **Total Defective Production**:
   ```dax
   Total Defective Production = SUM(fact_quality[defective_units])
   ```
4. **Good Units (Passed QA)**:
   ```dax
   Good Units = [Total_Production] - [Total Defective Production]
   ```
5. **Defect Rate %**:
   ```dax
   Defect Rate = DIVIDE([Total Defective Production], [Total_Production], 0)
   ```
6. **First Pass Yield % (`Yeild %`)**:
   ```dax
   Yeild % = DIVIDE([Good Units], [Total_Production], 0)
   ```
7. **Detroit Plant Production**:
   ```dax
   Detroit_Production = 
   CALCULATE([Total_Production], dim_plants[plant_name] = "Detroit")
   ```
8. **Company Production Benchmark**:
   ```dax
   Company Production = 
   CALCULATE([Total_Production], ALL(dim_plants))
   ```
9. **Total Downtime**:
   ```dax
   Total Downtime = SUM(fact_downtime[downtime_hours])
   ```

---

## 🖥️ Interactive Dashboard Visuals & Layout

The report features an executive manufacturing console:

* **Executive KPI Cards**:
  * **Total Production**: Gross manufactured units across facilities.
  * **Total Production Runs**: Total batch cycles scheduled and completed.
  * **Good Units**: Net usable equipment pieces ready for dispatch.
  * **Total Defective Production**: Total scrapped or reworked equipment pieces.
  * **Defect Rate %**: Percentage of production failing QA tolerances.
  * **First-Pass Yield % (`Yeild %`)**: Proportion of output passing quality on first run without rework.
  * **Detroit Production**: Dedicated volume tracking for the flagship Detroit manufacturing hub.
  * **Company Production**: Consolidated enterprise output benchmark.
* **Comparative Operational Visuals**:
  * **Plant Productivity vs. Downtime (Clustered Column Chart)**:
    * X-Axis: Manufacturing Plant Name (`dim_plants.plant_name`).
    * Y-Axis 1: Total Production Runs.
    * Y-Axis 2: Total Downtime Hours.
    * Evaluates plant efficiency by identifying facilities with high run frequencies yet excessive downtime hours.
* **Dynamic Slicing**:
  * **Advanced Plant Slicer (`advancedSlicerVisual`)**: Single/multi-select filtering across manufacturing plants to isolate performance metrics per region.

---

## 🛠️ How to Open & Inspect

1. Launch **Microsoft Power BI Desktop**.
2. Open the file `C:\Angel\05_PowerBI\NoviTech_Manufacturing.pbix`.
3. Interact with the **Advanced Plant Slicer** on the report canvas to see instantaneous filtering of Yield %, Defect Rates, and Production counts.
4. Review the **Data Model** to view table structures, DAX calculations, and relationship cardinalities.
