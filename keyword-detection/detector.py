```python
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from config import KEYWORDS

class KeywordDetector:
    def __init__(self):
        nltk.download('punkt')
        nltk.download('stopwords')
        self.stop_words = set(stopwords.words('english'))

    def detect_keywords(self, text):
        word_tokens = word_tokenize(text)
        filtered_text = [w for w in word_tokens if not w in self.stop_words]
        detected_keywords = [word for word in filtered_text if word in KEYWORDS]
        return detected_keywords

    def match_keywords(self, text):
        detected_keywords = self.detect_keywords(text)
        matched_keywords = [re.findall(r'\b{}\b'.format(keyword), text) for keyword in detected_keywords]
        return matched_keywords
```