from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BrandSerializer

from .models import Brand
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/brand-list/',
		'Detail View':'/brand-detail/<str:pk>/',
		'Create':'/brand-create/',
		'Update':'/brand-update/<str:pk>/',
		'Delete':'/brand-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def brandList(request):
	brands = Brand.objects.all().order_by('-id')
	serializer = BrandSerializer(brands, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def brandDetail(request, pk):
	brands = Brand.objects.get(id=pk)
	serializer = BrandSerializer(brands, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def brandCreate(request):
	serializer = BrandSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def brandUpdate(request, pk):
	brand = Brand.objects.get(id=pk)
	serializer = BrandSerializer(instance=brand, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def brandDelete(request, pk):
	brand = Brand.objects.get(id=pk)
	brand.delete()

	return Response('Item succsesfully delete!')



