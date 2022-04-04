from rest_framework import serializers
from .models import Reclamation

class ReclamationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Reclamation
		fields ='__all__'