from rest_framework import serializers
from .models import GroupComment

class GroupCommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = GroupComment
		fields ='__all__'