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

        df["al"] = df["al"].str.lower()
        df["nl"] = df["nl"].str.lower()
        df["al_teams"] = df["al_teams"].str.lower()

        # Extract AL data
        al_df = pd.DataFrame({
            'year': df['al_year'],
            'league': 'AL',
            'player': df['al'],
            'games': df['al_games'],
            'team': df['al_teams']
        })

        # Extract NL data
        nl_df = pd.DataFrame({
            'year': df['nl_year'],
            'league': 'NL',
            'player': df['nl'],
            'games': df['nl_games'],
            'team': df['nl_teams']
        })

        # Combine both
        df_final = pd.concat([al_df, nl_df], ignore_index=True)
       

        df_final['year'] = pd.to_datetime(df_final['year'])
        df_final['year'] = df_final['year'].dt.year

        return df_final

    except Exception as e:
        print(f"Error during data cleaning: {e}")
        return None
