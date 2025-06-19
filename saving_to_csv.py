import os
from rich.console import Console
import pandas as pd
from config.settings import RAW_DATA_DIR, CLEAN_DATA_DIR

console = Console()

def save_raw_data(df_raw: pd.DataFrame):
    file_path = f"{RAW_DATA_DIR}/baseball_data_raw.csv"
    console.print("[yellow]Saving raw data to CSV file...[/yellow]")
    df_raw.to_csv(file_path, index=False, header=False)
    console.print(f"[green]Raw data saved to:[/green] {file_path}")
    console.print(df_raw.head())

def save_cleaned_data(df_cleaned: pd.DataFrame):
    file_path = f"{CLEAN_DATA_DIR}/baseball_data_cleaned.csv"
    df_cleaned.to_csv(file_path, index=False)
    console.print("[green]✅ Data cleaned successfully![/green]")
    console.print(f"Cleaned data saved to: {file_path}")
    console.print(df_cleaned.head())
