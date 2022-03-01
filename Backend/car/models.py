from django.db import models

# Create your models here.

class Car(models.Model):
  modeleC = models.ForeignKey('carmodele.Carmodele',on_delete=models.CASCADE,null=True,blank=True)
  engineC = models.ForeignKey('carengine.Carengine',on_delete=models.CASCADE,null=True,blank=True)
  colorC = models.CharField(max_length=200,null=True, blank=True)
  dateCreationC = models.DateTimeField(auto_now_add=True)
  imageC = models.ImageField(upload_to='images/',null=True, blank=True)
  userprofileC = models.ForeignKey('userprofile.Userprofile',on_delete=models.CASCADE,null=True, blank=True)
  brandC = models.ForeignKey('brand.Brand',on_delete=models.CASCADE,null=True, blank=True)
  energyC = models.ForeignKey('carenergy.Carenergy',on_delete=models.CASCADE,null=True, blank=True)
  typeC = models.ForeignKey('cartype.Cartype',on_delete=models.CASCADE,null=True, blank=True)
  def __str__(self):
    return self.userprofileC.__str__()+' s Car '