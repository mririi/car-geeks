from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserentrepriseSerializer

from .models import Userentreprise
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/userentreprise-list/',
		'Detail View':'/userentreprise-detail/<str:pk>/',
		'Create':'/userentreprise-create/',
		'Update':'/userentreprise-update/<str:pk>/',
		'Delete':'/userentreprise-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def userentrepriseList(request):
	userentreprises = Userentreprise.objects.all().order_by('-id')
	serializer = UserentrepriseSerializer(userentreprises, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def userentrepriseDetail(request, pk):
	userentreprises = Userentreprise.objects.get(id=pk)
	serializer = UserentrepriseSerializer(userentreprises, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def userentrepriseCreate(request):
	serializer = UserentrepriseSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['PUT'])
def userentrepriseUpdate(request, pk):
	userentreprise = Userentreprise.objects.get(id=pk)
	serializer = UserentrepriseSerializer(instance=userentreprise, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def userentrepriseDelete(request, pk):
	userentreprise = Userentreprise.objects.get(id=pk)
	userentreprise.delete()

	return Response('Item succsesfully delete!')



