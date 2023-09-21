from django.db import models

# Create your models here.
class Library(models.Model):
    name = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
