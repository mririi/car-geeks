from django.db import models

# Create your models here.

class Reply(models.Model):
  contentR = models.TextField(unique=False,null=True,blank=True)
  nblikesR = models.IntegerField(default=0)
  nbCommentR = models.IntegerField(default=0)
  dateR = models.DateTimeField(auto_now_add=True)
  imageR = models.ImageField(upload_to='images/',null=True, blank=True)
  userprofileRep = models.ForeignKey('userprofile.Userprofile',on_delete=models.CASCADE,null=True,blank=True)
  questionRep = models.ForeignKey('question.Question',on_delete=models.CASCADE,null=True,blank=True)
  voteRep = models.ForeignKey('vote.Vote',on_delete=models.CASCADE,null=True,blank=True)

  def __str__(self):
    return 'Reply de '+self.userprofileRep.__str__()+' with title : '+self.contentR.__str__()