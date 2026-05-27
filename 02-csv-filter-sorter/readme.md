# 📊 CSV Grade Filter & Performance Sorter

A defensive Python data utility that processes student grades from a tabular CSV format, calculates individual multi-subject averages, filters out low-percentile results, and dynamically ranks the high achievers.

---

## 🛠️ Key Architecture Mechanics

* **Falsy & Missing Data Protection:** Utilizes an inline `.get() or 0` structural fallback pattern to neutralize empty strings (`""`) and missing data headers before casting strings into integers.
* **Granular Error Isolation:** Wraps individual row mutations inside a targeted `try-except` block to log and skip isolated row corruptions (like string-based attendance notes) without crashing the entire execution run.
* **Custom Lambda Sorting Engine:** Employs an explicit lambda function evaluation criteria (`key=lambda x: x["average"]`) to organize internal list components in descending rank order.
* **Safe Output Stream Hooks:** Leverages Python's native `csv.DictWriter` automated context manager to overwrite old files and stream structured lines without risking runtime memory or handle leaks.

---

## 🚀 Script Overview

```text
📁 02-csv-filter-sorter/
├── csv_sorter.py       # Main Python logic script
├── raw_csv.csv         # Raw student data source file
└── README.md           # Project documentation and specifications