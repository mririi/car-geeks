from django.db import models

# Create your models here.

class Servicepromotion(models.Model):
  Running = models.BooleanField(default=False)
  dateP = models.DateTimeField(auto_now_add=True)
  serviceP = models.ForeignKey('service.Service',on_delete=models.CASCADE,null=True,blank=True)
  nbDays=models.DecimalField(max_digits=20,decimal_places=0,null=True,blank=True)
  def __str__(self):
    return self.serviceP.__str__()