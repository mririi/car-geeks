from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CarengineSerializer

from .models import Carengine
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/carengine-list/',
		'Detail View':'/carengine-detail/<str:pk>/',
		'Create':'/carengine-create/',
		'Update':'/carengine-update/<str:pk>/',
		'Delete':'/carengine-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def carengineList(request):
	carengines = Carengine.objects.all().order_by('-id')
	serializer = CarengineSerializer(carengines, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def carengineDetail(request, pk):
	carengines = Carengine.objects.get(id=pk)
	serializer = CarengineSerializer(carengines, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def carengineCreate(request):
	serializer = CarengineSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def carengineUpdate(request, pk):
	carengine = Carengine.objects.get(id=pk)
	serializer = CarengineSerializer(instance=carengine, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def carengineDelete(request, pk):
	carengine = Carengine.objects.get(id=pk)
	carengine.delete()

	return Response('Item succsesfully delete!')



