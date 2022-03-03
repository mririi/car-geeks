from django.db import models

# Create your models here.

class Question(models.Model):
  titleQ = models.CharField(max_length=200,null=True,blank=True)
  contentQ = models.TextField(unique=True,null=True,blank=True)
  nblikes = models.IntegerField(default=0)
  nbrep = models.IntegerField(default=0)
  dateQ = models.DateTimeField(auto_now_add=True)
  imageQ = models.ImageField(upload_to='images/',null=True, blank=True)
  userprofileQ = models.ForeignKey('userprofile.Userprofile',on_delete=models.CASCADE,null=True,blank=True)
  categoryQ = models.ForeignKey('questioncategory.Questioncategory',on_delete=models.CASCADE,null=True,blank=True)
  voteQ = models.ForeignKey('vote.Vote',on_delete=models.CASCADE,null=True,blank=True)

  def __str__(self):
    return 'Question de '+self.userprofileQ.__str__()