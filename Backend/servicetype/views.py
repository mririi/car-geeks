from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ServicetypeSerializer

from .models import Servicetype
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/servicetype-list/',
		'Detail View':'/servicetype-detail/<str:pk>/',
		'Create':'/servicetype-create/',
		'Update':'/servicetype-update/<str:pk>/',
		'Delete':'/servicetype-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def servicetypeList(request):
	servicetypes = Servicetype.objects.all().order_by('-id')
	serializer = ServicetypeSerializer(servicetypes, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def servicetypeDetail(request, pk):
	servicetypes = Servicetype.objects.get(id=pk)
	serializer = ServicetypeSerializer(servicetypes, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def servicetypeCreate(request):
	serializer = ServicetypeSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def servicetypeUpdate(request, pk):
	servicetype = Servicetype.objects.get(id=pk)
	serializer = ServicetypeSerializer(instance=servicetype, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def servicetypeDelete(request, pk):
	servicetype = Servicetype.objects.get(id=pk)
	servicetype.delete()

	return Response('Item succsesfully delete!')



