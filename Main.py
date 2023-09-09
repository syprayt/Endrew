import requests
from bs4 import BeautifulSoup

response = requests.get("https://sinoptik.ua/")
if response.status_code == 200:
    bs = BeautifulSoup(response.text, features="html.parser")
    list = bs.find("p", {"class":"today-temp"})
    for elem in list:
        print(elem.text)