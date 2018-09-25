from django.db import models

# Create your models here.
class Adventure(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    date_start = models.DateField('date start')
    date_end = models.DateField('date end')
