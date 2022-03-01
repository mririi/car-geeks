from django.db import models

# Create your models here.

class Questioncategory(models.Model):
  typeC = models.CharField(max_length=200)

  def __str__(self):
    return self.typeC