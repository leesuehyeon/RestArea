from django.db import models

# Create your models here.
class Rest(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100, default='')
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)