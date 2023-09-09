import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.pokemon.com/us")
print(response.text)