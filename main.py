import os
import ssl
import smtplib
from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv()

email_emisor = os.getenv('EMAIL_EMISOR')
email_password = os.getenv('EMAIL_PASSWORD')
email_reseptor = os.getenv('EMAIL_RESEPTOR')

asunto = 'Email Test'
cuerpo = """This is an example of email with python"""

email_message = EmailMessage()
email_message['From'] = email_emisor
email_message['To'] = email_reseptor
email_message['Subject'] = asunto
email_message.set_content(cuerpo)

contexto = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as smtp:
    smtp.login(email_emisor, email_password)
    smtp.sendmail(email_emisor, email_reseptor, email_message.as_string())