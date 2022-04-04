from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PreferencesSerializer

from .models import Preferences
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/preferences-list/',
		'Detail View':'/preferences-detail/<str:pk>/',
		'Create':'/preferences-create/',
		'Update':'/preferences-update/<str:pk>/',
		'Delete':'/preferences-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def preferencesList(request):
	preferencess = Preferences.objects.all().order_by('-id')
	serializer = PreferencesSerializer(preferencess, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def preferencesDetail(request, pk):
	preferencess = Preferences.objects.get(id=pk)
	serializer = PreferencesSerializer(preferencess, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def preferencesCreate(request):
	serializer = PreferencesSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def preferencesUpdate(request, pk):
	preferences = Preferences.objects.get(id=pk)
	serializer = PreferencesSerializer(instance=preferences, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def preferencesDelete(request, pk):
	preferences = Preferences.objects.get(id=pk)
	preferences.delete()

	return Response('Item succsesfully delete!')



