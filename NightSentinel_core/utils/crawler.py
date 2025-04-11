import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class WebCrawler:
    def __init__(self, base_url, max_depth=2):
        self.base_url = base_url
        self.max_depth = max_depth
        self.visited = set()

    def crawl(self, url=None, depth=0):
        if depth > self.max_depth or url in self.visited:
            return

        self.visited.add(url)
        print(f"Crawling: {url}")

        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            for link in soup.find_all('a', href=True):
                full_url = urljoin(url, link['href'])
                if self.base_url in full_url:
                    self.crawl(full_url, depth + 1)
        except requests.RequestException as e:
            print(f"Error crawling {url}: {e}")

    def get_visited_urls(self):
        return self.visited