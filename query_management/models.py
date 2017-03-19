from datetime import datetime

from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

now = datetime.now()

query_choices = (
    ('result', 'Result Discrepency'),
    ('credit', 'Credit Discrepency'),
    ('pdc_issue', 'Issue of PDC'),
    ('other_certificate', 'Issue of some other certificate')
)

status_choices = (
    ('resolved', 'Resolved'),
    ('unresolved', 'Unresolved'),
    ('pending', 'Pending'),
    ('reschedule', 'Reschedule'),
    ('transfer', 'Transfered to other department')
)


# Query database table
class QueryToken(models.Model):
    student = models.IntegerField(blank=False)
    query_type = models.CharField(max_length=64, choices=query_choices,
                                  blank=False)
    email = models.CharField(max_length=48, db_index=True)
    phone = PhoneNumberField(db_index=True)
    department = models.CharField(max_length=8, blank=True)
    year = models.CharField(max_length=2, blank=True)
    date = models.DateField(default=now.date(), blank=False)
    time = models.TimeField(default=now.time(), blank=False)
    status = models.CharField(max_length=24, choices=status_choices,
                              default='unresolved')
    token_id = models.CharField(default='', blank=True, null=True,
                                max_length=24)
    description = models.CharField(default='', blank=True, max_length=240)

    def save(self, *args, **kwargs):
        if self.token_id == '':
            token_objects = QueryToken.objects.values_list(
                'token_id').order_by('-id')
            if token_objects.exists():
                token_object = token_objects[0]
                token = token_object[0]
                temp_token = int(token[2:]) + 1
                self.token_id = token[0:2] + str(temp_token)
            else:
                self.token_id = "SU1700001"
        super(QueryToken, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.token_id)

    def query_type_value(self):
        return self.get_query_type_display()

    class Meta:
        verbose_name_plural = 'Queries'
