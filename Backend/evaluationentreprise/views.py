from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EvaluationentrepriseSerializer

from .models import Evaluationentreprise
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/evaluationentreprise-list/',
		'Detail View':'/evaluationentreprise-detail/<str:pk>/',
		'Create':'/evaluationentreprise-create/',
		'Update':'/evaluationentreprise-update/<str:pk>/',
		'Delete':'/evaluationentreprise-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def evaluationentrepriseList(request):
	evaluationentreprises = Evaluationentreprise.objects.all().order_by('-id')
	serializer = EvaluationentrepriseSerializer(evaluationentreprises, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def evaluationentrepriseDetail(request, pk):
	evaluationentreprises = Evaluationentreprise.objects.get(id=pk)
	serializer = EvaluationentrepriseSerializer(evaluationentreprises, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def evaluationentrepriseCreate(request):
	serializer = EvaluationentrepriseSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def evaluationentrepriseUpdate(request, pk):
	evaluationentreprise = Evaluationentreprise.objects.get(id=pk)
	serializer = EvaluationentrepriseSerializer(instance=evaluationentreprise, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def evaluationentrepriseDelete(request, pk):
	evaluationentreprise = Evaluationentreprise.objects.get(id=pk)
	evaluationentreprise.delete()

	return Response('Item succsesfully delete!')



