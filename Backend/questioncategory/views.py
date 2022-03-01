from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import QuestioncategorySerializer

from .models import Questioncategory
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/questioncategory-list/',
		'Detail View':'/questioncategory-detail/<str:pk>/',
		'Create':'/questioncategory-create/',
		'Update':'/questioncategory-update/<str:pk>/',
		'Delete':'/questioncategory-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def questioncategoryList(request):
	questioncategorys = Questioncategory.objects.all().order_by('-id')
	serializer = QuestioncategorySerializer(questioncategorys, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def questioncategoryDetail(request, pk):
	questioncategorys = Questioncategory.objects.get(id=pk)
	serializer = QuestioncategorySerializer(questioncategorys, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def questioncategoryCreate(request):
	serializer = QuestioncategorySerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def questioncategoryUpdate(request, pk):
	questioncategory = Questioncategory.objects.get(id=pk)
	serializer = QuestioncategorySerializer(instance=questioncategory, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def questioncategoryDelete(request, pk):
	questioncategory = Questioncategory.objects.get(id=pk)
	questioncategory.delete()

	return Response('Item succsesfully delete!')



