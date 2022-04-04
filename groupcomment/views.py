from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import GroupCommentSerializer

from .models import GroupComment
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/groupcomment-list/',
		'Detail View':'/groupcomment-detail/<str:pk>/',
		'Create':'/groupcomment-create/',
		'Update':'/groupcomment-update/<str:pk>/',
		'Delete':'/groupcomment-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def groupcommentList(request):
	groupcomments = GroupComment.objects.all().order_by('-id')
	serializer = GroupCommentSerializer(groupcomments, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def groupcommentDetail(request, pk):
	groupcomments = GroupComment.objects.get(id=pk)
	serializer = GroupCommentSerializer(groupcomments, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def groupcommentCreate(request):
	serializer = GroupCommentSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['PUT'])
def groupcommentUpdate(request, pk):
	groupcomment = GroupComment.objects.get(id=pk)
	serializer = GroupCommentSerializer(instance=groupcomment, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def groupcommentDelete(request, pk):
	groupcomment = GroupComment.objects.get(id=pk)
	groupcomment.delete()

	return Response('Item succsesfully delete!')



