from django.db import models

# Create your models here.

class Preferences(models.Model):
  userprofilePref = models.ForeignKey('userprofile.Userprofile',on_delete=models.CASCADE)
  brandPref = models.ForeignKey('brand.Brand',on_delete=models.CASCADE)
  categoryPref = models.ForeignKey('questioncategory.Questioncategory',on_delete=models.CASCADE)

  def __str__(self):
    return 'Preferences de '+self.userprofilePref.__str__()