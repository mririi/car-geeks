from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Evaluation(models.Model):
  nbEval = models.IntegerField(default=0)
  commentEval = models.CharField(max_length=200,blank=True,null=True)
  userEval = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
  serviceEval = models.ForeignKey('service.Service',on_delete=models.CASCADE,null=True,blank=True)
  def __str__(self):
    return 'le Service de type '+self.serviceEval.__str__()
    