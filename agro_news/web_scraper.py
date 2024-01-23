import os

import requests
from bs4 import BeautifulSoup
from dotenv import find_dotenv
from dotenv import load_dotenv

load_dotenv(find_dotenv())

url = os.getenv("NEWS_URL")

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")


noticias = soup.find_all("li", class_="horizontal com-hora")


for noticia in noticias:
    # Extrai a data
    data = noticia.find("h3").text

    # Extrai a hora
    hora = noticia.find("span", class_="hora").text

    # Extrai o conteúdo
    texto = noticia.find("div").find("h2").text

    # Imprime as informações
    print(f"Data: {data}")
    print(f"Hora: {hora}")
    print(f"Conteúdo: {texto}")
