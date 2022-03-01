from django.db import models

# Create your models here.
class Notifications(models.Model):
  contentNo = models.CharField(max_length=200,null=True,blank=True)
  seenNo = models.BooleanField(default=False)
  userprofileNo = models.ForeignKey('userprofile.Userprofile',on_delete=models.CASCADE,null=True,blank=True)
  replyNo = models.ForeignKey('reply.Reply',on_delete=models.CASCADE,null=True,blank=True)
  questionNo = models.ForeignKey('question.Question',on_delete=models.CASCADE,null=True,blank=True)
  dateNo = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return 'Notification de '+self.replyNo.__str__()