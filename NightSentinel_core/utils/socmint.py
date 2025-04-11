import requests
from bs4 import BeautifulSoup

def scrape_twitter_profile(username):
    """Scrapes public information from a Twitter profile."""
    url = f"https://twitter.com/{username}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        tweets = [tweet.text for tweet in soup.find_all('div', {'data-testid': 'tweetText'})]
        return {
            'username': username,
            'tweets': tweets
        }
    except requests.RequestException as e:
        print(f"Error scraping Twitter profile: {e}")
        return None

def scrape_linkedin_profile(profile_url):
    """Scrapes public information from a LinkedIn profile."""
    try:
        response = requests.get(profile_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        name = soup.find('h1', {'class': 'text-heading-xlarge'}).text.strip()
        headline = soup.find('div', {'class': 'text-body-medium'}).text.strip()
        return {
            'name': name,
            'headline': headline
        }
    except requests.RequestException as e:
        print(f"Error scraping LinkedIn profile: {e}")
        return None