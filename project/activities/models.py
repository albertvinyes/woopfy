from django.db import models
from adventures.models import Adventure

# Create your models here.
class Activity(models.Model):
    name = models.CharField(max_length=32)
    adventure = models.ForeignKey(Adventure, on_delete=models.CASCADE)
