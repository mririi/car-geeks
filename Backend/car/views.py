from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CarSerializer

from .models import Car
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/car-list/',
		'Detail View':'/car-detail/<str:pk>/',
		'Create':'/car-create/',
		'Update':'/car-update/<str:pk>/',
		'Delete':'/car-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def carList(request):
	cars = Car.objects.all().order_by('-id')
	serializer = CarSerializer(cars, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def carDetail(request, pk):
	cars = Car.objects.get(id=pk)
	serializer = CarSerializer(cars, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def carCreate(request):
	serializer = CarSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def carUpdate(request, pk):
	car = Car.objects.get(id=pk)
	serializer = CarSerializer(instance=car, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def carDelete(request, pk):
	car = Car.objects.get(id=pk)
	car.delete()

	return Response('Item succsesfully delete!')



