# Mini ETL Project — Air Travel Data
Simple ETL project using Python and CSV data (Extract, Transform, Load)

## Dataset
- Source: [Air Travel CSV](https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv)
- Contains monthly airline passenger data for years 1958, 1959, and 1960.

## ETL Process
1. Extract: Load CSV data into Python using pandas.
2. Transform:
   - Rename columns for clarity
   - Remove null rows
   - Convert numeric columns to integer
3. Load: Save cleaned data into a new CSV file.

## Files
- `etl_airtravel.py` → Python script performing ETL
- `cleaned_airtravel.csv` → Cleaned dataset after ETL

## How to Run
1. Install pandas: `pip install pandas`
2. Run the script: `python etl_airtravel.py`
3. Output: `cleaned_airtravel.csv`

## Author
- Srivarsha
