from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostGroupSerializer

from .models import PostGroup
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/postgroup-list/',
		'Detail View':'/postgroup-detail/<str:pk>/',
		'Create':'/postgroup-create/',
		'Update':'/postgroup-update/<str:pk>/',
		'Delete':'/postgroup-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def postgroupList(request):
	groups = PostGroup.objects.all().order_by('-id')
	serializer = PostGroupSerializer(groups, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def postgroupDetail(request, pk):
	postgroups = PostGroup.objects.get(id=pk)
	serializer = PostGroupSerializer(postgroups, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def postgroupCreate(request):
	serializer = PostGroupSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['PUT'])
def postgroupUpdate(request, pk):
	postgroup = PostGroup.objects.get(id=pk)
	serializer = PostGroupSerializer(instance=postgroup, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def postgroupDelete(request, pk):
	postgroup = PostGroup.objects.get(id=pk)
	postgroup.delete()

	return Response('Item succsesfully delete!')



