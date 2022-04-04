from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ReclamationSerializer

from .models import Reclamation
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/reclamation-list/',
		'Detail View':'/reclamation-detail/<str:pk>/',
		'Create':'/reclamation-create/',
		'Update':'/reclamation-update/<str:pk>/',
		'Delete':'/reclamation-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def reclamationList(request):
	reclamations = Reclamation.objects.all().order_by('-id')
	serializer = ReclamationSerializer(reclamations, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def reclamationDetail(request, pk):
	reclamations = Reclamation.objects.get(id=pk)
	serializer = ReclamationSerializer(reclamations, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def reclamationCreate(request):
	serializer = ReclamationSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def reclamationUpdate(request, pk):
	reclamation = Reclamation.objects.get(id=pk)
	serializer = ReclamationSerializer(instance=reclamation, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def reclamationDelete(request, pk):
	reclamation = Reclamation.objects.get(id=pk)
	reclamation.delete()

	return Response('Item succsesfully delete!')



