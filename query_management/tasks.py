from django.core.mail import send_mail

from celery.registry import tasks
from celery.task import Task


queryDict = {
    "result": "Result Discrepency",
    "other_certificate": "Other certificate issue",
    "pdc_issue": "Issue of PDC",
    "credit": "Credit Discrepancy"
}


class RequestQueryTask(Task):
    # To test please run the smtp server
    # python -m smtpd -n -c DebuggingServer localhost:1025

    def run(self, query):
        message = ("Hello " + str(query.student) + "," +"\nYour request for " + queryDict[str(query.query_type)] + " has been accepted dated " + str(query.date) + " with current status as " + query.status + ".\nYour Query token is " + query.token_id + ".")
        send_mail("Sharda Univeristy Examination Cell", message, "examinationcell@sharda.ac.in", [query.email])


tasks.register(RequestQueryTask)
