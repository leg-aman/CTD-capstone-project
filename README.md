# CTD-CAPSTONE PROJECT: Data Analysis and Visualization

## Overview
This project involves web scraping MLB baseball data, cleaning it, storing it in a database, and creating a Streamlit dashboard for data visualization.

## Project Structure

```plaintext
CTD-CAPSTONE-PROJECT/
├── config/
│   └── settings.py
├── dashboard/
│   └── streamlit_app.py
├── data/
│   ├── clean/
│   │   └── baseball_data_cleaned.csv
│   ├── db/
│   │   └── mlb.db
│   ├── dropped/
│   │   └── dropped_data.csv
│   └── raw/
│       └── baseball_data_raw.csv
├── data_cleaning/
│   └── data_cleaning.py
├── database/
│   ├── cli_menu.py
│   └── db_handler.py
├── web_scraping/
│   └── web_scraper.py
├── requirements.txt
└── README.md


1. Data Scraping
"Our project starts with data scraping. We collected raw MLB player statistics from online sources using Python scripts. This automated process ensures we have up-to-date and comprehensive data for analysis."

2. Data Cleaning
"Next, we clean the data. This involves handling missing values, correcting data types, and standardizing formats. The cleaned data is saved as a CSV file, making it ready for further processing and analysis."

3. Database
"After cleaning, the data is stored in a structured database. This allows for efficient querying and management, and ensures data integrity for our application."

4. Visualization (Dashboard)
"Finally, we visualize the data using a Streamlit dashboard.

Users can filter by league and year range using the sidebar.
The dashboard displays tables and charts, such as the top 10 players by games pitched, total games pitched by year, and league breakdowns.
All visualizations update instantly based on user selections, making it easy to explore trends and leaders in MLB pitching."
Conclusion
"This end-to-end workflow—from scraping to visualization—demonstrates how we can turn raw sports data into interactive insights for users."
