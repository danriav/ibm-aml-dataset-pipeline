import os
import pandas as pd

# Define paths
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
raw_data_path = os.path.join(project_root, 'data', 'raw', 'transactions.csv')
processed_dir = os.path.join(project_root, 'data', 'processed')

# Create processed folder if it doesn't exist
os.makedirs(processed_dir, exist_ok=True)

# Load the raw CSV
print(" Loading dataset")
try:
    df = pd.read_csv(raw_data_path)
except FileNotFoundError:
    raise FileNotFoundError(f"Raw dataset not found at: {raw_data_path}")

expected_columns = {
    'transaction_id', 'customer_id', 'transaction_date', 'amount', 'merchant', 'category',
    'transaction_type', 'country', 'currency', 'is_fraud'
}

if not expected_columns.issubset(df.columns):
    missing = expected_columns - set(df.columns)
    raise ValueError(f"Dataset is missing expected columns: {missing}")

print("Data set loaded and schema validated.")

chunk_size = 50000
total_rows = df.shape[0]
num_chunks = (total_rows // chunk_size) + int(total_rows % chunk_size != 0)

print(f" Splitting data set into {num_chunks} chunks of {chunk_size} rows each...")

for i, chunk in enumerate(range(0, total_rows, chunk_size), start=1):
    chunk_df = df.iloc[chunk:chunk + chunk_size]
    chunk_file = os.path.join(processed_dir, f'transactions_part_{i}.csv')
    chunk_df.to_csv(chunk_file, index=False)
    print(f" Saved chunk {i} to {chunk_file}")

print(" Data transformation complete. Chunks are available in:", processed_dir)