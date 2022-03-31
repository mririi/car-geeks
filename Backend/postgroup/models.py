from django.db import models

# Create your models here.

class PostGroup(models.Model):
  detailsP = models.CharField(max_length=200,blank=True,null=True)
  accepted = models.BooleanField(default=False)
  nblikes = models.IntegerField(default=0)
  nbcomments = models.IntegerField(default=0)
  datecreation = models.DateTimeField(auto_now_add=True)
  imagePost = models.ImageField(upload_to='images/',null=True, blank=True)
  userprofilePost =models.ForeignKey('userprofile.Userprofile',on_delete=models.CASCADE,blank=True,null=True)
  groupPost =models.ForeignKey('group.Group',on_delete=models.CASCADE,blank=True,null=True)
  def __str__(self):
    return self.detailsP