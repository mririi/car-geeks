from rest_framework import serializers
from .models import Evaluationentreprise

class EvaluationentrepriseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Evaluationentreprise
		fields ='__all__'