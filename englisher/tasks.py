"""
    Celery tasks. Some of them will be launched periodically from admin panel via django-celery-beat
"""

import time
from django.core.mail import send_mail
from englisher.models import Email
from my_site.settings import EMAIL_HOST_USER

from my_site.celery import app

from celery import shared_task

@shared_task
def send_email(subject, body):
    emails = Email.objects.all()
    for email in emails:
        send_mail(subject, body, EMAIL_HOST_USER, [email.email])
        time.sleep(max(0.4, 0.1))
        


