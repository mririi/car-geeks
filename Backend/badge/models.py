from django.db import models

# Create your models here.

class Badge(models.Model):
  typeB = models.CharField(max_length=200)

  def __str__(self):
    return self.typeB