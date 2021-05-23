from django.db import models

# Create your models here.

class About(models.Model):
    role = models.CharField(max_length=100)
    descriptions = models.TextField()
    tech = models.CharField(max_length=100)
