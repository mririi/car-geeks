from django.db import models

# Create your models here.

class Entreprisepromotion(models.Model):
  Running = models.BooleanField(default=False)
  datePE = models.DateField(null=True)
  entreprisePE = models.ForeignKey('userentreprise.Userentreprise',on_delete=models.CASCADE,null=True,blank=True)
  nbDays=models.DecimalField(max_digits=20,decimal_places=0,null=True,blank=True)
  def __str__(self):
    return self.entreprisePE.__str__()