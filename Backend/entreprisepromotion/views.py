from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EntreprisepromotionSerializer

from .models import Entreprisepromotion
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/entreprisepromotion-list/',
		'Detail View':'/entreprisepromotion-detail/<str:pk>/',
		'Create':'/entreprisepromotion-create/',
		'Update':'/entreprisepromotion-update/<str:pk>/',
		'Delete':'/entreprisepromotion-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def entreprisepromotionList(request):
	entreprisepromotions = Entreprisepromotion.objects.all().order_by('-id')
	serializer = EntreprisepromotionSerializer(entreprisepromotions, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def entreprisepromotionDetail(request, pk):
	entreprisepromotions = Entreprisepromotion.objects.get(id=pk)
	serializer = EntreprisepromotionSerializer(entreprisepromotions, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def entreprisepromotionCreate(request):
	serializer = EntreprisepromotionSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def entreprisepromotionUpdate(request, pk):
	entreprisepromotion = Entreprisepromotion.objects.get(id=pk)
	serializer = EntreprisepromotionSerializer(instance=entreprisepromotion, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def entreprisepromotionDelete(request, pk):
	entreprisepromotion = Entreprisepromotion.objects.get(id=pk)
	entreprisepromotion.delete()

	return Response('Item succsesfully delete!')



