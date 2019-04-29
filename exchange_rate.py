import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

url = 'https://www.cbn.gov.ng/rates/ExchRateByCurrency.asp'

web_data = requests.get(url)

scrapped_data = web_data.content

soup = bs(scrapped_data, 'html.parser')

table = soup.find(id="ContentTextinner")

list_of_rows = []
for row in table.findAll('tr'):
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text
        text = text.replace('\n', ' ')
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

exchange_rate = pd.DataFrame(list_of_rows, columns=['Date', 'Currency', 'Buying (NGN)', 'Central (NGN)', 'Selling (NGN)'])

print(exchange_rate)
