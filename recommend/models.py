from django.db import models

# Create your models here.
class Cosmetics(models.Model):
    label = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    ingridients = models.TextField()
    price = models.FloatField()
    rank = models.FloatField()
