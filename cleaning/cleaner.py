import pandas as pd
from config.settings import CLEAN_DATA_DIR, DROPPED_DATA_DIR

def clean_data(df):
    try:
        df.columns = [
            'al_year', 'al', 'al_games', 'al_teams',
            'nl_year', 'nl', 'nl_games', 'nl_teams'
        ]

        
        df = df[~df['al_year'].isin(['Year', '-', None])]
        df = df[~df['al_year'].str.contains("[a-zA-Z]", na=False)]

        
        df = df[~df['al_games'].isin(['-'])]
        df = df[~df['nl_games'].isin(['-'])]

        
        df = df.dropna(how='all')

        
        df = df.drop(columns=["nl_year"], errors='ignore')

        
        df = df.drop_duplicates().reset_index(drop=True)

        
        empty_rows = df[df.isnull().all(axis=1)]
        empty_rows.to_csv(f"{DROPPED_DATA_DIR}/empty_rows.csv", index=False)

        
        df["al_year"] = df["al_year"].astype(int)
        df["al"] = df["al"].astype(str).str.strip()
        df["al_games"] = df["al_games"].astype(int)
        df["al_teams"] = df["al_teams"].astype(str).str.strip()

        df["nl"] = df["nl"].astype(str).str.strip()
        df["nl_games"] = df["nl_games"].astype(int)
        df["nl_teams"] = df["nl_teams"].astype(str).str.strip()

        return df

    except Exception as e:
        print(f"Error during data cleaning: {e}")
        return None
