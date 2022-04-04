from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserprofileSerializer

from .models import Userprofile
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/userprofile-list/',
		'Detail View':'/userprofile-detail/<str:pk>/',
		'Create':'/userprofile-create/',
		'Update':'/userprofile-update/<str:pk>/',
		'Delete':'/userprofile-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def userprofileList(request):
	userprofiles = Userprofile.objects.all().order_by('-id')
	serializer = UserprofileSerializer(userprofiles, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def userprofileDetail(request, pk):
	userprofiles = Userprofile.objects.get(id=pk)
	serializer = UserprofileSerializer(userprofiles, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def userprofileCreate(request):
	serializer = UserprofileSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['PUT'])
def userprofileUpdate(request, pk):
	userprofile = Userprofile.objects.get(id=pk)
	serializer = UserprofileSerializer(instance=userprofile, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def userprofileDelete(request, pk):
	userprofile = Userprofile.objects.get(id=pk)
	userprofile.delete()

	return Response('Item succsesfully delete!')



