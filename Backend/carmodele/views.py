from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CarmodeleSerializer

from .models import Carmodele
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/carmodele-list/',
		'Detail View':'/carmodele-detail/<str:pk>/',
		'Create':'/carmodele-create/',
		'Update':'/carmodele-update/<str:pk>/',
		'Delete':'/carmodele-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def carmodeleList(request):
	carmodeles = Carmodele.objects.all().order_by('-id')
	serializer = CarmodeleSerializer(carmodeles, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def carmodeleDetail(request, pk):
	carmodeles = Carmodele.objects.get(id=pk)
	serializer = CarmodeleSerializer(carmodeles, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def carmodeleCreate(request):
	serializer = CarmodeleSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def carmodeleUpdate(request, pk):
	carmodele = Carmodele.objects.get(id=pk)
	serializer = CarmodeleSerializer(instance=carmodele, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def carmodeleDelete(request, pk):
	carmodele = Carmodele.objects.get(id=pk)
	carmodele.delete()

	return Response('Item succsesfully delete!')



