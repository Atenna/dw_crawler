import requests
from bs4 import BeautifulSoup

def crawl(url):
    """
    Crawls DW Top Thema and returns a list of links.

    """
    base_url = 'https://learngerman.dw.com'
    urls = []
    
    try:
        response = requests.get(url)
        response.raise_for_status() 
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return []

    soup = BeautifulSoup(response.content, "html.parser")
    elements = soup.select_one('.sc-cdDgOI').select('a')

    for e in elements:
        urls.append(base_url + e['href'])

    print(f"Extracted URLs: {urls}")
    return urls

def get_content(url):
    """
    Fetches the content of a given URL.

    """
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None

    return response.content

if __name__ == '__main__':
    urls = crawl("https://learngerman.dw.com/de/top-thema/s-55861562")
    for url in urls:
        content = get_content(url)
        if content:
            print(f"Fetched content from {url}")
        else:
            print(f"Failed to fetch content from {url}")
