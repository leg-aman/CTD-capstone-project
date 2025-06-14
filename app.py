from scraping.scraper import scrape_data
from cleaning.cleaner import clean_data
import pandas as pd
from rich.console import Console
console = Console()

from config.settings import DB_PATH, RAW_DATA_DIR, CLEAN_DATA_DIR, BASE_URL

def main():

    # scraping data 
    console.print("[bold yellow]Starting the data scraping process...[/bold yellow]")

    df_raw = scrape_data(BASE_URL)
    if df_raw is not None and df_raw.empty is False:
        # Save the DataFrame to a CSV file
        df_raw.columns = [ 
            'al_year', 'al', 'al_games', 'al_teams', 'nl_year',
            'nl', 'nl_games', 'nl_teams'
        ]
        df_raw.to_csv(f"{RAW_DATA_DIR}/baseball_data_raw.csv", index=False,header=False)
        print(f"Data saved to {RAW_DATA_DIR}/baseball_data_raw.csv")

        print("Raw data scraped successfully! \n", df_raw.head())
    else:
        print("No data scraped.")

    # Clean the data
    console.print("[yellow]Cleaning data...[/yellow]")

    df_raw_1 = pd.read_csv(f"{RAW_DATA_DIR}/baseball_data_raw.csv")
    df_raw_2 = pd.DataFrame(df_raw_1)
    df_cleaned = clean_data(df_raw_2)
    if df_cleaned is not None and df_cleaned.empty is False:
        df_cleaned.to_csv(f"{CLEAN_DATA_DIR}/baseball_data_cleaned.csv", index=False)
        print(f"Cleaned data saved to {CLEAN_DATA_DIR}/baseball_data_cleaned.csv")
        console.print("[green]✅ Data cleaned successfully![/green] \n", df_cleaned.head())
    else:
        console.print("⚠️[red]  No cleaned data available.[/red]")

if __name__ == "__main__": 
    main()