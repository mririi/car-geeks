from rest_framework import serializers
from .models import Servicetype

class ServicetypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Servicetype
		fields ='__all__'