from django.db import models

# Create your models here.

class Car(models.Model):
  colorC = models.CharField(max_length=200,null=True, blank=True)
  dateCreationC = models.DateTimeField(auto_now_add=True)
  imageC = models.ImageField(upload_to='images/',null=True, blank=True)
  userprofileC = models.ForeignKey('userprofile.Userprofile',on_delete=models.CASCADE,null=True, blank=True)
  def __str__(self):
    return self.userprofileC.__str__()+' s Car '