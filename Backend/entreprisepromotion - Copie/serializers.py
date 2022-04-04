from rest_framework import serializers
from .models import Entreprisepromotion

class EntreprisepromotionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Entreprisepromotion
		fields ='__all__'