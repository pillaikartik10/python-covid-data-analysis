import csv
import requests
from bs4 import BeautifulSoup

#scraping data from the website

html = requests.get('https://www.worldometers.info/coronavirus/').text
html_soup = BeautifulSoup(html, 'html.parser')
rows = html_soup.find_all('tr')


#function to extract text

def extract_text(row, tag):
    element = BeautifulSoup(row, 'html.parser').find_all(tag)
    text = [col.get_text() for col in element]
    return text

heading = rows.pop(0)

#extracting columns 1- 8

heading_row = extract_text(str(heading), 'th')[1:9]

#function to store the scraped data into a .csv file

def test():
    with open('corona.csv', 'w') as store:
        Store = csv.writer(store, delimiter=',')
        Store.writerow(heading_row)
        for row in rows:
            test_data = extract_text(str(row), 'td')[1:9]
            Store.writerow(test_data)

test()
