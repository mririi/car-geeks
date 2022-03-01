from rest_framework import serializers
from .models import Cartype

class CartypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cartype
		fields ='__all__'