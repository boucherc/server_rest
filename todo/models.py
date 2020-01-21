from django.db import models


class Picture(models.Model):
    img = models.ImageField(upload_to='images/', null=False)

    def __str__(self):
        return self.image.name
