from django.contrib import admin

# posts/admin.py
from django.contrib import admin

from .models import Todo

admin.site.register(Todo)