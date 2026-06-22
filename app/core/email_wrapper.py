import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart 
from app.core.config import settings

logger = logging.GetLogger(__name__)

def send_email():
    """ Send an email (template) via Gmail SMTP """

def send_reset_email():
    reset_link = f"{settings.FRONTEND_URL}"

def send_welcome_email():
    """ Send a welcome email to any new staff registered with the company """
    subject_of_email = "willkommen bei MbPflege Restistry"
    html_body = f"""
    <p>Hallo {staff_fname}</p>
    <p>Ihr Konto wurde erfolgreich erstellt.</p>
    <p>Sie können sie sich jetzt unter <a href="{settings.FRONTEND_URL}">{settings.FRONTEND_URL}/a> 
    """
    text_body = f"Hallo {staff_fname}, Ihr Konto wurde erstellt. Login: {settings.FRONTEND_URL}"

    send_email(to_email, subject_of_email, html_body, text_body)