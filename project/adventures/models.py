import datetime
from django.db import models

# Create your models here.
class Adventure(models.Model):
    # TODO: remove optional flags
    today = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256, default="Description")
    location = models.CharField(max_length=256)
    date_start = models.DateField('date start', blank=True, default="2018-12-24")
    date_end = models.DateField('date end', blank=True, default="2018-12-24")
    closed = models.BooleanField(default=False)
