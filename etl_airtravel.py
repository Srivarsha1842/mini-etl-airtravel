import pandas as pd

# ----------------------
# 1) EXTRACT
# ----------------------
url = "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv"
df = pd.read_csv(url)

print("Original data:")
print(df.head())

# ----------------------
# 2) TRANSFORM
# ----------------------

# Rename columns
df.columns = ["Month", "1958", "1959", "1960"]

# Remove null rows
df = df.dropna()

# Convert a column to numeric
df["1958"] = df["1958"].astype(int)

print("\nTransformed data:")
print(df.head())

# ----------------------
# 3) LOAD
# ----------------------
output_file = "cleaned_airtravel.csv"
df.to_csv(output_file, index=False)
print(f"\nCleaned file saved as: {output_file}")
