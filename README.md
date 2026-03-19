# Research-Support-Tool-For-Drawing-Data-Chart

A lightweight Python-based command-line utility designed to assist academic writing and research analysis by generating basic visual outputs from structured data inputs.

This tool transforms spreadsheet-style data (e.g., CSV files) into simple visual representations such as line charts, bar charts, and pie charts. It is intended for exploratory analysis and inclusion in academic papers or research presentations.

---

## 🎯 Project Purpose

This project was developed as a small, research-support utility to:

- Assist with academic writing and analysis  
- Convert structured data into visual outputs  
- Provide simple, reproducible chart generation  
- Support exploratory data visualization under guidance and supervision  

The focus is on simplicity, clarity, and usability rather than complex analytics.

---

## ✨ Features

- 📈 Line Chart Generation  
- 📊 Bar Chart Generation  
- 🥧 Pie Chart Generation  
- 📁 CSV-based structured data input  
- 🖥️ One-line command execution  
- 📝 Basic documentation support  

---

## 📂 Input Format

The tool expects structured CSV input.

Example (`data.csv`):

```csv
Category,Value
A,10
B,20
C,30
```

For line and bar charts:

- The first column is treated as the x-axis.
- The second column is treated as the y-axis.

For pie charts:

- The first column is treated as labels.
- The second column is treated as values.

---

## 🚀 Usage

Run from the command line:

```bash
python main.py --input data.csv --type bar --output chart.png
```

### Arguments

| Argument   | Description                                |
|------------|--------------------------------------------|
| `--input`  | Path to input CSV file                     |
| `--type`   | Chart type (`line`, `bar`, `pie`)          |
| `--output` | Output image filename (e.g., result.png)   |

Example:

```bash
python main.py --input sample.csv --type line --output result.png
```

The script will generate a PNG file containing the selected chart.

---

## 🛠️ Installation

1. Clone the repository:

```bash
git clone git@github.com:cliff15037/Research-Support-Tool-For-Drawing-Data-Chart.git
cd Research-Support-Tool-For-Drawing-Data-Chart
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

Typical dependencies include:

- matplotlib  
- pandas  

---

## 🧱 Project Structure

```
.
├── main.py
├── requirements.txt
├── sample_data/
│   └── example.csv
├── output/
└── README.md
```

---

## 📚 Design Philosophy

This project intentionally prioritizes:

- Simplicity over complexity  
- Readability over optimization  
- Reproducibility over automation  
- Clear documentation for academic use  

It is not intended to replace full data science frameworks, but rather to provide a minimal, focused visualization tool for research support.

---

## 🔄 High-Level Workflow

```mermaid
flowchart LR
    A[Command Input] --> B[Parse Arguments]
    B --> C[Read CSV]
    C --> D[Validate Data]
    D --> E[Choose Chart Type]
    E --> F[Render Visualization]
    F --> G[Save PNG Output]
```

---

## 🔄 Iteration and Feedback

The tool may be updated based on:

- Research supervision feedback  
- Usability improvements  
- Documentation refinement  
- Minor feature extensions  

---

## 📄 License

This project is intended for academic and research support purposes.
