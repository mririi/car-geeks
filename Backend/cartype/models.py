from django.db import models

# Create your models here.

class Cartype(models.Model):
  descTC = models.CharField(max_length=200)

  def __str__(self):
    return self.descTC