from django.db import models

# Create your models here.
class GroupMember(models.Model):
  userprofileMem =models.ForeignKey('userprofile.Userprofile',on_delete=models.CASCADE,blank=True,null=True)
  groupMem =models.ForeignKey('group.Group',on_delete=models.CASCADE,blank=True,null=True)

  def __str__(self):
    return self.groupMem