```python
import os
from generator import ArticleGenerator
from config import Config

def main():
    # Load configuration
    config = Config()

    # Initialize article generator
    generator = ArticleGenerator(config)

    # Load scraped data
    with open(os.path.join(config.data_dir, 'scraped_data.json'), 'r') as f:
        data = json.load(f)

    # Generate articles
    articles = generator.generate_articles(data)

    # Save generated articles
    with open(os.path.join(config.data_dir, 'generated_articles.json'), 'w') as f:
        json.dump(articles, f)

if __name__ == "__main__":
    main()
```