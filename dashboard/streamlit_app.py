import numpy as np
import streamlit as st
import pandas as pd

def load_data():
    # Load the dataset
    df = pd.read_csv("../data/clean/baseball_data_cleaned.csv", parse_dates=['year'])
    return df

# Load the dataset
df = load_data()
data = df.copy()
# Set the title of the app 
st.title("MLB Leaders Dashboard")


#  add on/ off for league
st.sidebar.subheader("League Filter")
league_filter = st.sidebar.multiselect(
    "Select League(s):",
    options=df['league'].unique(),
    default=df['league'].unique()
)
# Filter the DataFrame based on the selected league(s)
df = df[df['league'].isin(league_filter)]


st.header("Year by Year Leaders for Games Pitched")
st.dataframe(df)

# Filter the dataset for the top 10 players by games pitched
df = df[df['games'] > 0].sort_values(by='games', ascending=False).head(10)
# Display the filtered dataset
st.subheader("Top 10 Players by Games Pitched")
st.dataframe(df)

# bar chart for total games pitched by year
st.subheader("Total Games Pitched by Year")
st.bar_chart(df, x='year', y='games',
             use_container_width=True)


df['league'] = df['league'].str.upper()
df_grouped = df.groupby(['year', 'league'])['games'].sum().unstack().fillna(0)
st.subheader("Total Games Pitched by League")  
st.area_chart(df_grouped, use_container_width=True)

