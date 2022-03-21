from django.db import models

# Create your models here.

class Reclamation(models.Model):
  nameRec = models.CharField(max_length=200,blank=True,null=True)
  emailRec = models.CharField(max_length=200,blank=True,null=True)
  messageRec = models.TextField(unique=False,blank=True,null=True)
  telRec = models.IntegerField(default=0,blank=True,null=True)
  dateRec = models.DateTimeField(auto_now=True,blank=True,null=True)
  def __str__(self):
    return 'contact us with the name of '+self.nameRec.__str__()