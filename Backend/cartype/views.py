from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CartypeSerializer

from .models import Cartype
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/cartype-list/',
		'Detail View':'/cartype-detail/<str:pk>/',
		'Create':'/cartype-create/',
		'Update':'/cartype-update/<str:pk>/',
		'Delete':'/cartype-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def cartypeList(request):
	cartypes = Cartype.objects.all().order_by('-id')
	serializer = CartypeSerializer(cartypes, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def cartypeDetail(request, pk):
	cartypes = Cartype.objects.get(id=pk)
	serializer = CartypeSerializer(cartypes, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def cartypeCreate(request):
	serializer = CartypeSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def cartypeUpdate(request, pk):
	cartype = Cartype.objects.get(id=pk)
	serializer = CartypeSerializer(instance=cartype, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def cartypeDelete(request, pk):
	cartype = Cartype.objects.get(id=pk)
	cartype.delete()

	return Response('Item succsesfully delete!')



