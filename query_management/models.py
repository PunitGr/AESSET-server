from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# TImeSlot database table
class TimeSlot(models.Model):
    slot_id = models.CharField(max_length=24, primary_key=True)
    count = models.IntegerField()

    def __str__(self):
        return str(self.slot_id)


# Query database table
class QueryToken(models.Model):
    student = models.IntegerField(blank=False)
    query_type = models.CharField(max_length=240, default='Exam')
    email = models.CharField(max_length=48, db_index=True)
    phone = PhoneNumberField(db_index=True)
    date = models.DateField(blank=False)
    time = models.CharField(max_length=12, blank=False)
    status = models.BooleanField(default=False)
    token_id = models.CharField(default='', blank=True, null=True,
                                max_length=24)
    slot = models.ForeignKey(TimeSlot, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.token_id == '':
            token_objects = QueryToken.objects.values_list('token_id').order_by('-id')
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

    class Meta:
        verbose_name_plural = 'Queries'
