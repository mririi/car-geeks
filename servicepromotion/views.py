from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ServicepromotionSerializer

from .models import Servicepromotion
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/servicepromotion-list/',
		'Detail View':'/servicepromotion-detail/<str:pk>/',
		'Create':'/servicepromotion-create/',
		'Update':'/servicepromotion-update/<str:pk>/',
		'Delete':'/servicepromotion-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def servicepromotionList(request):
	servicepromotions = Servicepromotion.objects.all().order_by('-id')
	serializer = ServicepromotionSerializer(servicepromotions, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def servicepromotionDetail(request, pk):
	servicepromotions = Servicepromotion.objects.get(id=pk)
	serializer = ServicepromotionSerializer(servicepromotions, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def servicepromotionCreate(request):
	serializer = ServicepromotionSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def servicepromotionUpdate(request, pk):
	servicepromotion = Servicepromotion.objects.get(id=pk)
	serializer = ServicepromotionSerializer(instance=servicepromotion, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def servicepromotionDelete(request, pk):
	servicepromotion = Servicepromotion.objects.get(id=pk)
	servicepromotion.delete()

	return Response('Item succsesfully delete!')



