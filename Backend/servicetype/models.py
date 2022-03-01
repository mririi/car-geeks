from django.db import models

# Create your models here.

class Servicetype(models.Model):
  descT = models.CharField(max_length=200)

  def __str__(self):
    return self.descT