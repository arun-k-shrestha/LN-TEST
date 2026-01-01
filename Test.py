import pandas as pd
df = pd.read_csv("LN_results_bi_combo.csv")

# Extract status
df["status"] = df["LND1"].str.extract(r"'(Success|Failure)'")

# Count results
counts = df["status"].value_counts()

print(counts)