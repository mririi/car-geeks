from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ServiceSerializer

from .models import Service
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/service-list/',
		'Detail View':'/service-detail/<str:pk>/',
		'Create':'/service-create/',
		'Update':'/service-update/<str:pk>/',
		'Delete':'/service-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def serviceList(request):
	services = Service.objects.all().order_by('-id')
	serializer = ServiceSerializer(services, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def serviceDetail(request, pk):
	services = Service.objects.get(id=pk)
	serializer = ServiceSerializer(services, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def serviceCreate(request):
	serializer = ServiceSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def serviceUpdate(request, pk):
	service = Service.objects.get(id=pk)
	serializer = ServiceSerializer(instance=service, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def serviceDelete(request, pk):
	service = Service.objects.get(id=pk)
	service.delete()

	return Response('Item succsesfully delete!')



