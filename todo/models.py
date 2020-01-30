from django.db import models
import datetime


class Picture(models.Model):
    img = models.ImageField(upload_to='images/', null=False)

    def __str__(self):
        return self.image.url()


class Result(models.Model):
    url = models.CharField(max_length=1000)
    score = models.FloatField()


