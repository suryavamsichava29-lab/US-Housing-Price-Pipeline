import pandas as pd

# --- 1. EXTRACTION PHASE ---
print("--- Extraction Phase ---")
df = pd.read_csv('raw_housing_data.csv')
print(f"Initial row count: {len(df)}")

# --- 2. TRANSFORMATION PHASE ---
print("\n--- Transformation Phase ---")
df = df.drop_duplicates()
df['Bedrooms'] = pd.to_numeric(df['Bedrooms'], errors='coerce')
df['Bedrooms'] = df['Bedrooms'].fillna(1)
df = df[df['Status'] == 'Sold']
print("Data cleaned and filtered.")

# --- 3. LOADING PHASE ---
print("\n--- Loading Phase ---")

# We are saving the clean data into a new file
# index=False ensures we don't save those row numbers (0, 2, 3, 5)
df.to_csv('master_housing_data.csv', index=False)

print("SUCCESS: Clean data loaded into 'master_housing_data.csv'")