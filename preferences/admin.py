from django.contrib import admin

# Register your models here.

from .models import Preferences

admin.site.register(Preferences)