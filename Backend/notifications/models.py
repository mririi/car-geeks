from django.db import models

# Create your models here.
class Notifications(models.Model):
  message = models.CharField(max_length=200,null=True,blank=True)
  seen = models.BooleanField(default=False)
  admin = models.BooleanField(default=False)
  byuserprofileNo = models.ForeignKey('userprofile.Userprofile',on_delete=models.CASCADE,null=True,blank=True,related_name="userprofiledoneit")
  userprofileNo = models.ForeignKey('userprofile.Userprofile',on_delete=models.CASCADE,null=True,blank=True)
  profileNo = models.ForeignKey('userprofile.Userprofile',on_delete=models.CASCADE,null=True,blank=True,related_name="profile")
  replyNo = models.ForeignKey('reply.Reply',on_delete=models.CASCADE,null=True,blank=True)
  questionNo = models.ForeignKey('question.Question',on_delete=models.CASCADE,null=True,blank=True)
  serviceNo = models.ForeignKey('service.Service',on_delete=models.CASCADE,null=True,blank=True)
  byuserentrepriseNo = models.ForeignKey('userentreprise.Userentreprise',on_delete=models.CASCADE,null=True,blank=True,related_name="userentreprisedoneit")
  entrepriseNo = models.ForeignKey('userentreprise.Userentreprise',on_delete=models.CASCADE,null=True,blank=True)
  dateNo = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return 'Notification de '+self.userprofileNo.__str__()