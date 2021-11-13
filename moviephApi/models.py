from django.db import models


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=250)
    url = models.CharField(max_length=250)
    image = models.CharField(max_length=400)


class Token(models.Model):
    token = models.CharField(max_length=400)