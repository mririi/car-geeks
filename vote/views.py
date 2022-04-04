from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import VoteSerializer

from .models import Vote
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/vote-list/',
		'Detail View':'/vote-detail/<str:pk>/',
		'Create':'/vote-create/',
		'Update':'/vote-update/<str:pk>/',
		'Delete':'/vote-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def voteList(request):
	votes = Vote.objects.all().order_by('-id')
	serializer = VoteSerializer(votes, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def voteDetail(request, pk):
	votes = Vote.objects.get(id=pk)
	serializer = VoteSerializer(votes, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def voteCreate(request):
	serializer = VoteSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def voteUpdate(request, pk):
	vote = Vote.objects.get(id=pk)
	serializer = VoteSerializer(instance=vote, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def voteDelete(request, pk):
	vote = Vote.objects.get(id=pk)
	vote.delete()

	return Response('Item succsesfully delete!')



