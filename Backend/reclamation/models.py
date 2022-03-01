from django.db import models

# Create your models here.

class Reclamation(models.Model):
  titleRec = models.CharField(max_length=200)
  contentRec = models.TextField(unique=False)
  dateRec = models.DateTimeField(auto_now=True)
  userprofileRec = models.ForeignKey('userprofile.Userprofile',on_delete=models.CASCADE)
  def __str__(self):
    return 'Reclamation de '+self.userprofileRec.__str__()