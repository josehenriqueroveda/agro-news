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

# Sentiment Analysis

The sentiment analysis module in `example.py` file is made by `Gemini API`, from Google. It is provided a prompt with the instructions and the news headline to be analyzed. The output is the sentiment of the news headline, which can be positive, negative, or neutral, and its scores from -1 to 1.

## Output example
```json
[
  {
    "classification": "POSITIVE",
    "score": 0.671,
    "headline": "Milho se apoia no dólar e sobe até 1,8% na B3 nesta segunda-feira"
  },
  {
    "classification": "NEGATIVE",
    "score": -0.412,
    "headline": "Exportação de milho avança menos de 500 toneladas na semana e representa apenas 6% de abril/23"
  },
  {
    "classification": "POSITIVE",
    "score": 0.654,
    "headline": "USDA informa venda de milho para o México nesta 2ª feira (15)"
  },
  {
    "classification": "POSITIVE",
    "score": 0.891,
    "headline": "Segunda-feira começa com milho subindo na Bolsa Brasileira"
  },
  {
    "classification": "NEGATIVE",
    "score": 0.8,
    "headline": "Milho/Cepea: Com novas quedas, Indicador volta a fechar abaixo dos R$ 60/sc"
  },
  {
    "classification": "POSITIVE",
    "score": 0.56,
    "headline": "Dólar ajuda milho fechar 6ªfeira em alta na B3, mas não evita desvalorização semanal"
  },
  {
    "classification": "POSITIVE",
    "score": 0.891,
    "headline": "Safras & Mercado eleva estimativas para produção de soja e milho do Brasil"
  },
  {
    "classification": "POSITIVE",
    "score": 0.767,
    "headline": "Preços futuros do milho abrem a sexta-feira em alta na B3 e em Chicago"
  },
  {
    "classification": "POSITIVE",
    "score": 0.78,
    "headline": "Milho: Cotação futura finaliza a sessão desta 4ª feira com ganhos na CBOT"
  },
  {
    "classification": "NEUTRAL",
    "score": 0,
    "headline": "Novo leilão de frete de milho ocorrerá na quinta-feira (11)"
  },
  {
    "classification": "POSITIVE",
    "score": 0.678,
    "headline": "Ucrânia enviará 600 mil t de milho à China em abril e 400 mil t em maio, dizem corretores"
  },
  {
    "classification": "NEUTRAL",
    "score": 0.0,
    "headline": "Preços futuros do milho trabalham com leves altas nesta 4ª feira em Chicago"
  }
]
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
