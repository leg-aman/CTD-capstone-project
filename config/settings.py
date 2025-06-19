DB_PATH = 'data/db/mlb.db'
RAW_DATA_DIR = './data/raw'
CLEAN_DATA_DIR = 'data/clean'
DROPPED_DATA_DIR = 'data/dropped'
BASE_URL = 'https://www.baseball-almanac.com/pitching/pigamp4.shtml'
TITLE = 'Year by Year Leaders for Games Pitched'
DESCRIPTION = (
    "This script scrapes MLB data from Baseball Almanac, cleans it, "
    "and saves it to a SQLite database. It also provides a CLI menu for database operations."
)
VERSION = '1.0.0'
AUTHOR = 'Amanuel Feyisa'