from django.db import models

# Create your models here.

class Vote(models.Model):
  dateCreationVo = models.DateTimeField(auto_now_add=True)
  questionVo = models.ForeignKey('question.Question',on_delete=models.CASCADE,null=True, blank=True)
  replyVo = models.ForeignKey('reply.Reply',on_delete=models.CASCADE,null=True, blank=True)
  userprofileVo = models.ForeignKey('userprofile.Userprofile',on_delete=models.CASCADE,null=True, blank=True)

  def __str__(self):
    return 'Vote de '+self.userprofileVo.__str__()+' sur '+self.questionVo.__str__()
  