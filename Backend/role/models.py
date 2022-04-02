from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Role(models.Model):
  entreprise=models.BooleanField(default=False)
  service=models.BooleanField(default=False)
  admin=models.BooleanField(default=False)
  staff=models.BooleanField(default=False)
  groupadmin=models.BooleanField(default=False)
  userRole =models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
  def __str__(self):
    return self.userRole.__str__()