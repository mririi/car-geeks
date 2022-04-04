from django.db import models

# Create your models here.

class GroupVote(models.Model):
  dateCreationVo = models.DateTimeField(auto_now_add=True)
  postVo = models.ForeignKey('postgroup.Postgroup',on_delete=models.CASCADE,null=True, blank=True)
  userprofileVo = models.ForeignKey('userprofile.Userprofile',on_delete=models.CASCADE,null=True, blank=True)
  userentrepriseVo = models.ForeignKey('userentreprise.Userentreprise',on_delete=models.CASCADE,null=True, blank=True)

  def __str__(self):
    return 'Vote de '+self.userprofileVo.__str__()