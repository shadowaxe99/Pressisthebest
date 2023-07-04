```python
import os
from some_publishing_library import PublisherAPI

from config import PUBLISHING_PLATFORM_API_KEY, PUBLISHING_PLATFORM_API_SECRET

class ArticlePublisher:
    def __init__(self):
        self.publisher = PublisherAPI(PUBLISHING_PLATFORM_API_KEY, PUBLISHING_PLATFORM_API_SECRET)

    def publish_article(self, article, image):
        try:
            response = self.publisher.publish(article, image)
            if response.status_code == 200:
                print("Article published successfully.")
            else:
                print(f"Failed to publish article. Status code: {response.status_code}")
        except Exception as e:
            print(f"An error occurred while publishing the article: {str(e)}")

if __name__ == "__main__":
    publisher = ArticlePublisher()
    article = "path_to_your_article"
    image = "path_to_your_image"
    publisher.publish_article(article, image)
```