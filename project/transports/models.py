from django.db import models
from adventures.models import Adventure

# Create your models here.
class Transport(models.Model):
    TRANSPORT_OPTIONS = (
            ('1', 'Car'),
            ('2', 'Train'),
            ('3', 'Ship'),
            ('4', 'Flight'),
        )

    name = models.CharField(max_length=32)
    information = models.CharField(max_length=64)
    transport_type = models.CharField(max_length=32, choices=TRANSPORT_OPTIONS)
    is_departure = models.BooleanField()
    is_arrival = models.BooleanField()
    departure_date = models.DateTimeField('departure date and time');
    departure_location = models.CharField(max_length=256)
    adventure = models.ForeignKey(Adventure, on_delete=models.CASCADE)
