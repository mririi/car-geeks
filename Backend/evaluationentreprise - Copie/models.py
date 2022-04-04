from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Evaluationentreprise(models.Model):
  nbEval = models.IntegerField(default=0)
  commentEval = models.CharField(max_length=200,blank=True,null=True)
  userentrepriseEval = models.ForeignKey('userentreprise.Userentreprise',on_delete=models.CASCADE,null=True,blank=True)
  userEval = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
  def __str__(self):
    return 'Evaluation de '+self.userEval.__str__()+' sur '+self.userentrepriseEval.__str__()
    