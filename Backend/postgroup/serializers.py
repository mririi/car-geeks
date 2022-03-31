from rest_framework import serializers
from .models import PostGroup

class PostGroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = PostGroup
		fields ='__all__'