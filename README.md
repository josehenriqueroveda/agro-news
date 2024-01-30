# Agro News Web Scraper

The Agro News Web Scraper is a Python-based tool designed to automate the process of gathering news related to agriculture from a specified URL. The tool is designed to be efficient, reliable, and easy to use, making it an invaluable resource for anyone interested in staying up-to-date with the latest developments in the agricultural sector.

## Project Purpose

The purpose of this project is to provide a streamlined way of collecting and storing news data related to agriculture. By automating this process, we can ensure that the most recent and relevant news is always readily available for analysis and review.

## Features

- Automated web scraping from a specified URL
- Data filtering to include only news from the current date
- Data storage in a specified database
- Error logging for easy debugging and issue resolution

## Dependencies

This project relies on several Python libraries:

- `pandas` for data manipulation and analysis
- `requests` for sending HTTP requests
- `BeautifulSoup` for parsing HTML and XML documents
- `SQLAlchemy` for SQL toolkit and Object-Relational Mapping (ORM) for Python
- `python-dotenv` for environment variable handling

## How It Works

The script begins by loading environment variables from a .env file and setting up a logger for error tracking. The `main()` function then calls several other functions in sequence:

- `get_soup(URL)`: Sends a GET request to the specified URL and returns a BeautifulSoup object.
- `get_news_data(soup)`: Extracts news data from the BeautifulSoup object and returns a list of dictionaries, each containing a date and a list of news items for that date.
- `create_dataframe(data_list)`: Converts the list of dictionaries to a pandas DataFrame.
- `filter_by_today(df)`: Filters the DataFrame for news items from today's date.
- `save_to_database(df)`: Saves the DataFrame to a database table.

If any of these functions encounter an error, they log the error and raise an exception, which is caught in `main()` and logged.

## Usage

To use this script, you'll need to set the following environment variables in a .env file:

- `NEWS_URL`: The URL to scrape news data from.
- `CROP`: A string to be added to each row in the 'crop' column of the DataFrame.
- `DB_SCHEMA`: The schema of the database table to save the DataFrame to.

And the database engine (imported from `connection.py`).

Once these variables are set, you can run the script with `python web_scraper.py`.

## Note

The script ignores any news items whose text is in the `IGNORE_LIST` list. This list can be customized as needed.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
