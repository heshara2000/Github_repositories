import requests
import sqlalchemy
import pandas as pd # For transformation and manipulation
from sqlalchemy import create_engine # To create a connection to a database

def extract() -> dict:
    """ This function extracts data from 
    http://universities.hipolabs.com API.
    """
    API_URL = "http://universities.hipolabs.com/search?country=United+States"
    data = requests.get(API_URL).json()
    return data

def transform(data: dict) -> pd.DataFrame:
    """ Transforms the dataset into the desired data structure and filters it.
    """
    df = pd.DataFrame(data)
    print(f"Total Number of universities from API: {len(data)}")
    # Filter to get only universities in California
    df = df[df["name"].str.contains("California")]
    print(f"Number of universities in California: {len(df)}")
    df['domains'] = [','.join(map(str, l)) for l in df['domains']]
    df['web_pages'] = [','.join(map(str, l)) for l in df['web_pages']]
    df = df.reset_index(drop=True)
    return df[["domains", "country", "web_pages", "name"]]

def load(df: pd.DataFrame) -> None:
    """ Loads the data into an SQLite database. """
    disk_engine = create_engine('sqlite:///my_lite_store.db')
    df.to_sql('cal_uni', disk_engine, if_exists='replace')
    print("Data loaded successfully into the SQLite database.")

if __name__ == "__main__":
    # Main block to execute the ETL pipeline
    data = extract()
    df = transform(data)
    load(df)
