from rest_framework import serializers
from .models import Carengine

class CarengineSerializer(serializers.ModelSerializer):
	class Meta:
		model = Carengine
		fields ='__all__'