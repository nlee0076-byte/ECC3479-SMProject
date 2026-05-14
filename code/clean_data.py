import pandas as pd
from pathlib import Path

print("Starting data cleaning...")

# Load raw data
df = pd.read_csv("data/raw/Students Social Media Addiction.csv")

print(f"Loaded {len(df)} rows")

# ---- CLEANING ----

# 1. Rename columns (make them consistent and clear)
df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")

print("Columns renamed:", list(df.columns))

# 2. Check missing values
print("Missing values:\n", df.isnull().sum())

# Drop missing values (simple approach)
df = df.dropna()

print(f"After dropping missing: {len(df)} rows")

# 3. Fix inconsistent text (example: lowercase categories)
if "most_used_platform" in df.columns:
    df["most_used_platform"] = df["most_used_platform"].str.lower().str.strip()
    print("Most used platform lowercased")

# 4. Filter age group (18–30)
if "age" in df.columns:
    df = df[(df["age"] >= 18) & (df["age"] <= 30)]
    print(f"After age filter: {len(df)} rows")

# 5. Create usage categories (optional but good)
if "avg_daily_usage_hours" in df.columns:
    df["usage_group"] = pd.cut(
        df["avg_daily_usage_hours"],
        bins=[0, 2, 4, 10],
        labels=["low", "medium", "high"]
    )
    print("Usage group added")

# ---- SAVE CLEAN DATA ----

df.to_csv("data/clean/cleaned_social_media.csv", index=False)
print("✅ Cleaned dataset saved to data/clean/")

# ---- SUMMARY STATISTICS ----
output_dir = Path("output")
output_dir.mkdir(parents=True, exist_ok=True)

numeric_summary = df.select_dtypes(include=["number"]).describe().T
numeric_summary = numeric_summary[["count", "mean", "std", "min", "25%", "50%", "75%", "max"]].round(2)

numeric_summary.to_csv(output_dir / "clean_data_summary.csv")

# Write a markdown table without requiring optional dependencies
md = numeric_summary.reset_index().rename(columns={"index": "variable"})
columns = md.columns.tolist()
header = "| " + " | ".join(columns) + " |\n"
separator = "| " + " | ".join(["---"] * len(columns)) + " |\n"
rows = ["| " + " | ".join(str(value) for value in row) + " |" for row in md.values.tolist()]
with open(output_dir / "clean_data_summary.md", "w", encoding="utf-8") as md_file:
    md_file.write("# Clean Data Summary Statistics\n\n")
    md_file.write(header)
    md_file.write(separator)
    md_file.write("\n".join(rows) + "\n")

print("✅ Summary statistics saved to output/clean_data_summary.csv and output/clean_data_summary.md")
