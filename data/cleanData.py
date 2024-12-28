import os
import pandas as pd

# Set the working directory to the project root (if necessary)
os.chdir("/Users/lvs/BA-Data-Scraping")

# File paths
input_file = os.path.join("data", "raw", "jobs.csv")  # Input file in 'data/raw'
output_file = os.path.join("data", "jobs_cleaned.csv")  # Output file in 'data'

# Read the CSV file
df = pd.read_csv(input_file)

# Normalize text for better duplicate detection
def normalize_text(text):
    return text.strip().lower() if isinstance(text, str) else text

df["company"] = df["company"].apply(normalize_text)
df["location"] = df["location"].apply(normalize_text)
df["description"] = df["description"].apply(normalize_text)

# Remove duplicates based on relevant columns
df_cleaned = df.drop_duplicates(subset=["company", "location", "description"], keep="first")

# Check if an 'id' column exists and remove it
if "id" in df_cleaned.columns:
    df_cleaned = df_cleaned.drop(columns=["id"])

# Add new sequential numbering
df_cleaned = df_cleaned.reset_index(drop=True)
df_cleaned.index += 1  # Start numbering at 1
df_cleaned.insert(0, "id", df_cleaned.index)  # Insert new ID column

# Save the cleaned file
df_cleaned.to_csv(output_file, index=False, encoding="utf-8")

print(f"The file has been cleaned. {len(df) - len(df_cleaned)} duplicates were removed.")
print(f"The cleaned file has been saved in the 'data' folder as '{output_file}'.")