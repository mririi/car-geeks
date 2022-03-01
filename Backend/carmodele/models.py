from django.db import models

# Create your models here.

class Carmodele(models.Model):
  descMod = models.CharField(max_length=200)

  def __str__(self):
    return self.descMod