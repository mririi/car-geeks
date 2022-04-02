from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostgroupSerializer

from .models import Postgroup
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
	groups = Postgroup.objects.all().order_by('-id')
	serializer = PostgroupSerializer(groups, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def postgroupDetail(request, pk):
	postgroups = Postgroup.objects.get(id=pk)
	serializer = PostgroupSerializer(postgroups, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def postgroupCreate(request):
	serializer = PostgroupSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['PUT'])
def postgroupUpdate(request, pk):
	postgroup = Postgroup.objects.get(id=pk)
	serializer = PostgroupSerializer(instance=postgroup, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def postgroupDelete(request, pk):
	postgroup = Postgroup.objects.get(id=pk)
	postgroup.delete()

	return Response('Item succsesfully delete!')



