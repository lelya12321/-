import requests
from bs4 import BeautifulSoup

URL = 'https://auto.ru/rostov-na-donu/cars/geely/all/'
HEADERS = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 YaBrowser/21.8.0.1379 Yowser/2.5 Safari/537.36'}

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('a', class_='Button Button_color_whiteHoverBlue Button_size_s Button_type_link Button_width_default ListingPagination-module__page')
    if pagination:
        return int(pagination[-1].get_text())
    else:
        return 22
    # print(pagination)

def get_contetn(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_="ListingItem__main")

    cars = []
    for item in items:
        cars.append({
                'title': item.find(class_='Link ListingItemTitle__link').get_text(),
                'link': item.find('a', class_='Link ListingItemTitle__link').get('href'),
                # 'price': item.find('a', class_='Link ListingItemPrice-module__link').get_text(),
            })
    print(cars)



def parse():
    html = get_html(URL)
    if html.status_code==200:
        cars = []
        pages_count = get_pages_count(html.text)
        print(pages_count)
        for page in range(2, pages_count+1):
            print(f'парсинг страницы {page} из {pages_count}')
            html = get_html(URL, params={'page':page})

            get_contetn(html.text)
        print(cars)
    else:
        print('error')

parse()
