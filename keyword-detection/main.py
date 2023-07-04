```python
import os
import sys
sys.path.append(os.path.abspath(os.path.join('..')))

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re

from config import KEYWORDS_FILE

def load_keywords():
    with open(KEYWORDS_FILE, 'r') as file:
        keywords = file.read().splitlines()
    return keywords

def detect_keywords(text, keywords):
    words = word_tokenize(text)
    words = [word.lower() for word in words if word.isalpha()]
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    detected_keywords = set(words) & set(keywords)
    return detected_keywords

def main():
    keywords = load_keywords()
    text = input("Enter text to detect keywords: ")
    detected_keywords = detect_keywords(text, keywords)
    print("Detected keywords: ", detected_keywords)

if __name__ == "__main__":
    main()
```