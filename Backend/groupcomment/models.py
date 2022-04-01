from django.db import models

# Create your models here.

class GroupComment(models.Model):
  contentCom = models.CharField(max_length=200,blank=True,null=True)
  dateinscrit = models.DateTimeField(auto_now_add=True)
  userprofileCom =models.ForeignKey('userprofile.Userprofile',on_delete=models.CASCADE,blank=True,null=True)
  postCom =models.ForeignKey('postgroup.PostGroup',on_delete=models.CASCADE,blank=True,null=True)
  def __str__(self):
    return self.contentCom
