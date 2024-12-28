import pandas as pd

# Pfad zur CSV-Datei
csv_file = "data/jobs.csv"

# CSV-Datei in ein DataFrame laden
df = pd.read_csv(csv_file)

# DataFrame anzeigen
print(df.head())
