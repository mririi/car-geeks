from django.db import models

# Create your models here.

class Carenergy(models.Model):
  descE = models.CharField(max_length=200)

  def __str__(self):
    return self.descE