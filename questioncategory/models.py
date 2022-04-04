from django.db import models

# Create your models here.

class Questioncategory(models.Model):
  typeC = models.CharField(max_length=200)
  imageCat = models.ImageField(upload_to='images/',null=True, blank=True)
  def __str__(self):
    return self.typeC