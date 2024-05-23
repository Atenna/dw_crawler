import requests, json
from bs4 import BeautifulSoup

def crawl(url):
    '''
    The function crawls DW Top Thema and returns a list of links
    '''
    base_url = 'https://learngerman.dw.com'
    urls = []
    response = requests.get(url)
    if response:
        pass
    else:
        raise Exception(f"Non-success status code: {response.status_code}")

    soup = BeautifulSoup(response.content, "html.parser")
    elements = soup.select_one('.sc-cdDgOI').select('a')

    for e in elements:
        urls.append(base_url + e['href'])
    print(str(urls))
    return urls

def get_content(url):

    response = requests.get(url)
    if response:
        pass
    else:
        raise Exception(f"Non-success status code: {response.status_code}")

if __name__ == '__main__':
    crawl("https://learngerman.dw.com/de/top-thema/s-55861562")
