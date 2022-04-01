from django.db import models
# Create your models here.

class Email(models.Model):
  subject = models.TextField(null=True,blank=True)
  message = models.TextField(null=True,blank=True)
  to = models.CharField(max_length=200,null=True,blank=True)
