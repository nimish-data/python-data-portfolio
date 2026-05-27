# 📊 JSON Data Pipeline & Report Generator

A self-contained Python data processing pipeline that reads raw data records, cleanses entry inconsistencies, and automatically compiles an aggregated metrics report.

## 🛠️ Core Mechanics
* **Robust File Handling:** Uses Python context managers (`with`) for isolated read/write file operations.
* **Fault Tolerance:** Employs safe dictionary `.get()` default fallbacks to prevent system crashes on missing schema data fields.
* **Data Aggregation:** Uses inline generator expressions to compute real-time cumulative performance statistics.

## 🚀 How To Run
```bash
python data_filter.py