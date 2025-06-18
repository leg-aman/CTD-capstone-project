import sqlite3
import pandas as pd
from config.settings import DB_PATH, CLEAN_DATA_DIR
from rich.console import Console
console = Console()

def create_db_connection():
    """Create a database connection to the SQLite database specified by DB_PATH."""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        console.print("[green]✅ Database connection established successfully![/green]")
        return conn, cursor
    except sqlite3.Error as e:
        console.print(f"[red]⚠️  Database connection error: {e}[/red]")
        return None

def db_handler():
    try:
        # Connect to the SQLite database
        conn, cursor = create_db_connection()
        if conn is None:
            return False

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
        conn.close()
        return True
    except sqlite3.Error as e:
        console.print(f"[red]⚠️  Database error: {e}[/red]")
        return False
    except Exception as e:
        console.print(f"[red]⚠️  Error saving data to database: {e}[/red]")
        return False

def top_players_by_league(league,conn, cursor, top_n=5):
    """Fetch top players by games pitched in a specific league."""
    
    if conn is None:
        return None

    query = f'''
        SELECT player, SUM(games) as total_games
        FROM baseball_data
        WHERE league = ?
        GROUP BY player
        ORDER BY total_games DESC
        LIMIT ?
    '''
    cursor.execute(query, (league, top_n))
    results = cursor.fetchall()
    conn.close()
    if results:
        df = pd.DataFrame(results, columns=['Player', 'Total Games'])
        console.print(f"[green]✅ Top {top_n} players in {league}:[/green]")
        console.print(df)
        return df
    else:
        console.print(f"[red]⚠️  No data found for league: {league}[/red]")
        return None
    
def players_above_avg(threshold, conn, cursor):
    """Fetch players with games pitched above a specified average threshold."""
    
    if conn is None:
        return None

    query = '''
        SELECT player, AVG(games) as avg_games
        FROM baseball_data
        GROUP BY player
        HAVING avg_games > ?
    '''
    cursor.execute(query, (threshold,))
    results = cursor.fetchall()
    conn.close()
    
    if results:
        df = pd.DataFrame(results, columns=['Player', 'Average Games'])
        console.print(f"[green]✅ Players with average games pitched above {threshold}:[/green]")
        console.print(df)
        return df
    else:
        console.print(f"[red]⚠️  No players found with average games above {threshold}[/red]")
        return None
def top_years_by_games_pitched(conn, cursor ,top_n=5):
    """Fetch top years with the most games pitched."""
   
    if conn is None:
        return None

    query = '''
        SELECT year, SUM(games) as total_games
        FROM baseball_data
        GROUP BY year
        ORDER BY total_games DESC
        LIMIT ?
    '''
    cursor.execute(query,conn, cursor,(top_n,))
    results = cursor.fetchall()
    conn.close()
    
    if results:
        df = pd.DataFrame(results, columns=['Year', 'Total Games'])
        console.print(f"[green]✅ Top {top_n} years with most games pitched:[/green]")
        console.print(df)
        return df
    else:
        console.print("[red]⚠️  No data found for top years[/red]")
        return None
def players_from_team(team ,conn, cursor):
    """Fetch players from a specific team."""
    
    if conn is None:
        return None

    query = '''
        SELECT player, SUM(games) as total_games
        FROM baseball_data
        WHERE team LIKE ?
        GROUP BY player
    '''
    cursor.execute(query, (f'%{team}%',))
    results = cursor.fetchall()
    conn.close()
    
    if results:
        df = pd.DataFrame(results, columns=['Player', 'Total Games'])
        console.print(f"[green]✅ Players from team '{team}':[/green]")
        console.print(df)
        return df
    else:
        console.print(f"[red]⚠️  No players found for team: {team}[/red]")
        return None