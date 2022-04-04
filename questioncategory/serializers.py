from rest_framework import serializers
from .models import Questioncategory

class QuestioncategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Questioncategory
		fields ='__all__'