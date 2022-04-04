from rest_framework import serializers
from .models import Userprofile

class UserprofileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Userprofile
		fields ='__all__'