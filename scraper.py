# scraper.py

import requests
from bs4 import BeautifulSoup
import pandas as pd

import config
import json

async def scrape_trendyol():
    url = config.Config.TRENDYOL_URL

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    price_elements = soup.find_all('div', class_='prc-box-dscntd')
    name_elements = soup.find_all('div', class_='prdct-desc-cntnr')

    data = []
    if len(price_elements) == len(name_elements):
        for price_element, name_element in zip(price_elements, name_elements):
            price = price_element.text.strip()
            spans = name_element.find_all('span')
            if len(spans) >= 2:
                brand = spans[0].text.strip()
                product_name = spans[1].text.strip()
                data.append({'Product': product_name, 'Brand': brand, 'Price': price})

    df = pd.DataFrame(data)
    return df


async def scrape_kosmos_max_date():
    url = config.Config.KOSMOS_MAX_DATE
    df_kosmos = pd.DataFrame(columns=['ID', 'Name', 'Code', 'Foreign Code', 'Description', 'Foreign Name', 'Data Type'])

    response = requests.get(url)
    data = []
    print("response status code geliyor")
    print(response.status_code)
    print("response status code gidiyor")
    if response.status_code == 200:
        json_data = response.json()
        for item in json_data:
            
            id = item.get('id')
            name = item.get('name')
            code = item.get('code')
            foreign_code = item.get('foreignCode')
            description = item.get('description')
            foreign_name = item.get('foreignName')
            data_type = item.get('dataType')

            data.append({'ID': id, 'Name': name, 'Code': code, 'Foreign Code': foreign_code, 
                                          'Description': description, 'Foreign Name': foreign_name, 'Data Type': data_type})
           # df_kosmos = df_kosmos.append({'ID': id, 'Name': name, 'Code': code, 'Foreign Code': foreign_code, 
           #                               'Description': description, 'Foreign Name': foreign_name, 'Data Type': data_type}, 
           #                                ignore_index=True)
        df_kosmos = pd.concat([df_kosmos, pd.DataFrame(data)], ignore_index=True)
        return df_kosmos