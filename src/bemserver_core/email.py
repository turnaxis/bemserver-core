"""Email"""

import smtplib
from email.message import EmailMessage

from bemserver_core.celery import celery, logger
from dotenv import load_dotenv
import os

load_dotenv()

class EmailSender:
    """Basic mail sender class

    This implementation does not provide SMTP authentication. It assumes an open
    relay is available, typically localhost.
    """

    def __init__(self):
        self._enabled = False
        self._sender_addr = None
        self._host = None

    def init_core(self, bsc):
        """Initialize with settings from BEMServerCore configuration"""
        self._enabled = bsc.config["SMTP_ENABLED"]
        self._sender_addr = bsc.config["SMTP_FROM_ADDR"]
        self._host = bsc.config["SMTP_HOST"]

    def send(self, dest_addrs, subject, content):
        """Create and send message"""
        if self._enabled:
            msg = EmailMessage()
            msg["Subject"] = subject
            msg["From"] = self._sender_addr
            msg["To"] = ", ".join(dest_addrs)
            msg.set_content(content)
            with smtplib.SMTP(self._host, timeout=3) as smtp:
                smtp.send_message(msg)


ems = EmailSender()


@celery.task(name="Email")
def send_email(dest_addrs, subject, content):
    """Send message in a task"""
    logger.info("Send email to %", dest_addrs)
    ems.send(dest_addrs, subject, content)

@celery.task(name="send_email")
def smtp_send_email(recipient, subject, content):
    """Send the 2FA token to the user's email using smtplib."""
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = os.getenv("MAIL_SENDER")
    msg["To"] = recipient
    msg.set_content(content)

    try:
        with smtplib.SMTP(os.getenv("MAIL_SERVER"), os.getenv("MAIL_PORT")) as server:
            server.starttls()  # Secure the connection
            server.login(os.getenv("MAIL_USERNAME"), os.getenv("MAIL_PASSWORD"))
            server.send_message(msg)
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")