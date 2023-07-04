import unittest
from web_scraper.scraper import Scraper
from keyword_detection.detector import Detector
from article_generator.generator import ArticleGenerator
from image_generator.generator import ImageGenerator
from email_sender.sender import EmailSender
from article_publisher.publisher import Publisher

class TestWebScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = Scraper()

    def test_scrape(self):
        self.assertIsNotNone(self.scraper.scrape())

class TestKeywordDetection(unittest.TestCase):
    def setUp(self):
        self.detector = Detector()

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
        self.assertTrue(self.sender.send())

class TestArticlePublisher(unittest.TestCase):
    def setUp(self):
        self.publisher = Publisher()

    def test_publish(self):
        self.assertTrue(self.publisher.publish())

if __name__ == '__main__':
    unittest.main()