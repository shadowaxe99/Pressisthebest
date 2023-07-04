```python
import os
from generator import ImageGenerator
from config import IMAGE_API_KEY, IMAGE_API_SECRET

def main():
    # Initialize the image generator with API keys from config
    image_generator = ImageGenerator(IMAGE_API_KEY, IMAGE_API_SECRET)

    # Path to the directory containing the articles
    articles_dir = os.path.join(os.getcwd(), 'articles')

    # Iterate over all articles
    for article_file in os.listdir(articles_dir):
        with open(os.path.join(articles_dir, article_file), 'r') as file:
            article = file.read()

        # Generate an image for the article
        image = image_generator.generate_image(article)

        # Save the image
        image_file = os.path.join(os.getcwd(), 'images', f'{os.path.splitext(article_file)[0]}.png')
        image.save(image_file)

if __name__ == "__main__":
    main()
```