from pathlib import Path

import pandas as pd
import openpyxl


# Select required columns
REQUIRED_COLUMNS = [
    "Plate",
    "Id_coment",
    "Contact_name",
    "Phone",
    "Address",
    "Technician",
    "Date",
    "Programmer",
    "Fail_reason",
    "Failed",
    "Total_vehicles",
    "Vehicles_ok",
    "Pending_vehicles",
    "Vehicle_at_day",
    "Hour",
    "Units"
    ]


# Load dataframe from Excel file
def load_excel_data(excel_file_path):
    df_data = pd.read_excel(
        excel_file_path,
        sheet_name="Sheet1",
        engine="openpyxl"
    )

    # Select required columns
    df_data = df_data[REQUIRED_COLUMNS]

    # Remove empty rows
    df_data = df_data.dropna(how="all")

    return df_data


# Create Excel backup file
def create_backup_file(backup_rows, today):
    # Reports directory
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    reports_backup = reports_dir / f"comment_backup_{today}.xlsx"

    df_backup = pd.DataFrame(backup_rows)

    with pd.ExcelWriter(reports_backup) as writer:
        df_backup.to_excel(
            writer,
            sheet_name="Comments done",
            index=False
        )


# Remove all rows except headers
def clean_excel_file(excel_file_path):
    excel_file = openpyxl.load_workbook(excel_file_path)

    sheet = excel_file["Sheet1"]

    # Remove rows except headers
    sheet.delete_rows(2, sheet.max_row)

    excel_file.save(excel_file_path)