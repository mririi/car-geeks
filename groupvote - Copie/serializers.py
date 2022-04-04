from rest_framework import serializers
from .models import GroupVote

class GroupVoteSerializer(serializers.ModelSerializer):
	class Meta:
		model = GroupVote
		fields ='__all__'