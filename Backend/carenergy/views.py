from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CarenergySerializer

from .models import Carenergy
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/carenergy-list/',
		'Detail View':'/carenergy-detail/<str:pk>/',
		'Create':'/carenergy-create/',
		'Update':'/carenergy-update/<str:pk>/',
		'Delete':'/carenergy-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def carenergyList(request):
	carenergys = Carenergy.objects.all().order_by('-id')
	serializer = CarenergySerializer(carenergys, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def carenergyDetail(request, pk):
	carenergys = Carenergy.objects.get(id=pk)
	serializer = CarenergySerializer(carenergys, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def carenergyCreate(request):
	serializer = CarenergySerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def carenergyUpdate(request, pk):
	carenergy = Carenergy.objects.get(id=pk)
	serializer = CarenergySerializer(instance=carenergy, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def carenergyDelete(request, pk):
	carenergy = Carenergy.objects.get(id=pk)
	carenergy.delete()

	return Response('Item succsesfully delete!')



