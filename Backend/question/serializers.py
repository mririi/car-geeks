from rest_framework import serializers
from .models import Question

class QuestionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Question
		fields ='__all__'
		extra_kwargs = {'url': {'lookup_field': 'slug'}}
		lookup_field ='slug'
    	