from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EvaluationSerializer

from .models import Evaluation
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/evaluation-list/',
		'Detail View':'/evaluation-detail/<str:pk>/',
		'Create':'/evaluation-create/',
		'Update':'/evaluation-update/<str:pk>/',
		'Delete':'/evaluation-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def evaluationList(request):
	evaluations = Evaluation.objects.all().order_by('-id')
	serializer = EvaluationSerializer(evaluations, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def evaluationDetail(request, pk):
	evaluations = Evaluation.objects.get(id=pk)
	serializer = EvaluationSerializer(evaluations, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def evaluationCreate(request):
	serializer = EvaluationSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def evaluationUpdate(request, pk):
	evaluation = Evaluation.objects.get(id=pk)
	serializer = EvaluationSerializer(instance=evaluation, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def evaluationDelete(request, pk):
	evaluation = Evaluation.objects.get(id=pk)
	evaluation.delete()

	return Response('Item succsesfully delete!')



