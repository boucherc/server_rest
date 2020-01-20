from django.db import models


class Todo(models.Model):
    name = models.TextField
    img = models.ImageField(upload_to='images/')
