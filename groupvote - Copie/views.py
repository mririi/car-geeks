from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import GroupVoteSerializer

from .models import GroupVote
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/groupvote-list/',
		'Detail View':'/groupvote-detail/<str:pk>/',
		'Create':'/groupvote-create/',
		'Update':'/groupvote-update/<str:pk>/',
		'Delete':'/groupvote-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def groupvoteList(request):
	groupvotes = GroupVote.objects.all().order_by('-id')
	serializer = GroupVoteSerializer(groupvotes, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def groupvoteDetail(request, pk):
	groupvotes = GroupVote.objects.get(id=pk)
	serializer = GroupVoteSerializer(groupvotes, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def groupvoteCreate(request):
	serializer = GroupVoteSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['PUT'])
def groupvoteUpdate(request, pk):
	groupvote = GroupVote.objects.get(id=pk)
	serializer = GroupVoteSerializer(instance=groupvote, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def groupvoteDelete(request, pk):
	groupvote = GroupVote.objects.get(id=pk)
	groupvote.delete()

	return Response('Item succsesfully delete!')



