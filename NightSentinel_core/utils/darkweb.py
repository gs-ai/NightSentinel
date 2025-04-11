import requests
from stem import Signal
from stem.control import Controller

def initialize_tor_session():
    """Initializes a Tor session for accessing .onion sites."""
    session = requests.Session()
    session.proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }
    return session

def renew_tor_ip():
    """Renews the Tor IP address by sending a signal to the Tor controller."""
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password='your_password')  # Replace with your Tor control password
        controller.signal(Signal.NEWNYM)

def crawl_onion_site(url, session):
    """Crawls a .onion site using the Tor session."""
    try:
        response = session.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error accessing {url}: {e}")
        return None