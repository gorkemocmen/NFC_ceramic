import pandas as pd

csv_path = 'data/daily_texts.csv'

# Try reading without specifying delimiter
df = pd.read_csv(csv_path)
print("Default read:")
print(df.head())

# Try reading with semicolon delimiter
df_semicolon = pd.read_csv(csv_path, delimiter=';')
print("\nSemicolon delimiter read:")
print(df_semicolon.head())
