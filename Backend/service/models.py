from django.db import models

# Create your models here.

class Service(models.Model):
  titleS = models.CharField(max_length=200,null=True,blank=True)
  priceS = models.DecimalField(max_digits=20,decimal_places=2,null=True,blank=True)
  contactS = models.CharField(max_length=200,null=True,blank=True)
  addressS = models.CharField(max_length=200,null=True,blank=True)
  dateS = models.DateTimeField(auto_now=True)
  imageS = models.ImageField(upload_to='images/',null=True, blank=True)
  userprofileS = models.ForeignKey('userprofile.Userprofile',on_delete=models.CASCADE,null=True,blank=True)
  evaluationS = models.ForeignKey('evaluation.Evaluation',on_delete=models.CASCADE,null=True,blank=True)
  typeS = models.ForeignKey('servicetype.Servicetype',on_delete=models.CASCADE,null=True,blank=True)
  def __str__(self):
    return self.titleS