import requests
from bs4 import BeautifulSoup

def scrape_ebay(search_term):
    url = f"https://www.ebay.com/sch/i.html?_nkw={search_term}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    listings = []
    for item in soup.select('.s-item'):
        title = item.select_one('.s-item__title').text
        price = item.select_one('.s-item__price').text
        link = item.select_one('.s-item__link')['href']
        listings.append({"title": title, "price": price, "url": link})
    
    return listings