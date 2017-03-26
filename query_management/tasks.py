from django.core.mail import send_mail

from celery.registry import tasks
from celery.task import Task


class RequestQueryTask(Task):
    # To test please run the smtp server
    # python -m smtpd -n -c DebuggingServer localhost:1025

    def run(self, query):
        message = ("Hello there")
        send_mail("hello", message, "hey@sharda.ac.in", [query.email])


tasks.register(RequestQueryTask)
