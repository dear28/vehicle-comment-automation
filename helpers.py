from pathlib import Path

import pandas as pd


# Create log file path
def create_log_path(today):
    base_dir = Path(__file__).resolve().parent
    log_dir = base_dir / "logs"

    # Create log directory if it does not exist
    log_dir.mkdir(exist_ok=True)

    return log_dir / f"log_{today}.txt"


# Save information in log file
def save_log(log_path, info):
    with open(log_path, "a", encoding="utf-8") as log:          
        log.write(f"{info}\n")


# Helper to normalize numeric data
def normalize_numeric_value(value):
    if pd.isna(value):
        return ""

    return str(int(float(value)))