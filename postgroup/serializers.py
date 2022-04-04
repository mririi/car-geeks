from rest_framework import serializers
from .models import Postgroup

class PostgroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = Postgroup
		fields ='__all__'