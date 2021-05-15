import requests
from bs4 import BeautifulSoup
import pandas as pd

searchterm = 'mcdavid+young+guns'

url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw={searchterm}&_sacat=0&LH_Sold=1&LH_Complete=1&rt=nc&LH_PrefLoc=2'

def get_data(searchterm):
    url = f'https://www.ebay.com/sch/i.html?_from=R40&_nkw={searchterm}&_sacat=0&LH_Sold=1&LH_Complete=1&rt=nc&LH_PrefLoc=2'
    r = requests.get('http://localhost:8050/render.html', params = {'url': url, 'wait' : 2})
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


def parse(soup):
    #cardlist = []
    results = soup.find_all('div', {'class': 's-item__info clearfix'})
    print(len(results))
    for card in results:
            cards = {
                'title': card.find('h3', {'class': 's-item__title s-item__title--has-tags'}).text,
                'soldprice': float(card.find('span', {'class': 's-item__price'}).text.replace('$','').replace(',','').strip()),
                'solddate': card.find('span', {'class': 's-item__title--tagblock__COMPLETED'}).find('span', {'class':'POSITIVE'}).text,
                'bids': card.find('span', {'class': 's-item__bids'}).text,
                'link': card.find('a', {'class': 's-item__link'})['href'],
            }
            print(len(cards))
    return

soup = get_data(url)
parse(soup)
'''
def parse(soup):
    productslist = []
    results = soup.find_all('div', {'class': 's-item__info clearfix'})
    for item in results:
        product = {
            'title': item.find('h3', {'class': 's-item__title s-item__title--has-tags'}).text,
            'soldprice': float(item.find('span', {'class': 's-item__price'}).text.replace('£','').replace(',','').strip()),
            'solddate': item.find('span', {'class': 's-item__title--tagblock__COMPLETED'}).find('span', {'class':'POSITIVE'}).text,
            'bids': item.find('span', {'class': 's-item__bids'}).text,
            'link': item.find('a', {'class': 's-item__link'})['href'],
        }
        productslist.append(product)
    return productslist

def output(productslist, searchterm):
    productsdf =  pd.DataFrame(productslist)
    productsdf.to_csv(searchterm + 'output.csv', index=False)
    print('Saved to CSV')
    return

soup = get_data(searchterm)
productslist = parse(soup)
output(productslist, searchterm)
'''