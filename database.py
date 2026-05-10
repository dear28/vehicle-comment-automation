import pyodbc


# Create database connection
def create_connection(log_path, save_log):
    try:
        connection = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=YOUR_SERVER;"
            "DATABASE=YOUR_DATABASE;"
            "UID=YOUR_USERNAME;"
            "PWD=YOUR_PASSWORD"
        )

        return connection
    
    except Exception as e:
        save_log(log_path, f"Database connection error: {e}")
        return None


# Insert comment into database
def insert_comment(
        connection,
        plate,
        comment,
        programmer,
        log_path,
        save_log
):
    query = """
        INSERT INTO vehicle_comment(Date, Plate, Comment, Programmer)
        VALUES(GETDATE(), ?, ?, ?);
    """

    # Insert the comment
    try:
        with connection.cursor() as cursor:            
            cursor.execute(query, plate, comment, programmer)

        connection.commit()

    except Exception as e:
        save_log(log_path, f"Insert error: {e}")