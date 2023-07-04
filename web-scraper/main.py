```python
import requests
from bs4 import BeautifulSoup
import tweepy
from scraper import Scraper
import config

def main():
    # Load configuration
    url = config.WEBSITE_URL
    twitter_credentials = config.TWITTER_CREDENTIALS

    # Initialize Twitter API
    auth = tweepy.OAuthHandler(twitter_credentials['consumer_key'], twitter_credentials['consumer_secret'])
    auth.set_access_token(twitter_credentials['access_token'], twitter_credentials['access_token_secret'])
    api = tweepy.API(auth)

    # Initialize scraper
    scraper = Scraper(api)

    # Scrape website
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    website_data = scraper.scrape_website(soup)

    # Scrape Twitter
    twitter_data = scraper.scrape_twitter()

    # Save data
    scraper.save_data(website_data, 'website_data.json')
    scraper.save_data(twitter_data, 'twitter_data.json')

if __name__ == "__main__":
    main()
```