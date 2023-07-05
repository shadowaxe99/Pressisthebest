```python
import os
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from config import ARTICLE_PATH, IMAGE_PATH

def generate_wordcloud(article_file):
    with open(os.path.join(ARTICLE_PATH, article_file), 'r') as file:
        text = file.read()
    wordcloud = WordCloud(width = 1000, height = 500).generate(text)
    return wordcloud

def save_image(wordcloud, image_file):
    plt.figure(figsize=(15,8))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.savefig(os.path.join(IMAGE_PATH, image_file), bbox_inches='tight')
    plt.close()

def generate_images():
    for article_file in os.listdir(ARTICLE_PATH):
        wordcloud = generate_wordcloud(article_file)
        image_file = os.path.splitext(article_file)[0] + '.png'
        save_image(wordcloud, image_file)
```
This code assumes that the image generation is done by creating word clouds from the text of the articles. The `ARTICLE_PATH` and `IMAGE_PATH` are assumed to be defined in the `config.py` file. The `PIL`, `wordcloud`, and `matplotlib` libraries are used for image generation and saving. The `os` library is used for file and directory handling.