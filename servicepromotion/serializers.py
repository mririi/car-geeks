from rest_framework import serializers
from .models import Servicepromotion

class ServicepromotionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Servicepromotion
		fields ='__all__'