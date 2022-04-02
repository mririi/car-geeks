from django.db import models

# Create your models here.

class Preferences(models.Model):
  userprofilePref = models.ForeignKey('userprofile.Userprofile',on_delete=models.CASCADE,null=True,blank=True)
  categoryPref1 = models.ForeignKey('questioncategory.Questioncategory',on_delete=models.CASCADE,null=True,blank=True)
  categoryPref2 = models.ForeignKey('questioncategory.Questioncategory',on_delete=models.CASCADE,null=True,blank=True,related_name="cat2")
  categoryPref3 = models.ForeignKey('questioncategory.Questioncategory',on_delete=models.CASCADE,null=True,blank=True,related_name="cat3")
  def __str__(self):
    return 'Preferences de '+self.userprofilePref.__str__()