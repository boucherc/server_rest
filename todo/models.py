from django.db import models

class Todo(models.Model):
    description = models.CharField(max_length=100, blank=True, default='')
    deadline = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)
    priority = models.CharField(choices=[('low', 'low'),('normal', 'normal'),('high', 'high')], default='normal', max_length=100)
    tags = models.TextField(blank=True)

    class Meta:
        ordering = ('deadline',)

class Picture(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    img = models.TextField

    class Meta:
        ordering = ('name',)
