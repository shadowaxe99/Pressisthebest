```python
import requests
from bs4 import BeautifulSoup
import tweepy
import config

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def scrape_twitter(user):
    auth = tweepy.OAuthHandler(config.TWITTER_API_KEY, config.TWITTER_API_SECRET)
    auth.set_access_token(config.TWITTER_ACCESS_TOKEN, config.TWITTER_ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    
    tweets = api.user_timeline(screen_name=user, count=200, tweet_mode="extended")
    return tweets

def save_data(data, filename):
    with open(filename, 'w') as f:
        f.write(str(data))

def main():
    website_data = scrape_website(config.WEBSITE_URL)
    save_data(website_data, 'website_data.txt')
    
    twitter_data = scrape_twitter(config.TWITTER_USER)
    save_data(twitter_data, 'twitter_data.txt')

if __name__ == "__main__":
    main()
```