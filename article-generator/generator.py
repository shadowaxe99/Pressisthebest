```python
import openai
import language_tool_python
from config import OPENAI_API_KEY, GRAMMAR_CHECK_API_KEY

class ArticleGenerator:
    def __init__(self):
        self.tool = language_tool_python.LanguageTool('en-US')
        openai.api_key = OPENAI_API_KEY

    def generate_article(self, prompt):
        response = openai.Completion.create(
          engine="text-davinci-002",
          prompt=prompt,
          temperature=0.5,
          max_tokens=500
        )
        return response.choices[0].text.strip()

    def grammar_check(self, text):
        matches = self.tool.check(text)
        corrected_text = language_tool_python.correct(text, matches)
        return corrected_text

    def save_article(self, article, filename):
        with open(filename, 'w') as file:
            file.write(article)

if __name__ == "__main__":
    generator = ArticleGenerator()
    prompt = "Write an article about the importance of web scraping and data analysis."
    article = generator.generate_article(prompt)
    corrected_article = generator.grammar_check(article)
    generator.save_article(corrected_article, "generated_article.txt")
```