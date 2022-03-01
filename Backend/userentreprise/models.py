from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Userentreprise(models.Model):
  nameE = models.CharField(max_length=200,blank=True,null=True)
  typeE = models.CharField(max_length=200,blank=True,null=True)
  adresseE = models.CharField(max_length=200,blank=True,null=True)
  emailE = models.CharField(max_length=200,blank=True,null=True)
  contactE = models.IntegerField(default=0)
  dateinscritE = models.DateTimeField(auto_now_add=True)
  imageE = models.ImageField(upload_to='images/',null=True, blank=True)
  roleE = models.ForeignKey('role.Role',on_delete=models.CASCADE,blank=True,null=True)
  userE =models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)

  def __str__(self):
    return self.nomE