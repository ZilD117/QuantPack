import requests
from bs4 import BeautifulSoup
import csv

# The website you want to scrap.
URL = "https://news.yahoo.com/science/"

def fetch_titles(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        titles = soup.find_all('h3', attrs={"data-test-locator": "stream-item-title"})
        title_texts = [title.get_text() for title in titles]
        return title_texts
    else:
        print("Failed to retrieve the webpage")
        return []

def save_to_csv(titles, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Title"])
        for title in titles:
            writer.writerow([title])


if __name__ == "__main__":
    scraped_titles = fetch_titles(URL)
    save_to_csv(scraped_titles, '/Users/yaoyunjing/Desktop/个人/QuantFinance/science_titles.csv')