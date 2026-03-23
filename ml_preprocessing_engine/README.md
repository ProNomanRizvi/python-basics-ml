# ML Preprocessing Engine

## 📌 What This Project Does
This project reads raw numerical data from a file and processes it through
a structured pipeline:

1. **Load** → Read raw data from file, reject invalid entries
2. **Clean** → Remove duplicates and outliers
3. **Normalize** → Scale all values to 0–1 range
4. **Report** → Display full statistical summary
5. **Save** → Write report to output file

---

## 📂 Folder Structure
```
ml_preprocessing_engine/
├── data/
│   ├── raw_data.txt       # Input data
│   └── report.txt         # Generated report
├── src/
│   ├── base_pipeline.py   # Parent class for all pipeline stages
│   ├── loader.py          # Loads and validates raw file data
│   ├── cleaner.py         # Removes duplicates and outliers
│   ├── normalizer.py      # Normalizes data to 0–1 range
│   └── reporter.py        # Generates and saves summary report
├── main.py
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run
```bash
# Clone the repository
git clone <your-repo-url>
cd ml_preprocessing_engine

# Run the engine
python main.py
```

**Requirement:** Python 3.8 or higher

---

## 🧱 Class Overview

| Class | Responsibility |
|---|---|
| `BasePipeline` | Parent class — defines shared structure for all pipeline stages |
| `DataLoader` | Reads raw file, parses lines, rejects non-numeric values |
| `DataCleaner` | Removes duplicate values and statistical outliers (mean ± 1.5 std_dev) |
| `DataNormalizer` | Scales all values to 0–1 range using min-max normalization |
| `Reporter` | Calculates and displays summary stats, saves report to file |

---

## 🛠 Tools & Environment
- Python 3.x
- Git & GitHub
- Kali Linux

---

## 👤 Author
**Noman Rizvi**  
Goal: Job-ready Machine Learning Engineer by 2026