from rest_framework import serializers
from .models import Userentreprise

class UserentrepriseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Userentreprise
		fields ='__all__'