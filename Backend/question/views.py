from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import QuestionSerializer

from .models import Question
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/question-list/',
		'Detail View':'/question-detail/<str:pk>/',
		'Create':'/question-create/',
		'Update':'/question-update/<str:pk>/',
		'Delete':'/question-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def questionList(request):
	questions = Question.objects.all().order_by('-id')
	serializer = QuestionSerializer(questions, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def questionDetail(request, pk):
	questions = Question.objects.get(id=pk)
	serializer = QuestionSerializer(questions, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def questionCreate(request):
	serializer = QuestionSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['PUT'])
def questionUpdate(request, pk):
	question = Question.objects.get(id=pk)
	serializer = QuestionSerializer(instance=question, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def questionDelete(request, pk):
	question = Question.objects.get(id=pk)
	question.delete()

	return Response('Item succsesfully delete!')



