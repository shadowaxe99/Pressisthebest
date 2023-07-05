import unittest
import pytest

# Importing modules to be tested
from web_scraper.main import WebScraper
from keyword_detection.main import KeywordDetector
from article_generator.main import ArticleGenerator
from image_generator.main import ImageGenerator
from email_sender.main import EmailSender
from article_publisher.main import ArticlePublisher

class TestWebScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = WebScraper()

    def test_scrape(self):
        self.assertIsNotNone(self.scraper.scrape())

class TestKeywordDetector(unittest.TestCase):
    def setUp(self):
        self.detector = KeywordDetector()

    def test_detect(self):
        self.assertIsNotNone(self.detector.detect())

class TestArticleGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = ArticleGenerator()

    def test_generate(self):
        self.assertIsNotNone(self.generator.generate())

class TestImageGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = ImageGenerator()

    def test_generate(self):
        self.assertIsNotNone(self.generator.generate())

class TestEmailSender(unittest.TestCase):
    def setUp(self):
        self.sender = EmailSender()

    def test_send(self):
        self.assertIsNotNone(self.sender.send())

class TestArticlePublisher(unittest.TestCase):
    def setUp(self):
        self.publisher = ArticlePublisher()

    def test_publish(self):
        self.assertIsNotNone(self.publisher.publish())

if __name__ == '__main__':
    unittest.main()