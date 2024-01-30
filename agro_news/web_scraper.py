import logging
import os
from datetime import datetime

import pandas as pd
import requests
from bs4 import BeautifulSoup
from db.connection import engine
from dotenv import find_dotenv
from dotenv import load_dotenv

# Constants
LOG_FILENAME = "agro_news/logs/scraper.log"
LOG_LEVEL = logging.ERROR
LOG_FORMAT = "%(asctime)s:%(levelname)s:%(message)s"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
URL = os.getenv("NEWS_URL")
CROP = os.getenv("CROP")
SCHEMA = os.getenv("DB_SCHEMA")
IGNORE_LIST = [
    "Categorias",
    "Siga nossas redes sociais:",
    "Conteúdo Relacionado",
    "Conteúdos mais lidos",
    "Conteúdos mais comentados",
    "SOBRE NÓS",
    "SIGA-NOS",
]

# Load environment variables
load_dotenv(find_dotenv())

# Set up logging
logging.basicConfig(filename=LOG_FILENAME, level=LOG_LEVEL, format=LOG_FORMAT)
logger = logging.getLogger(__name__)


def get_soup(url):
    try:
        response = requests.get(url, headers=HEADERS)
        return BeautifulSoup(response.content, "html.parser")
    except Exception as e:
        logger.error(f"Failed to get soup from url {url}. Error: {e}")
        raise


def get_news_data(soup):
    try:
        data_list = []
        tags = soup.find_all(["h3", "h2"])
        news_list = []
        date = None

        for tag in tags:
            if tag.name == "h3":
                if (
                    date
                ):  # if 'date' is not None, means we have collected some news, so save it
                    data_list.append({"Date": date, "News": news_list})
                    news_list = []  # reset the news_list for next date
                date = tag.text.strip()
            elif tag.name == "h2":
                news_text = tag.text.strip()
                # Only append the news_text to news_list if it's not in the ignore_list
                if news_text not in IGNORE_LIST:
                    news_list.append(news_text)

        # Save the last collected news
        if date and news_list:
            data_list.append({"Date": date, "News": news_list})

        return data_list
    except Exception as e:
        logger.error(f"Failed to get news data. Error: {e}")
        raise


def create_dataframe(data_list):
    try:
        df = pd.concat(
            [
                pd.DataFrame(
                    {"date_news": data["Date"], "news": data["News"], "crop": CROP}
                )
                for data in data_list
            ],
            ignore_index=True,
        )
        df["date_news"] = pd.to_datetime(
            df["date_news"], errors="coerce", dayfirst=True
        )
        return df
    except Exception as e:
        logger.error(f"Failed to create dataframe. Error: {e}")
        raise


def filter_by_today(df: pd.DataFrame):
    try:
        today = datetime.today().strftime("%d/%m/%Y")
        return df[df["date_news"] == today]
    except Exception as e:
        logger.error(f"Failed to filter dataframe by today. Error: {e}")
        raise


def save_to_database(df: pd.DataFrame):
    try:
        df.to_sql(
            "AGRO_NEWS", con=engine, schema=SCHEMA, if_exists="append", index=False
        )
    except Exception as e:
        logger.error(f"Failed to save dataframe to database. Error: {e}")
        raise


def main():
    try:
        soup = get_soup(URL)
        data_list = get_news_data(soup)
        df = create_dataframe(data_list)
        df = filter_by_today(df)
        save_to_database(df)
    except Exception as e:
        logger.error(f"An error occurred in main. Error: {e}")
        raise


if __name__ == "__main__":
    main()
