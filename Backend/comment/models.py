from django.db import models

# Create your models here.

class Comment(models.Model):
  contentCo = models.TextField(unique=False,null=True,blank=True)
  dateCo = models.DateTimeField(auto_now_add=True)
  userprofileCo = models.ForeignKey('userprofile.Userprofile',on_delete=models.CASCADE,null=True,blank=True)
  userentrepriseCo = models.ForeignKey('userentreprise.Userentreprise',on_delete=models.CASCADE,null=True,blank=True)
  replyCo = models.ForeignKey('reply.Reply',on_delete=models.CASCADE,null=True,blank=True)

  def __str__(self):
    return 'Comment of '+self.userprofileCo.__str__()