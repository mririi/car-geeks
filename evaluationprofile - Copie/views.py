from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EvaluationProfileSerializer

from .models import EvaluationProfile
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/evaluationprofile-list/',
		'Detail View':'/evaluationprofile-detail/<str:pk>/',
		'Create':'/evaluationprofile-create/',
		'Update':'/evaluationprofile-update/<str:pk>/',
		'Delete':'/evaluationprofile-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def evaluationprofileList(request):
	evaluations = EvaluationProfile.objects.all().order_by('-id')
	serializer = EvaluationProfileSerializer(evaluations, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def evaluationprofileDetail(request, pk):
	evaluations = EvaluationProfile.objects.get(id=pk)
	serializer = EvaluationProfileSerializer(evaluations, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def evaluationprofileCreate(request):
	serializer = EvaluationProfileSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def evaluationprofileUpdate(request, pk):
	evaluation = EvaluationProfile.objects.get(id=pk)
	serializer = EvaluationProfileSerializer(instance=evaluation, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def evaluationprofileDelete(request, pk):
	evaluation = EvaluationProfile.objects.get(id=pk)
	evaluation.delete()

	return Response('Item succsesfully delete!')



