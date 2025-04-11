import mechanize
import socket
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class BrowserMixin(object):

    def get_browser(self):
        '''Returns a mechanize.Browser object configured with the framework's global options.'''
        br = mechanize.Browser()
        # set the user-agent header
        br.addheaders = [('User-agent', self._global_options['user-agent'])]
        # set debug options
        if self._global_options['verbosity'] >= 2:
            br.set_debug_http(True)
            br.set_debug_redirects(True)
            br.set_debug_responses(True)
        # set proxy
        if self._global_options['proxy']:
            br.set_proxies({'http': self._global_options['proxy'], 'https': self._global_options['proxy']})
        # additional settings
        br.set_handle_robots(False)
        # set timeout
        socket.setdefaulttimeout(self._global_options['timeout'])
        return br

class BrowserAutomationMixin:
    def __init__(self):
        self.driver = None

    def setup_browser(self):
        """Sets up a stealthy browser instance."""
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--disable-infobars')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')

        self.driver = webdriver.Chrome(options=chrome_options)

    def visit_url(self, url):
        """Visits a URL using the browser."""
        if not self.driver:
            self.setup_browser()
        self.driver.get(url)
        time.sleep(2)  # Randomized delay for stealth

    def extract_page_content(self):
        """Extracts the page content of the current browser window."""
        if self.driver:
            return self.driver.page_source
        return None

    def close_browser(self):
        """Closes the browser instance."""
        if self.driver:
            self.driver.quit()
            self.driver = None
