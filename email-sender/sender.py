import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

from config import SMTP_SERVER, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD, EMAIL_FROM, EMAIL_TO

def send_email(subject, body, attachment_path):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_FROM
    msg['To'] = ', '.join(EMAIL_TO)
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    if attachment_path is not None:
        attachment_name = os.path.basename(attachment_path)
        attachment = open(attachment_path, "rb")

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)

        part.add_header('Content-Disposition', "attachment; filename= %s" % attachment_name)

        msg.attach(part)

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(SMTP_USERNAME, SMTP_PASSWORD)
    text = msg.as_string()
    server.sendmail(EMAIL_FROM, EMAIL_TO, text)
    server.quit()