from django.db import models

# Create your models here.
class GroupMember(models.Model):
  accepted = models.BooleanField(default=False)
  userprofileMem =models.ForeignKey('userprofile.Userprofile',on_delete=models.CASCADE,blank=True,null=True)
  userentrepriseMem =models.ForeignKey('userentreprise.Userentreprise',on_delete=models.CASCADE,blank=True,null=True)
  groupMem =models.ForeignKey('group.Group',on_delete=models.CASCADE,blank=True,null=True)

  def __str__(self):
    return self.groupMem.__str__()