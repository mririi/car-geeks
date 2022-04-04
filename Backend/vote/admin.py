from django.contrib import admin

# Register your models here.

from .models import Vote

admin.site.register(Vote)