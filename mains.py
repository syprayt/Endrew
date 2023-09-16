import requests
from bs4 import BeautifulSoup
import sqlite3
response = requests.get("https://www.bbc.com/ukrainian/features-66330880")
if response.status_code == 200:
    bs = BeautifulSoup(response.text, features="html.parser")
    list = bs.find_all("h2", {"class": "bbc-1aaitma eglt09e0"})
    list2 = bs.find_all("p", {"class": "bbc-1y32vyc e17g058b0"})
    connection = sqlite3.connect("Database.sl3")
    cur = connection.cursor()
    cur.execute("DROP TABLE first_table")
    cur.execute("CREATE TABLE IF NOT EXISTS first_table (place TEXT, name TEXT, description TEXT)")
    for i in range(10):
        cur.execute("INSERT INTO first_table (place, name, description) VALUES (?, ?, ?)", (i + 1, list[i].text, list2[i].text))
    connection.commit()
    connection.close()

