from scraping.scraper import scrape_data
from config.settings import RAW_DATA_DIR, BASE_URL

from data_cleaning.data_cleaning import clean_data
from database.db_handler import db_handler
from database.cli_menu import cli_menu
from saving_to_csv import save_raw_data, save_cleaned_data

import pandas as pd
from rich.console import Console

console = Console()

def main():
    console.print("[bold yellow]Starting the data scraping process...[/bold yellow]")

    df_raw = scrape_data(BASE_URL)
    if df_raw is not None and not df_raw.empty:
        # Rename columns
        df_raw.columns = [
            'al_year', 'al', 'al_games', 'al_teams', 'nl_year',
            'nl', 'nl_games', 'nl_teams'
        ]
        console.print("[green]✅ Data scraped successfully![/green]")

        save_raw_data(df_raw)

        # Read back and clean data
        df_raw_read = pd.read_csv(f"{RAW_DATA_DIR}/baseball_data_raw.csv")
        df_cleaned = clean_data(df_raw_read)

        if df_cleaned is not None and not df_cleaned.empty:
            save_cleaned_data(df_cleaned)
        else:
            console.print("⚠️[red] No cleaned data available.[/red]")
    else:
        console.print("[red]No data scraped.[/red]")

    # Save to database
    console.print("[bold yellow]Saving cleaned data to the database...[/bold yellow]")
    save_to_db = db_handler()
    if save_to_db:
        menu = input("Do you want to view database CLI menu? (yes/no): ").strip().lower()
        if menu == 'yes':
            cli_menu()
