from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Userprofile(models.Model):
  firstname = models.CharField(max_length=200,blank=True,null=True)
  lastname = models.CharField(max_length=200,blank=True,null=True)
  address = models.CharField(max_length=200,blank=True,null=True)
  country = models.CharField(max_length=200,blank=True,null=True)
  email = models.CharField(max_length=200,blank=True,null=True)
  age = models.IntegerField(default=0)
  tel = models.IntegerField(default=0)
  bio = models.TextField(default="",blank=True,null=True)
  nbquestions = models.IntegerField(default=0)
  nbreplies = models.IntegerField(default=0)
  nblikes = models.IntegerField(default=0)
  nbvisits = models.IntegerField(default=0)
  dateinscrit = models.DateTimeField(auto_now_add=True)
  imageU = models.ImageField(upload_to='images/',null=True, blank=True)
  roleU = models.ForeignKey('role.Role',on_delete=models.CASCADE,blank=True,null=True)
  badgeU = models.ForeignKey('badge.Badge',on_delete=models.CASCADE,blank=True,null=True)
  preferencesU = models.ForeignKey('preferences.Preferences',on_delete=models.CASCADE,blank=True,null=True)
  userU =models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)

  