```python
import os
from publisher import ArticlePublisher

def main():
    # Load configuration
    with open('config.py') as f:
        config = eval(f.read())

    # Initialize publisher
    publisher = ArticlePublisher(config['publishing_platform_api_key'])

    # Get list of articles to publish
    articles_to_publish = os.listdir(config['articles_directory'])

    # Publish each article
    for article in articles_to_publish:
        with open(os.path.join(config['articles_directory'], article), 'r') as f:
            content = f.read()
        publisher.publish(content)

if __name__ == "__main__":
    main()
```