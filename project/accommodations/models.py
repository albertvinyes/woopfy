from django.db import models
from adventures.models import Adventure

class Accommodation(models.Model):
    name = models.CharField(max_length=32)
    location = models.CharField(max_length=256)
    date_start = models.DateField('date check-in')
    date_end = models.DateField('date check-out')
    adventure = models.ForeignKey(Adventure, on_delete=models.CASCADE)
