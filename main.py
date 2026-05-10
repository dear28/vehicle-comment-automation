from datetime import datetime
from pathlib import Path
from excel_manager import load_excel_data, create_backup_file, clean_excel_file
from helpers import normalize_numeric_value, create_log_path, save_log
from database import insert_comment, create_connection
from comments import generate_comment


def main():
    excel_file_path = Path("templates/excel_file.xlsx")
    today = datetime.today().strftime("%Y-%m-%d")
    df_data = load_excel_data(excel_file_path)
    log_path = create_log_path(today)
    save_log(log_path, "Process started")
    backup_rows = []

    connection = None
    
    try:
        connection = create_connection(log_path, save_log)

        for row in df_data.itertuples(index=False):

            id_comment = normalize_numeric_value(row.Id_coment)

            comment_data = {
                "plate": row.Plate,
                "client": row.Contact_name,
                "phone": normalize_numeric_value(row.Phone),
                "address": row.Address,
                "technician": row.Technician,
                "date_comment": row.Date,
                "programmer": row.Programmer,
                "reason": row.Fail_reason,
                "total_failed": normalize_numeric_value(row.Failed),
                "total_vehicles": row.Total_vehicles,
                "total_vehicles_ok": normalize_numeric_value(row.Vehicles_ok),
                "total_pending_vehicles": normalize_numeric_value(row.Pending_vehicles),
                "vehicles_per_day": normalize_numeric_value(row.Vehicle_at_day),
                "hour_comment": row.Hour,
                "total_units": normalize_numeric_value(row.Units)
            }

            comment = generate_comment(id_comment, comment_data)

            if connection:
                insert_comment(
                    connection,
                    comment_data["plate"],
                    comment,
                    comment_data["programmer"],
                    log_path,
                    save_log
                    )

            # Create list backup
            backup_rows.append({
                "Plate": comment_data["plate"],
                "Comment": comment,
                "Programmer": comment_data["programmer"]
            })            

        create_backup_file(backup_rows, today)

        clean_excel_file(excel_file_path)
    except Exception as e:
        save_log(log_path, f"Unexpected error: {e}")
    finally:
        if connection:
            connection.close()
        
    save_log(
    log_path,
    f"Process completed successfully. Total comments: {len(backup_rows)}"
)

if __name__ == "__main__":
    main()