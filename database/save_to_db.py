import sqlite3
import pandas as pd
from config.settings import DB_PATH, CLEAN_DATA_DIR
from rich.console import Console
console = Console()

def save_to_db():
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Read the cleaned data from CSV
        df_cleaned = pd.read_csv(f"{CLEAN_DATA_DIR}/baseball_data_cleaned.csv")

        # Create a table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS baseball_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                year INTEGER,
                league TEXT,
                player TEXT,
                games INTEGER,
                teams TEXT            )
        ''')

        # Insert data into the table
        df_cleaned.to_sql('baseball_data', conn, if_exists='replace', index=False)

        # Commit the changes and close the connection
        conn.commit()
        console.print("[green]✅ Data saved to database successfully![/green]")
    except Exception as e:
        console.print(f"[red]⚠️  Error saving data to database: {e}[/red]")