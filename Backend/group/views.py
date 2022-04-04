from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import GroupSerializer

from .models import Group
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/group-list/',
		'Detail View':'/group-detail/<str:pk>/',
		'Create':'/group-create/',
		'Update':'/group-update/<str:pk>/',
		'Delete':'/group-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def groupList(request):
	groups = Group.objects.all().order_by('-id')
	serializer = GroupSerializer(groups, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def groupDetail(request, pk):
	groups = Group.objects.get(id=pk)
	serializer = GroupSerializer(groups, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def groupCreate(request):
	serializer = GroupSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['PUT'])
def groupUpdate(request, pk):
	group = Group.objects.get(id=pk)
	serializer = GroupSerializer(instance=group, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def groupDelete(request, pk):
	group = Group.objects.get(id=pk)
	group.delete()

	return Response('Item succsesfully delete!')



