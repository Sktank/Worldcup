from django.db import models

# Create your models here.

class Team(models.Model):
    country = models.CharField(max_length=200)
    rank = models.IntegerField()
    description = models.TextField()
    manager = models.CharField(max_length=100)
    group = models.CharField(default='A', max_length=10)
    population = models.IntegerField(default=30000000)
    image_url = models.CharField(max_length=50, default='none')

class Stadium(models.Model):
    name = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    seats = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    image_url = models.CharField(max_length=50)
