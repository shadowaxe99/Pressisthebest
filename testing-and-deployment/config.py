# Configuration file for testing and deployment

# Directories
WEB_SCRAPER_DIR = "../web-scraper"
KEYWORD_DETECTION_DIR = "../keyword-detection"
ARTICLE_GENERATOR_DIR = "../article-generator"
IMAGE_GENERATOR_DIR = "../image-generator"
EMAIL_SENDER_DIR = "../email-sender"
ARTICLE_PUBLISHER_DIR = "../article-publisher"

# Test data
TEST_WEBSITES = ["https://example.com", "https://test.com"]
TEST_TWITTER_ACCOUNTS = ["@example", "@test"]
TEST_KEYWORDS = ["test", "example"]
TEST_RECIPIENTS = ["test@example.com", "example@test.com"]

# Test settings
RUN_UNIT_TESTS = True
RUN_INTEGRATION_TESTS = True
RUN_SYSTEM_TESTS = True

# Deployment settings
DEPLOYMENT_PLATFORM = "Heroku"
DEPLOYMENT_SETTINGS = {
    "app_name": "web-scraper-article-generator",
    "buildpacks": ["heroku/python"],
    "config_vars": {
        "WEB_CONCURRENCY": "4",
        "LOG_TO_STDOUT": "1"
    }
}