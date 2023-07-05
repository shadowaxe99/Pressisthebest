```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from config import EMAIL_ADDRESS, EMAIL_PASSWORD, RECIPIENT_ADDRESS

from sender import send_email

def main():
    # Get the list of articles to send
    articles = os.listdir('articles')

    for article in articles:
        # Create a multipart message
        msg = MIMEMultipart()

        # Setup the parameters of the message
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = RECIPIENT_ADDRESS
        msg['Subject'] = "New Article: " + article

        # Attach the body with the msg instance
        msg.attach(MIMEText(article, 'plain'))

        # Open the file in bynary
        binary = open('articles/' + article, 'rb')

        payload = MIMEBase('application', 'octate-stream', Name=article)

        # To change the payload into encoded form
        payload = encoders.encode_base64(payload)

        # Add header with pdf name
        payload.add_header('Content-Decomposition', 'attachment', filename=article)
        msg.attach(payload)

        # Use the SMTP library to send the email
        send_email(msg)

if __name__ == "__main__":
    main()
```