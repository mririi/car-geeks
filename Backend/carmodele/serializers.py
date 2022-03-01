from rest_framework import serializers
from .models import Carmodele

class CarmodeleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Carmodele
		fields ='__all__'