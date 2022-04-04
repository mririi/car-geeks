from rest_framework import serializers
from .models import EvaluationProfile

class EvaluationProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = EvaluationProfile
		fields ='__all__'