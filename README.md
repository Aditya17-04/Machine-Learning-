# Machine Learning - Insurance Data Analysis

A Python project for exploratory data analysis (EDA) on an insurance dataset.

## Dataset

**insurance.csv** — Contains 1338 records with 7 columns:

| Column | Description |
|---|---|
| `age` | Age of the primary beneficiary |
| `sex` | Gender of the beneficiary |
| `bmi` | Body Mass Index |
| `children` | Number of children/dependents covered |
| `smoker` | Whether the beneficiary is a smoker |
| `region` | Residential region in the US |
| `charges` | Individual medical costs billed by health insurance |

## Features

- Load and inspect the dataset (shape, info, describe)
- Check for missing values
- Visualize distributions of numeric columns (`age`, `bmi`, `children`, `charges`) using histograms
- Count plot for categorical columns (e.g. `children`)

## Requirements

- Python 3.x
- numpy
- pandas
- seaborn
- matplotlib

## Setup

1. Create and activate a virtual environment:
   ```bash
   python -m venv machine
   .\machine\Scripts\Activate.ps1
   ```

2. Install dependencies:
   ```bash
   pip install numpy pandas seaborn matplotlib
   ```

## Usage

```bash
python main.py
```
