from rest_framework import serializers
from .models import Carenergy

class CarenergySerializer(serializers.ModelSerializer):
	class Meta:
		model = Carenergy
		fields ='__all__'