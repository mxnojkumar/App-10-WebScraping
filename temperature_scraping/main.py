import requests
import selectorlib
import time
from datetime import datetime
import sqlite3

URL = "https://programmer100.pythonanywhere.com/"

connection = sqlite3.connect("temperature_scraping/temp_data.db")


def scraper(url):
    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("temperature_scraping/extract.yaml")
    value = extractor.extract(source)['temperature']
    return value


def store(extracted):
    row = extracted.split(",")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO temperature VALUES(?, ?)", row)
    connection.commit()
    
    
if __name__ == "__main__":
    while True:
        scraped = scraper(URL)
        extracted = extract(scraped)
        current = datetime.now()
        now = current.strftime("%d-%m-%Y %H:%M:%S")
        temp_now = f"{now},{extracted}"
        store(temp_now)
        print(temp_now)
        time.sleep(2)