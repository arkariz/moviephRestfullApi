from django.db import models


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=250)
    year = models.CharField(max_length=5)
    url = models.CharField(max_length=250)
    image = models.CharField(max_length=400, null=True)
    star = models.CharField(max_length=10, null=True)
    duration = models.CharField(max_length=10, null=True)
    genre = models.CharField(max_length=25, null=True)
    imdb = models.CharField(max_length=25, null=True)
    video_url = models.CharField(max_length=400, null=True)

    def __str__(self):
        return self.title


class Token(models.Model):
    token = models.CharField(max_length=400)

    def __str__(self):
        return self.token