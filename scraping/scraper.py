from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from rich.console import Console
console = Console()

def scrape_data(url):
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    )
    # Initialize the WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Open the URL
        driver.get(url)

        # Wait for the table to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "table"))
        )

        # Find the table and extract data
        table = driver.find_element(By.TAG_NAME, "table")
        rows = table.find_elements(By.TAG_NAME, "tr")[2:]

        data = [] 
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            cols = [col.text.strip() for col in cols]
            data.append(cols)

        console.print("[green]✅ Data scraped successfully![/green]")

        # Convert to DataFrame
        df = pd.DataFrame(data)
        # print(df.head())

        return df
    except Exception as e:
        console.print(f"[red]Error during scraping: {e}[/red]")
        return None

    finally:
        driver.quit()
