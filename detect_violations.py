# src/detect_violations.py
import pandas as pd
import os

def detect_violations():
    # Get absolute path to data file
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_file = os.path.join(base_dir, "data", "sla_logs.csv")

    # Read CSV
    try:
        df = pd.read_csv(data_file)
    except FileNotFoundError:
        print(f"Error: {data_file} not found!")
        return []

    # Example: detect SLA violations where response_time > 200ms
    if 'response_time' not in df.columns:
        print("Error: CSV must have 'response_time' column")
        return []

    violations = df[df['response_time'] > 200].to_dict('records')
    return violations
