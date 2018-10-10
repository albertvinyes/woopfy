from django.db import models
from adventures.models import Adventure

# Create your models here.
class Activity(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    start = models.DateTimeField('date and time start')
    adventure = models.ForeignKey(Adventure, on_delete=models.CASCADE)
