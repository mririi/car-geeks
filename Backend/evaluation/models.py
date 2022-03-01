from django.db import models

# Create your models here.

class Evaluation(models.Model):
  nbEval = models.IntegerField(default=0)
  userprofileEval = models.ForeignKey('userprofile.Userprofile',on_delete=models.CASCADE,null=True,blank=True)
  serviceEval = models.ForeignKey('service.Service',on_delete=models.CASCADE,null=True,blank=True)

  def __str__(self):
    return 'Evaluation de '+self.userprofileEval.__str__()+' sur le Service de type '+self.serviceEval.__str__()