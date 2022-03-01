from django.db import models

# Create your models here.

class Group(models.Model):
  titleG = models.CharField(max_length=200,blank=True,null=True)
  nbposts = models.IntegerField(default=0)
  nbmembers = models.IntegerField(default=0)
  dateinscrit = models.DateTimeField(auto_now_add=True)
  imageG = models.ImageField(upload_to='images/',null=True, blank=True)
  userprofileG =models.ForeignKey('userprofile.Userprofile',on_delete=models.CASCADE,blank=True,null=True)

  def __str__(self):
    return self.titleG